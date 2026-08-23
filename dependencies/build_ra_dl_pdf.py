import subprocess
import os
import shutil

img_abs_path = os.path.abspath("solutions/web_app/assets/images/arya_solving.jpg")

tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=1.5cm, top=1.8cm, bottom=1.8cm]{geometry}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{skins}

\definecolor{primarydark}{HTML}{0f172a}
\definecolor{warnbg}{HTML}{fef3c7}
\definecolor{warnborder}{HTML}{f59e0b}
\definecolor{warntext}{HTML}{92400e}

\pagestyle{empty}

\begin{document}
\centering

\vspace*{0.3cm}
{\Huge \bfseries \color{primarydark} TRIBHUVAN UNIVERSITY\par}
\vspace{0.2cm}
{\Large \bfseries INSTITUTE OF ENGINEERING (IOE)\par}
\vspace{0.3cm}
{\LARGE \bfseries DIGITAL LOGIC (EX 152 / CT 152)\par}
\vspace{0.6cm}

\begin{tcolorbox}[colback=warnbg,colframe=warnborder,arc=3mm,boxrule=1.5pt,width=0.94\textwidth,center]
  \centering
  {\Large \bfseries \color{warntext} IN PROGRESS --- RA IS WORKING ON THIS SUBJECT}\par
  \vspace{0.2cm}
  {\normalsize \color{warntext} Digital Logic solutions are currently being solved, verified, and updated by RA with redrawn circuit schematics, timing waveforms, and K-maps.}
\end{tcolorbox}

\vspace{0.4cm}

\begin{tcolorbox}[colback=white,colframe=primarydark,arc=3mm,boxrule=1pt,width=0.90\textwidth,center]
  \centering
  \vspace{0.2cm}
  \includegraphics[width=0.85\textwidth,height=13.5cm,keepaspectratio]{""" + img_abs_path + r"""}
  \vspace{0.2cm}
\end{tcolorbox}

\vfill
{\large \bfseries Check back soon for the verified master edition!\par}
\vspace{0.2cm}
{\small Reference Resource Portal $\cdot$ Central Examination Solutions $\cdot$ August 2026\par}

\end{document}
"""

with open("dependencies/ra_working_dl.tex", "w") as f:
    f.write(tex_content)

res = subprocess.run(["pdflatex", "-interaction=nonstopmode", "ra_working_dl.tex"], cwd="dependencies", capture_output=True, text=True)
if res.returncode == 0:
    print("Compiled ra_working_dl.pdf successfully!")
    pdf_src = "dependencies/ra_working_dl.pdf"
    
    # Copy to all target locations
    targets = [
        "solutions/web_app/downloads/dl/Digital Logic Solutions.pdf",
        "solutions/web_app/downloads/dl/digital_logic_solutions.pdf",
        "solutions/web_app/downloads/digital_logic_master.pdf",
        "subjects/2_digital_logic/Digital Logic Solutions.pdf"
    ]
    
    for t in targets:
        os.makedirs(os.path.dirname(t), exist_ok=True)
        shutil.copyfile(pdf_src, t)
        print(f"Copied to: {t}")
else:
    print("Compilation error:")
    print(res.stdout[-1000:])
