# build_edc_master_solutions.py
# Comprehensive master generator for IOE Electronic Devices & Circuits Solutions (EX 151 / EX 501 / CT 501)

import os
import subprocess
import shutil
from edc_ch1_2083_baishakh import get_chapter_2083_baishakh
from edc_ch2_2082_bhadra import get_chapter_2082_bhadra
from edc_ch3_2082_baishakh import get_chapter_2082_baishakh
from edc_ch4_2081_ashwin import get_chapter_2081_ashwin

def get_preamble():
    return r"""\documentclass[11pt,a4paper,oneside]{book}
\usepackage[utf8]{inputenc}
\usepackage[margin=1.8cm, top=2.2cm, bottom=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{array}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{setspace}

\usetikzlibrary{shapes.gates.logic.US,positioning,calc,arrows.meta}

% Line Spacing and Paragraph Spacing
\setstretch{1.22}
\setlength{\parskip}{0.5em}
\setlength{\parindent}{0pt}
\setlist[enumerate]{itemsep=0.35em, topsep=0.35em, parsep=0.15em}
\setlist[itemize]{itemsep=0.35em, topsep=0.35em, parsep=0.15em}

% Custom Color Palette
\definecolor{primarydark}{HTML}{0f172a}
\definecolor{secondaryblue}{HTML}{1e3a8a}
\definecolor{accentindigo}{HTML}{4338ca}
\definecolor{boxbg}{HTML}{f8fafc}
\definecolor{boxborder}{HTML}{cbd5e1}
\definecolor{alertborder}{HTML}{3b82f6}
\definecolor{ansbg}{HTML}{f0fdf4}
\definecolor{ansborder}{HTML}{16a34a}
\definecolor{diagbg}{HTML}{ffffff}
\definecolor{diagborder}{HTML}{4338ca}

% Typography & Headings
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries\color{primarydark}}{\chaptertitlename\ \thechapter}{12pt}{\Huge}
\titleformat{\section}
{\normalfont\Large\bfseries\color{secondaryblue}}{\thesection}{1em}{}
\titleformat{\subsection}
{\normalfont\large\bfseries\color{accentindigo}}{\thesubsection}{1em}{}

% Headers & Footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\bfseries\sffamily\color{secondaryblue} Electronic Devices \& Circuits (EX 151) --- IOE Master Solutions}
\fancyhead[R]{\small\sffamily\color{gray} Tribhuvan University}
\fancyfoot[C]{\sffamily\bfseries\thepage}
\renewcommand{\headrulewidth}{0.6pt}

% Custom TColorBoxes with Enhanced Internal Spacing
\newtcolorbox{questionbox}[1]{
  colback=boxbg,
  colframe=alertborder,
  coltitle=white,
  fonttitle=\bfseries\sffamily,
  title={#1},
  arc=2.5mm,
  boxrule=1pt,
  boxsep=5pt,
  top=7pt,
  bottom=7pt,
  left=8pt,
  right=8pt,
  before upper={\setstretch{1.2}},
  breakable,
  enhanced
}

\newtcolorbox{answerbox}{
  colback=ansbg,
  colframe=ansborder,
  coltitle=white,
  fonttitle=\bfseries\sffamily,
  title={Final Verified Result},
  arc=2.5mm,
  boxrule=1pt,
  boxsep=5pt,
  top=6pt,
  bottom=6pt,
  left=8pt,
  right=8pt,
  before upper={\setstretch{1.2}},
  breakable,
  enhanced
}

\newtcolorbox{schematicbox}[1]{
  colback=diagbg,
  colframe=diagborder,
  coltitle=white,
  fonttitle=\bfseries\sffamily,
  title={Circuit Schematic / Analysis Diagram: #1},
  arc=2.5mm,
  boxrule=1pt,
  boxsep=6pt,
  top=8pt,
  bottom=8pt,
  left=8pt,
  right=8pt,
  breakable,
  enhanced
}

\begin{document}

% Title Page
\begin{titlepage}
  \centering
  \vspace*{1.5cm}
  {\Huge \bfseries \color{primarydark} TRIBHUVAN UNIVERSITY\par}
  \vspace{0.4cm}
  {\Large \bfseries \color{secondaryblue} INSTITUTE OF ENGINEERING (IOE)\par}
  \vspace{1.5cm}
  {\Huge \bfseries \color{accentindigo} ELECTRONIC DEVICES \& CIRCUITS\par}
  \vspace{0.5cm}
  {\LARGE Course Code: EX 151 / EX 501 / CT 501\par}
  \vspace{0.3cm}
  {\large BE Electronics, Information and Communication (BEI) \& BE Computer (BCT)\par}
  \vspace{2.0cm}
  
  \begin{tcolorbox}[colback=boxbg,colframe=alertborder,width=0.88\textwidth,arc=3mm,center]
    \centering
    \Large \textbf{Comprehensive Master Examination Solutions}\par
    \vspace{0.3cm}
    \normalsize \textit{Complete step-by-step mathematical derivations, small-signal AC models, DC biasing calculations, power amplifier efficiencies, oscillator analyses, and high-precision TikZ schematics for all exam sittings.}
  \end{tcolorbox}
  
  \vfill
  {\large \textbf{Academic Exam Papers Covered:}\par}
  {\normalsize 2083 Baishakh $\cdot$ 2082 Bhadra $\cdot$ 2082 Baishakh $\cdot$ 2081 Ashwin\par}
  \vspace{1.0cm}
  {\small IOE Examination Reference Edition $\cdot$ August 2026\par}
\end{titlepage}

\tableofcontents
\newpage
"""

