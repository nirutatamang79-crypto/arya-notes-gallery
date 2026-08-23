import re
import os
import json
import subprocess
import fitz
from PIL import Image, ImageChops

def autocrop(im, pad=25):
    # Find bounding box of non-white pixels
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        w, h = im.size
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        return im.crop(bbox)
    return im

os.makedirs('solutions/web_app/assets/circuits', exist_ok=True)
os.makedirs('dependencies/circuit_standalone_tmp', exist_ok=True)

with open('solutions/Electrical_Circuits_and_Machines_Solutions_Master.tex', 'r') as f:
    full_text = f.read()

# Split text into chapters based on \section{
sections_raw = re.split(r'\\section\{', full_text)

chapters = []
all_questions = []

figure_map = {
    "5.1": "assets/figures/bode_2083_baishakh.png",
    "5.2": "assets/figures/bode_2082_bhadra.png",
    "5.3": "assets/figures/bode_2082_baishakh.png",
    "5.4": "assets/figures/bode_2081_ashwin.png",
    "7.2": "assets/figures/bh_hysteresis.png",
    "9.2": "assets/figures/dc_generator_occ.png",
    "9.3": "assets/figures/im_torque_speed.png",
}

for sec_idx, sec_text in enumerate(sections_raw[1:], 1):
    sec_lines = sec_text.split('}', 1)
    sec_title = sec_lines[0].replace('\\&', '&').strip()
    sec_body = sec_lines[1] if len(sec_lines) > 1 else ""
    
    ch_match = re.match(r'Question\s+(\d+)\s*:\s*(.*)', sec_title)
    if ch_match:
        ch_num = int(ch_match.group(1))
        ch_name = ch_match.group(2).strip()
    else:
        ch_num = sec_idx
        ch_name = sec_title
        
    chapter_data = {
        "chapter_num": ch_num,
        "chapter_title": f"Question {ch_num}: {ch_name}" if "Question" not in sec_title else sec_title,
        "questions": []
    }
    
    subsections = re.split(r'\\subsection\*?\{', sec_body)
    
    for sub_idx, sub_text in enumerate(subsections[1:], 1):
        sub_lines = sub_text.split('}', 1)
        sub_header = sub_lines[0].replace('\\&', '&').strip()
        sub_body = sub_lines[1] if len(sub_lines) > 1 else ""
        
        year_match = re.search(r'(208\d\s+[A-Za-z]+)', sub_header)
        exam_year = year_match.group(1) if year_match else "General"
        
        q_match = re.search(r'Question\s+(\d+)', sub_header)
        q_num = f"Question {q_match.group(1)}" if q_match else f"Part {sub_idx}"
        
        marks_match = re.search(r'\[(.*?)\]', sub_header)
        marks = marks_match.group(1) if marks_match else ""
        
        q_id = f"q{ch_num}_{sub_idx}_{re.sub(r'[^a-zA-Z0-9]', '_', exam_year).lower()}"
        
        problem_box_match = re.search(r'\\begin\{questionbox\}\{Problem Statement \((.*?)\)\}(.*?)\\end\{questionbox\}', sub_body, re.DOTALL)
        if problem_box_match:
            problem_text = problem_box_match.group(2).strip()
        else:
            problem_text = ""
            
        circ_match = re.search(r'(\\begin\{circuitikz\}.*?\\end\{circuitikz\})', sub_body, re.DOTALL)
        circ_img_path = None
        if circ_match:
            tikz_code = circ_match.group(1)
            clean_name = f"circuit_{q_id}"
            tex_content = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=1.5cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{circuitikz}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,positioning}
\pagestyle{empty}
\begin{document}
\begin{center}
''' + tikz_code + r'''
\end{center}
\end{document}'''
            tex_file = f'dependencies/circuit_standalone_tmp/{clean_name}.tex'
            with open(tex_file, 'w') as f:
                f.write(tex_content)
            
            res = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies/circuit_standalone_tmp', tex_file],
                                 capture_output=True, text=True)
            pdf_file = f'dependencies/circuit_standalone_tmp/{clean_name}.pdf'
            if os.path.exists(pdf_file):
                doc = fitz.open(pdf_file)
                page = doc[0]
                pix = page.get_pixmap(dpi=300)
                temp_png = f'dependencies/circuit_standalone_tmp/{clean_name}_raw.png'
                pix.save(temp_png)
                
                # Crop whitespace
                img = Image.open(temp_png).convert('RGB')
                cropped_img = autocrop(img)
                final_png = f'solutions/web_app/assets/circuits/{clean_name}.png'
                cropped_img.save(final_png)
                circ_img_path = f"assets/circuits/{clean_name}.png"
                print(f"Rendered & Cropped: {clean_name}.png ({cropped_img.size[0]}x{cropped_img.size[1]})")
            else:
                print(f"Failed compiling circuit: {clean_name}")
                
        ch_sub_key = f"{ch_num}.{sub_idx}"
        fig_img_path = figure_map.get(ch_sub_key, None)
        
        answer_box_match = re.search(r'\\begin\{answerbox\}(.*?)\\end\{answerbox\}', sub_body, re.DOTALL)
        final_answer = answer_box_match.group(1).strip() if answer_box_match else ""
        
        if problem_box_match:
            sol_body = sub_body[problem_box_match.end():]
        else:
            sol_body = sub_body
            
        if answer_box_match:
            sol_body = sol_body[:sol_body.find(r'\begin{answerbox}')]
            
        # Clean problem_statement and raw_solution by removing embedded circuitikz code from text display
        problem_cleaned = re.sub(r'\\begin\{center\}\s*\\begin\{circuitikz\}.*?\\end\{circuitikz\}\s*\\end\{center\}', '', problem_text, flags=re.DOTALL).strip()
        
        q_item = {
            "id": q_id,
            "ch_num": ch_num,
            "sub_idx": sub_idx,
            "sub_header": sub_header,
            "exam_year": exam_year,
            "q_num": q_num,
            "marks": marks,
            "problem_statement": problem_cleaned if problem_cleaned else problem_text,
            "circuit_image": circ_img_path,
            "figure_image": fig_img_path,
            "final_answer": final_answer,
            "raw_solution": sol_body.strip()
        }
        chapter_data["questions"].append(q_item)
        all_questions.append(q_item)
        
    chapters.append(chapter_data)

out_json = {
    "title": "IOE Electrical Circuits & Machines (EE 154 / ENEE 154) - Master Solutions",
    "years": ["2083 Baishakh", "2082 Bhadra", "2082 Baishakh", "2081 Ashwin"],
    "total_questions": len(all_questions),
    "chapters": chapters
}

with open('solutions/web_app/questions_data.json', 'w') as f:
    json.dump(out_json, f, indent=2)

print(f"ALL DONE! Saved questions_data.json with {len(chapters)} chapters and {len(all_questions)} questions.")
