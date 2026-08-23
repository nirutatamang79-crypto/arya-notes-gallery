import json
import re

with open('solutions/web_app/questions_data.json', 'r') as f:
    data = json.load(f)

def latex_to_html(tex):
    if not tex:
        return ""
    
    s = tex
    
    # Remove comments
    s = re.sub(r'(?<!\\)%.*$', '', s, flags=re.MULTILINE)
    
    # Remove center environments with circuitikz
    s = re.sub(r'\\begin\{center\}\s*\\begin\{circuitikz\}.*?\\end\{circuitikz\}\s*\\end\{center\}', '', s, flags=re.DOTALL)
    s = re.sub(r'\\begin\{circuitikz\}.*?\\end\{circuitikz\}', '', s, flags=re.DOTALL)
    
    # Convert paragraph, subsubsection, paragraph
    s = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'<h3 class="solution-heading">\1</h3>', s)
    s = re.sub(r'\\paragraph\*?\{([^}]+)\}', r'<h4 class="step-heading">\1</h4>', s)
    
    # Convert textbf, textit, texttt
    s = re.sub(r'\\textbf\{([^}]+)\}', r'<strong>\1</strong>', s)
    s = re.sub(r'\\textit\{([^}]+)\}', r'<em>\1</em>', s)
    s = re.sub(r'\\texttt\{([^}]+)\}', r'<code>\1</code>', s)
    
    # Convert itemize and enumerate
    s = re.sub(r'\\begin\{itemize\}(?:\[.*?\])?', r'<ul class="solution-list">', s)
    s = re.sub(r'\\end\{itemize\}', r'</ul>', s)
    s = re.sub(r'\\begin\{enumerate\}(?:\[.*?\])?', r'<ol class="solution-list">', s)
    s = re.sub(r'\\end\{enumerate\}', r'</ol>', s)
    s = re.sub(r'\\item\s+', r'<li>', s)
    
    # Convert align and equation environments
    s = re.sub(r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}', r'$$\\begin{aligned}\1\\end{aligned}$$', s, flags=re.DOTALL)
    s = re.sub(r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}', r'$$\1$$', s, flags=re.DOTALL)
    s = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', s, flags=re.DOTALL)
    
    # Fix double newlines into paragraphs
    paragraphs = s.split('\n\n')
    formatted_paras = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith('<h') or p.startswith('<ul') or p.startswith('<ol') or p.startswith('$$'):
            formatted_paras.append(p)
        elif p.startswith('<li>'):
            formatted_paras.append(p)
        else:
            formatted_paras.append(f'<p>{p}</p>')
            
    res = '\n'.join(formatted_paras)
    return res

for ch in data['chapters']:
    for q in ch['questions']:
        q['problem_statement_html'] = latex_to_html(q['problem_statement'])
        q['solution_html'] = latex_to_html(q['raw_solution'])
        q['final_answer_html'] = latex_to_html(q['final_answer'])

with open('solutions/web_app/questions_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Formatted all questions with clean HTML and KaTeX syntax!")
