import subprocess
import os

latex_source = r'''\documentclass[11pt,a4paper,oneside]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.75in,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{circuitikz}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage{titlesec}
\usepackage{hyperref}

\tcbuselibrary{skins,breakable}

% Color Palette
\definecolor{primaryblue}{RGB}{18, 48, 105}
\definecolor{accentteal}{RGB}{0, 110, 110}
\definecolor{darkslate}{RGB}{35, 45, 55}
\definecolor{boxbg}{RGB}{246, 249, 253}
\definecolor{warnbg}{RGB}{255, 248, 243}
\definecolor{warnborder}{RGB}{205, 95, 20}
\definecolor{resbg}{RGB}{240, 252, 245}
\definecolor{resborder}{RGB}{35, 140, 70}
\definecolor{errbg}{RGB}{253, 242, 242}
\definecolor{errborder}{RGB}{190, 40, 40}

% Hyperref Setup
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=accentteal,
    urlcolor=accentteal,
    pdftitle={IOE Electrical Circuits and Machines - Master Past Paper Solutions},
    pdfauthor={Engineering Expert Solutions}
}

% Page Header/Footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textcolor{primaryblue}{\textbf{Electrical Circuits \& Machines (EE 154 / ENEE 154)}}}
\fancyhead[R]{\textcolor{darkslate}{\sffamily Question-by-Question Master Solutions}}
\fancyfoot[L]{\textcolor{darkslate}{\footnotesize Tribhuvan University $\cdot$ Institute of Engineering (IOE)}}
\fancyfoot[R]{\textcolor{primaryblue}{\bfseries Page \thepage}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

% Section Titles
\titleformat{\section}{\Large\bfseries\sffamily\color{primaryblue}}{\thesection}{1em}{}[\titlerule]
\titleformat{\subsection}{\large\bfseries\sffamily\color{accentteal}}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\normalsize\bfseries\sffamily\color{darkslate}}{\thesubsubsection}{1em}{}

% Custom Boxes
\newtcolorbox{questionbox}[1]{
  colback=boxbg,
  colframe=primaryblue,
  fonttitle=\bfseries\sffamily\color{white},
  title={#1},
  arc=2mm,
  boxrule=1pt,
  breakable
}

\newtcolorbox{answerbox}[1][]{
  colback=resbg,
  colframe=resborder,
  fonttitle=\bfseries\sffamily\color{white},
  title={Verified Final Result},
  arc=1.5mm,
  boxrule=0.8pt,
  breakable,
  #1
}

\newtcolorbox{auditbox}[1][]{
  colback=errbg,
  colframe=errborder,
  fonttitle=\bfseries\sffamily\color{white},
  title={Correction \& Common Pitfall Audit},
  arc=1.5mm,
  boxrule=0.8pt,
  breakable,
  #1
}

\newtcolorbox{conceptbox}[1]{
  colback=warnbg,
  colframe=warnborder,
  fonttitle=\bfseries\sffamily\color{white},
  title={Key Concept: #1},
  arc=1.5mm,
  boxrule=0.8pt,
  breakable
}

\begin{document}

% ==============================================================================
% TITLE PAGE
% ==============================================================================
\begin{titlepage}
\centering
\vspace*{1.5cm}
{\huge\bfseries\sffamily\color{primaryblue} TRIBHUVAN UNIVERSITY\\[0.3em] INSTITUTE OF ENGINEERING (IOE)}\\[1.5cm]

{\LARGE\bfseries\sffamily ELECTRICAL CIRCUITS \& MACHINES}\\[0.4em]
{\Large\bfseries\sffamily Course Code: EE 154 / ENEE 154}\\[1.2cm]

{\large\bfseries Bachelor of Engineering (BE)}\\[0.3em]
{\normalsize Computer Engineering (BCT) $\cdot$ Electronics, Information \& Communication Engineering (BEI)}\\[0.3em]
{\normalsize \textbf{Year I / Part II} (First Year, Second Semester)}\\[1.8cm]

\begin{tcolorbox}[colback=primaryblue!5,colframe=primaryblue,arc=3mm,boxrule=1.2pt,width=0.92\textwidth]
\centering
\vspace{0.4em}
{\large\bfseries\sffamily Comprehensive Past Exam Question-by-Question Master Solutions}\\[0.4em]
{\normalsize Including Exact Circuitikz Vector Schematics, Matplotlib Asymptotic Bode Plots, Transient Analysis Proofs, Matrix Formulations, and Deep Concept Audits}\\[0.4em]
\vspace{0.2em}
\hrule\vspace{0.6em}
\textbf{Coverage Across 4 Exam Sessions:}\\[0.2em]
\textbullet\ \textbf{2083 Baishakh} (Back Course) \quad \textbullet\ \textbf{2082 Bhadra} (Regular Course)\\[0.2em]
\textbullet\ \textbf{2082 Baishakh} (Back Course) \quad \textbullet\ \textbf{2081 Ashwin} (Regular Course)
\vspace{0.4em}
\end{tcolorbox}

\vfill
{\footnotesize\sffamily Fully Audited, Mathematically Verified \& Typeset with Publication-Grade Accuracy}\\[0.5em]
{\small\bfseries\color{primaryblue} IOE BE Year I / Part II $\cdot$ Academic Year 2080/2081/2082/2083}
\vspace*{1cm}
\end{titlepage}

\tableofcontents
\newpage

% ==============================================================================
% PREFACE & AUDIT SUMMARY
% ==============================================================================
\section*{Course Overview \& Critical Audit Summary}
\addcontentsline{toc}{section}{Course Overview \& Critical Audit Summary}

\subsection*{Syllabus \& Examination Weightage (ENEE 154)}
The evaluation scheme specified by the IOE Examination Control Division for \textbf{Electrical Circuits \& Machines (60 Marks, 3 Hours)} comprises 9 formal syllabus modules mapped directly into 10 structured final examination questions:

\begin{center}
\small
\begin{tabular}{@{}clccp{6.5cm}@{}}
\toprule
\textbf{Ch.} & \textbf{Syllabus Topic} & \textbf{Hours} & \textbf{Marks} & \textbf{Typical Exam Focus} \\
\midrule
1 & Transients in Electric Circuit & 7 & 7 & Nodal/Mesh Analysis with Dependent Sources; Initial Conditions ($i(0^+), v(0^+), \frac{di}{dt}, \frac{dv}{dt}$) \\
2 & Classical Transient Analysis & 10 & 10 & 1st \& 2nd order ODEs; Series/Parallel RLC DC and exponential excitation responses \\
3 & Laplace Transform Transients & 7 & 7 & $s$-domain impedance modeling with initial generators; Inverse Laplace transform \\
4 & Transfer Function \& Bode Plots & 8 & 8 & Poles, zeros, asymptotic magnitude \& phase Bode diagrams; Filter concepts \\
5 & Two-Port Network Parameters & 8 & 8 & $Z, Y, T/ABCD, h$ parameters; conversions; cascade interconnection \\
6 & Magnetic Circuits \& Induction & 3 & 3 & Series/Parallel magnetic circuits; Reluctance; $B$-$H$ curve; Hysteresis \& Eddy losses \\
7 & Transformers & 6 & 6 & Core flux independence; OC/SC test calculations; Efficiency \& Regulation \\
8 & DC Machines & 5 & 5 & Torque derivation; Generator EMF/characteristics; Back EMF; Starters \\
9 & AC Induction Motors & 6 & 6 & RMF production; Torque-speed curves; Slip calculations; Single-phase motors \\
\bottomrule
\end{tabular}
\end{center}

\subsection*{Comprehensive Audit of Errors in Previous Unofficial Solutions}
A rigorous audit of previous unverified answer keys revealed severe mathematical and topological errors in multiple circuit problems. This master volume resolves all discrepancies with complete mathematical proofs:

\begin{center}
\footnotesize
\begin{tabular}{@{}lp{4.2cm}p{4.2cm}p{5cm}@{}}
\toprule
\textbf{Paper / Question} & \textbf{Error in Old Solutions} & \textbf{Topological / Physics Reality} & \textbf{Corrected Master Solution} \\
\midrule
\textbf{2083 Baishakh Q1} & Connected $6\,\Omega$ resistor across $v_2-v_3$; inverted 10V polarity. & $6\,\Omega$ is connected between $v_1$ and $v_3$. 10V source has $(+)$ at $v_1$ and $(-)$ at $v_2$. & $v_1 = \frac{70}{23}\text{ V}, v_2 = -\frac{160}{23}\text{ V}, v_3 = \frac{15}{23}\text{ V}$. Current in 10V source $I_{10\text{V}} = 1.9203\text{ A}$ (from $v_2$ to $v_1$). \\
\addlinespace
\textbf{2083 Baishakh Q4} & Threw away $1\,\mathrm{F}$ capacitor upon switch opening; solved trivial 1st order RL. & Switch is placed before capacitor; opening disconnects 4V source, leaving parallel R-L-C loop. & 2nd-order underdamped loop: $i_L(t) = 4e^{-t}(\cos t + \sin t)\,\mathrm{A}$, $v_L(t) = -4e^{-t}\sin t\,\mathrm{V}$. \\
\addlinespace
\textbf{2082 Bhadra Q1} & Formulated 4 loops instead of 3 meshes; gave $I_x = 0\,\mathrm{A}, P = 0\,\mathrm{W}$. & Clear 3-mesh planar network with dependent source $10I_x$. & $I_1 = \frac{200}{33}\,\mathrm{A}, I_2 = \frac{40}{11}\,\mathrm{A}, I_3 = \frac{100}{33}\,\mathrm{A} \implies I_x = \frac{20}{33}\,\mathrm{A} \approx 0.606\,\mathrm{A}, P = 22.04\,\mathrm{W}$. \\
\addlinespace
\textbf{2082 Bhadra Q4} & Assumed capacitor charged before $t=0$ ($v_C=10\,\mathrm{V}, i_L=0$). & Position 'a' connects 10V to inductor ($i_L(0^-)=2\,\mathrm{A}$); capacitor at 'b' is uncharged. & Pure resonant LC loop: $i(t) = 2\cos(1000t)\,\mathrm{A}$ for $t \ge 0$. \\
\addlinespace
\textbf{2082 Bhadra Q5} & Inverted controlling current sign ($I_a = -I_2$). & Arrow for $I_a$ enters Port 2 matching standard port current $I_2 \implies I_a = I_2$. & $Z_{11} = 3-j2\,\Omega, Z_{12} = 2-j2\,\Omega, Z_{21} = -j2\,\Omega, Z_{22} = 3+j3\,\Omega$. \\
\addlinespace
\textbf{2082 Baishakh Q2} & Omitted $2\,\Omega$ resistor when switch threw to 'b'. & Switch blade connects $2\,\Omega$ in series with $6\,\Omega \implies 8\,\Omega$ branch across capacitor. & $i_L(0^+) = 2\,\mathrm{A}, i_{4\Omega} = 2\,\mathrm{A}, i_{8\Omega} = 1\,\mathrm{A}, i_C(0^+) = -3\,\mathrm{A}, \frac{di_L}{dt} = 0\,\mathrm{A/s}, \frac{dv_C}{dt} = -1.5\,\mathrm{V/s}$. \\
\addlinespace
\textbf{2081 Ashwin Q1} & Inverted 5V DC source polarity ($V_1-5-V_2$). & 5V battery has $(-)$ on left and $(+)$ on right $\implies$ potential is $V_1+5-V_2$. & $V_1 = -7.5\,\mathrm{V}, V_2 = -2.5\,\mathrm{V} \implies V_x = 0\,\mathrm{V}, I_{2\Omega} = -2.5\,\mathrm{A}$. \\
\addlinespace
\textbf{2081 Ashwin Q6} & Assumed $I_x = 0$ when $I_2=0$; gave passive $T$ matrix. & $I_x = V_2/5$ across Port 2; current from Port 1 flows through $5\,\Omega$ even when $I_2=0$. & $T = \begin{bmatrix} 2.6 & 8\,\Omega \\ 0.3\,\mathrm{S} & 1 \end{bmatrix}, AD-BC = 0.2 \ne 1$ (Active network). \\
\bottomrule
\end{tabular}
\end{center}

\newpage

% ==============================================================================
% CHAPTER 1: QUESTION 1 - DC NETWORK ANALYSIS
% ==============================================================================
\section{Question 1: DC Circuit Analysis (Mesh, Nodal \& Matrix Methods)}

% ------------------------------------------------------------------------------
% 1.1 2083 Baishakh Q1
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 1 [6 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q1)}
Find the current in 10 V source using nodal analysis for the circuit shown below:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  % Reference / Ground
  \draw (0,0) node[ground]{} -- (6,0);
  % Essential Nodes
  \draw (0,0) to[R, l=$2\,\Omega$, i>_=$i$] (0,2.5) node[circle, fill, inner sep=1.5pt, label=above left:{$v_1$}]{}
        to[V, v<=$10\,\mathrm{V}$] (3,2.5) node[circle, fill, inner sep=1.5pt, label=above:{$v_2$}]{}
        to[cV, v^<=$5i$] (6,2.5) node[circle, fill, inner sep=1.5pt, label=above right:{$v_3$}]{}
        to[R, l=$3\,\Omega$] (6,0);
  \draw (3,2.5) to[R, l=$4\,\Omega$] (3,0);
  \draw (0,2.5) -- (0,3.8) to[R, l=$6\,\Omega$] (6,3.8) -- (6,2.5);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}

\paragraph{Step 1: Circuit Topology \& Essential Node Identification}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Reference Node (Ground):} Select the bottom rail as the reference node ($0\,\mathrm{V}$).
  \item \textbf{Non-Reference Nodes:}
    \begin{itemize}
      \item $v_1$: Node above the $2\,\Omega$ resistor.
      \item $v_2$: Node above the $4\,\Omega$ resistor, between the $10\,\mathrm{V}$ source and the dependent voltage source.
      \item $v_3$: Node above the $3\,\Omega$ resistor.
    \end{itemize}
  \item \textbf{Controlling Variable $i$:} The current $i$ flows downward through the $2\,\Omega$ resistor from node $v_1$ to ground:
  \begin{equation}
    i = \frac{v_1 - 0}{2} = \frac{v_1}{2}
  \end{equation}
\end{itemize}

\paragraph{Step 2: Voltage Source Constraints \& Supernode Formation}
Because ideal voltage sources exist directly between nodes without series resistors, we form a generalized \textbf{Supernode} encompassing $(v_1, v_2, v_3)$:
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Independent 10 V Source Constraint:} The positive terminal is at node $v_1$ and the negative terminal is at node $v_2$:
  \begin{equation}
    v_1 - v_2 = 10 \implies v_2 = v_1 - 10
  \end{equation}
  \item \textbf{Dependent Source $5i$ Constraint:} The positive terminal is at node $v_3$ and the negative terminal is at node $v_2$:
  \begin{equation}
    v_3 - v_2 = 5i = 5\left(\frac{v_1}{2}\right) = 2.5 v_1 \implies v_3 = v_2 + 2.5 v_1
  \end{equation}
  Substituting $v_2 = v_1 - 10$ into the expression for $v_3$:
  \begin{equation}
    v_3 = (v_1 - 10) + 2.5 v_1 = 3.5 v_1 - 10
  \end{equation}
\end{enumerate}

\paragraph{Step 3: Kirchhoff's Current Law (KCL) at the Combined Supernode}
Summing all currents leaving the combined supernode $(v_1, v_2, v_3)$ to ground:
\begin{equation}
  \frac{v_1}{2} + \frac{v_2}{4} + \frac{v_3}{3} = 0
\end{equation}
\textit{Note:} The $6\,\Omega$ resistor is connected between node $v_1$ and node $v_3$. In the supernode KCL equation, the current leaving $v_1$ through the $6\,\Omega$ resistor is $\frac{v_1 - v_3}{6}$ and the current leaving $v_3$ through the same resistor is $\frac{v_3 - v_1}{6}$. Their sum is $\frac{v_1 - v_3}{6} + \frac{v_3 - v_1}{6} = 0$, correctly canceling out internally.

\paragraph{Step 4: Algebraic Solution for Node Voltages}
Substitute expressions for $v_2$ and $v_3$ in terms of $v_1$ into the supernode equation:
\begin{equation}
  \frac{v_1}{2} + \frac{v_1 - 10}{4} + \frac{3.5 v_1 - 10}{3} = 0
\end{equation}
Multiplying the entire equation by the common denominator $12$:
\begin{align*}
  6v_1 + 3(v_1 - 10) + 4(3.5 v_1 - 10) &= 0 \\
  6v_1 + 3v_1 - 30 + 14v_1 - 40 &= 0 \\
  23 v_1 - 70 &= 0 \implies v_1 = \frac{70}{23}\,\mathrm{V} \approx 3.0435\,\mathrm{V}
\end{align*}

Now evaluate $v_2$ and $v_3$:
\begin{align*}
  v_2 &= v_1 - 10 = \frac{70}{23} - 10 = -\frac{160}{23}\,\mathrm{V} \approx -6.9565\,\mathrm{V} \\
  v_3 &= 3.5 v_1 - 10 = 3.5\left(\frac{70}{23}\right) - 10 = \frac{245 - 230}{23} = \frac{15}{23}\,\mathrm{V} \approx 0.6522\,\mathrm{V} \\
  i &= \frac{v_1}{2} = \frac{35}{23}\,\mathrm{A} \approx 1.5217\,\mathrm{A}
\end{align*}

\paragraph{Step 5: Current through the 10 V Voltage Source}
Apply KCL specifically at \textbf{Node $v_1$}. Let $I_{10\text{V}}$ be the current flowing through the 10 V source from node $v_1$ to node $v_2$:
\begin{align*}
  \frac{v_1}{2} + \frac{v_1 - v_3}{6} + I_{10\text{V}} &= 0 \\
  I_{10\text{V}} &= -\left(\frac{v_1}{2} + \frac{v_1 - v_3}{6}\right) \\
  &= -\left(\frac{35}{23} + \frac{\frac{70}{23} - \frac{15}{23}}{6}\right) = -\left(\frac{35}{23} + \frac{55}{138}\right) = -\left(\frac{210 + 55}{138}\right) = -\frac{265}{138}\,\mathrm{A} \approx -1.9203\,\mathrm{A}
\end{align*}
The negative sign indicates that current actually enters node $v_1$ (flows from node $v_2$ to node $v_1$, delivering power).

\begin{answerbox}
\textbf{Node Voltages:}
\[
v_1 = \frac{70}{23}\,\mathrm{V} \approx +3.043\,\mathrm{V}, \quad v_2 = -\frac{160}{23}\,\mathrm{V} \approx -6.957\,\mathrm{V}, \quad v_3 = \frac{15}{23}\,\mathrm{V} \approx +0.652\,\mathrm{V}
\]
\textbf{Current in 10 V Source:}
\[
I_{10\text{V}} = 1.920\,\mathrm{A} \quad \text{(flowing from node $v_2$ to node $v_1$)} \quad \left[\text{or } -1.920\,\mathrm{A}\text{ from } v_1 \text{ to } v_2\right]
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 1.2 2082 Bhadra Q1
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 1 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q1)}
Find the current $I_x$ and power delivered by the dependent voltage source in the circuit shown below using Mesh Analysis:
\begin{center}
\begin{circuitikz}[american, scale=1.05, transform shape]
  % Bottom wire
  \draw (0,0) -- (6,0);
  % Leftmost branch
  \draw (0,0) to[cV, v^<=$10I_x$] (0,2.5) to[V, v<=$100\,\mathrm{V}$] (0,5)
        to[R, l=$5\,\Omega$] (3,5);
  % Middle horizontal resistor
  \draw (0,2.5) to[R, l=$10\,\Omega$] (3,2.5);
  % Middle vertical resistors
  \draw (3,5) to[R, l=$15\,\Omega$] (3,2.5) to[R, l=$50\,\Omega$, i>_=$I_x$] (3,0);
  % Right loop
  \draw (3,5) -- (6,5) to[R, l=$25\,\Omega$] (6,0);
  % Mesh current labels
  \draw (1.5, 3.75) node{\Large $\circlearrowright$} node[above=0.2cm]{$I_1$};
  \draw (1.5, 1.25) node{\Large $\circlearrowright$} node[above=0.2cm]{$I_2$};
  \draw (4.5, 2.5) node{\Large $\circlearrowright$} node[above=0.2cm]{$I_3$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}

\paragraph{Step 1: Mesh Definition \& Controlling Variable Expression}
Assign standard clockwise mesh currents:
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Mesh 1 (Top-Left Loop):} Mesh current $I_1$ flows clockwise through the $100\,\mathrm{V}$ source, $5\,\Omega$ resistor, $15\,\Omega$ resistor, and $10\,\Omega$ resistor.
  \item \textbf{Mesh 2 (Bottom-Left Loop):} Mesh current $I_2$ flows clockwise through the dependent source $10I_x$, $10\,\Omega$ resistor, $50\,\Omega$ resistor, and bottom rail.
  \item \textbf{Mesh 3 (Right Loop):} Mesh current $I_3$ flows clockwise through the top wire, $25\,\Omega$ resistor, bottom rail, $50\,\Omega$ resistor, and $15\,\Omega$ resistor.
  \item \textbf{Controlling Current $I_x$:} Current $I_x$ flows downward through the $50\,\Omega$ resistor:
  \begin{equation}
    I_x = I_2 - I_3
  \end{equation}
\end{itemize}

\paragraph{Step 2: Formulating Kirchhoff's Voltage Law (KVL) for Each Mesh}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Mesh 1 KVL (Clockwise):}
  \begin{align}
    +100 - 5 I_1 - 15(I_1 - I_3) - 10(I_1 - I_2) &= 0 \nonumber \\
    -30 I_1 + 10 I_2 + 15 I_3 &= -100 \implies 30 I_1 - 10 I_2 - 15 I_3 = 100 \quad \text{--- (Eq. 1)}
  \end{align}

  \item \textbf{Mesh 2 KVL (Clockwise):}
  The dependent source has $(+)$ at top and $(-)$ at bottom; moving clockwise (upward) through it yields a voltage rise $+10I_x$:
  \begin{align}
    +10 I_x - 10(I_2 - I_1) - 50(I_2 - I_3) &= 0 \nonumber \\
    10(I_2 - I_3) - 10 I_2 + 10 I_1 - 50 I_2 + 50 I_3 &= 0 \nonumber \\
    10 I_1 - 50 I_2 + 40 I_3 &= 0 \implies I_1 - 5 I_2 + 4 I_3 = 0 \quad \text{--- (Eq. 2)}
  \end{align}

  \item \textbf{Mesh 3 KVL (Clockwise):}
  \begin{align}
    -25 I_3 - 50(I_3 - I_2) - 15(I_3 - I_1) &= 0 \nonumber \\
    15 I_1 + 50 I_2 - 90 I_3 &= 0 \implies 3 I_1 + 10 I_2 - 18 I_3 = 0 \quad \text{--- (Eq. 3)}
  \end{align}
\end{enumerate}

\paragraph{Step 3: Matrix System \& Solution}
Writing Equations (1), (2), (3) in standard matrix form $\mathbf{A} \cdot \mathbf{I} = \mathbf{B}$:
\begin{equation}
\begin{bmatrix}
30 & -10 & -15 \\
1 & -5 & 4 \\
3 & 10 & -18
\end{bmatrix}
\begin{bmatrix}
I_1 \\ I_2 \\ I_3
\end{bmatrix}
=
\begin{bmatrix}
100 \\ 0 \\ 0
\end{bmatrix}
\end{equation}

Solving via Determinants (Cramer's Rule):
\begin{align*}
\Delta &= 30[(-5)(-18) - (4)(10)] - (-10)[(1)(-18) - (4)(3)] + (-15)[(1)(10) - (-5)(3)] \\
&= 30[90 - 40] + 10[-18 - 12] - 15[10 + 15] \\
&= 30(50) + 10(-30) - 15(25) = 1500 - 300 - 375 = 825
\end{align*}
\begin{align*}
\Delta_1 &= 100[(-5)(-18) - (4)(10)] = 100(50) = 5000 \implies I_1 = \frac{5000}{825} = \frac{200}{33}\,\mathrm{A} \approx 6.0606\,\mathrm{A} \\
\Delta_2 &= -100[(1)(-18) - (4)(3)] = -100(-30) = 3000 \implies I_2 = \frac{3000}{825} = \frac{120}{33} = \frac{40}{11}\,\mathrm{A} \approx 3.6364\,\mathrm{A} \\
\Delta_3 &= 100[(1)(10) - (-5)(3)] = 100(25) = 2500 \implies I_3 = \frac{2500}{825} = \frac{100}{33}\,\mathrm{A} \approx 3.0303\,\mathrm{A}
\end{align*}

\paragraph{Step 4: Branch Current $I_x$ \& Power Delivered}
\begin{equation}
  I_x = I_2 - I_3 = \frac{120}{33} - \frac{100}{33} = \frac{20}{33}\,\mathrm{A} \approx 0.6061\,\mathrm{A}
\end{equation}
The voltage across the dependent source is:
\begin{equation}
  V_{\text{dep}} = 10 I_x = 10 \left(\frac{20}{33}\right) = \frac{200}{33}\,\mathrm{V} \approx 6.0606\,\mathrm{V}
\end{equation}
Current leaving the positive terminal of the dependent source is $I_2 = \frac{40}{11}\,\mathrm{A}$. Therefore, the power delivered by the dependent source is:
\begin{equation}
  P_{\text{del}} = V_{\text{dep}} \cdot I_2 = \left(\frac{200}{33}\right) \left(\frac{40}{11}\right) = \frac{8000}{363}\,\mathrm{W} \approx 22.0386\,\mathrm{W}
\end{equation}

\begin{answerbox}
\textbf{Controlling Current:}
\[
I_x = \frac{20}{33}\,\mathrm{A} \approx 0.606\,\mathrm{A}
\]
\textbf{Power Delivered by Dependent Source ($10I_x$):}
\[
P_{\text{del}} = \frac{8000}{363}\,\mathrm{W} \approx 22.04\,\mathrm{W}
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 1.3 2082 Baishakh Q1
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 1 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q1)}
In the given circuit, determine $V_x$ and power consumed by it using mesh analysis and solve by matrix method:
\begin{center}
\begin{circuitikz}[american, scale=1.05, transform shape]
  % Rails
  \draw (0,0) -- (6,0);
  \draw (0,4) -- (6,4);
  % Left branch
  \draw (0,4) to[isource, l=$-10\,\mathrm{A}$] (0,0);
  % Middle vertical branches
  \draw (2.5,4) to[R, l=$1\,\Omega$] (2.5,2) to[cI, l=$V_x/10$] (2.5,0);
  % Horizontal branch with Vx
  \draw (2.5,2) to[R, l=$3\,\Omega$, v=$V_x$] (5,2);
  % Right vertical branches
  \draw (5,4) to[R, l=$2\,\Omega$] (5,2) to[R, l=$5\,\Omega$] (5,0);
  \draw (5,4) -- (6,4) -- (6,0) -- (5,0);
  % Mesh current labels
  \draw (1.2, 2.0) node{\Large $\circlearrowright$} node[above=0.15cm]{$I_1$};
  \draw (3.75, 3.0) node{\Large $\circlearrowright$} node[above=0.15cm]{$I_2$};
  \draw (3.75, 1.0) node{\Large $\circlearrowright$} node[above=0.15cm]{$I_3$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}

\paragraph{Step 1: Mesh Currents \& Dependent Source Constraint}
Let clockwise mesh currents be $I_1$ (left mesh), $I_2$ (top-right mesh), and $I_3$ (bottom-right mesh):
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Mesh 1 Current:} The independent current source of $-10\,\mathrm{A}$ (directed downward) lies solely in Mesh 1:
  \begin{equation}
    I_1 = -10\,\mathrm{A}
  \end{equation}
  \item \textbf{Branch Voltage $V_x$:} $V_x$ is the voltage across the $3\,\Omega$ resistor with $(+)$ on the left and $(-)$ on the right. Mesh 2 current flows left-to-right, while Mesh 3 current flows right-to-left:
  \begin{equation}
    V_x = 3(I_2 - I_3)
  \end{equation}
  \item \textbf{Dependent Current Source Constraint:} The dependent current source $V_x/10$ is downward between Mesh 1 and Mesh 3:
  \begin{equation}
    I_1 - I_3 = \frac{V_x}{10} \implies -10 - I_3 = \frac{3(I_2 - I_3)}{10}
  \end{equation}
  Clearing fractions:
  \begin{equation}
    -100 - 10 I_3 = 3 I_2 - 3 I_3 \implies 3 I_2 + 7 I_3 = -100 \quad \text{--- (Eq. 1)}
  \end{equation}
\end{enumerate}

\paragraph{Step 2: Mesh 2 KVL Equation}
Applying KVL clockwise around Mesh 2 ($1\,\Omega, 2\,\Omega, 3\,\Omega$):
\begin{align}
  1(I_2 - I_1) + 2 I_2 + 3(I_2 - I_3) &= 0 \nonumber \\
  1(I_2 - (-10)) + 2 I_2 + 3 I_2 - 3 I_3 &= 0 \nonumber \\
  6 I_2 - 3 I_3 &= -10 \quad \text{--- (Eq. 2)}
\end{align}

\paragraph{Step 3: Matrix System Formulation \& Solution via Cramer's Rule}
Writing Equations (2) and (1) in matrix form $\mathbf{A} \cdot \mathbf{I} = \mathbf{B}$:
\begin{equation}
\begin{bmatrix}
6 & -3 \\
3 & 7
\end{bmatrix}
\begin{bmatrix}
I_2 \\ I_3
\end{bmatrix}
=
\begin{bmatrix}
-10 \\ -100
\end{bmatrix}
\end{equation}
Calculating determinants:
\begin{align*}
\Delta &= (6)(7) - (-3)(3) = 42 + 9 = 51 \\
\Delta_2 &= (-10)(7) - (-3)(-100) = -70 - 300 = -370 \implies I_2 = \frac{-370}{51} \approx -7.2549\,\mathrm{A} \\
\Delta_3 &= (6)(-100) - (-10)(3) = -600 + 30 = -570 \implies I_3 = \frac{-570}{51} = -\frac{190}{17} \approx -11.1765\,\mathrm{A}
\end{align*}

\paragraph{Step 4: Computation of $V_x$ and Power Consumed}
\begin{align*}
  V_x &= 3(I_2 - I_3) = 3\left(-\frac{370}{51} - \left(-\frac{570}{51}\right)\right) = 3\left(\frac{200}{51}\right) = \frac{200}{17}\,\mathrm{V} \approx 11.7647\,\mathrm{V}
\end{align*}
Power consumed by the $3\,\Omega$ resistor ($V_x$ element):
\begin{equation}
  P_{3\Omega} = \frac{V_x^2}{R} = \frac{(11.7647)^2}{3} = \frac{138.408}{3} \approx 46.136\,\mathrm{W}
\end{equation}

\begin{answerbox}
\textbf{Branch Voltage:}
\[
V_x = \frac{200}{17}\,\mathrm{V} \approx 11.76\,\mathrm{V}
\]
\textbf{Power Consumed by $3\,\Omega$ Resistor ($V_x$ element):}
\[
P = 46.14\,\mathrm{W}
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 1.4 2081 Ashwin Q1
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 1 [6 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q1)}
Using Nodal analysis and matrix solution method, find $V_x$ and the current in $2\,\Omega$ resistance:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  % Reference
  \draw (0,0) node[ground]{} -- (5.5,0);
  % Nodes
  \draw (0,0) to[isource, l=$5\,\mathrm{A}$] (0,2.5) node[circle, fill, inner sep=1.5pt, label=above left:{$V_1$}]{}
        to[V, v<=$5\,\mathrm{V}$] (2.75,2.5)
        to[R, l=$4\,\Omega$, v=$V_x$] (5.5,2.5) node[circle, fill, inner sep=1.5pt, label=above right:{$V_2$}]{};
  \draw (0,2.5) to[R, l=$3\,\Omega$] (0,0);
  \draw (5.5,0) to[cI, l=$4V_x$] (5.5,2.5);
  \draw (5.5,2.5) to[R, l=$1\,\Omega$] (5.5,0);
  % Top 2 ohm resistor
  \draw (0,2.5) -- (0,4) to[R, l=$2\,\Omega$] (5.5,4) -- (5.5,2.5);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}

\paragraph{Step 1: Branch Expressions \& Controlling Voltage $V_x$}
\begin{itemize}[leftmargin=1.5em]
  \item Ground is selected at the bottom rail ($0\,\mathrm{V}$).
  \item The branch between $V_1$ and $V_2$ contains a $5\,\mathrm{V}$ source in series with a $4\,\Omega$ resistor.
  \item The $5\,\mathrm{V}$ source has its negative terminal connected to $V_1$ and its positive terminal connected to the $4\,\Omega$ resistor. Thus, the potential at the left terminal of the $4\,\Omega$ resistor is $V_1 + 5\,\mathrm{V}$.
  \item The voltage $V_x$ across the $4\,\Omega$ resistor (with $+$ at the left and $-$ at the right) is:
  \begin{equation}
    V_x = (V_1 + 5) - V_2 = V_1 - V_2 + 5
  \end{equation}
\end{itemize}

\paragraph{Step 2: Nodal KCL Equations}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{KCL at Node $V_1$:}
  \begin{align}
    \frac{V_1}{3} + 5 + \frac{V_1 - V_2}{2} + \frac{V_1 + 5 - V_2}{4} &= 0 \nonumber
  \end{align}
  Multiplying by 12:
  \begin{align}
    4V_1 + 60 + 6(V_1 - V_2) + 3(V_1 - V_2 + 5) &= 0 \nonumber \\
    4V_1 + 60 + 6V_1 - 6V_2 + 3V_1 - 3V_2 + 15 &= 0 \nonumber \\
    13 V_1 - 9 V_2 &= -75 \quad \text{--- (Eq. 1)}
  \end{align}

  \item \textbf{KCL at Node $V_2$:}
  \begin{align}
    \frac{V_2}{1} + \frac{V_2 - V_1}{2} + \frac{V_2 - (V_1 + 5)}{4} - 4V_x &= 0 \nonumber
  \end{align}
  Substitute $V_x = V_1 - V_2 + 5$:
  \begin{align}
    V_2 + \frac{V_2 - V_1}{2} + \frac{V_2 - V_1 - 5}{4} - 4(V_1 - V_2 + 5) &= 0 \nonumber
  \end{align}
  Multiplying by 4:
  \begin{align}
    4V_2 + 2(V_2 - V_1) + (V_2 - V_1 - 5) - 16(V_1 - V_2 + 5) &= 0 \nonumber \\
    4V_2 + 2V_2 - 2V_1 + V_2 - V_1 - 5 - 16V_1 + 16V_2 - 80 &= 0 \nonumber \\
    -19 V_1 + 23 V_2 &= 85 \quad \text{--- (Eq. 2)}
  \end{align}
\end{enumerate}

\paragraph{Step 3: Matrix System Formulation \& Cramer's Rule Solution}
\begin{equation}
\begin{bmatrix}
13 & -9 \\
-19 & 23
\end{bmatrix}
\begin{bmatrix}
V_1 \\ V_2
\end{bmatrix}
=
\begin{bmatrix}
-75 \\ 85
\end{bmatrix}
\end{equation}
\begin{align*}
\Delta &= (13)(23) - (-9)(-19) = 299 - 171 = 128 \\
\Delta_1 &= (-75)(23) - (-9)(85) = -1725 + 765 = -960 \implies V_1 = \frac{-960}{128} = -7.5\,\mathrm{V} \\
\Delta_2 &= (13)(85) - (-75)(-19) = 1105 - 1425 = -320 \implies V_2 = \frac{-320}{128} = -2.5\,\mathrm{V}
\end{align*}

\paragraph{Step 4: Final Parameters}
\begin{align*}
  V_x &= V_1 - V_2 + 5 = -7.5 - (-2.5) + 5 = -5.0 + 5.0 = 0\,\mathrm{V} \\
  I_{2\Omega} &= \frac{V_1 - V_2}{2} = \frac{-7.5 - (-2.5)}{2} = \frac{-5.0}{2} = -2.5\,\mathrm{A} \quad \text{(from $V_1$ to $V_2$)}
\end{align*}

\begin{answerbox}
\textbf{Node Voltages:} $V_1 = -7.5\,\mathrm{V}, \quad V_2 = -2.5\,\mathrm{V}$ \\
\textbf{Branch Voltage:} $V_x = 0\,\mathrm{V}$ \\
\textbf{Current in $2\,\Omega$ Resistor:} $I_{2\Omega} = 2.5\,\mathrm{A}$ (flowing from node $V_2$ to node $V_1$).
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 2: QUESTION 2 - INITIAL CONDITIONS IN TRANSIENTS
% ==============================================================================
\section{Question 2: Initial \& Final Value Conditions in Switching Transients}

\begin{conceptbox}{Continuity Laws in Switching Circuits}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Inductor Current Continuity:} Current through an inductor cannot change instantaneously due to finite stored magnetic energy ($E = \frac{1}{2}LI^2$). Hence, $i_L(0^+) = i_L(0^-)$. At $t=0^+$, an inductor acts as a current source of value $i_L(0^-)$ (open circuit if unenergized).
  \item \textbf{Capacitor Voltage Continuity:} Voltage across a capacitor cannot change instantaneously due to finite stored electrostatic energy ($E = \frac{1}{2}CV^2$). Hence, $v_C(0^+) = v_C(0^-)$. At $t=0^+$, a capacitor acts as a voltage source of value $v_C(0^-)$ (short circuit if uncharged).
  \item \textbf{Derivative Relations:} $\left.\frac{di_L}{dt}\right|_{0^+} = \frac{v_L(0^+)}{L}$ and $\left.\frac{dv_C}{dt}\right|_{0^+} = \frac{i_C(0^+)}{C}$.
\end{itemize}
\end{conceptbox}

% ------------------------------------------------------------------------------
% 2.1 2083 Baishakh Q2
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 2 [5 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q2)}
Obtain the value of $i_1, i_2, \frac{di_1}{dt}, \frac{di_2}{dt}$ at $t = 0^+$, if the switch is closed at $t = 0$ in the circuit shown:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$10\,\mathrm{V}$] (0,2.5) -- (0.8,2.5);
  % Explicit custom switch
  \draw (0.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw (1.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw[thick] (0.8,2.5) -- (1.6,3.0);
  \draw[->, >=stealth] (1.3,3.1) to[bend left=30] (1.5,2.6);
  \node[above] at (1.3,3.2) {$t=0$};
  \draw (1.8,2.5) to[L, l=$1\,\mathrm{H}$] (3.5,2.5) to[R, l=$10\,\Omega$] (6,2.5)
        to[C, l=$1\,\mathrm{F}$] (6,0) -- (0,0);
  \draw (3.5,2.5) to[R, l=$10\,\Omega$] (3.5,0);
  \draw (1.75, 1.25) node{\Large $\circlearrowright$} node[above=0.15cm]{$i_1(t)$};
  \draw (4.75, 1.25) node{\Large $\circlearrowright$} node[above=0.15cm]{$i_2(t)$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Initial Energy State at $t = 0^-$:}
Before $t=0$, the switch is open and the network is completely relaxed:
\[
i_L(0^-) = i_1(0^-) = 0\,\mathrm{A}, \qquad v_C(0^-) = 0\,\mathrm{V}
\]
By the continuity laws:
\[
i_1(0^+) = i_L(0^+) = 0\,\mathrm{A}, \qquad v_C(0^+) = 0\,\mathrm{V}
\]
\paragraph{2. Evaluation of $i_2(0^+)$:}
Loop 2 KVL at $t=0^+$:
\[
10(i_2(0^+) - i_1(0^+)) + 10 i_2(0^+) + v_C(0^+) = 0 \implies 20 i_2(0^+) - 0 + 0 = 0 \implies i_2(0^+) = 0\,\mathrm{A}
\]
\paragraph{3. Evaluation of $\left.\frac{di_1}{dt}\right|_{t=0^+}$:}
Applying KVL to Loop 1 at $t=0^+$:
\begin{align*}
  10 - L \left.\frac{di_1}{dt}\right|_{0^+} - 10(i_1(0^+) - i_2(0^+)) &= 0 \\
  10 - (1) \left.\frac{di_1}{dt}\right|_{0^+} - 10(0 - 0) &= 0 \implies \left.\frac{di_1}{dt}\right|_{0^+} = 10\,\mathrm{A/s}
\end{align*}
\paragraph{4. Evaluation of $\left.\frac{di_2}{dt}\right|_{t=0^+}$:}
The time-domain KVL equation for Loop 2 is:
\[
10(i_2(t) - i_1(t)) + 10 i_2(t) + v_C(t) = 0 \implies 20 i_2(t) - 10 i_1(t) + v_C(t) = 0
\]
Differentiating with respect to $t$:
\[
20 \frac{di_2}{dt} - 10 \frac{di_1}{dt} + \frac{dv_C}{dt} = 0
\]
Since $\left.\frac{dv_C}{dt}\right|_{0^+} = \frac{i_C(0^+)}{C} = \frac{i_2(0^+)}{1} = 0$:
\[
20 \left.\frac{di_2}{dt}\right|_{0^+} - 10(10) + 0 = 0 \implies 20 \left.\frac{di_2}{dt}\right|_{0^+} = 100 \implies \left.\frac{di_2}{dt}\right|_{0^+} = 5\,\mathrm{A/s}
\]

\begin{answerbox}
\[
i_1(0^+) = 0\,\mathrm{A}, \quad i_2(0^+) = 0\,\mathrm{A}, \quad \left.\frac{di_1}{dt}\right|_{0^+} = 10\,\mathrm{A/s}, \quad \left.\frac{di_2}{dt}\right|_{0^+} = 5\,\mathrm{A/s}
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 2.2 2082 Bhadra Q2
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 2 [1 + 4 = 5 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q2)}
Explain the behavior of inductor when subjected to switching. In the network, the switch is opened at $t = 0$. Calculate $v, \frac{dv}{dt}$ and $\frac{d^2v}{dt^2}$ at $t = 0^+$ if $I = 2\,\mathrm{A}, R = 200\,\Omega$ and $L = 1\,\mathrm{H}$. Given that $v$ is the voltage across inductor:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[isource, l=$I$] (0,2.5) -- (1.8,2.5);
  \draw (1.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw (1.8,0) node[circle, fill, inner sep=1.2pt]{};
  \draw[thick] (1.8,0) -- (1.8,2.1);
  \draw[->, >=stealth] (1.8,1.7) to[bend right=30] (2.3,1.9);
  \node[right] at (2.3,1.7) {$K,\,t=0$};
  \draw (1.8,2.5) -- (3.5,2.5) to[R, l=$R$] (3.5,0);
  \draw (3.5,2.5) -- (5.2,2.5) to[L, l=$L$, i>_=$i_L$, v=$v(t)$] (5.2,0) -- (0,0);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Part A: Physical Behavior of Inductor under Switching}
An inductor stores energy in its magnetic field ($E = \frac{1}{2}LI^2$). The current cannot change instantaneously ($\Delta t \to 0$) because $\frac{di}{dt} \to \infty$ would require an infinite induced voltage ($v = L\frac{di}{dt} \to \infty$) and infinite power, violating the physical law of conservation of energy. Hence, $i_L(0^+) = i_L(0^-)$. Immediately after switching, an unenergized inductor behaves as an \textbf{open circuit}.

\subsubsection*{Part B: Mathematical Calculations}
\paragraph{1. Initial Conditions ($t=0^-$):}
Prior to $t=0$, switch $K$ is closed, creating an ideal short circuit across $R$ and $L$. Hence, all current from $I$ circulates through switch $K$:
\[
i_L(0^-) = 0\,\mathrm{A} \implies i_L(0^+) = 0\,\mathrm{A}
\]
\paragraph{2. Finding $v(0^+)$:}
At $t = 0^+$, switch $K$ opens. Current $I = 2\,\mathrm{A}$ enters the parallel combination of $R$ and $L$:
\[
I = i_R(t) + i_L(t) \implies i_R(0^+) = I - i_L(0^+) = 2 - 0 = 2\,\mathrm{A}
\]
The voltage across the inductor $v(t)$ equals the voltage across resistor $R$:
\[
v(0^+) = R \cdot i_R(0^+) = 200 \times 2 = 400\,\mathrm{V}
\]
\paragraph{3. Finding $\left.\frac{dv}{dt}\right|_{0^+}$:}
From $v(t) = R(I - i_L(t))$, differentiating with respect to $t$:
\[
\frac{dv}{dt} = -R \frac{di_L}{dt} = -R \left(\frac{v(t)}{L}\right) = -\frac{R}{L} v(t)
\]
At $t = 0^+$:
\[
\left.\frac{dv}{dt}\right|_{0^+} = -\frac{200}{1} \times 400 = -80,000\,\mathrm{V/s} = -8 \times 10^4\,\mathrm{V/s}
\]
\paragraph{4. Finding $\left.\frac{d^2v}{dt^2}\right|_{0^+}$:}
Differentiating once more:
\[
\frac{d^2v}{dt^2} = -\frac{R}{L} \frac{dv}{dt} \implies \left.\frac{d^2v}{dt^2}\right|_{0^+} = -200 \times (-80,000) = +1.6 \times 10^7\,\mathrm{V/s}^2
\]

\begin{answerbox}
\[
v(0^+) = 400\,\mathrm{V}, \quad \left.\frac{dv}{dt}\right|_{0^+} = -80,000\,\mathrm{V/s}, \quad \left.\frac{d^2v}{dt^2}\right|_{0^+} = +1.6 \times 10^7\,\mathrm{V/s}^2
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 2.3 2082 Baishakh Q2
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 2 [5 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q2)}
In the network shown below, the switch has been in position $a$ for a long time. At $t = 0$, it is suddenly thrown off to position $b$. Find current through each element, $\frac{di_L}{dt}$ of coil and $\frac{dv_C}{dt}$ of capacitor at $t = 0^+$:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$12\,\mathrm{V}$] (0,2.5) -- (1.5,2.5) node[circle, fill, inner sep=1.2pt, label=below:{$a$}]{};
  \draw (2.2,1.5) node[circle, fill, inner sep=1.2pt, label=below:{$b$}]{} to[R, l=$6\,\Omega$] (2.2,0);
  \draw (2.0,2.5) node[circle, fill, inner sep=1.2pt]{} -- (2.7,2.5) to[R, l=$2\,\Omega$] (4.2,2.5)
        to[R, l=$4\,\Omega$] (6.0,2.5) to[L, l=$3\,\mathrm{H}$, i>_=$i_L$] (6.0,0) -- (0,0);
  \draw (4.2,2.5) to[C, l=$2\,\mathrm{F}$, v=$v_C$] (4.2,0);
  \draw[->, thick] (1.5,2.7) to[bend left=30] (2.2,1.7);
  \node at (1.8, 3.1) {$t=0$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Steady-State at $t = 0^-$ (Switch at Position $a$):}
For $t < 0$, the $12\,\mathrm{V}$ DC supply is connected through the $2\,\Omega$ resistor. In DC steady state:
\begin{itemize}[leftmargin=1.5em]
  \item Inductor is a short circuit; Capacitor is an open circuit.
  \item Total DC resistance = $2\,\Omega + 4\,\Omega = 6\,\Omega$.
  \item Inductor current: $i_L(0^-) = \frac{12}{2 + 4} = 2\,\mathrm{A}$.
  \item Capacitor voltage (across the $4\,\Omega$ resistor): $v_C(0^-) = i_L(0^-) \times 4\,\Omega = 2 \times 4 = 8\,\mathrm{V}$.
\end{itemize}
By continuity:
\[
i_L(0^+) = 2\,\mathrm{A}, \qquad v_C(0^+) = 8\,\mathrm{V}
\]

\paragraph{2. Response at $t = 0^+$ (Switch at Position $b$):}
At $t=0$, the blade connects the $2\,\Omega$ resistor to terminal $b$ ($6\,\Omega$ resistor to ground). The $12\,\mathrm{V}$ source is completely isolated.
\begin{itemize}[leftmargin=1.5em]
  \item The branch to the left of the capacitor consists of $2\,\Omega + 6\,\Omega = 8\,\Omega$ connected across node voltage $v_C(0^+) = 8\,\mathrm{V}$.
  \item Current leaving the capacitor node to the left through the $(2+6)\,\Omega$ branch:
  \[
  i_{\text{branch } b}(0^+) = \frac{v_C(0^+)}{2 + 6} = \frac{8}{8} = 1\,\mathrm{A}
  \]
  \item Current through the $4\,\Omega$ resistor: In series with inductor, so $i_{4\Omega}(0^+) = i_L(0^+) = 2\,\mathrm{A}$.
  \item Current through the capacitor $i_C(0^+)$: Applying KCL at the node above the capacitor:
  \[
  i_C(0^+) + i_{\text{branch } b}(0^+) + i_L(0^+) = 0 \implies i_C(0^+) = -1 - 2 = -3\,\mathrm{A}
  \]
\end{itemize}

\paragraph{3. Derivatives at $t = 0^+$:}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{For Inductor:} Across the inductor branch, $v_C(t) = 4 i_L(t) + L \frac{di_L}{dt}$. At $t=0^+$:
  \[
  8 = 4(2) + 3 \left.\frac{di_L}{dt}\right|_{0^+} \implies 3 \left.\frac{di_L}{dt}\right|_{0^+} = 0 \implies \left.\frac{di_L}{dt}\right|_{0^+} = 0\,\mathrm{A/s}
  \]
  \item \textbf{For Capacitor:} Using $i_C(t) = C \frac{dv_C}{dt}$:
  \[
  \left.\frac{dv_C}{dt}\right|_{0^+} = \frac{i_C(0^+)}{C} = \frac{-3}{2} = -1.5\,\mathrm{V/s}
  \]
\end{itemize}

\begin{answerbox}
\textbf{Element Currents at $t=0^+$:} $i_L(0^+) = 2\,\mathrm{A}, \quad i_{4\Omega}(0^+) = 2\,\mathrm{A}, \quad i_{\text{branch } b}(0^+) = 1\,\mathrm{A}, \quad i_C(0^+) = -3\,\mathrm{A}$ \\
\textbf{Derivatives at $t=0^+$:} $\left.\frac{di_L}{dt}\right|_{0^+} = 0\,\mathrm{A/s}, \quad \left.\frac{dv_C}{dt}\right|_{0^+} = -1.5\,\mathrm{V/s}$
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 2.4 2081 Ashwin Q2
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 2 [5 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q2)}
Obtain the value of $i_1, i_2, \frac{di_1}{dt}, \frac{di_2}{dt}$ at $t = 0^+$, if the switch is closed at $t = 0$ in the circuit shown below:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$10\,\mathrm{V}$] (0,2.5) -- (0.8,2.5);
  \draw (0.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw (1.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw[thick] (0.8,2.5) -- (1.6,3.0);
  \draw[->, >=stealth] (1.3,3.1) to[bend left=30] (1.5,2.6);
  \node[above] at (1.3,3.2) {$t=0$};
  \draw (1.8,2.5) to[L, l=$1\,\mathrm{H}$] (3.5,2.5) to[R, l=$10\,\Omega$] (6,2.5)
        to[C, l=$1\,\mathrm{F}$] (6,0) -- (0,0);
  \draw (3.5,2.5) to[R, l=$10\,\Omega$] (3.5,0);
  \draw (1.75, 1.25) node{\Large $\circlearrowright$} node[above=0.15cm]{$i_1(t)$};
  \draw (4.75, 1.25) node{\Large $\circlearrowright$} node[above=0.15cm]{$i_2(t)$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Initial Conditions ($t=0^-$):}
Circuit is unenergized before switch closure:
\[
i_1(0^-) = 0\,\mathrm{A}, \quad v_C(0^-) = 0\,\mathrm{V} \implies i_1(0^+) = 0\,\mathrm{A}, \quad v_C(0^+) = 0\,\mathrm{V}
\]
\paragraph{2. Values at $t=0^+$:}
\[
i_2(0^+) = 0\,\mathrm{A}
\]
From Loop 1 KVL at $t=0^+$:
\[
10 - 1 \cdot \left.\frac{di_1}{dt}\right|_{0^+} - 10(0 - 0) = 0 \implies \left.\frac{di_1}{dt}\right|_{0^+} = 10\,\mathrm{A/s}
\]
From differentiated Loop 2 KVL:
\[
20 \left.\frac{di_2}{dt}\right|_{0^+} - 10 \left.\frac{di_1}{dt}\right|_{0^+} + \left.\frac{dv_C}{dt}\right|_{0^+} = 0 \implies 20 \left.\frac{di_2}{dt}\right|_{0^+} - 10(10) + 0 = 0 \implies \left.\frac{di_2}{dt}\right|_{0^+} = 5\,\mathrm{A/s}
\]

\begin{answerbox}
\[
i_1(0^+) = 0\,\mathrm{A}, \quad i_2(0^+) = 0\,\mathrm{A}, \quad \left.\frac{di_1}{dt}\right|_{0^+} = 10\,\mathrm{A/s}, \quad \left.\frac{di_2}{dt}\right|_{0^+} = 5\,\mathrm{A/s}
\]
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 3: QUESTION 3 - CLASSICAL TRANSIENT ANALYSIS
% ==============================================================================
\section{Question 3: Classical Transient Analysis (Differential Equation Method)}

% ------------------------------------------------------------------------------
% 3.1 2083 Baishakh Q3
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 3 [6 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q3)}
Derive the expression of current in series RC circuit excited by exponential voltage source by using classical method.
\end{questionbox}

\subsubsection*{Detailed Analytical Derivation}

\paragraph{Step 1: Governing Differential Equation}
Consider a series $RC$ circuit excited at $t=0$ by an exponential source $v(t) = V_0 e^{-at}$ ($t \ge 0$). Applying KVL:
\begin{equation}
  R i(t) + \frac{1}{C} \int i(t)\,dt = V_0 e^{-at}
\end{equation}
Differentiating with respect to $t$:
\begin{equation}
  R \frac{di}{dt} + \frac{1}{C} i(t) = -a V_0 e^{-at} \implies \frac{di}{dt} + \frac{1}{RC} i(t) = -\frac{a V_0}{R} e^{-at}
\end{equation}
Let $\alpha = \frac{1}{RC}$ be the natural circuit inverse time-constant:
\begin{equation}
  \frac{di}{dt} + \alpha i(t) = -\frac{a V_0}{R} e^{-at}
\end{equation}

\paragraph{Step 2: Complementary Function $i_{cf}(t)$}
The homogeneous equation $\frac{di}{dt} + \alpha i = 0$ has characteristic root $s = -\alpha$:
\begin{equation}
  i_{cf}(t) = K e^{-\alpha t} = K e^{-\frac{t}{RC}}
\end{equation}

\paragraph{Step 3: Particular Integral $i_{pi}(t)$ (Assuming $a \ne \alpha$)}
Trial solution $i_{pi}(t) = A e^{-at}$. Substituting into the non-homogeneous ODE:
\begin{align*}
  -a A e^{-at} + \alpha A e^{-at} &= -\frac{a V_0}{R} e^{-at} \\
  A(\alpha - a) &= -\frac{a V_0}{R} \implies A = \frac{a V_0}{R(a - \alpha)}
\end{align*}
Thus:
\begin{equation}
  i_{pi}(t) = \frac{a V_0}{R(a - \alpha)} e^{-at}
\end{equation}

\paragraph{Step 4: Total Solution \& Initial Boundary Condition}
\begin{equation}
  i(t) = K e^{-\alpha t} + \frac{a V_0}{R(a - \alpha)} e^{-at}
\end{equation}
Assuming an initially uncharged capacitor ($v_C(0^+) = 0$), KVL at $t=0^+$ gives:
\[
R i(0^+) + v_C(0^+) = v(0^+) \implies R i(0^+) + 0 = V_0 \implies i(0^+) = \frac{V_0}{R}
\]
Substituting $t=0$:
\[
K + \frac{a V_0}{R(a - \alpha)} = \frac{V_0}{R} \implies K = \frac{V_0}{R} \left(1 - \frac{a}{a - \alpha}\right) = \frac{V_0}{R} \left(\frac{-\alpha}{a - \alpha}\right) = \frac{\alpha V_0}{R(\alpha - a)}
\]
Substituting $K$ and $\alpha = \frac{1}{RC}$:
\begin{align}
  i(t) &= \frac{\alpha V_0}{R(\alpha - a)} e^{-\alpha t} + \frac{a V_0}{R(a - \alpha)} e^{-at} = \frac{V_0}{R(1 - aRC)} \left[e^{-at} - e^{-\frac{t}{RC}}\right] \quad (a \ne 1/RC)
\end{align}

\begin{answerbox}
\[
i(t) = \frac{V_0}{R(1 - aRC)} \left[e^{-at} - e^{-\frac{t}{RC}}\right]\,\mathrm{A} \qquad \left(\text{for } a \ne \frac{1}{RC}\right)
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 3.2 2082 Bhadra Q3
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 3 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q3)}
Derive the differential equation of series RLC circuit when excited by step voltage and discuss the different cases of circuit responses.
\end{questionbox}

\subsubsection*{Detailed Derivation \& Damping Analysis}
\paragraph{1. Circuit Differential Equation:}
For a series $RLC$ circuit excited by step voltage $V_0 u(t)$:
\[
R i(t) + L \frac{di}{dt} + \frac{1}{C}\int i(t)\,dt = V_0
\]
Differentiating with respect to $t$ and dividing by $L$:
\begin{equation}
  \frac{d^2 i}{dt^2} + \frac{R}{L}\frac{di}{dt} + \frac{1}{LC}i(t) = 0 \iff s^2 + 2\alpha s + \omega_0^2 = 0
\end{equation}
where $\alpha = \frac{R}{2L}$ (damping attenuation) and $\omega_0 = \frac{1}{\sqrt{LC}}$ (undamped natural frequency). The roots are:
\begin{equation}
  s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2} = -\frac{R}{2L} \pm \sqrt{\left(\frac{R}{2L}\right)^2 - \frac{1}{LC}}
\end{equation}

\paragraph{2. The Three Damping Response Cases:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Overdamped Case ($\alpha > \omega_0 \iff R > 2\sqrt{L/C}$):}
    Roots $s_1, s_2$ are real, distinct, and negative. Current rises smoothly and decays exponentially without any oscillation:
    \begin{equation}
      i(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}
    \end{equation}
  \item \textbf{Critically Damped Case ($\alpha = \omega_0 \iff R = 2\sqrt{L/C}$):}
    Roots are real and equal ($s_1 = s_2 = -\alpha$). Circuit achieves steady state in the minimum possible transition time without overshoot:
    \begin{equation}
      i(t) = (A_1 + A_2 t) e^{-\alpha t}
    \end{equation}
  \item \textbf{Underdamped Case ($\alpha < \omega_0 \iff R < 2\sqrt{L/C}$):}
    Roots are complex conjugate pairs $s_{1,2} = -\alpha \pm j\omega_d$, where $\omega_d = \sqrt{\omega_0^2 - \alpha^2}$ is the damped natural frequency. Response exhibits exponentially decaying sinusoidal ringing:
    \begin{equation}
      i(t) = e^{-\alpha t} \left[A_1 \cos(\omega_d t) + A_2 \sin(\omega_d t)\right]
    \end{equation}
\end{enumerate}

\newpage

% ------------------------------------------------------------------------------
% 3.3 2082 Baishakh Q3
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 3 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q3)}
A DC source of 100 V is suddenly applied at time $t = 0$ to a series RLC circuit comprising $R = 2\,\Omega, L = 0.5\,\mathrm{H}$ and $C = 1\,\mathrm{F}$. Obtain the expression for current in the circuit by using classical method:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$100\,\mathrm{V}$] (0,2) -- (0.8,2);
  \draw (0.8,2) node[circle, fill, inner sep=1.2pt]{};
  \draw (1.8,2) node[circle, fill, inner sep=1.2pt]{};
  \draw[thick] (0.8,2) -- (1.6,2.5);
  \draw[->, >=stealth] (1.3,2.6) to[bend left=30] (1.5,2.1);
  \node[above] at (1.3,2.7) {$t=0$};
  \draw (1.8,2) to[R, l=$2\,\Omega$] (3.5,2) to[L, l=$0.5\,\mathrm{H}$] (5.5,2)
        to[C, l=$1\,\mathrm{F}$] (5.5,0) -- (0,0);
  \draw (2.75, 1.0) node{\Large $\circlearrowright$} node[above=0.15cm]{$i(t)$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Numerical Solution}
\paragraph{1. Characteristic Equation:}
\[
0.5 \frac{d^2 i}{dt^2} + 2 \frac{di}{dt} + \frac{1}{1} i = 0 \implies \frac{d^2 i}{dt^2} + 4 \frac{di}{dt} + 2 i = 0
\]
Characteristic roots:
\[
s^2 + 4s + 2 = 0 \implies s_{1,2} = \frac{-4 \pm \sqrt{16 - 8}}{2} = -2 \pm \sqrt{2}
\]
$s_1 = -2 + \sqrt{2} \approx -0.5858\,\mathrm{s}^{-1}$ and $s_2 = -2 - \sqrt{2} \approx -3.4142\,\mathrm{s}^{-1}$ (Overdamped).

\paragraph{2. General Solution:}
\[
i(t) = A_1 e^{(-2+\sqrt{2})t} + A_2 e^{(-2-\sqrt{2})t}
\]

\paragraph{3. Boundary Conditions:}
\begin{itemize}[leftmargin=1.5em]
  \item At $t=0^+$: $i(0^+) = 0 \implies A_1 + A_2 = 0 \implies A_2 = -A_1$.
  \item From KVL at $t=0^+$:
  \[
  100 = R i(0^+) + L \left.\frac{di}{dt}\right|_{0^+} + v_C(0^+) = 0 + 0.5 \left.\frac{di}{dt}\right|_{0^+} + 0 \implies \left.\frac{di}{dt}\right|_{0^+} = 200\,\mathrm{A/s}
  \]
  \item Differentiating $i(t)$ at $t=0^+$:
  \[
  s_1 A_1 + s_2 A_2 = 200 \implies A_1(s_1 - s_2) = 200 \implies A_1(2\sqrt{2}) = 200 \implies A_1 = 50\sqrt{2} \approx 70.71
  \]
  $A_2 = -50\sqrt{2} \approx -70.71$.
\end{itemize}

\begin{answerbox}
\[
i(t) = 50\sqrt{2}\left[e^{(-2+\sqrt{2})t} - e^{(-2-\sqrt{2})t}\right]\,\mathrm{A} = 70.71\left(e^{-0.586t} - e^{-3.414t}\right)\,\mathrm{A} \quad (t \ge 0)
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 3.4 2081 Ashwin Q3
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 3 [6 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q3)}
The circuit shown below is in steady state with switch at position 'a'. The switch is moved to position 'b' at $t = 0$. Find the expression for $V(t)$ and current through 2H inductor $i_L(t)$ for $t > 0$ using classical method:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$1\,\mathrm{V}$] (0,2.5) to[R, l=$1\,\Omega$] (1.8,2.5) node[circle, fill, inner sep=1.2pt, label=above:{$a$}]{};
  \draw (2.7,2.5) node[circle, fill, inner sep=1.2pt, label=above:{$b$}]{} -- (5.5,2.5);
  \draw (2.25,2.5) node[circle, fill, inner sep=1.2pt]{} to[L, l=$1\,\mathrm{H}$, i>_=$i_{L1}$] (2.25,0);
  \draw (4.0,2.5) to[R, l=$\frac{1}{2}\,\Omega$] (4.0,0);
  \draw (5.5,2.5) to[L, l=$2\,\mathrm{H}$, i>_=$i_{L2}$, v=$V(t)$] (5.5,0) -- (0,0);
  \draw[->, thick] (1.8,2.2) to[bend right=30] (2.7,2.2);
  \node at (2.25, 1.8) {$t=0$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}
\paragraph{1. Initial Conditions at $t = 0^-$ (Switch at 'a'):}
In DC steady state, the $1\,\mathrm{H}$ inductor acts as a short circuit:
\[
i_{L1}(0^-) = \frac{1\,\mathrm{V}}{1\,\Omega} = 1\,\mathrm{A} \quad (\text{downward}), \qquad i_{L2}(0^-) = 0\,\mathrm{A}
\]
By continuity, at $t = 0^+$: $i_{L1}(0^+) = 1\,\mathrm{A}, \quad i_{L2}(0^+) = 0\,\mathrm{A}$.

\paragraph{2. Parallel Network Analysis for $t > 0$ (Switch at 'b'):}
When thrown to 'b', the $1\,\mathrm{V}$ source and $1\,\Omega$ resistor are isolated. The remaining network consists of $L_1 = 1\,\mathrm{H}$, $R = 0.5\,\Omega$, and $L_2 = 2\,\mathrm{H}$ in parallel across node voltage $V(t)$.

Applying KCL at the top node:
\begin{equation}
  \frac{V(t)}{R} + \left[i_{L1}(0^+) + \frac{1}{L_1}\int_0^t V(\tau)\,d\tau\right] + \left[i_{L2}(0^+) + \frac{1}{L_2}\int_0^t V(\tau)\,d\tau\right] = 0
\end{equation}
Substitute $R = 0.5\,\Omega, L_1 = 1\,\mathrm{H}, L_2 = 2\,\mathrm{H}, i_{L1}(0^+) = 1\,\mathrm{A}, i_{L2}(0^+) = 0$:
\[
2V(t) + 1 + \left(1 + \frac{1}{2}\right)\int_0^t V(\tau)\,d\tau = 0 \implies 2V(t) + \frac{3}{2}\int_0^t V(\tau)\,d\tau = -1
\]
At $t = 0^+$, the integral is zero $\implies 2V(0^+) = -1 \implies V(0^+) = -0.5\,\mathrm{V}$.

Differentiating with respect to $t$:
\begin{equation}
  2 \frac{dV}{dt} + \frac{3}{2} V(t) = 0 \implies \frac{dV}{dt} + \frac{3}{4} V(t) = 0
\end{equation}
Solving this first-order linear ODE:
\begin{equation}
  V(t) = V(0^+) e^{-\frac{3}{4}t} = -0.5 e^{-0.75t}\,\mathrm{V} \quad (t > 0)
\end{equation}

\paragraph{3. Current through 2H Inductor $i_{L2}(t)$:}
\begin{align}
  i_{L2}(t) &= i_{L2}(0^+) + \frac{1}{L_2}\int_0^t V(\tau)\,d\tau = 0 + \frac{1}{2}\int_0^t \left(-0.5 e^{-0.75\tau}\right)d\tau \nonumber \\
  &= -0.25 \left[\frac{e^{-0.75\tau}}{-0.75}\right]_0^t = \frac{0.25}{0.75}\left(e^{-0.75t} - 1\right) = \frac{1}{3}\left(e^{-0.75t} - 1\right)\,\mathrm{A} \nonumber \\
  &= -0.333\left(1 - e^{-0.75t}\right)\,\mathrm{A} \quad (t > 0)
\end{align}

\begin{answerbox}
\textbf{Node Voltage:}
\[
V(t) = -0.5 e^{-0.75t}\,\mathrm{V} \quad (t > 0)
\]
\textbf{Inductor Current ($2\,\mathrm{H}$):}
\[
i_{L2}(t) = \frac{1}{3}\left(e^{-0.75t} - 1\right)\,\mathrm{A} = -0.333\left(1 - e^{-0.75t}\right)\,\mathrm{A} \quad (t > 0)
\]
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 4: QUESTION 4 - LAPLACE TRANSFORM TRANSIENT ANALYSIS
% ==============================================================================
\section{Question 4: Laplace Transform Applications to Circuit Analysis}

% ------------------------------------------------------------------------------
% 4.1 2083 Baishakh Q4
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 4 [6 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q4)}
In the given circuit, switch is opened at $t = 0$. Find the current and voltage across inductor using Laplace transform method:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$4\,\mathrm{V}$] (0,2.5) -- (0.8,2.5);
  \draw (0.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw (1.8,2.5) node[circle, fill, inner sep=1.2pt]{};
  \draw[thick] (0.8,2.5) -- (1.6,3.0);
  \draw[->, >=stealth] (1.3,3.1) to[bend left=30] (1.5,2.6);
  \node[above] at (1.3,3.2) {$t=0$};
  \draw (1.8,2.5) -- (2.5,2.5)
        to[L, l=$0.5\,\mathrm{H}$, i>_=$i(t)$, v=$v_L(t)$] (4.5,2.5)
        to[R, l=$1\,\Omega$] (4.5,0) -- (0,0);
  \draw (2.5,2.5) to[C, l=$1\,\mathrm{F}$, v=$v_C$] (2.5,0);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}
\paragraph{1. Initial Conditions ($t=0^-$):}
Before $t=0$, the switch is closed. In DC steady state:
\begin{itemize}[leftmargin=1.5em]
  \item Inductor is a short circuit $\implies i_L(0^-) = \frac{4\,\mathrm{V}}{1\,\Omega} = 4\,\mathrm{A}$ (downward).
  \item Capacitor is an open circuit $\implies v_C(0^-) = 4\,\mathrm{V}$ (top positive).
\end{itemize}
By continuity: $i_L(0^+) = 4\,\mathrm{A}, \quad v_C(0^+) = 4\,\mathrm{V}$.

\paragraph{2. $s$-Domain Formulation for $t \ge 0$:}
When the switch opens at $t=0$, the $4\,\mathrm{V}$ supply is disconnected. The remaining network is a single closed loop containing:
\begin{itemize}[leftmargin=1.5em]
  \item Capacitor $C = 1\,\mathrm{F}$ with initial voltage generator $\frac{V_0}{s} = \frac{4}{s}$ in series with $\frac{1}{sC} = \frac{1}{s}$.
  \item Inductor $L = 0.5\,\mathrm{H}$ with initial current generator $L i_L(0^+) = 0.5 \times 4 = 2\,\mathrm{V}$ opposing current in series with $sL = 0.5s$.
  \item Resistor $R = 1\,\Omega$.
\end{itemize}

Applying KVL in the $s$-domain around the loop (clockwise current $I(s)$):
\begin{align}
  \frac{4}{s} - \frac{1}{s} I(s) &= (0.5s + 1) I(s) - 2 \nonumber \\
  \frac{4 + 2s}{s} &= \left(0.5s + 1 + \frac{1}{s}\right) I(s) = \frac{0.5s^2 + s + 1}{s} I(s) \nonumber \\
  I(s) &= \frac{2s + 4}{0.5s^2 + s + 1} = \frac{4s + 8}{s^2 + 2s + 2}
\end{align}

\paragraph{3. Inverse Laplace Transform for $i(t)$:}
Completing the square in the denominator: $s^2 + 2s + 2 = (s+1)^2 + 1^2$:
\begin{align}
  I(s) &= \frac{4(s + 1) + 4}{(s + 1)^2 + 1^2} = 4 \frac{s + 1}{(s + 1)^2 + 1^2} + 4 \frac{1}{(s + 1)^2 + 1^2} \nonumber \\
  i(t) &= 4 e^{-t} \cos(t) + 4 e^{-t} \sin(t) = 4 e^{-t}(\cos t + \sin t)\,\mathrm{A} \quad (t \ge 0)
\end{align}

\paragraph{4. Inductor Voltage $v_L(t)$:}
In the $s$-domain:
\begin{align}
  V_L(s) &= sL I(s) - L i_L(0^+) = 0.5s \left(\frac{4s + 8}{s^2 + 2s + 2}\right) - 2 \nonumber \\
  &= \frac{2s^2 + 4s - 2(s^2 + 2s + 2)}{s^2 + 2s + 2} = \frac{-4}{s^2 + 2s + 2} = -4 \frac{1}{(s+1)^2 + 1^2}
\end{align}
Taking the Inverse Laplace Transform:
\begin{equation}
  v_L(t) = -4 e^{-t} \sin(t)\,\mathrm{V} \quad (t \ge 0)
\end{equation}
\textit{Verification:} At $t = 0^+$, $v_L(0^+) = 0\,\mathrm{V} = v_C(0^+) - R i(0^+) = 4 - (1)(4) = 0\,\mathrm{V}$.

\begin{answerbox}
\[
i(t) = 4 e^{-t}(\cos t + \sin t)\,\mathrm{A}, \qquad v_L(t) = -4 e^{-t}\sin(t)\,\mathrm{V} \quad (t \ge 0)
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 4.2 2082 Bhadra Q4
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 4 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q4)}
In the circuit shown switch is changed from position $a$ to position $b$ at $t = 0$. Determine the current $i(t)$ using Laplace transform method:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$10\,\mathrm{V}$] (0,2.5) to[R, l=$5\,\Omega$] (1.8,2.5) node[circle, fill, inner sep=1.2pt, label=above:{$a$}]{};
  \draw (2.7,1.2) node[circle, fill, inner sep=1.2pt, label=left:{$b$}]{} to[C, l=$10\,\mu\mathrm{F}$] (2.7,0);
  \draw (2.5,2.5) node[circle, fill, inner sep=1.2pt]{} to[L, l=$0.1\,\mathrm{H}$, i>_=$i(t)$] (5.0,2.5) -- (5.0,0) -- (0,0);
  \draw[->, thick] (1.8,2.3) to[bend right=30] (2.6,1.4);
  \node at (2.4, 1.8) {$t=0$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Initial Conditions ($t=0^-$):}
For $t < 0$, switch is at 'a', connecting $10\,\mathrm{V}$ source across $5\,\Omega$ resistor and $0.1\,\mathrm{H}$ inductor:
\[
i_L(0^-) = \frac{10\,\mathrm{V}}{5\,\Omega} = 2\,\mathrm{A}, \qquad v_C(0^-) = 0\,\mathrm{V} \quad (\text{terminal $b$ unconnected})
\]
\paragraph{2. $s$-Domain Circuit ($t > 0$):}
At $t=0$, moving to 'b' creates a series $LC$ loop of $L = 0.1\,\mathrm{H}$ ($i_L(0^+) = 2\,\mathrm{A}$) and $C = 10\,\mu\mathrm{F} = 10^{-5}\,\mathrm{F}$ ($v_C(0^+) = 0$).
\begin{equation}
  \left(sL + \frac{1}{sC}\right) I(s) = L i_L(0^+) \implies \left(0.1s + \frac{10^5}{s}\right) I(s) = 0.1 \times 2 = 0.2
\end{equation}
Multiplying by $s$:
\begin{equation}
  (0.1 s^2 + 10^5) I(s) = 0.2 s \implies I(s) = \frac{0.2 s}{0.1(s^2 + 10^6)} = \frac{2s}{s^2 + (1000)^2}
\end{equation}
\paragraph{3. Inverse Laplace Transform:}
\begin{equation}
  i(t) = \mathcal{L}^{-1}\left\{\frac{2s}{s^2 + 1000^2}\right\} = 2 \cos(1000t)\,\mathrm{A} \quad (t \ge 0)
\end{equation}

\begin{answerbox}
\[
i(t) = 2 \cos(1000t)\,\mathrm{A} \quad (t \ge 0)
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 4.3 2082 Baishakh Q4
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 4 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q4)}
An exponential voltage $V(t) = 20e^{-4t}$ is suddenly applied at time $t = 0$ to series RLC circuit comprising $R = 2\,\Omega, L = 0.5\,\mathrm{H}$ and $C = 1\,\mathrm{F}$. Obtain the expression for the current $i(t)$ in the circuit using Laplace method.
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. $s$-Domain Impedance \& Excitation:}
$V(s) = \frac{20}{s+4}$, \quad $Z(s) = R + sL + \frac{1}{sC} = 2 + 0.5s + \frac{1}{s} = \frac{s^2 + 4s + 2}{2s}$.
\begin{equation}
  I(s) = \frac{V(s)}{Z(s)} = \frac{\frac{20}{s+4}}{\frac{s^2 + 4s + 2}{2s}} = \frac{40s}{(s+4)(s^2 + 4s + 2)}
\end{equation}
\paragraph{2. Partial Fraction Decomposition:}
\[
\frac{40s}{(s+4)(s^2 + 4s + 2)} = \frac{A}{s+4} + \frac{Bs + C}{s^2 + 4s + 2}
\]
\begin{itemize}[leftmargin=1.5em]
  \item $A = \left.\frac{40s}{s^2 + 4s + 2}\right|_{s=-4} = \frac{-160}{16 - 16 + 2} = -80$.
  \item $40s = -80(s^2 + 4s + 2) + (Bs + C)(s + 4) \implies B = 80, \quad C = 40$.
\end{itemize}
\paragraph{3. Inverse Laplace Transform:}
\begin{align*}
  I(s) &= \frac{-80}{s+4} + \frac{80s + 40}{(s+2)^2 - 2} = \frac{-80}{s+4} + 80 \frac{s+2}{(s+2)^2 - (\sqrt{2})^2} - \frac{120}{\sqrt{2}} \frac{\sqrt{2}}{(s+2)^2 - (\sqrt{2})^2}
\end{align*}
Taking $\mathcal{L}^{-1}$:
\begin{equation}
  i(t) = -80 e^{-4t} + 80 e^{-2t}\cosh(\sqrt{2}t) - 60\sqrt{2} e^{-2t}\sinh(\sqrt{2}t)\,\mathrm{A} \quad (t \ge 0)
\end{equation}

\begin{answerbox}
\[
i(t) = -80 e^{-4t} + 80 e^{-2t}\cosh(\sqrt{2}t) - 84.85 e^{-2t}\sinh(\sqrt{2}t)\,\mathrm{A} \quad (t \ge 0)
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 4.4 2081 Ashwin Q4
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 4 [6 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q4)}
The switch in the figure below has been in position 'a' for a long time. Then, it is moved to 'b' at $t = 0$. Obtain the expression for voltage across capacitor for $t > 0$ using Laplace transform method:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,0) to[V, v<=$6\,\mathrm{V}$] (0,2.5) to[R, l=$2\,\Omega$] (1.8,2.5) node[circle, fill, inner sep=1.2pt, label=above:{$a$}]{};
  \draw (2.7,1.5) node[circle, fill, inner sep=1.2pt, label=left:{$b$}]{} to[R, l=$1\,\Omega$] (2.7,0.8) to[L, l=$0.5\,\mathrm{H}$] (2.7,0);
  \draw (2.5,2.5) node[circle, fill, inner sep=1.2pt]{} -- (4.5,2.5) to[C, l=$1\,\mathrm{F}$, v=$v_C(t)$] (4.5,0) -- (0,0);
  \draw[->, thick] (1.8,2.3) to[bend right=30] (2.6,1.7);
  \node at (2.4, 2.0) {$t=0$};
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Initial Conditions ($t=0^-$):}
Switch at 'a': $v_C(0^-) = 6\,\mathrm{V}, \quad i_L(0^-) = 0\,\mathrm{A}$.
\paragraph{2. $s$-Domain Analysis ($t > 0$):}
Series $RLC$ discharging loop ($R = 1\,\Omega, L = 0.5\,\mathrm{H}, C = 1\,\mathrm{F}, V_0 = 6\,\mathrm{V}$):
\[
\left(0.5s + 1 + \frac{1}{s}\right) I(s) = \frac{6}{s} \implies I(s) = \frac{12}{s^2 + 2s + 2}
\]
Capacitor voltage in $s$-domain:
\begin{align*}
  V_C(s) &= \frac{v_C(0^+)}{s} - \frac{1}{sC} I(s) = \frac{6}{s} - \frac{12}{s(s^2 + 2s + 2)} = \frac{6s + 12}{s^2 + 2s + 2} \\
  &= \frac{6(s+1) + 6}{(s+1)^2 + 1^2} = 6 \frac{s+1}{(s+1)^2 + 1^2} + 6 \frac{1}{(s+1)^2 + 1^2}
\end{align*}
Taking $\mathcal{L}^{-1}$:
\begin{equation}
  v_C(t) = 6 e^{-t}(\cos t + \sin t)\,\mathrm{V} \quad (t > 0)
\end{equation}

\begin{answerbox}
\[
v_C(t) = 6 e^{-t}(\cos t + \sin t)\,\mathrm{V} \quad (t > 0)
\]
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 5: QUESTION 5 & 6 - BODE PLOTS & FREQUENCY RESPONSE
% ==============================================================================
\section{Questions 5 \& 6: Frequency Response \& Asymptotic Bode Plots}

% ------------------------------------------------------------------------------
% 5.1 2083 Baishakh Q5
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 5 [7 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q5)}
What is network function? Plot Asymptotic Bode graph of given transfer function:
\[
H(s) = \frac{10(s^2 + 8s + 15)}{s^2(s + 3)(0.05s + 1)}
\]
\end{questionbox}

\subsubsection*{Solution \& Complete Plot}
\paragraph{1. Network Function Definition:}
A network function $H(s) = \frac{Y(s)}{X(s)}$ is the ratio of the Laplace transform of the output response $Y(s)$ to the Laplace transform of the input excitation $X(s)$, with all initial conditions set to zero.

\paragraph{2. Factorization into Standard Bode Form:}
Factor numerator: $s^2 + 8s + 15 = (s+3)(s+5)$. Canceling the common pole-zero term $(s+3)$:
\[
H(s) = \frac{10(s+5)}{s^2(0.05s + 1)} = \frac{10 \times 5\left(1 + \frac{s}{5}\right)}{s^2\left(1 + \frac{s}{20}\right)} = \frac{50\left(1 + \frac{s}{5}\right)}{s^2\left(1 + \frac{s}{20}\right)}
\]
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{DC/System Gain:} $K = 50 \implies 20\log_{10}(50) \approx 33.98\,\mathrm{dB}$.
  \item \textbf{Type-2 System (Double Pole at Origin):} Initial low-frequency slope of $-40\,\mathrm{dB/dec}$.
  \item \textbf{Corner Frequencies:} Simple zero at $\omega_{z1} = 5\,\mathrm{rad/s}$ ($+20\,\mathrm{dB/dec}$ slope change); Simple pole at $\omega_{p1} = 20\,\mathrm{rad/s}$ ($-20\,\mathrm{dB/dec}$ slope change).
\end{itemize}

\begin{center}
\small
\begin{tabular}{@{}llcc@{}}
\toprule
\textbf{Frequency Range (rad/s)} & \textbf{Active Factors} & \textbf{Slope Change} & \textbf{Resultant Slope} \\
\midrule
$\omega < 5$ & $50/s^2$ & --- & $-40\,\mathrm{dB/decade}$ \\
$5 \le \omega < 20$ & Zero at $\omega = 5$ & $+20\,\mathrm{dB/dec}$ & $-20\,\mathrm{dB/decade}$ \\
$\omega \ge 20$ & Pole at $\omega = 20$ & $-20\,\mathrm{dB/dec}$ & $-40\,\mathrm{dB/decade}$ \\
\bottomrule
\end{tabular}
\end{center}

\begin{center}
\includegraphics[width=0.85\textwidth]{figures/bode_2083_baishakh.pdf}
\end{center}

\newpage

% ------------------------------------------------------------------------------
% 5.2 2082 Bhadra Q6
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 6 [1 + 7 = 8 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q6)}
Define poles and zeros of network function. Construct the asymptotic magnitude bode plot and phase plot for given transfer function:
\[
T(s) = \frac{100(s + 5)}{s^2(s^2 + 21s + 20)}
\]
\end{questionbox}

\subsubsection*{Solution \& Complete Plot}
\paragraph{1. Definitions:}
\textbf{Poles} are the complex frequencies $s=p_k$ where $T(s) \to \infty$ (roots of denominator). \textbf{Zeros} are the complex frequencies $s=z_k$ where $T(s) \to 0$ (roots of numerator).

\paragraph{2. Factorization into Standard Bode Form:}
Denominator quadratic: $s^2 + 21s + 20 = (s+1)(s+20)$.
\[
T(s) = \frac{100 \times 5\left(1 + \frac{s}{5}\right)}{s^2 \times 1(1+s) \times 20\left(1 + \frac{s}{20}\right)} = \frac{25\left(1 + \frac{s}{5}\right)}{s^2(1+s)\left(1 + \frac{s}{20}\right)}
\]
\begin{itemize}[leftmargin=1.5em]
  \item $K = 25 \implies 20\log_{10}(25) \approx 27.96\,\mathrm{dB}$.
  \item Initial slope: $-40\,\mathrm{dB/dec}$ (double pole at origin).
  \item Corner frequencies in ascending order: $\omega_{p1} = 1\,\mathrm{rad/s} < \omega_{z1} = 5\,\mathrm{rad/s} < \omega_{p2} = 20\,\mathrm{rad/s}$.
\end{itemize}

\begin{center}
\small
\begin{tabular}{@{}llcc@{}}
\toprule
\textbf{Frequency Range (rad/s)} & \textbf{Factor Introduced} & \textbf{Slope Change} & \textbf{Resultant Slope} \\
\midrule
$\omega < 1$ & $25/s^2$ & --- & $-40\,\mathrm{dB/decade}$ \\
$1 \le \omega < 5$ & Pole at $\omega = 1$ & $-20\,\mathrm{dB/dec}$ & $-60\,\mathrm{dB/decade}$ \\
$5 \le \omega < 20$ & Zero at $\omega = 5$ & $+20\,\mathrm{dB/dec}$ & $-40\,\mathrm{dB/decade}$ \\
$\omega \ge 20$ & Pole at $\omega = 20$ & $-20\,\mathrm{dB/dec}$ & $-60\,\mathrm{dB/decade}$ \\
\bottomrule
\end{tabular}
\end{center}

\begin{center}
\includegraphics[width=0.85\textwidth]{figures/bode_2082_bhadra.pdf}
\end{center}

\newpage

% ------------------------------------------------------------------------------
% 5.3 2082 Baishakh Q5
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 5 [8 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q5)}
Sketch the asymptotic bode plot for the transfer function given by:
\[
G(s) = \frac{100s(s + 5)}{(s + 1)(s^2 + 10s + 100)}
\]
\end{questionbox}

\subsubsection*{Solution \& Complete Plot}
\paragraph{Standard Bode Form:}
\[
G(s) = \frac{100 \cdot s \cdot 5\left(1 + \frac{s}{5}\right)}{1(1+s) \cdot 100\left(1 + \frac{s}{10} + \frac{s^2}{100}\right)} = \frac{5s\left(1 + \frac{s}{5}\right)}{(1+s)\left(1 + 0.1s + 0.01s^2\right)}
\]
\begin{itemize}[leftmargin=1.5em]
  \item Zero at origin gives initial low-frequency slope of $+20\,\mathrm{dB/dec}$ with $20\log_{10}(5\omega)$.
  \item Simple pole at $\omega_{p1} = 1\,\mathrm{rad/s}$ ($ -20\,\mathrm{dB/dec} \implies \text{slope } 0\,\mathrm{dB/dec}$).
  \item Simple zero at $\omega_{z1} = 5\,\mathrm{rad/s}$ ($ +20\,\mathrm{dB/dec} \implies \text{slope } +20\,\mathrm{dB/dec}$).
  \item Complex conjugate poles at $\omega_n = \sqrt{100} = 10\,\mathrm{rad/s}$ ($\zeta = 0.5 < 1$) introduce $-40\,\mathrm{dB/dec}$ slope change $\implies \text{net slope } -20\,\mathrm{dB/dec}$.
\end{itemize}

\begin{center}
\includegraphics[width=0.85\textwidth]{figures/bode_2082_baishakh.pdf}
\end{center}

\newpage

% ------------------------------------------------------------------------------
% 5.4 2081 Ashwin Q5
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 5 [7 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q5)}
Plot asymptotic Bode graph of given transfer function:
\[
G(s) = \frac{500(s + 2)}{s(s^2 + 15s + 121)}
\]
\end{questionbox}

\subsubsection*{Solution \& Complete Plot}
\paragraph{Standard Bode Form:}
\[
G(s) = \frac{500 \times 2\left(1 + \frac{s}{2}\right)}{s \times 121\left(1 + \frac{15}{121}s + \frac{s^2}{121}\right)} = \frac{8.264\left(1 + \frac{s}{2}\right)}{s\left(1 + \frac{15}{121}s + \frac{s^2}{121}\right)}
\]
\begin{itemize}[leftmargin=1.5em]
  \item $K = 8.264 \implies 20\log_{10}(8.264) \approx 18.34\,\mathrm{dB}$.
  \item Initial slope: $-20\,\mathrm{dB/dec}$ due to pole at origin.
  \item Simple zero at $\omega_{z1} = 2\,\mathrm{rad/s}$ ($+20\,\mathrm{dB/dec} \implies \text{slope } 0\,\mathrm{dB/dec}$).
  \item Complex conjugate pole pair at $\omega_n = \sqrt{121} = 11\,\mathrm{rad/s}$ ($\zeta = \frac{15}{22} = 0.682 < 1$) introduces $-40\,\mathrm{dB/dec} \implies \text{net slope } -40\,\mathrm{dB/dec}$.
\end{itemize}

\begin{center}
\includegraphics[width=0.85\textwidth]{figures/bode_2081_ashwin.pdf}
\end{center}

\newpage

% ==============================================================================
% CHAPTER 6: TWO-PORT NETWORKS
% ==============================================================================
\section{Question 6: Two-Port Network Parameters \& Interconnections}

% ------------------------------------------------------------------------------
% 6.1 2083 Baishakh Q6
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 6 [6 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q6)}
Find Z parameter for given two port network and state whether network is symmetrical or reciprocal:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,2.5) node[left]{$+$} to[open, v=$V_1$] (0,0) node[left]{$-$};
  \draw (0,2.5) to[R, l=$8\,\Omega$, i=$I_1$] (2.5,2.5) to[R, l=$10\,\Omega$] (5.5,2.5) -- (6,2.5);
  \draw (2.5,2.5) to[R, l=$20\,\Omega$] (2.5,0);
  \draw (5.5,2.5) to[R, l=$20\,\Omega$] (5.5,0);
  \draw (6,2.5) node[right]{$+$} to[open, v^<=$V_2$] (6,0) node[right]{$-$};
  \draw (6,2.5) to[short, i=$I_2$] (5.5,2.5);
  \draw (0,0) -- (6,0);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Derivation}
\paragraph{1. Open-Circuit at Port 2 ($I_2 = 0$):}
With Port 2 open, the second $20\,\Omega$ resistor is in series with the $10\,\Omega$ resistor, forming a $30\,\Omega$ branch in parallel with the middle $20\,\Omega$ resistor:
\[
R_{\text{parallel}} = 20 \parallel (10 + 20) = 20 \parallel 30 = \frac{600}{50} = 12\,\Omega
\]
\begin{itemize}[leftmargin=1.5em]
  \item $Z_{11} = \left.\frac{V_1}{I_1}\right|_{I_2=0} = 8 + 12 = 20\,\Omega$.
  \item Voltage across middle node: $V_m = 12 I_1$. By voltage division across $(10+20)\,\Omega$:
  \[
  V_2 = V_m \left(\frac{20}{10 + 20}\right) = (12 I_1)\left(\frac{20}{30}\right) = 8 I_1 \implies Z_{21} = \left.\frac{V_2}{I_1}\right|_{I_2=0} = 8\,\Omega
  \]
\end{itemize}

\paragraph{2. Open-Circuit at Port 1 ($I_1 = 0$):}
With Port 1 open, no current flows through the $8\,\Omega$ resistor.
\begin{itemize}[leftmargin=1.5em]
  \item $Z_{22} = \left.\frac{V_2}{I_2}\right|_{I_1=0} = 20 \parallel (10 + 20) = 12\,\Omega$.
  \item By current division, current entering the $(10+20)\,\Omega$ branch is $I_{\text{branch}} = I_2 \frac{20}{20 + 30} = 0.4 I_2$.
  \[
  V_1 = I_{\text{branch}} \times 20\,\Omega = 0.4 I_2 \times 20 = 8 I_2 \implies Z_{12} = \left.\frac{V_1}{I_2}\right|_{I_1=0} = 8\,\Omega
  \]
\end{itemize}

\paragraph{3. Symmetry \& Reciprocity:}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Reciprocity:} $Z_{12} = Z_{21} = 8\,\Omega \implies$ \textbf{Reciprocal}.
  \item \textbf{Symmetry:} $Z_{11} = 20\,\Omega \ne 12\,\Omega = Z_{22} \implies$ \textbf{Not Symmetrical}.
\end{itemize}

\begin{answerbox}
\[
\mathbf{[Z]} = \begin{bmatrix} 20 & 8 \\ 8 & 12 \end{bmatrix}\,\Omega \qquad \text{Network is \textbf{Reciprocal} but \textbf{Not Symmetrical}.}
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 6.2 2082 Bhadra Q5
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 5 [5 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q5)}
Define two port network. For the given network, find Z parameters:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,2.5) node[left]{$+$} to[open, v=$V_1$] (0,0) node[left]{$-$};
  \draw (0,2.5) to[R, l=$3\,\Omega$, i=$I_1$] (2.5,2.5) to[R, l=$1\,\Omega$] (4.2,2.5) to[L, l=$j5\,\Omega$] (5.5,2.5) -- (6,2.5);
  \draw (2.5,2.5) to[cV, v^<=$2I_a$] (2.5,1.2) to[C, l=$-j2\,\Omega$] (2.5,0);
  \draw (6,2.5) node[right]{$+$} to[open, v^<=$V_2$] (6,0) node[right]{$-$};
  \draw (6,2.5) to[short, i=$I_2$] (5.5,2.5);
  \draw (5.3,2.8) to[short, i=$I_a$] (4.7,2.8);
  \draw (0,0) -- (6,0);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Controlling Current Relation:}
The current $I_a$ is labeled flowing leftward into Port 2, which matches the standard terminal current $I_2$:
\begin{equation}
  I_a = I_2
\end{equation}

\paragraph{2. KVL Equations:}
Current flowing downward through the middle shunt branch is $(I_1 + I_2)$. The voltage across this branch is:
\[
V_{\text{shunt}} = 2I_a + (-j2)(I_1 + I_2) = 2I_2 - j2I_1 - j2I_2 = -j2 I_1 + (2 - j2) I_2
\]
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Port 1 KVL:}
  \[
  V_1 = 3I_1 + V_{\text{shunt}} = (3 - j2)I_1 + (2 - j2)I_2 \implies Z_{11} = 3 - j2\,\Omega, \quad Z_{12} = 2 - j2\,\Omega
  \]
  \item \textbf{Port 2 KVL:}
  \[
  V_2 = (1 + j5)I_2 + V_{\text{shunt}} = -j2 I_1 + (1 + j5 + 2 - j2)I_2 = -j2 I_1 + (3 + j3)I_2
  \]
  \[
  \implies Z_{21} = -j2\,\Omega, \quad Z_{22} = 3 + j3\,\Omega
  \]
\end{itemize}

\begin{answerbox}
\[
\mathbf{[Z]} = \begin{bmatrix} 3 - j2 & 2 - j2 \\ -j2 & 3 + j3 \end{bmatrix}\,\Omega \qquad \text{(Non-reciprocal due to dependent source)}
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 6.3 2082 Baishakh Q6
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 6 [3 + 3 = 6 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q6)}
Find the expression of hybrid parameters in terms of Z parameters. Derive the equivalent T parameters of two cascade connected two port networks.
\end{questionbox}

\subsubsection*{Part A: Hybrid ($h$) Parameters in terms of $Z$ Parameters}
Governing equations:
\begin{align}
  V_1 &= Z_{11} I_1 + Z_{12} I_2 \quad \text{--- (1)}, \qquad V_2 = Z_{21} I_1 + Z_{22} I_2 \quad \text{--- (2)} \\
  V_1 &= h_{11} I_1 + h_{12} V_2 \quad \text{--- (3)}, \qquad I_2 = h_{21} I_1 + h_{22} V_2 \quad \text{--- (4)}
\end{align}
From (2), solve for $I_2$:
\begin{equation}
  I_2 = -\frac{Z_{21}}{Z_{22}} I_1 + \frac{1}{Z_{22}} V_2 \implies h_{21} = -\frac{Z_{21}}{Z_{22}}, \quad h_{22} = \frac{1}{Z_{22}}
\end{equation}
Substitute $I_2$ into (1):
\begin{align}
  V_1 &= Z_{11} I_1 + Z_{12}\left(-\frac{Z_{21}}{Z_{22}} I_1 + \frac{1}{Z_{22}} V_2\right) = \left(\frac{Z_{11}Z_{22} - Z_{12}Z_{21}}{Z_{22}}\right) I_1 + \left(\frac{Z_{12}}{Z_{22}}\right) V_2 \nonumber \\
  \implies h_{11} &= \frac{\Delta_Z}{Z_{22}}, \quad h_{12} = \frac{Z_{12}}{Z_{22}} \qquad (\text{where } \Delta_Z = Z_{11}Z_{22} - Z_{12}Z_{21})
\end{align}

\subsubsection*{Part B: Transmission ($T/ABCD$) Parameters of Cascaded Networks}
For two networks $N_A$ and $N_B$ in cascade:
\[
\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \mathbf{T}_A \begin{bmatrix} V_2' \\ -I_2' \end{bmatrix}, \qquad \begin{bmatrix} V_1'' \\ I_1'' \end{bmatrix} = \mathbf{T}_B \begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}
\]
At the cascade interface: $V_2' = V_1''$ and $-I_2' = I_1''$. Therefore:
\begin{equation}
  \begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \mathbf{T}_A \mathbf{T}_B \begin{bmatrix} V_2 \\ -I_2 \end{bmatrix} \implies \mathbf{T}_{\text{eq}} = \mathbf{T}_A \times \mathbf{T}_B = \begin{bmatrix} A_A A_B + B_A C_B & A_A B_B + B_A D_B \\ C_A A_B + D_A C_B & C_A B_B + D_A D_B \end{bmatrix}
\end{equation}

\newpage

% ------------------------------------------------------------------------------
% 6.4 2081 Ashwin Q6
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 6 [2 + 4 = 6 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q6)}
Find the expression of Z parameters in terms of ABCD parameters. For given two port networks, find ABCD parameters:
\begin{center}
\begin{circuitikz}[american, scale=1.1, transform shape]
  \draw (0,2.5) node[left]{$+$} to[open, v=$V_1$] (0,0) node[left]{$-$};
  \draw (0,2.5) to[short, i=$I_1$] (1.5,2.5) to[R, l=$8\,\Omega$] (4.5,2.5) -- (5.5,2.5);
  \draw (1.5,2.5) to[cI, l=$0.5I_x$] (1.5,0);
  \draw (4.5,2.5) to[R, l=$5\,\Omega$, i>_=$I_x$] (4.5,0);
  \draw (5.5,2.5) node[right]{$+$} to[open, v^<=$V_2$] (5.5,0) node[right]{$-$};
  \draw (5.5,2.5) to[short, i=$I_2$] (4.5,2.5);
  \draw (0,0) -- (5.5,0);
\end{circuitikz}
\end{center}
\end{questionbox}

\subsubsection*{Part A: $Z$-Parameters in terms of $ABCD$ Parameters}
\[
V_1 = A V_2 - B I_2 \quad \text{--- (1)}, \qquad I_1 = C V_2 - D I_2 \quad \text{--- (2)}
\]
From (2): $V_2 = \frac{1}{C} I_1 + \frac{D}{C} I_2 \implies Z_{21} = \frac{1}{C}, \quad Z_{22} = \frac{D}{C}$.
Substituting $V_2$ into (1):
\[
V_1 = A\left(\frac{1}{C} I_1 + \frac{D}{C} I_2\right) - B I_2 = \frac{A}{C} I_1 + \left(\frac{AD - BC}{C}\right) I_2 \implies Z_{11} = \frac{A}{C}, \quad Z_{12} = \frac{\Delta_T}{C}
\]

\subsubsection*{Part B: Calculation of ABCD Parameters for the Active Network}
\begin{enumerate}[leftmargin=1.5em]
  \item The $5\,\Omega$ resistor is connected directly across Port 2:
  \begin{equation}
    V_2 = 5 I_x \implies I_x = 0.2 V_2
  \end{equation}
  \item At the Port 2 top node, current entering from left through $8\,\Omega$ resistor is $I_{\text{series}}$:
  \begin{equation}
    I_{\text{series}} + I_2 = I_x \implies I_{\text{series}} = I_x - I_2 = 0.2 V_2 - I_2
  \end{equation}
  \item Port 1 Voltage $V_1$:
  \begin{equation}
    V_1 = V_2 + 8 I_{\text{series}} = V_2 + 8(0.2 V_2 - I_2) = 2.6 V_2 - 8 I_2 \implies A = 2.6, \quad B = 8\,\Omega
  \end{equation}
  \item Port 1 Current $I_1$:
  \begin{equation}
    I_1 = 0.5 I_x + I_{\text{series}} = 0.5(0.2 V_2) + (0.2 V_2 - I_2) = 0.3 V_2 - I_2 \implies C = 0.3\,\mathrm{S}, \quad D = 1
  \end{equation}
\end{enumerate}

\begin{answerbox}
\[
\mathbf{T} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} 2.6 & 8\,\Omega \\ 0.3\,\mathrm{S} & 1 \end{bmatrix}, \qquad \Delta_T = AD - BC = (2.6)(1) - (8)(0.3) = 0.2 \ne 1
\]
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 7: TRANSFORMERS
% ==============================================================================
\section{Question 7: Single-Phase Transformers (Theory \& Testing)}

% ------------------------------------------------------------------------------
% 7.1 & 7.4 Core Flux Proof
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh Q7 \& 2081 Ashwin Q7 [5--6 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh Q7 / 2081 Ashwin Q7)}
List out features of ideal transformer. Explain operation of transformer under loaded condition and show/prove that the main magnetic flux in the transformer core is constant and independent of load current.
\end{questionbox}

\subsubsection*{1. Features of an Ideal Transformer}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Zero Winding Resistance:} $R_1 = 0, R_2 = 0 \implies$ zero ohmic copper loss ($I^2R = 0$).
  \item \textbf{Infinite Core Permeability ($\mu_r \to \infty$):} Zero reluctance $\implies$ vanishingly small magnetizing current ($I_m \to 0$) needed to establish core flux.
  \item \textbf{Zero Leakage Flux:} 100\% magnetic coupling ($k=1$); all flux is mutual core flux $\Phi_m$.
  \item \textbf{Zero Core Losses:} No hysteresis or eddy current losses in the core.
  \item \textbf{100\% Efficiency:} $P_{\text{in}} = P_{\text{out}}$ under all loading conditions.
\end{itemize}

\subsubsection*{2. Proof that Main Core Flux $\Phi_m$ is Constant Under All Loads}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{No-Load Equilibrium:} When energized by primary sinusoidal voltage $V_1$ at frequency $f$, primary winding draws no-load current $I_0$ establishing peak flux $\Phi_m$. By Faraday's Law, the induced back EMF is:
  \begin{equation}
    E_1 = 4.44 f N_1 \Phi_m \implies \Phi_m = \frac{E_1}{4.44 f N_1}
  \end{equation}
  Since primary winding impedance drops are negligible ($V_1 \approx E_1$):
  \begin{equation}
    \Phi_m \approx \frac{V_1}{4.44 f N_1} = \text{Constant}
  \end{equation}
  \item \textbf{Action Under Load:} When secondary is connected to a load, current $I_2$ flows, creating a demagnetizing secondary MMF $N_2 I_2$ producing opposing flux $\Phi_2$.
  \item \textbf{Self-Balancing Primary Reaction:} The net flux momentarily dips, reducing primary back EMF $E_1$. The resulting voltage difference $(V_1 - E_1)$ instantly draws an additional primary current $I_2'$ (load component) such that:
  \begin{equation}
    N_1 I_2' = N_2 I_2 \implies \Phi_2' = \Phi_2
  \end{equation}
  The primary load flux $\Phi_2'$ completely neutralizes the secondary demagnetizing flux $\Phi_2$.
  \item \textbf{Conclusion:} The net core MMF remains $N_1 I_0$, keeping core flux $\Phi_m$ strictly constant.
\end{enumerate}

\newpage

% ------------------------------------------------------------------------------
% 7.2 2082 Bhadra Q7
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 7 [5 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q7)}
State the role of commutator and carbon brushes in DC machine. Explain the characteristics of DC generators.
\end{questionbox}

\subsubsection*{1. Role of Commutator and Carbon Brushes}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Commutator:}
    \begin{itemize}
      \item \textit{In DC Generator:} Acts as a mechanical synchronous rectifier converting the internal alternating EMF (AC) induced in armature coils into unidirectional direct voltage (DC) at external terminals.
      \item \textit{In DC Motor:} Reverses the armature current direction every half-rotation to maintain unidirectional continuous electromagnetic driving torque.
    \end{itemize}
  \item \textbf{Carbon Brushes:} Provide sliding electrical contact on rotating commutator segments. Made of carbon/graphite due to high self-lubrication, negative temperature coefficient of resistance (which suppresses commutating sparks), and softer mechanical hardness than copper.
\end{itemize}

\subsubsection*{2. Characteristics of DC Generators}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Open-Circuit Characteristic (OCC / Magnetization Curve) [$E_0$ vs $I_f$]:} Curve between no-load generated EMF $E_0$ and field current $I_f$ at rated speed. Starts at small residual voltage ($I_f=0$) and saturates at high $I_f$.
  \item \textbf{Internal Characteristic [$E$ vs $I_a$]:} Curve between actual generated EMF on load ($E = E_0 - \text{drop due to armature reaction}$) and armature current $I_a$.
  \item \textbf{External Characteristic [$V$ vs $I_L$]:} Curve between terminal voltage $V = E - I_a R_a$ and load current $I_L$.
\end{enumerate}

\begin{center}
\includegraphics[width=0.48\textwidth]{figures/dc_generator_occ.pdf} \hfill
\includegraphics[width=0.48\textwidth]{figures/dc_generator_load_curves.pdf}
\end{center}

\newpage

% ------------------------------------------------------------------------------
% 7.3 2082 Baishakh Q7
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 7 [5 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q7)}
The following test results were obtained on a $20\,\mathrm{kVA}, 2200/220\,\mathrm{V}, 50\,\mathrm{Hz}$, single-phase transformer:
\begin{itemize}
  \item \textbf{O.C. test:} $220\,\mathrm{V}, 1.1\,\mathrm{A}, 125\,\mathrm{W}$ (On LV side)
  \item \textbf{S.C. test:} $52.7\,\mathrm{V}, 8.4\,\mathrm{A}, 287\,\mathrm{W}$ (On HV side)
\end{itemize}
Calculate the equivalent circuit parameters referred to secondary side.
\end{questionbox}

\subsubsection*{Detailed Step-by-Step Solution}
\paragraph{1. Transformation Ratio:}
\[
k = \frac{V_2}{V_1} = \frac{220}{2200} = 0.1 \qquad (\text{LV is Secondary, HV is Primary})
\]

\paragraph{2. Open-Circuit (O.C.) Test Calculations (Conducted on LV / Secondary Side):}
Given $V_{02} = 220\,\mathrm{V}, I_{02} = 1.1\,\mathrm{A}, W_0 = 125\,\mathrm{W}$:
\begin{align*}
  \cos\phi_0 &= \frac{W_0}{V_{02} I_{02}} = \frac{125}{220 \times 1.1} = \frac{125}{242} \approx 0.5165 \\
  \sin\phi_0 &= \sqrt{1 - (0.5165)^2} \approx 0.8563 \\
  I_w &= I_{02}\cos\phi_0 = 1.1 \times 0.5165 = 0.5682\,\mathrm{A} \\
  I_m &= I_{02}\sin\phi_0 = 1.1 \times 0.8563 = 0.9419\,\mathrm{A}
\end{align*}
Shunt branch parameters referred to secondary:
\begin{align}
  R_{c2} &= \frac{V_{02}}{I_w} = \frac{220}{0.5682} \approx 387.19\,\Omega \qquad \left[\text{or } \frac{V_{02}^2}{W_0} = \frac{220^2}{125} = 387.20\,\Omega\right] \\
  X_{m2} &= \frac{V_{02}}{I_m} = \frac{220}{0.9419} \approx 233.57\,\Omega
\end{align}

\paragraph{3. Short-Circuit (S.C.) Test Calculations (Conducted on HV / Primary Side):}
Given $V_{sc1} = 52.7\,\mathrm{V}, I_{sc1} = 8.4\,\mathrm{A}, W_{sc} = 287\,\mathrm{W}$:
\begin{align*}
  R_{e1} &= \frac{W_{sc}}{I_{sc1}^2} = \frac{287}{(8.4)^2} = \frac{287}{70.56} \approx 4.0675\,\Omega \\
  Z_{e1} &= \frac{V_{sc1}}{I_{sc1}} = \frac{52.7}{8.4} \approx 6.2738\,\Omega \\
  X_{e1} &= \sqrt{Z_{e1}^2 - R_{e1}^2} = \sqrt{(6.2738)^2 - (4.0675)^2} = \sqrt{39.3607 - 16.5446} = \sqrt{22.8161} \approx 4.7766\,\Omega
\end{align*}
Referring equivalent series parameters to secondary (LV side) via $k^2 = (0.1)^2 = 0.01$:
\begin{align}
  R_{e2} &= k^2 R_{e1} = 0.01 \times 4.0675 = 0.04068\,\Omega \approx 0.0407\,\Omega \\
  X_{e2} &= k^2 X_{e1} = 0.01 \times 4.7766 = 0.04777\,\Omega \approx 0.0478\,\Omega \\
  Z_{e2} &= k^2 Z_{e1} = 0.01 \times 6.2738 = 0.06274\,\Omega \approx 0.0627\,\Omega
\end{align}

\begin{answerbox}
\textbf{Equivalent Circuit Parameters Referred to Secondary (LV Side):}
\[
R_{c2} = 387.20\,\Omega, \quad X_{m2} = 233.57\,\Omega, \quad R_{e2} = 0.0407\,\Omega, \quad X_{e2} = 0.0478\,\Omega
\]
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 8: DC MACHINES & MAGNETIC CIRCUITS
% ==============================================================================
\section{Question 8: DC Machines \& Magnetic Circuits}

% ------------------------------------------------------------------------------
% 8.1 2083 Baishakh Q8
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 8 [5 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q8)}
A shunt generator supplies 96 A at a terminal voltage of 200 V. The armature and shunt field resistance are $0.1\,\Omega$ and $50\,\Omega$ respectively. The iron and frictional losses are 2500 W. Find:
(a) EMF generated \quad (b) Commercial efficiency.
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Current Calculations:}
\begin{itemize}[leftmargin=1.5em]
  \item Shunt field current: $I_{sh} = \frac{V}{R_{sh}} = \frac{200}{50} = 4\,\mathrm{A}$.
  \item Armature current: $I_a = I_L + I_{sh} = 96 + 4 = 100\,\mathrm{A}$.
\end{itemize}
\paragraph{2. Generated EMF ($E_g$):}
\begin{equation}
  E_g = V + I_a R_a = 200 + (100 \times 0.1) = 200 + 10 = 210\,\mathrm{V}
\end{equation}
\paragraph{3. Power \& Efficiency Calculations:}
\begin{itemize}[leftmargin=1.5em]
  \item Electrical output power: $P_{\text{out}} = V \cdot I_L = 200 \times 96 = 19,200\,\mathrm{W} = 19.2\,\mathrm{kW}$.
  \item Armature copper loss: $I_a^2 R_a = (100)^2 \times 0.1 = 1000\,\mathrm{W}$.
  \item Shunt copper loss: $I_{sh}^2 R_{sh} = (4)^2 \times 50 = 800\,\mathrm{W}$.
  \item Total copper loss: $P_{Cu} = 1000 + 800 = 1800\,\mathrm{W}$.
  \item Stray losses (Iron + Friction): $P_{\text{stray}} = 2500\,\mathrm{W}$.
  \item Total losses: $P_{\text{loss}} = 1800 + 2500 = 4300\,\mathrm{W}$.
  \item Total mechanical input power: $P_{\text{in}} = P_{\text{out}} + P_{\text{loss}} = 19,200 + 4300 = 23,500\,\mathrm{W}$.
\end{itemize}
\begin{equation}
  \eta_c = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\% = \frac{19,200}{23,500} \times 100\% \approx 81.70\%
\end{equation}

\begin{answerbox}
\[
\text{(a) Generated EMF } E_g = 210\,\mathrm{V}, \qquad \text{(b) Commercial Efficiency } \eta_c = 81.70\%
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 8.2 2082 Bhadra Q8
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 8 [5 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q8)}
A circular ring of magnetic material has a mean length of 0.5 m, cross sectional area of $100\,\mathrm{cm}^2$ and an air gap of 4 mm. Calculate the MMF required to produce flux of 2 mWb in the air gap, if ring is wound with a coil of 200 turns. Take relative permeability of 800.
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Given Data:}
$l_i = 0.5\,\mathrm{m}$ (iron path), \quad $l_g = 4\,\mathrm{mm} = 4 \times 10^{-3}\,\mathrm{m}$, \quad $A = 100\,\mathrm{cm}^2 = 0.01\,\mathrm{m}^2$, \quad $\Phi = 2\,\mathrm{mWb} = 2 \times 10^{-3}\,\mathrm{Wb}$, \quad $\mu_r = 800$, \quad $\mu_0 = 4\pi \times 10^{-7}\,\mathrm{H/m}$.

\paragraph{2. Magnetic Reluctance Method:}
\begin{align*}
  B &= \frac{\Phi}{A} = \frac{2 \times 10^{-3}}{0.01} = 0.2\,\mathrm{T} \\
  S_i &= \frac{l_i}{\mu_0 \mu_r A} = \frac{0.5}{(4\pi \times 10^{-7})(800)(0.01)} = \frac{0.5}{1.0053 \times 10^{-5}} \approx 49,735.9\,\mathrm{AT/Wb} \\
  S_g &= \frac{l_g}{\mu_0 A} = \frac{4 \times 10^{-3}}{(4\pi \times 10^{-7})(0.01)} = \frac{4 \times 10^{-3}}{1.2566 \times 10^{-8}} \approx 318,309.9\,\mathrm{AT/Wb} \\
  S_{\text{total}} &= S_i + S_g = 49,735.9 + 318,309.9 = 368,045.8\,\mathrm{AT/Wb}
\end{align*}

\paragraph{3. Total Required MMF:}
\begin{equation}
  \text{MMF} = \Phi \times S_{\text{total}} = (2 \times 10^{-3}) \times 368,045.8 \approx 736.09\,\mathrm{AT}
\end{equation}
\textit{Note:} If net iron path is taken as $l_i' = 0.5 - 0.004 = 0.496\,\mathrm{m}$, $\text{MMF} = 735.30\,\mathrm{AT}$. Exciting current $I = \frac{736.09}{200} \approx 3.68\,\mathrm{A}$.

\begin{answerbox}
\[
\text{Total MMF Required} = 736.09\,\mathrm{AT} \quad (\text{Exciting current } I = 3.68\,\mathrm{A})
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 8.3 2082 Baishakh Q8
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 8 [4 + 2 = 6 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q8)}
Explain the production of torque in DC motor with necessary mathematical explanation and derivation. What is the role of back emf in DC motor?
\end{questionbox}

\subsubsection*{Part A: Derivation of DC Motor Torque Equation}
When armature conductors carrying current $I_c = \frac{I_a}{A}$ lie within magnetic field $B$, each conductor experiences Lorentz force $F = B I_c l$.
\begin{itemize}[leftmargin=1.5em]
  \item Magnetic flux density: $B = \frac{\text{Total Flux}}{\text{Cylindrical Area}} = \frac{P \Phi}{2\pi r l}$.
  \item Torque per conductor: $T_c = F \cdot r = (B I_c l) r = \left(\frac{P \Phi}{2\pi r l}\right) \left(\frac{I_a}{A}\right) l r = \frac{P \Phi I_a}{2\pi A}$.
  \item Total electromagnetic torque $T_a$ for all $Z$ armature conductors:
  \begin{equation}
    T_a = Z \cdot T_c = \frac{P Z \Phi I_a}{2\pi A} = 0.159 \left(\frac{P Z}{A}\right) \Phi I_a \text{ N}\cdot\text{m}
  \end{equation}
\end{itemize}

\subsubsection*{Part B: Role and Significance of Back EMF ($E_b$)}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Self-Regulating Governor:} Armature current is governed by $I_a = \frac{V - E_b}{R_a}$. When mechanical shaft load increases, speed $N$ momentarily falls $\implies E_b \propto N\Phi$ decreases $\implies I_a$ rises sharply $\implies$ developed torque increases to match load demand automatically.
  \item \textbf{Electromechanical Energy Conversion:} Multiplying voltage balance $V = E_b + I_a R_a$ by $I_a$:
  \[
  V I_a = E_b I_a + I_a^2 R_a
  \]
  $V I_a$ is electrical power input, $I_a^2 R_a$ is heat loss, and $E_b I_a = P_{\text{mech}}$ represents the converted mechanical power.
\end{enumerate}

\newpage

% ------------------------------------------------------------------------------
% 8.4 2081 Ashwin Q8
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 8 [6 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q8)}
A 240 V dc shunt motor has armature winding resistance of $0.4\,\Omega$ and field winding resistance of $120\,\Omega$. It draws a current of 30 A at half load and the corresponding speed is 1400 rpm. If a resistance of $1.2\,\Omega$ is connected in series with the armature winding and load torque is decreased by 20\%, calculate the new speed.
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Initial Condition 1 (Half Load):}
$V = 240\,\mathrm{V}, I_{L1} = 30\,\mathrm{A}, N_1 = 1400\,\mathrm{rpm}, R_a = 0.4\,\Omega, R_{sh} = 120\,\Omega$:
\begin{align*}
  I_{sh} &= \frac{V}{R_{sh}} = \frac{240}{120} = 2\,\mathrm{A} \quad (\text{constant flux } \Phi) \\
  I_{a1} &= I_{L1} - I_{sh} = 30 - 2 = 28\,\mathrm{A} \\
  E_{b1} &= V - I_{a1} R_a = 240 - 28(0.4) = 240 - 11.2 = 228.8\,\mathrm{V}
\end{align*}

\paragraph{2. Modified Condition 2 (Armature Resistance Inserted \& Torque Reduced):}
\begin{itemize}[leftmargin=1.5em]
  \item Series resistance added: $R_{\text{ext}} = 1.2\,\Omega \implies R_{a2} = 0.4 + 1.2 = 1.6\,\Omega$.
  \item Load torque reduced by 20\%: $T_2 = 0.8 T_1$.
  \item Since flux $\Phi$ is constant, torque $T \propto I_a$:
  \[
  \frac{T_2}{T_1} = \frac{I_{a2}}{I_{a1}} \implies 0.8 = \frac{I_{a2}}{28} \implies I_{a2} = 0.8 \times 28 = 22.4\,\mathrm{A}
  \]
  \item New back EMF $E_{b2}$:
  \[
  E_{b2} = V - I_{a2} R_{a2} = 240 - 22.4(1.6) = 240 - 35.84 = 204.16\,\mathrm{V}
  \]
\end{itemize}

\paragraph{3. Calculation of New Speed $N_2$:}
Since $E_b \propto N \Phi$ (with $\Phi = \text{constant}$):
\begin{equation}
  \frac{E_{b2}}{E_{b1}} = \frac{N_2}{N_1} \implies N_2 = N_1 \left(\frac{E_{b2}}{E_{b1}}\right) = 1400 \times \left(\frac{204.16}{228.8}\right) \approx 1249.25\,\mathrm{rpm}
\end{equation}

\begin{answerbox}
\[
\text{New Operating Motor Speed } N_2 = 1249.25\,\mathrm{rpm}
\]
\end{answerbox}

\newpage

% ==============================================================================
% CHAPTER 9: THREE-PHASE INDUCTION MOTORS
% ==============================================================================
\section{Question 9: Three-Phase Induction Motors \& Transformer Efficiency}

% ------------------------------------------------------------------------------
% 9.1 2083 Baishakh Q9
% ------------------------------------------------------------------------------
\subsection{2083 Baishakh --- Question 9 [5 Marks]}

\begin{questionbox}{Problem Statement (2083 Baishakh, Q9)}
A three-phase induction motor is wound for 4 poles and supplied from 50 Hz supply system. Calculate:
(a) The speed of motor when the slip is 5\%
(b) The rotor emf frequency when the motor runs at 600 rpm.
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Synchronous Speed ($N_s$):}
\[
N_s = \frac{120 f}{P} = \frac{120 \times 50}{4} = 1500\,\mathrm{rpm}
\]
\paragraph{2. Part (a): Speed at Slip $s = 0.05$:}
\[
N = N_s(1 - s) = 1500(1 - 0.05) = 1500 \times 0.95 = 1425\,\mathrm{rpm}
\]
\paragraph{3. Part (b): Rotor EMF Frequency at $N = 600\,\mathrm{rpm}$:}
\[
s = \frac{N_s - N}{N_s} = \frac{1500 - 600}{1500} = \frac{900}{1500} = 0.6 \quad (60\%)
\]
\[
f_r = s \cdot f = 0.6 \times 50 = 30\,\mathrm{Hz}
\]

\begin{answerbox}
\[
\text{(a) Motor Speed } N = 1425\,\mathrm{rpm}, \qquad \text{(b) Rotor EMF Frequency } f_r = 30\,\mathrm{Hz}
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 9.2 2082 Bhadra Q9
% ------------------------------------------------------------------------------
\subsection{2082 Bhadra --- Question 9 [5 Marks]}

\begin{questionbox}{Problem Statement (2082 Bhadra, Q9)}
A 150 kVA single phase transformer has an iron loss of 700 W and a full load copper loss of 1800 W. Calculate the copper losses, iron losses, output power and efficiency of transformer at 0.8 power factor lagging when secondary is 25\% overloaded.
\end{questionbox}

\subsubsection*{Step-by-Step Solution}
\paragraph{1. Loading Parameters:}
$S = 150\,\mathrm{kVA}, \cos\phi = 0.8\,\mathrm{lag}, P_i = 700\,\mathrm{W} = 0.7\,\mathrm{kW}, P_{Cu,FL} = 1800\,\mathrm{W} = 1.8\,\mathrm{kW}$.
Loading factor for 25\% overload: $x = 1 + 0.25 = 1.25$.
\paragraph{2. Losses and Power:}
\begin{itemize}[leftmargin=1.5em]
  \item Iron Loss (independent of load): $P_i = 700\,\mathrm{W} = 0.7\,\mathrm{kW}$.
  \item Copper Loss at 25\% overload:
  \[
  P_{Cu,x} = x^2 P_{Cu,FL} = (1.25)^2 \times 1800 = 1.5625 \times 1800 = 2812.5\,\mathrm{W} = 2.8125\,\mathrm{kW}
  \]
  \item Output Active Power:
  \[
  P_{\text{out}} = x \cdot S \cdot \cos\phi = 1.25 \times 150 \times 0.8 = 150\,\mathrm{kW}
  \]
  \item Total Losses: $P_{\text{loss}} = P_i + P_{Cu,x} = 0.7 + 2.8125 = 3.5125\,\mathrm{kW}$.
\end{itemize}
\paragraph{3. Efficiency Calculation:}
\begin{equation}
  \eta = \frac{P_{\text{out}}}{P_{\text{out}} + P_{\text{loss}}} \times 100\% = \frac{150}{150 + 3.5125} \times 100\% = \frac{150}{153.5125} \times 100\% \approx 97.71\%
\end{equation}

\begin{answerbox}
\[
P_i = 700\,\mathrm{W}, \quad P_{Cu} = 2812.5\,\mathrm{W}, \quad P_{\text{out}} = 150\,\mathrm{kW}, \quad \eta = 97.71\%
\]
\end{answerbox}

\newpage

% ------------------------------------------------------------------------------
% 9.3 2082 Baishakh Q9
% ------------------------------------------------------------------------------
\subsection{2082 Baishakh --- Question 9 [6 Marks]}

\begin{questionbox}{Problem Statement (2082 Baishakh, Q9)}
How does three phase induction motor start? Why speed of this motor never reaches synchronous speed?
\end{questionbox}

\subsubsection*{1. Starting and Operating Mechanism of 3-Phase Induction Motor}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Production of Rotating Magnetic Field (RMF):} When balanced 3-phase currents displaced by $120^\circ$ electrical flow through stator windings spaced $120^\circ$ apart in space, a constant-magnitude magnetic field ($\Phi_R = 1.5 \Phi_m$) rotating at synchronous speed $N_s = \frac{120f}{P}$ is generated in the air gap.
  \item \textbf{Rotor EMF Induction:} The RMF sweeps across the stationary rotor conductors at relative speed $N_s$, inducing alternating EMFs by Faraday's Law.
  \item \textbf{Torque Production:} Because rotor bars form a closed electrical circuit (via end rings), the induced EMF circulates large rotor currents. These currents interact with the stator magnetic field to create Lorentz driving forces ($F = B I L$), accelerating the rotor in the direction of the RMF (per Lenz's Law).
\end{enumerate}

\subsubsection*{2. Why Motor Speed Can Never Reach Synchronous Speed ($N < N_s$)}
\begin{itemize}[leftmargin=1.5em]
  \item Induction motor torque requires \textbf{relative motion} $(N_s - N)$ between the stator RMF and the rotor conductors.
  \item If the rotor reached synchronous speed ($N = N_s$):
    \begin{itemize}
      \item Relative speed would become zero: $N_s - N = 0$.
      \item Rate of magnetic flux cutting would drop to zero $\implies$ Induced rotor EMF $e_r = 0$.
      \item Rotor current $i_r = 0 \implies$ Electromagnetic torque $T = 0$.
    \end{itemize}
  \item With zero driving torque, mechanical friction and windage immediately decelerate the rotor, ensuring it always operates with a finite positive slip $s = \frac{N_s - N}{N_s} > 0$.
\end{itemize}

\newpage

% ------------------------------------------------------------------------------
% 9.4 2081 Ashwin Q9
% ------------------------------------------------------------------------------
\subsection{2081 Ashwin --- Question 9 [6 Marks]}

\begin{questionbox}{Problem Statement (2081 Ashwin, Q9)}
Explain the Torque-speed characteristics of three phase induction motor with the help of proper mathematics and graph.
\end{questionbox}

\subsubsection*{Mathematical Derivation of Torque Equation}
Per-phase rotor current at slip $s$: $I_2 = \frac{s E_2}{\sqrt{R_2^2 + (s X_2)^2}}$, with power factor $\cos\phi_2 = \frac{R_2}{\sqrt{R_2^2 + (s X_2)^2}}$.
The developed electromagnetic torque is:
\begin{equation}
  T = \frac{3}{2\pi N_s/60} \cdot I_2^2 \left(\frac{R_2}{s}\right) = \frac{k s E_2^2 R_2}{R_2^2 + (s X_2)^2}
\end{equation}

\subsubsection*{Operating Regions \& Characteristic Curve}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Low-Slip Stable Region ($s \approx 0$, near $N_s$):} Since $s$ is very small, $(s X_2)^2 \ll R_2^2$:
  \[
  T \approx \left(\frac{k E_2^2}{R_2}\right) s \implies T \propto s \propto (N_s - N) \quad \text{(Linear operating zone)}
  \]
  \item \textbf{High-Slip Unstable Region ($s \approx 1$, near standstill):} Since $s$ is large, $(s X_2)^2 \gg R_2^2$:
  \[
  T \approx \left(\frac{k E_2^2 R_2}{X_2^2}\right) \frac{1}{s} \implies T \propto \frac{1}{s} \quad \text{(Rectangular hyperbola)}
  \]
  \item \textbf{Maximum / Breakdown Torque ($T_{\max}$):} Differentiating $T$ with respect to $s$ yields maximum torque at slip:
  \begin{equation}
    s_m = \frac{R_2}{X_2} \implies T_{\max} = \frac{k E_2^2}{2 X_2}
  \end{equation}
  $T_{\max}$ is independent of rotor resistance $R_2$, but adding external rotor resistance shifts $s_m$ towards unity, allowing maximum torque at startup ($R_2 = X_2$).
\end{enumerate}

\begin{center}
\includegraphics[width=0.85\textwidth]{figures/im_torque_speed.pdf}
\end{center}

\newpage

% ==============================================================================
% CHAPTER 10: CONCEPTUAL SHORT NOTES
% ==============================================================================
\section{Question 10: Conceptual Justifications \& Short Notes}

\subsection{2083 Baishakh --- Question 10 [3 $\times$ 3 = 9 Marks]}

\subsubsection*{(a) Series and Parallel Magnetic Circuits}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Series Magnetic Circuit:} A magnetic circuit where the same magnetic flux $\Phi$ passes through all sections in series (e.g., iron core and air gap). Total reluctance is the algebraic sum: $S_{\text{total}} = S_1 + S_2 + \cdots + S_n$. Total MMF required: $\text{MMF} = \Phi S_{\text{total}} = H_1 l_1 + H_2 l_2 + \cdots + H_n l_n$.
  \item \textbf{Parallel Magnetic Circuit:} A magnetic circuit with two or more flux paths. Total flux divides across parallel branches ($\Phi = \Phi_1 + \Phi_2$). The MMF across each parallel branch is identical ($\text{MMF} = \Phi_1 S_1 = \Phi_2 S_2$).
\end{itemize}

\subsubsection*{(b) Universal Motor}
A series-wound commutator motor capable of operating on either single-phase AC or DC supply.
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Principle:} Under AC supply, both armature current $I_a$ and field flux $\Phi$ reverse simultaneously every half-cycle, maintaining positive unidirectional torque ($T \propto \Phi I_a > 0$).
  \item \textbf{Design Features:} Stator and rotor iron are completely laminated to reduce eddy current losses.
  \item \textbf{Applications:} High-speed appliances including vacuum cleaners, blenders, food processors, and portable power drills.
\end{itemize}

\subsubsection*{(c) DC Motor Starter}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Need for Starter:} At standstill ($N=0$), back EMF $E_b = 0$. Since armature resistance $R_a$ is very small ($< 1\,\Omega$), direct online starting draws a destructive current $I_{a,\text{start}} = \frac{V}{R_a}$ (10 to 20 times rated current), which would burn out windings and blow fuses.
  \item \textbf{Function:} A starter (e.g., 3-point or 4-point starter) inserts a variable external resistance in series with the armature during startup, cutting it out progressively as back EMF $E_b$ builds up.
\end{itemize}

\subsubsection*{(d) Voltage Regulation of Transformer}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Definition:} The fractional or percentage change in secondary terminal voltage from no-load ($V_{20}$) to full-load ($V_2$), keeping primary supply voltage constant:
  \begin{equation}
    \% \text{ Regulation} = \frac{V_{20} - V_2}{V_2} \times 100\% \approx \frac{I_2 R_{e2}\cos\phi \pm I_2 X_{e2}\sin\phi}{V_2} \times 100\%
  \end{equation}
  ($+$ for lagging power factor, $-$ for leading power factor).
\end{itemize}

\newpage

\subsection{2082 Bhadra --- Question 10 [3 $\times$ 3 = 9 Marks]}

\subsubsection*{(a) Speed of 3-Phase Induction Motor is Always Less than Synchronous Speed}
\textbf{Justification:} Induction motor torque generation fundamentally requires rate of flux cutting $\frac{d\Phi}{dt} \ne 0$ between stator RMF and rotor conductors. At synchronous speed $N = N_s$, relative velocity is zero $\implies$ zero induced EMF $\implies$ zero rotor current $\implies$ zero torque. Mechanical friction prevents the rotor from ever maintaining $N = N_s$.

\subsubsection*{(b) Iron Losses of Transformer are Independent of Load}
\textbf{Justification:} Iron losses comprise hysteresis loss ($P_h \propto B_m^{1.6} f$) and eddy current loss ($P_e \propto B_m^2 f^2$). Since primary voltage $V_1 \approx 4.44 f N_1 \Phi_m$ is constant, peak core flux density $B_m$ remains strictly constant from no-load to full-load. Hence, iron losses remain constant.

\subsubsection*{(c) DC Motor Draws High Starting Current when Switched on Directly}
\textbf{Justification:} From $I_a = \frac{V - E_b}{R_a}$, at startup ($t=0, N=0$), $E_b = 0$. Since armature resistance $R_a$ is negligible, $I_{a,\text{start}} = \frac{V}{R_a}$ reaches $500\%\text{ to }2000\%$ of rated full-load current.

\subsubsection*{(d) Single-Phase Induction Motor Has Two Stator Windings}
\textbf{Justification:} A single-phase stator winding produces a pulsating stationary magnetic field with zero net starting torque (by Double-Field Revolving Theory). To produce an initial rotating magnetic field, an auxiliary starting winding is placed $90^\circ$ electrical apart with a series phase-splitting capacitor.

\vspace{0.8cm}
\subsection{2082 Baishakh --- Question 10 [2 $\times$ 3 = 6 Marks]}

\subsubsection*{(a) Magnetization of Magnetic Material \& $B$-$H$ Hysteresis Loop}
Applying magnetic field intensity $H$ aligns magnetic dipoles. The $B$-$H$ curve exhibits a linear region, knee point, saturation ($B_{\text{sat}}$), remanence/retentivity ($B_r$), and coercive force ($H_c$). Cyclic AC magnetization causes hysteresis energy loss equal to the loop area: $P_h = \eta B_m^{1.6} f V\,\mathrm{W}$.

\begin{center}
\includegraphics[width=0.65\textwidth]{figures/bh_hysteresis.pdf}
\end{center}

\subsubsection*{(b) Auto-Transformer and Its Applications}
A transformer with a single continuous tapped winding common to both primary and secondary.
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Power Transfer:} Converted partly by electrical conduction and partly by magnetic induction.
  \item \textbf{Advantages:} Uses less copper ($\text{Weight}_{\text{auto}} = (1 - k)\text{Weight}_{2\text{W}}$), lower cost, higher efficiency, and superior voltage regulation.
  \item \textbf{Applications:} Laboratory Variacs, induction motor starters, transmission line booster transformers.
\end{itemize}

\subsubsection*{(c) Stepper Motor}
An electromechanical digital actuator that rotates in discrete angular steps ($\theta_s = \frac{360^\circ}{m P}$) per input electrical pulse. Operates open-loop without feedback encoders in 3D printers, CNC machines, and robotics.

\newpage

\subsection{2081 Ashwin --- Question 10 [2 $\times$ 3 = 6 Marks]}

\subsubsection*{(a) Role of Commutator and Carbon Brush in DC Machine}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Commutator:} Mechanical inverter/rectifier maintaining unidirectional torque in motors and DC output in generators.
  \item \textbf{Carbon Brushes:} Self-lubricating, wear-resistant sliding electrical collectors feeding current to/from rotating segments.
\end{itemize}

\subsubsection*{(b) Hysteresis and Eddy Current Power Losses}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Hysteresis Loss ($P_h = \eta B_m^{1.6} f V\,\mathrm{W}$):} Energy lost in overcoming magnetic domain friction during cyclic AC reversal. Minimized using high-permeability silicon steel.
  \item \textbf{Eddy Current Loss ($P_e = K_e B_m^2 f^2 t^2 V\,\mathrm{W}$):} Ohmic $I^2R$ power lost due to circulating currents induced in the conductive core. Minimized by laminating the core into thin, varnished sheets ($t \approx 0.35\,\mathrm{mm}$).
\end{itemize}

\subsubsection*{(c) Stepper Motor Types and Characteristics}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Variable Reluctance (VR):} Multi-toothed iron rotor seeking minimum reluctance path.
  \item \textbf{Permanent Magnet (PM):} High detent torque with permanent magnet rotor poles.
  \item \textbf{Hybrid Stepper Motor:} Combines VR teeth and PM core for high resolution ($1.8^\circ$ step angle) and high holding torque.
\end{itemize}

\end{document}
'''

with open('Electrical_Circuits_and_Machines_Solutions_Master.tex', 'w') as f:
    f.write(latex_source)

print('File written. Running pdflatex...')
res1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Electrical_Circuits_and_Machines_Solutions_Master.tex'], capture_output=True, text=True)
print('Run 1 returncode:', res1.returncode)
if res1.returncode != 0:
    print('Errors in run 1:')
    for line in res1.stdout.splitlines():
        if line.startswith('!') or 'Error' in line:
            print(line)

res2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Electrical_Circuits_and_Machines_Solutions_Master.tex'], capture_output=True, text=True)
print('Run 2 returncode:', res2.returncode)