def generate_and_compile():
    tex_path = "dependencies/edc_master_solutions.tex"
    
    print("Assembling complete EDC master LaTeX document...")
    full_tex = (
        get_preamble()
        + get_chapter_2083_baishakh()
        + get_chapter_2082_bhadra()
        + get_chapter_2082_baishakh()
        + get_chapter_2081_ashwin()
        + "\n\\end{document}\n"
    )
    
    with open(tex_path, "w") as f:
        f.write(full_tex)
    print(f"Saved LaTeX source to {tex_path} ({len(full_tex)} characters)")

    # Compile with pdflatex (2 passes for TOC and page numbering)
    print("Compiling Pass 1...")
    res1 = subprocess.run(["pdflatex", "-interaction=nonstopmode", "edc_master_solutions.tex"], cwd="dependencies", capture_output=True, text=True)
    if res1.returncode != 0:
        print("Pass 1 errors:")
        print(res1.stdout[-1500:])
        return False

    print("Compiling Pass 2...")
    res2 = subprocess.run(["pdflatex", "-interaction=nonstopmode", "edc_master_solutions.tex"], cwd="dependencies", capture_output=True, text=True)
    if res2.returncode != 0:
        print("Pass 2 errors:")
        print(res2.stdout[-1500:])
        return False

    pdf_src = "dependencies/edc_master_solutions.pdf"
    if os.path.exists(pdf_src):
        pdf_size = os.path.getsize(pdf_src)
        print(f"Compiled successfully! PDF generated: {pdf_src} ({pdf_size} bytes)")
        
        # Copy to destination paths
        dest1 = "subjects/5_electronic_devices_and_circuits/EDC Solutions.pdf"
        dest2 = "solutions/web_app/downloads/edc/edc_solutions.pdf"
        dest3 = "solutions/web_app/downloads/edc/EDC Solutions.pdf"
        
        os.makedirs("solutions/web_app/downloads/edc", exist_ok=True)
        shutil.copyfile(pdf_src, dest1)
        shutil.copyfile(pdf_src, dest2)
        shutil.copyfile(pdf_src, dest3)
        print(f"Synchronized PDF to:\n  - {dest1}\n  - {dest2}\n  - {dest3}")
        return True
    else:
        print("Error: PDF was not produced.")
        return False

if __name__ == "__main__":
    generate_and_compile()
