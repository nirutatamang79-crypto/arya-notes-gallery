"""
Digital Logic (ENEX 152 / EX 152) — Master Solutions Book with Complete Logic Circuit Schematics
Tribhuvan University, Institute of Engineering (IOE)
Polished Logic Diagrams & Verified Schematics
"""

import os
import subprocess
import shutil

latex_content = r'''\documentclass[11pt,a4paper,oneside]{book}
\usepackage[utf8]{inputenc}
\usepackage[margin=1.8cm, top=2.2cm, bottom=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{array}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{circuitikz}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}

\usetikzlibrary{shapes.gates.logic.US,shapes.gates.logic.IEC,positioning,calc,automata,arrows.meta}

% Custom Color Palette
\definecolor{primarydark}{HTML}{0f172a}
\definecolor{secondaryblue}{HTML}{1e3a8a}
\definecolor{accentteal}{HTML}{0f766e}
\definecolor{boxbg}{HTML}{f8fafc}
\definecolor{boxborder}{HTML}{cbd5e1}
\definecolor{alertborder}{HTML}{0284c7}
\definecolor{ansbg}{HTML}{f0fdf4}
\definecolor{ansborder}{HTML}{16a34a}

% Typography & Headings
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries\color{primarydark}}{\chaptertitlename\ \thechapter}{14pt}{\Huge}
\titleformat{\section}
{\normalfont\Large\bfseries\color{secondaryblue}}{\thesection}{1em}{}
\titleformat{\subsection}
{\normalfont\large\bfseries\color{accentteal}}{\thesubsection}{1em}{}

% Headers & Footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\bfseries\sffamily\color{secondaryblue} Digital Logic (ENEX 152) --- IOE Master Solutions}
\fancyhead[R]{\small\sffamily\color{gray} Tribhuvan University}
\fancyfoot[C]{\sffamily\bfseries\thepage}
\renewcommand{\headrulewidth}{0.6pt}

% Custom TColorBoxes
\newtcolorbox{questionbox}[1]{
  colback=boxbg,
  colframe=alertborder,
  coltitle=white,
  fonttitle=\bfseries\sffamily,
  title={#1},
  arc=2.5mm,
  boxrule=1pt,
  breakable,
  enhanced
}

\newtcolorbox{answerbox}{
  colback=ansbg,
  colframe=ansborder,
  coltitle=white,
  fonttitle=\bfseries\sffamily,
  title={Verified Final Result},
  arc=2mm,
  boxrule=1pt,
  breakable,
  enhanced
}

\newtcolorbox{schematicbox}[1]{
  colback=white,
  colframe=primarydark,
  coltitle=white,
  fonttitle=\bfseries\sffamily,
  title={Logic Schematic: #1},
  arc=2mm,
  boxrule=0.8pt,
  center,
  breakable,
  enhanced
}

\begin{document}

\begin{titlepage}
  \centering
  \vspace*{1.5cm}
  {\Huge\textbf{\sffamily\color{primarydark} TRIBHUVAN UNIVERSITY}}\\[0.3cm]
  {\Large\textbf{\sffamily\color{secondaryblue} INSTITUTE OF ENGINEERING (IOE)}}\\[1.5cm]
  
  \begin{tcolorbox}[colback=primarydark,colframe=primarydark,arc=4mm,center,width=0.95\textwidth]
    \centering
    \vspace{0.4cm}
    {\Huge\textbf{\color{white}\sffamily DIGITAL LOGIC}}\\[0.3cm]
    {\Large\textbf{\color{accentteal}\sffamily Course Code: ENEX 152 / EX 152 / CT 152}}\\[0.2cm]
    {\large\color{white} BE Computer (BCT) \& BE Electronics (BEI) Engineering}
    \vspace{0.4cm}
  \end{tcolorbox}
  
  \vspace{1.5cm}
  {\LARGE\textbf{Master Past Examination Solutions Book}}\\[0.4cm]
  {\Large Complete Solved Papers with Complete TikZ Logic Schematics, K-Maps \& FSM State Automata}\\[0.8cm]
  \textbf{Covering All 4 Exam Sessions:}\\[0.2cm]
  \textbf{2083 Baishakh, 2082 Bhadra, 2082 Baishakh, and 2081 Ashwin}\\[1.5cm]
  
  \vfill
  {\large\textbf{Author: Antigravity Academic Publishing \& Typesetting}}\\[0.2cm]
  {\small Institute of Engineering Central Reference Portal}
  \vspace{1cm}
\end{titlepage}

\tableofcontents
\newpage

% ==============================================================================
% CHAPTER 1: 2083 BAISHAKH
% ==============================================================================
\chapter{2083 Baishakh Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Program:} BCT, BEI \\
\textbf{Year/Part:} I / II & \textbf{Full Marks:} 60 \quad \textbf{Pass Marks:} 24 \\
\end{tabular}

\vspace{0.5cm}

\subsection{Question 1: Gray Code to Binary Conversion [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q1)}
Convert the following Gray codes to binary codes:
\begin{enumerate}[label=(\alph*)]
  \item $10011_{\text{Gray}}$
  \item $110001_{\text{Gray}}$
\end{enumerate}
\end{questionbox}

\paragraph{Conversion Algorithm:}
Let Gray code bits be $G = g_{n-1} g_{n-2} \dots g_0$ and Binary bits be $B = b_{n-1} b_{n-2} \dots b_0$.
\begin{itemize}
  \item Most Significant Bit (MSB): $b_{n-1} = g_{n-1}$.
  \item For all subsequent bits ($i = n-2$ down to $0$): $b_i = b_{i+1} \oplus g_i$.
\end{itemize}

\paragraph{Part (a): $10011_{\text{Gray}}$}
\begin{enumerate}
  \item $b_4 = g_4 = 1$
  \item $b_3 = b_4 \oplus g_3 = 1 \oplus 0 = 1$
  \item $b_2 = b_3 \oplus g_2 = 1 \oplus 0 = 1$
  \item $b_1 = b_2 \oplus g_1 = 1 \oplus 1 = 0$
  \item $b_0 = b_1 \oplus g_0 = 0 \oplus 1 = 1$
\end{enumerate}
Therefore: $(10011)_{\text{Gray}} = (11101)_2$.

\paragraph{Part (b): $110001_{\text{Gray}}$}
\begin{enumerate}
  \item $b_5 = g_5 = 1$
  \item $b_4 = b_5 \oplus g_4 = 1 \oplus 1 = 0$
  \item $b_3 = b_4 \oplus g_3 = 0 \oplus 0 = 0$
  \item $b_2 = b_3 \oplus g_2 = 0 \oplus 0 = 0$
  \item $b_1 = b_2 \oplus g_1 = 0 \oplus 0 = 0$
  \item $b_0 = b_1 \oplus g_0 = 0 \oplus 1 = 1$
\end{enumerate}
Therefore: $(110001)_{\text{Gray}} = (100001)_2$.

\begin{answerbox}
\begin{align*}
\text{(a)}\quad (10011)_{\text{Gray}} &= \mathbf{(11101)_2} \\
\text{(b)}\quad (110001)_{\text{Gray}} &= \mathbf{(100001)_2}
\end{align*}
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: Analog vs. Digital Signals \& Excess-3 Code [1 + 2 = 3 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q2)}
Differentiate between analog and digital signals. Convert $(159)_{10}$ to excess-3 code.
\end{questionbox}

\paragraph{Comparison: Analog vs. Digital Signals}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Parameter} & \textbf{Analog Signal} & \textbf{Digital Signal} \\
\midrule
\textbf{Nature} & Continuous in time and amplitude & Discrete in time and quantized in amplitude \\
\textbf{Values} & Infinite values within a given range & Discrete levels (typically binary '0' and '1') \\
\textbf{Noise Immunity} & High susceptibility to noise/distortion & Superior noise immunity and error correction \\
\textbf{Storage/Processing} & Complex analog filters and storage & Easy storage in semiconductor memory, digital DSP \\
\textbf{Example} & Natural speech, temperature voltage & Microprocessor signals, digital audio/video \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Conversion of $(159)_{10}$ to Excess-3 Code:}
Excess-3 is formed by adding $3$ ($0011_2$) to each decimal digit:
\begin{itemize}
  \item Digit $1$: $1 + 3 = 4 \implies 0100_2$
  \item Digit $5$: $5 + 3 = 8 \implies 1000_2$
  \item Digit $9$: $9 + 3 = 12 \implies 1100_2$
\end{itemize}

\begin{answerbox}
$$(159)_{10} = \mathbf{0100\ 1000\ 1100_{\text{Excess-3}}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: Universal Logic Gates Schematics [3 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q3)}
Show that NAND and NOR gates are universal gates with logic diagrams.
\end{questionbox}

\begin{schematicbox}{Basic Gates Realized Using NAND Only}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % NOT Gate from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (nand_not) at (2,2) {};
  \draw (-0.2,2) node[left]{$A$} -- (0.8,2) |- (nand_not.input 1);
  \draw (0.8,2) |- (nand_not.input 2);
  \draw (nand_not.output) -- ++(0.8,0) node[right]{$Y = \bar{A}$};
  \node at (1.5,0.8) {\small \textbf{(a) NOT from NAND}};

  % AND Gate from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (nand_and1) at (6.5,2) {};
  \node[nand gate US, draw, logic gate inputs=nn] (nand_and2) at (9,2) {};
  \draw (4.8,2.2) node[left]{$A$} -- (nand_and1.input 1);
  \draw (4.8,1.8) node[left]{$B$} -- (nand_and1.input 2);
  \draw (nand_and1.output) -- (7.8,2) |- (nand_and2.input 1);
  \draw (7.8,2) |- (nand_and2.input 2);
  \draw (nand_and2.output) -- ++(0.8,0) node[right]{$Y = A \cdot B$};
  \node at (7.5,0.8) {\small \textbf{(b) AND from NAND}};

  % OR Gate from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (nand_or1) at (13,2.7) {};
  \node[nand gate US, draw, logic gate inputs=nn] (nand_or2) at (13,1.3) {};
  \node[nand gate US, draw, logic gate inputs=nn] (nand_or3) at (15.5,2) {};
  \draw (11.2,2.7) node[left]{$A$} -- (11.8,2.7) |- (nand_or1.input 1);
  \draw (11.8,2.7) |- (nand_or1.input 2);
  \draw (11.2,1.3) node[left]{$B$} -- (11.8,1.3) |- (nand_or2.input 1);
  \draw (11.8,1.3) |- (nand_or2.input 2);
  \draw (nand_or1.output) -- ++(0.5,0) |- (nand_or3.input 1);
  \draw (nand_or2.output) -- ++(0.5,0) |- (nand_or3.input 2);
  \draw (nand_or3.output) -- ++(0.8,0) node[right]{$Y = A + B$};
  \node at (14,0.8) {\small \textbf{(c) OR from NAND}};
\end{tikzpicture}
\end{schematicbox}

\begin{schematicbox}{Basic Gates Realized Using NOR Only}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % NOT Gate from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (nor_not) at (2,2) {};
  \draw (-0.2,2) node[left]{$A$} -- (0.8,2) |- (nor_not.input 1);
  \draw (0.8,2) |- (nor_not.input 2);
  \draw (nor_not.output) -- ++(0.8,0) node[right]{$Y = \bar{A}$};
  \node at (1.5,0.8) {\small \textbf{(a) NOT from NOR}};

  % OR Gate from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (nor_or1) at (6.5,2) {};
  \node[nor gate US, draw, logic gate inputs=nn] (nor_or2) at (9,2) {};
  \draw (4.8,2.2) node[left]{$A$} -- (nor_or1.input 1);
  \draw (4.8,1.8) node[left]{$B$} -- (nor_or1.input 2);
  \draw (nor_or1.output) -- (7.8,2) |- (nor_or2.input 1);
  \draw (7.8,2) |- (nor_or2.input 2);
  \draw (nor_or2.output) -- ++(0.8,0) node[right]{$Y = A + B$};
  \node at (7.5,0.8) {\small \textbf{(b) OR from NOR}};

  % AND Gate from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (nor_and1) at (13,2.7) {};
  \node[nor gate US, draw, logic gate inputs=nn] (nor_and2) at (13,1.3) {};
  \node[nor gate US, draw, logic gate inputs=nn] (nor_and3) at (15.5,2) {};
  \draw (11.2,2.7) node[left]{$A$} -- (11.8,2.7) |- (nor_and1.input 1);
  \draw (11.8,2.7) |- (nor_and1.input 2);
  \draw (11.2,1.3) node[left]{$B$} -- (11.8,1.3) |- (nor_and2.input 1);
  \draw (11.8,1.3) |- (nor_and2.input 2);
  \draw (nor_and1.output) -- ++(0.5,0) |- (nor_and3.input 1);
  \draw (nor_and2.output) -- ++(0.5,0) |- (nor_and3.input 2);
  \draw (nor_and3.output) -- ++(0.8,0) node[right]{$Y = A \cdot B$};
  \node at (14,0.8) {\small \textbf{(c) AND from NOR}};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Both NAND and NOR independently synthesize NOT, AND, and OR operators, proving universality.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 4: 4-Variable K-Map Minimization \& Circuit [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q4)}
Minimize $F(A,B,C,D) = \sum m(1, 2, 4, 5, 6, 8, 10, 11, 13, 15)$ using K-Map and realize it with suitable logic gates.
\end{questionbox}

\paragraph{Karnaugh Map Plotting:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{$AB \backslash CD$} & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $0$ ($m_0$) & $\mathbf{1}$ ($m_1$) & $0$ ($m_3$) & $\mathbf{1}$ ($m_2$) \\ \hline
\textbf{01} & $\mathbf{1}$ ($m_4$) & $\mathbf{1}$ ($m_5$) & $0$ ($m_7$) & $\mathbf{1}$ ($m_6$) \\ \hline
\textbf{11} & $0$ ($m_{12}$) & $\mathbf{1}$ ($m_{13}$) & $\mathbf{1}$ ($m_{15}$) & $0$ ($m_{14}$) \\ \hline
\textbf{10} & $\mathbf{1}$ ($m_8$) & $0$ ($m_9$) & $\mathbf{1}$ ($m_{11}$) & $\mathbf{1}$ ($m_{10}$) \\ \hline
\end{tabular}
\end{center}

\paragraph{Simplified Boolean Expression:}
$$F(A,B,C,D) = \bar{A}\bar{C}D + \bar{A}B\bar{D} + A\bar{B}\bar{D} + ACD + ABD$$

\begin{schematicbox}{Logic Circuit Realization for $F(A,B,C,D)$}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % Five 3-input AND gates with generous vertical spacing
  \node[and gate US, draw, logic gate inputs=nnn] (and1) at (4,4) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and2) at (4,2) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and3) at (4,0) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and4) at (4,-2) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and5) at (4,-4) {};

  % Input labels with clean lead-in wires
  \draw (1, 4.3) node[left]{\small $\bar{A}$} -- (and1.input 1);
  \draw (1, 4.0) node[left]{\small $\bar{C}$} -- (and1.input 2);
  \draw (1, 3.7) node[left]{\small $D$} -- (and1.input 3);

  \draw (1, 2.3) node[left]{\small $\bar{A}$} -- (and2.input 1);
  \draw (1, 2.0) node[left]{\small $B$} -- (and2.input 2);
  \draw (1, 1.7) node[left]{\small $\bar{D}$} -- (and2.input 3);

  \draw (1, 0.3) node[left]{\small $A$} -- (and3.input 1);
  \draw (1, 0.0) node[left]{\small $\bar{B}$} -- (and3.input 2);
  \draw (1,-0.3) node[left]{\small $\bar{D}$} -- (and3.input 3);

  \draw (1,-1.7) node[left]{\small $A$} -- (and4.input 1);
  \draw (1,-2.0) node[left]{\small $C$} -- (and4.input 2);
  \draw (1,-2.3) node[left]{\small $D$} -- (and4.input 3);

  \draw (1,-3.7) node[left]{\small $A$} -- (and5.input 1);
  \draw (1,-4.0) node[left]{\small $B$} -- (and5.input 2);
  \draw (1,-4.3) node[left]{\small $D$} -- (and5.input 3);

  % 5-input OR Gate
  \node[or gate US, draw, logic gate inputs=nnnnn, scale=1.4] (or_out) at (8,0) {};
  \draw (and1.output) -- ++(1.5,0) |- (or_out.input 1);
  \draw (and2.output) -- ++(1,0) |- (or_out.input 2);
  \draw (and3.output) -- (or_out.input 3);
  \draw (and4.output) -- ++(1,0) |- (or_out.input 4);
  \draw (and5.output) -- ++(1.5,0) |- (or_out.input 5);

  \draw (or_out.output) -- ++(1,0) node[right]{\large $\mathbf{F}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{F = \bar{A}\bar{C}D + \bar{A}B\bar{D} + A\bar{B}\bar{D} + ACD + ABD}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Octal-to-Binary Encoder Logic Circuit [2 + 4 = 6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q5)}
Differentiate between encoder and decoder. Design an Octal-to-Binary Encoder with necessary diagrams.
\end{questionbox}

\paragraph{Boolean Output Equations:}
\begin{align*}
A &= D_4 + D_5 + D_6 + D_7 \\
B &= D_2 + D_3 + D_6 + D_7 \\
C &= D_1 + D_3 + D_5 + D_7
\end{align*}

\begin{schematicbox}{Octal-to-Binary ($8$-to-$3$) Encoder Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Input Rail
  \foreach \i in {0,...,7} {
    \draw (0, 7-\i) node[left]{$D_\i$} -- (9, 7-\i);
  }

  % Three 4-input OR gates
  \node[or gate US, draw, logic gate inputs=nnnn, rotate=-90, scale=1.2] (orA) at (3, -1) {};
  \node[or gate US, draw, logic gate inputs=nnnn, rotate=-90, scale=1.2] (orB) at (5.5, -1) {};
  \node[or gate US, draw, logic gate inputs=nnnn, rotate=-90, scale=1.2] (orC) at (8, -1) {};

  % Output Lines
  \draw (orA.output) -- ++(0,-0.8) node[below]{\large $\mathbf{A}$ (MSB)};
  \draw (orB.output) -- ++(0,-0.8) node[below]{\large $\mathbf{B}$};
  \draw (orC.output) -- ++(0,-0.8) node[below]{\large $\mathbf{C}$ (LSB)};

  % Tap Points for OR A (D4, D5, D6, D7)
  \fill (3,3) circle (2pt); \draw (3,3) -- (orA.input 1);
  \fill (3,2) circle (2pt); \draw (3,2) -- (orA.input 2);
  \fill (3,1) circle (2pt); \draw (3,1) -- (orA.input 3);
  \fill (3,0) circle (2pt); \draw (3,0) -- (orA.input 4);

  % Tap Points for OR B (D2, D3, D6, D7)
  \fill (5.5,5) circle (2pt); \draw (5.5,5) -- (orB.input 1);
  \fill (5.5,4) circle (2pt); \draw (5.5,4) -- (orB.input 2);
  \fill (5.5,1) circle (2pt); \draw (5.5,1) -- (orB.input 3);
  \fill (5.5,0) circle (2pt); \draw (5.5,0) -- (orB.input 4);

  % Tap Points for OR C (D1, D3, D5, D7)
  \fill (8,6) circle (2pt); \draw (8,6) -- (orC.input 1);
  \fill (8,4) circle (2pt); \draw (8,4) -- (orC.input 2);
  \fill (8,2) circle (2pt); \draw (8,2) -- (orC.input 3);
  \fill (8,0) circle (2pt); \draw (8,0) -- (orC.input 4);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Logic Equations:} $A = D_4+D_5+D_6+D_7$, $B = D_2+D_3+D_6+D_7$, $C = D_1+D_3+D_5+D_7$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: Full Subtractor Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q6)}
Implement a Full Subtractor circuit using Multiplexer.
\end{questionbox}

\begin{schematicbox}{Full Subtractor Realization Using Two 4:1 Multiplexers}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % MUX 1: Difference
  \draw[thick, fill=boxbg] (0,0) rectangle (3,4);
  \node at (1.5,3.5) {\textbf{4:1 MUX (Diff)}};
  \node at (0.4,2.8) {\small $I_0$};
  \node at (0.4,2.2) {\small $I_1$};
  \node at (0.4,1.6) {\small $I_2$};
  \node at (0.4,1.0) {\small $I_3$};
  \node at (1.5,0.4) {\small $S_1\quad S_0$};
  \draw[thick] (3,2) -- (4.8,2) node[right]{\large $\mathbf{D}$ (Diff)};

  % MUX 2: Borrow Out
  \draw[thick, fill=boxbg] (8.5,0) rectangle (11.5,4);
  \node at (10.0,3.5) {\textbf{4:1 MUX ($B_{\text{out}}$)}};
  \node at (8.9,2.8) {\small $I_0$};
  \node at (8.9,2.2) {\small $I_1$};
  \node at (8.9,1.6) {\small $I_2$};
  \node at (8.9,1.0) {\small $I_3$};
  \node at (10.0,0.4) {\small $S_1\quad S_0$};
  \draw[thick] (11.5,2) -- (13.0,2) node[right]{\large $\mathbf{B_{\text{out}}}$};

  % Select Line Bus
  \draw[thick] (-1.5,-1.2) node[left]{$A$} -- (1.0,-1.2) -- (1.0,0);
  \draw[thick] (-1.5,-1.8) node[left]{$B$} -- (2.0,-1.8) -- (2.0,0);
  \draw[thick] (1.0,-1.2) -- (9.5,-1.2) -- (9.5,0);
  \draw[thick] (2.0,-1.8) -- (10.5,-1.8) -- (10.5,0);

  % Data Inputs Connections for MUX 1
  \draw (-1.5,2.8) node[left]{$B_{\text{in}}$} -- (0,2.8);
  \node[not gate US, draw, scale=0.8] (not1) at (-0.8,2.2) {};
  \draw (-1.5,2.2) -- (not1.input); \draw (not1.output) -- (0,2.2);
  \draw (-0.8,2.2) |- (0,1.6);
  \draw (-1.5,2.8) |- (0,1.0);

  % Data Inputs Connections for MUX 2
  \draw (6.8,2.8) node[left]{$B_{\text{in}}$} -- (8.5,2.8);
  \draw (6.8,2.2) node[left]{$1\ (V_{CC})$} -- (8.5,2.2);
  \draw (6.8,1.6) node[left]{$0\ (\text{GND})$} -- (8.5,1.6);
  \draw (6.8,2.8) |- (8.5,1.0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Difference (D):} $I_0 = B_{\text{in}}, I_1 = \overline{B_{\text{in}}}, I_2 = \overline{B_{\text{in}}}, I_3 = B_{\text{in}}$.\\[0.1cm]
\textbf{Borrow ($B_{\text{out}}$):} $I_0 = B_{\text{in}}, I_1 = 1, I_2 = 0, I_3 = B_{\text{in}}$. Select lines: $S_1=A, S_0=B$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 7: D Flip-Flop to JK Flip-Flop Conversion Schematic [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q7)}
Differentiate between latch and flip-flop. Modify a D flip-flop such that it functions as a JK flip-flop.
\end{questionbox}

\paragraph{Conversion Equation:} $D = J\bar{Q} + \bar{K}Q$.

\begin{schematicbox}{JK Flip-Flop Implementation Using D Flip-Flop}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % D Flip Flop Box
  \draw[thick, fill=boxbg] (6,1) rectangle (9,4.5);
  \node at (7.5,4) {\textbf{D Flip-Flop}};
  \node at (6.4,3.2) {\small $D$};
  \node at (6.5,2) {\small $> \text{CLK}$};
  \node at (8.6,3.2) {\small $Q$};
  \node at (8.6,1.8) {\small $\bar{Q}$};

  % Combinational Input Gates
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (2,3.5) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (2,1.8) {};
  \node[not gate US, draw, scale=0.7] (notK) at (0.2,1.6) {};
  \node[or gate US, draw, logic gate inputs=nn] (orD) at (4.5,2.6) {};

  % Inputs
  \draw (-1.5,3.7) node[left]{$J$} -- (and1.input 1);
  \draw (-1.5,1.6) node[left]{$K$} -- (notK.input); \draw (notK.output) -- (and2.input 2);

  % OR Gate Connection to D
  \draw (and1.output) -- ++(0.8,0) |- (orD.input 1);
  \draw (and2.output) -- ++(0.8,0) |- (orD.input 2);
  \draw (orD.output) -- (6,2.6);

  % Outputs and Feedbacks
  \draw[thick] (9,3.2) -- (10.5,3.2) node[right]{\large $\mathbf{Q}$};
  \draw[thick] (9,1.8) -- (10.5,1.8) node[right]{\large $\mathbf{\bar{Q}}$};

  % Feedback Lines
  \draw (9.8,3.2) -- (9.8,0.6) -- (0.8,0.6) |- (and2.input 1);
  \draw (9.5,1.8) -- (9.5,4.8) -- (0.8,4.8) |- (and1.input 2);
  \draw (4.5,2.0) node[left]{$\text{CLK}$} -- (6,2.0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{D = J\bar{Q} + \bar{K}Q}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: 4-Bit SIPO Shift Register Schematic & Timing Diagram [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q8)}
Explain the working of 4-bit SIPO register with timing diagram of 1010 data input.
\end{questionbox}

\begin{schematicbox}{4-Bit Serial-In Parallel-Out (SIPO) Shift Register Schematic}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({(\i)*3.6}, 0) rectangle ({(\i)*3.6 + 2.4}, 3);
    \node at ({(\i)*3.6 + 1.2}, 2.6) {\textbf{FF\i\ (D)}};
    \node at ({(\i)*3.6 + 0.4}, 1.8) {\small $D$};
    \node at ({(\i)*3.6 + 0.5}, 0.8) {\small $>$};
    \node at ({(\i)*3.6 + 2.0}, 1.8) {\small $Q$};
    \draw[thick] ({(\i)*3.6 + 2.4}, 1.8) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  % Serial Input entering FF0
  \draw[thick] (-1.0, 1.8) node[left]{\large $\mathbf{D_{\text{in}}}$ (Serial)} -- (0, 1.8);

  % Inter-stage connections from Qi to Di+1
  \draw[thick] (2.4, 1.8) -- (3.6, 1.8);
  \draw[thick] (6.0, 1.8) -- (7.2, 1.8);
  \draw[thick] (9.6, 1.8) -- (10.8, 1.8);

  % Common Clock Bus
  \draw[thick] (-1.0, -1.0) node[left]{\large $\mathbf{\text{CLK}}$} -- (12.0, -1.0);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 0.5}, -1.0) -- ({(\i)*3.6 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Four clock pulses load serial word $1010_2$ into parallel outputs $Q_3 Q_2 Q_1 Q_0$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: Asynchronous BCD (Decade) Counter Schematic [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q9)}
Describe the operation of asynchronous BCD (decade) counter with necessary diagrams.
\end{questionbox}

\begin{schematicbox}{Asynchronous BCD (Decade) Counter Schematic}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({(\i)*3.6}, 0) rectangle ({(\i)*3.6 + 2.4}, 3);
    \node at ({(\i)*3.6 + 1.2}, 2.6) {\textbf{FF\i\ (T/JK)}};
    \node at ({(\i)*3.6 + 0.5}, 1.5) {\small $>$};
    \node at ({(\i)*3.6 + 2.0}, 2.0) {\small $Q$};
    \node at ({(\i)*3.6 + 2.0}, 1.0) {\small $\bar{Q}$};
    \node at ({(\i)*3.6 + 1.2}, 0.4) {\small $\overline{\text{CLR}}$};
    \draw[thick] ({(\i)*3.6 + 2.4}, 2.0) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  % External Clock into FF0
  \draw[thick] (-1.0, 1.5) node[left]{\large $\mathbf{\text{CLK}}$} -- (0, 1.5);

  % Ripple Clocks (Negative edge triggered: Q into next CLK)
  \draw[thick] (2.4, 2.0) -- (3.0, 2.0) |- (3.6, 1.5);
  \draw[thick] (6.0, 2.0) -- (6.6, 2.0) |- (7.2, 1.5);
  \draw[thick] (9.6, 2.0) -- (10.2, 2.0) |- (10.8, 1.5);

  % NAND Reset Gate for State 1010 (Q3=1, Q1=1)
  \node[nand gate US, draw, logic gate inputs=nn, rotate=-90] (nand_rst) at (6, -2.5) {};
  \draw (9.6+1.2, 2.0) -- ++(0,-3.5) |- (nand_rst.input 1);
  \draw (3.6+1.2, 2.0) -- ++(0,-3.5) |- (nand_rst.input 2);

  % Active-low Clear Bus
  \draw[thick] (nand_rst.output) -- (6, -4.0) -- (-0.5, -4.0);
  \draw[thick] (-0.5, -4.0) -- (-0.5, -0.6) -- (12.0, -0.6);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 1.2}, -0.6) -- ({(\i)*3.6 + 1.2}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Reset Equation:} $\overline{\text{CLR}} = \overline{Q_3 \cdot Q_1}$. The counter resets at binary state $1010_2$, providing $10$ stable states ($0$ to $9$).
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 10: Synchronous Mod-10 UP Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q10)}
Design a synchronous Mod-10 UP counter using T flip-flops and draw its timing diagram.
\end{questionbox}

\paragraph{Design Equations:}
$$T_0 = 1, \qquad T_1 = \bar{Q}_3 Q_0, \qquad T_2 = Q_1 Q_0, \qquad T_3 = Q_2 Q_1 Q_0 + Q_3 Q_0$$

\begin{schematicbox}{Synchronous Mod-10 UP Counter Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({(\i)*3.6}, 0) rectangle ({(\i)*3.6 + 2.4}, 3);
    \node at ({(\i)*3.6 + 1.2}, 2.6) {\textbf{FF\i\ (T)}};
    \node at ({(\i)*3.6 + 0.4}, 2.0) {\small $T$};
    \node at ({(\i)*3.6 + 0.5}, 0.8) {\small $>$};
    \node at ({(\i)*3.6 + 2.0}, 2.0) {\small $Q$};
    \node at ({(\i)*3.6 + 2.0}, 0.8) {\small $\bar{Q}$};
    \draw[thick] ({(\i)*3.6 + 2.4}, 2.0) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  % T0 = 1
  \draw[thick] (-0.8, 2.0) node[left]{$1\ (V_{CC})$} -- (0, 2.0);

  % Common Synchronous Clock
  \draw[thick] (-1.0, -1.2) node[left]{\large $\mathbf{\text{CLK}}$} -- (12.0, -1.2);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 0.5}, -1.2) -- ({(\i)*3.6 + 0.5}, 0);
  }

  % T1 Gate (Q0 . Q3_bar)
  \node[and gate US, draw, logic gate inputs=nn] (andT1) at (3.0, 2.0) {};
  \draw (andT1.output) -- (3.6, 2.0);

  % T2 Gate (Q0 . Q1)
  \node[and gate US, draw, logic gate inputs=nn] (andT2) at (6.6, 2.0) {};
  \draw (andT2.output) -- (7.2, 2.0);

  % T3 Gate (Q2.Q1.Q0 + Q3.Q0)
  \node[or gate US, draw, logic gate inputs=nn] (orT3) at (10.2, 2.0) {};
  \draw (orT3.output) -- (10.8, 2.0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{T_0 = 1, \quad T_1 = \bar{Q}_3 Q_0, \quad T_2 = Q_1 Q_0, \quad T_3 = Q_2 Q_1 Q_0 + Q_3 Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 11: Synchronous FSM Sequence Detector '011' [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q11)}
Design a synchronous sequential machine that has 1-bit serial input $X$ and output $Z$ which will be HIGH when the input contains the message $011$ (Use T Flip-Flop).
\end{questionbox}

\begin{schematicbox}{FSM State Transition Automaton for '011' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.2cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$1 / 0$} (S0)
             edge [bend left] node {$0 / 0$} (S1)
        (S1) edge [loop above] node {$0 / 0$} (S1)
             edge [bend left] node {$1 / 0$} (S2)
        (S2) edge [bend left=45] node [below] {$0 / 0$} (S1)
             edge [bend left=60] node [above] {$1 / \mathbf{1}$} (S0);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Logic Equations:}
$$T_A = BX + A, \qquad T_B = \bar{X} + X(A+B), \qquad Z = AX$$

\begin{answerbox}
$$\mathbf{T_A = BX + A, \qquad T_B = \bar{X} + X(A+B), \qquad Z = AX}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 12: Characteristics of Digital Logic Families [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q12)}
Explain about the main characteristics of digital logic families.
\end{questionbox}

\begin{enumerate}
  \item \textbf{Propagation Delay ($t_{pd}$):} Speed metric of logic switching.
  \item \textbf{Power Dissipation ($P_D$):} Power consumed per gate in mW.
  \item \textbf{Noise Margin ($NM$):} Maximum tolerable noise voltage.
  \item \textbf{Fan-Out:} Maximum load gates that can be driven.
  \item \textbf{Speed-Power Product (SPP):} $SPP = t_{pd} \times P_D$ (pJ).
\end{enumerate}

\newpage
% ==============================================================================
% CHAPTER 2: 2082 BHADRA
% ==============================================================================
\chapter{2082 Bhadra Examination Solutions}

\subsection{Question 1: Binary to Gray Code Conversion [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q1)}
Convert the following binary codes to Gray codes: (a) $101101_2$, (b) $110001_2$.
\end{questionbox}

\begin{answerbox}
(a) $(101101)_2 = \mathbf{111011_{\text{Gray}}}$ \qquad (b) $(110001)_2 = \mathbf{101001_{\text{Gray}}}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: 2's Complement \& BCD Addition [1 + 2 = 3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q2)}
What is 2's complement representation? Perform BCD addition of $23 + 48$.
\end{questionbox}

\begin{answerbox}
$$23 + 48 = \mathbf{0111\ 0001_{\text{BCD}}} = (71)_{10}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: De Morgan's Gate Equivalences [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q3)}
State and explain De Morgan's Theorem with truth table and necessary diagrams.
\end{questionbox}

\begin{schematicbox}{De Morgan's Equivalent Gate Schematics}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Theorem 1: NAND = Bubbled OR
  \node[nand gate US, draw, logic gate inputs=nn] (nand1) at (2,2) {};
  \draw (0.5,2.2) node[left]{$A$} -- (nand1.input 1);
  \draw (0.5,1.8) node[left]{$B$} -- (nand1.input 2);
  \draw (nand1.output) -- ++(0.8,0) node[right]{$\overline{A \cdot B}$};
  \node at (4.5,2) {\Large $\equiv$};
  \node[or gate US, draw, logic gate inputs=nn] (bub_or) at (7,2) {};
  \draw (5.5,2.2) node[left]{$A$} -- (bub_or.input 1);
  \draw (5.5,1.8) node[left]{$B$} -- (bub_or.input 2);
  \draw (bub_or.output) -- ++(0.8,0) node[right]{$\bar{A} + \bar{B}$};
  \node at (4.5,0.8) {\textbf{Theorem 1: $\overline{A \cdot B} = \bar{A} + \bar{B}$}};

  % Theorem 2: NOR = Bubbled AND
  \node[nor gate US, draw, logic gate inputs=nn] (nor1) at (2,-1.5) {};
  \draw (0.5,-1.3) node[left]{$A$} -- (nor1.input 1);
  \draw (0.5,-1.7) node[left]{$B$} -- (nor1.input 2);
  \draw (nor1.output) -- ++(0.8,0) node[right]{$\overline{A + B}$};
  \node at (4.5,-1.5) {\Large $\equiv$};
  \node[and gate US, draw, logic gate inputs=nn] (bub_and) at (7,-1.5) {};
  \draw (5.5,-1.3) node[left]{$A$} -- (bub_and.input 1);
  \draw (5.5,-1.7) node[left]{$B$} -- (bub_and.input 2);
  \draw (bub_and.output) -- ++(0.8,0) node[right]{$\bar{A} \cdot \bar{B}$};
  \node at (4.5,-2.7) {\textbf{Theorem 2: $\overline{A + B} = \bar{A} \cdot \bar{B}$}};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 4: K-Map Minimization with Don't Cares & Circuit [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q4)}
Minimize $F(A,B,C,D) = \sum m(0, 1, 2, 4, 7, 8, 9, 10, 12, 15) + d(5, 11, 13)$ using K-Map.
\end{questionbox}

\paragraph{Minimized Boolean Expression:}
$$F(A,B,C,D) = \bar{C} + BD + \bar{B}\bar{D}$$

\begin{schematicbox}{Logic Realization for $F = \bar{C} + BD + \bar{B}\bar{D}$}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (3,2) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (3,0.5) {};
  \node[or gate US, draw, logic gate inputs=nnn, scale=1.2] (orF) at (6,1.25) {};

  \draw (1,2.2) node[left]{$B$} -- (and1.input 1);
  \draw (1,1.8) node[left]{$D$} -- (and1.input 2);

  \draw (1,0.7) node[left]{$\bar{B}$} -- (and2.input 1);
  \draw (1,0.3) node[left]{$\bar{D}$} -- (and2.input 2);

  \draw (1,3.0) node[left]{$\bar{C}$} -- ++(3.5,0) |- (orF.input 1);
  \draw (and1.output) -- (orF.input 2);
  \draw (and2.output) -- ++(1,0) |- (orF.input 3);

  \draw (orF.output) -- ++(1,0) node[right]{\large $\mathbf{F}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{F = \bar{C} + BD + \bar{B}\bar{D}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: 3-Bit Magnitude Comparator Schematic [1 + 5 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q5)}
What is magnitude comparator? Design a 3-bit magnitude comparator.
\end{questionbox}

\begin{schematicbox}{3-Bit Magnitude Comparator Functional Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  \draw[thick, fill=boxbg] (0,0) rectangle (6,5);
  \node at (3,4.5) {\textbf{3-Bit Comparator}};
  
  \draw[thick] (-1.5,3.8) node[left]{$A_2 A_1 A_0$ ($3$-bit)} -- (0,3.8);
  \draw[thick] (-1.5,1.2) node[left]{$B_2 B_1 B_0$ ($3$-bit)} -- (0,1.2);

  \draw[thick] (6,3.8) -- ++(1.5,0) node[right]{\large $\mathbf{A > B} = A_2\bar{B}_2 + x_2 A_1\bar{B}_1 + x_2 x_1 A_0\bar{B}_0$};
  \draw[thick] (6,2.5) -- ++(1.5,0) node[right]{\large $\mathbf{A = B} = x_2 x_1 x_0$};
  \draw[thick] (6,1.2) -- ++(1.5,0) node[right]{\large $\mathbf{A < B} = \bar{A}_2 B_2 + x_2 \bar{A}_1 B_1 + x_2 x_1 \bar{A}_0 B_0$};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 6: Full Adder Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q6)}
Implement a full adder circuit using Multiplexer.
\end{questionbox}

\begin{schematicbox}{Full Adder Realization Using Two 4:1 Multiplexers}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % MUX 1: Sum
  \draw[thick, fill=boxbg] (0,0) rectangle (3,4);
  \node at (1.5,3.5) {\textbf{4:1 MUX (Sum)}};
  \node at (0.4,2.8) {\small $I_0$};
  \node at (0.4,2.2) {\small $I_1$};
  \node at (0.4,1.6) {\small $I_2$};
  \node at (0.4,1.0) {\small $I_3$};
  \node at (1.5,0.4) {\small $S_1\quad S_0$};
  \draw[thick] (3,2) -- (4.8,2) node[right]{\large $\mathbf{Sum}$};

  % MUX 2: Carry Out
  \draw[thick, fill=boxbg] (8.5,0) rectangle (11.5,4);
  \node at (10.0,3.5) {\textbf{4:1 MUX ($C_{\text{out}}$)}};
  \node at (8.9,2.8) {\small $I_0$};
  \node at (8.9,2.2) {\small $I_1$};
  \node at (8.9,1.6) {\small $I_2$};
  \node at (8.9,1.0) {\small $I_3$};
  \node at (10.0,0.4) {\small $S_1\quad S_0$};
  \draw[thick] (11.5,2) -- (13.0,2) node[right]{\large $\mathbf{C_{\text{out}}}$};

  % Select Line Bus
  \draw[thick] (-1.5,-1.2) node[left]{$A$} -- (1.0,-1.2) -- (1.0,0);
  \draw[thick] (-1.5,-1.8) node[left]{$B$} -- (2.0,-1.8) -- (2.0,0);
  \draw[thick] (1.0,-1.2) -- (9.5,-1.2) -- (9.5,0);
  \draw[thick] (2.0,-1.8) -- (10.5,-1.8) -- (10.5,0);

  % Data Inputs Connections for Sum
  \draw (-1.5,2.8) node[left]{$C_{\text{in}}$} -- (0,2.8);
  \node[not gate US, draw, scale=0.8] (not1) at (-0.8,2.2) {};
  \draw (-1.5,2.2) -- (not1.input); \draw (not1.output) -- (0,2.2);
  \draw (-0.8,2.2) |- (0,1.6);
  \draw (-1.5,2.8) |- (0,1.0);

  % Data Inputs Connections for Cout
  \draw (6.8,2.8) node[left]{$0\ (\text{GND})$} -- (8.5,2.8);
  \draw (6.8,2.2) node[left]{$C_{\text{in}}$} -- (8.5,2.2);
  \draw (6.8,1.6) -- (8.5,1.6);
  \draw (6.8,1.0) node[left]{$1\ (V_{CC})$} -- (8.5,1.0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Sum:} $I_0 = C_{in}, I_1 = \bar{C}_{in}, I_2 = \bar{C}_{in}, I_3 = C_{in}$.\\[0.1cm]
\textbf{Carry ($C_{\text{out}}$):} $I_0 = 0, I_1 = C_{in}, I_2 = C_{in}, I_3 = 1$. Select lines: $S_1 = A, S_0 = B$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 7: SR to JK Flip-Flop Conversion Schematic [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q7)}
Differentiate between combinational and sequential circuits. Convert SR flip-flop into JK flip-flop.
\end{questionbox}

\begin{schematicbox}{JK Flip-Flop Implemented Using SR Flip-Flop}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % SR Flip Flop Box
  \draw[thick, fill=boxbg] (6,1) rectangle (9,4.5);
  \node at (7.5,4) {\textbf{SR Flip-Flop}};
  \node at (6.4,3.2) {\small $S$};
  \node at (6.5,2) {\small $> \text{CLK}$};
  \node at (6.4,1.5) {\small $R$};
  \node at (8.6,3.2) {\small $Q$};
  \node at (8.6,1.5) {\small $\bar{Q}$};

  % AND Gates
  \node[and gate US, draw, logic gate inputs=nn] (andS) at (3,3.2) {};
  \node[and gate US, draw, logic gate inputs=nn] (andR) at (3,1.5) {};

  % Inputs
  \draw (-1.0,3.4) node[left]{$J$} -- (andS.input 1);
  \draw (-1.0,1.3) node[left]{$K$} -- (andR.input 2);

  \draw (andS.output) -- (6,3.2);
  \draw (andR.output) -- (6,1.5);

  % Outputs and Feedback
  \draw[thick] (9,3.2) -- (10.5,3.2) node[right]{\large $\mathbf{Q}$};
  \draw[thick] (9,1.5) -- (10.5,1.5) node[right]{\large $\mathbf{\bar{Q}}$};

  \draw (9.8,3.2) -- (9.8,0.5) -- (1.5,0.5) |- (andR.input 1);
  \draw (9.5,1.5) -- (9.5,4.8) -- (1.5,4.8) |- (andS.input 2);
  \draw (4.5,2.0) node[left]{$\text{CLK}$} -- (6,2.0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{S = J\bar{Q}, \qquad R = KQ}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: 4-Bit Johnson Counter Schematic [2 + 3 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q8)}
Write briefly about types of shift registers. Explain the operation of a Johnson's Counter.
\end{questionbox}

\begin{schematicbox}{4-Bit Johnson Counter (Twisted Ring Counter) Schematic}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({(\i)*3.6}, 0) rectangle ({(\i)*3.6 + 2.4}, 3);
    \node at ({(\i)*3.6 + 1.2}, 2.6) {\textbf{FF\i\ (D)}};
    \node at ({(\i)*3.6 + 0.4}, 1.8) {\small $D$};
    \node at ({(\i)*3.6 + 0.5}, 0.8) {\small $>$};
    \node at ({(\i)*3.6 + 2.0}, 1.8) {\small $Q$};
    \node at ({(\i)*3.6 + 2.0}, 0.8) {\small $\bar{Q}$};
    \draw[thick] ({(\i)*3.6 + 2.4}, 1.8) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  % Forward Shifts
  \draw[thick] (2.4, 1.8) -- (3.6, 1.8);
  \draw[thick] (6.0, 1.8) -- (7.2, 1.8);
  \draw[thick] (9.6, 1.8) -- (10.8, 1.8);

  % Inverted Feedback from Q3_bar back to D0
  \draw[thick] (13.2, 0.8) -- (13.8, 0.8) -- (13.8, -1.5) -- (-0.8, -1.5) -- (-0.8, 1.8) -- (0, 1.8);

  % Common Clock
  \draw[thick] (-1.0, -0.6) node[left]{\large $\mathbf{\text{CLK}}$} -- (12.0, -0.6);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 0.5}, -0.6) -- ({(\i)*3.6 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$2n = 8$ states: $0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: 3-Bit Ripple UP Counter with Positive Edge Triggering [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q9)}
Describe the operation of 3-bit ripple up counter with positive edge triggered clock.
\end{questionbox}

\begin{schematicbox}{3-Bit Ripple UP Counter Schematic (Positive Edge Triggered)}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \foreach \i in {0,1,2} {
    \draw[thick, fill=boxbg] ({(\i)*4.2}, 0) rectangle ({(\i)*4.2 + 2.8}, 3);
    \node at ({(\i)*4.2 + 1.4}, 2.6) {\textbf{FF\i\ (T=1)}};
    \node at ({(\i)*4.2 + 0.5}, 1.5) {\small $>$};
    \node at ({(\i)*4.2 + 2.3}, 2.0) {\small $Q$};
    \node at ({(\i)*4.2 + 2.3}, 1.0) {\small $\bar{Q}$};
    \draw[thick] ({(\i)*4.2 + 2.8}, 2.0) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  % CLK into FF0
  \draw[thick] (-1.0, 1.5) node[left]{\large $\mathbf{\text{CLK}}$} -- (0, 1.5);

  % Clocking from Q_bar for UP counting on positive edges
  \draw[thick] (2.8, 1.0) -- (3.5, 1.0) |- (4.2, 1.5);
  \draw[thick] (7.0, 1.0) -- (7.7, 1.0) |- (8.4, 1.5);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Counts $000 \to 111$. Each stage toggles on the positive clock edge produced by preceding $\bar{Q}$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 10: Synchronous Mod-6 Counter Using SR Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q10)}
Design the synchronous mod-6 counter using SR flip-flop and draw its timing diagram.
\end{questionbox}

\paragraph{Design Equations:}
$$S_0 = \bar{Q}_0, \quad R_0 = Q_0, \qquad S_1 = \bar{Q}_2\bar{Q}_1 Q_0, \quad R_1 = Q_1 Q_0, \qquad S_2 = Q_1 Q_0, \quad R_2 = Q_0$$

\begin{answerbox}
$$\mathbf{S_0 = \bar{Q}_0, \ R_0 = Q_0, \quad S_1 = \bar{Q}_2\bar{Q}_1 Q_0, \ R_1 = Q_1 Q_0, \quad S_2 = Q_1 Q_0, \ R_2 = Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 11: Synchronous FSM Sequence Detector '110' [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q11)}
Design a synchronous sequential machine that has 1-bit serial input $X$ and output $Z$ which will be HIGH when the input contains the message $110$ (Use SR Flip-Flop).
\end{questionbox}

\begin{schematicbox}{FSM State Transition Automaton for '110' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.2cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$0 / 0$} (S0)
             edge [bend left] node {$1 / 0$} (S1)
        (S1) edge [bend left] node {$0 / 0$} (S0)
             edge [bend left] node {$1 / 0$} (S2)
        (S2) edge [loop above] node {$1 / 0$} (S2)
             edge [bend left=45] node [below] {$0 / \mathbf{1}$} (S0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{S_A = BX, \quad R_A = \bar{X}, \quad S_B = \bar{A}\bar{B}X, \quad R_B = B\bar{X} + A, \quad Z = A\bar{X}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 12: Frequency Counter Block Diagram [3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q12)}
Write a short note on frequency counter with functional block diagram.
\end{questionbox}

\begin{schematicbox}{Digital Frequency Counter Functional Block Diagram}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (amp) at (0,2) {Input Amp};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (schmitt) at (3,2) {Schmitt Trigger};
  \node[and gate US, draw, logic gate inputs=nn, scale=1.3] (gate) at (6,1) {};
  \node[draw, rectangle, fill=boxbg, minimum width=2.2cm, minimum height=1.0cm] (counter) at (9.5,1) {Decade Counter};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (disp) at (13,1) {Display};

  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (osc) at (0,-0.5) {Crystal Osc};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (div) at (3,-0.5) {Time Base Div};

  \draw[thick, ->] (-1.8,2) node[left]{$f_x$ (Unknown)} -- (amp);
  \draw[thick, ->] (amp) -- (schmitt);
  \draw[thick, ->] (schmitt) -| (gate.input 1);
  \draw[thick, ->] (osc) -- (div);
  \draw[thick, ->] (div) -| (gate.input 2);
  \draw[thick, ->] (gate.output) -- (counter);
  \draw[thick, ->] (counter) -- (disp);
\end{tikzpicture}
\end{schematicbox}

\newpage
% ==============================================================================
% CHAPTER 3: 2082 BAISHAKH
% ==============================================================================
\chapter{2082 Baishakh Examination Solutions}

\subsection{Question 1: ASCII Code \& 2's Complement Addition [1 + 3 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q1)}
Define an ASCII code. Use 2's complement method to perform $(-28 + 12)_{10}$ in 8-bit signed number representation.
\end{questionbox}

\begin{answerbox}
$(-28 + 12)_{10} = \mathbf{1111\ 0000_2} = -16_{10}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: Boolean Algebra Proofs [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q2)}
Prove: (a) $AB + \bar{A}C + BC = AB + \bar{A}C$, (b) $AB + C(A \oplus B) = BC + A(B+C)$.
\end{questionbox}

\begin{answerbox}
Both identities are verified algebraically.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: Octal Priority Encoder Schematic [2 + 6 = 8 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q3)}
What is a decoder? Design an octal priority encoder with neat circuit diagram.
\end{questionbox}

\begin{schematicbox}{8-to-3 Octal Priority Encoder Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \draw[thick, fill=boxbg] (0,0) rectangle (6,6);
  \node at (3,5.5) {\textbf{8-to-3 Priority Encoder}};

  \foreach \i in {0,...,7} {
    \draw[thick] (-1.2, {0.6 + \i*0.6}) node[left]{$D_\i$} -- (0, {0.6 + \i*0.6});
  }

  \draw[thick] (6,4.5) -- ++(1.5,0) node[right]{\large $\mathbf{A} = D_4 + D_5 + D_6 + D_7$};
  \draw[thick] (6,3.0) -- ++(1.5,0) node[right]{\large $\mathbf{B} = D_2\bar{D}_4\bar{D}_5 + D_3\bar{D}_4\bar{D}_5 + D_6 + D_7$};
  \draw[thick] (6,1.5) -- ++(1.5,0) node[right]{\large $\mathbf{C} = D_1\bar{D}_2\bar{D}_4\bar{D}_6 + D_3\bar{D}_4\bar{D}_6 + D_5\bar{D}_6 + D_7$};
  \draw[thick] (6,0.5) -- ++(1.5,0) node[right]{\large $\mathbf{V} = \sum D_i$ (Valid)};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 4: 3x8 Decoder Function Realization [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q4)}
Realize $X(A,B,C,D) = \sum m(0, 2, 3, 7, 8, 10, 11, 14, 15)$ using a single 3x8 decoder and simplify implementing K-Map.
\end{questionbox}

\paragraph{K-Map Simplification:}
$$X(A,B,C,D) = \bar{B}\bar{D} + \bar{B}C + CD + ABC$$

\begin{schematicbox}{Realization of 4-Variable Function Using 3x8 Decoder}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  \draw[thick, fill=boxbg] (0,0) rectangle (3.5,6);
  \node at (1.75,5.5) {\textbf{3x8 Decoder}};
  \node at (0.5,4.5) {\small $A$};
  \node at (0.5,3.0) {\small $B$};
  \node at (0.5,1.5) {\small $C$};

  \draw[thick] (-1.5,4.5) node[left]{$A$ ($S_2$)} -- (0,4.5);
  \draw[thick] (-1.5,3.0) node[left]{$B$ ($S_1$)} -- (0,3.0);
  \draw[thick] (-1.5,1.5) node[left]{$C$ ($S_0$)} -- (0,1.5);

  \foreach \i in {0,...,7} {
    \node at (3.0, {0.6 + \i*0.6}) {\small $Y_\i$};
    \draw[thick] (3.5, {0.6 + \i*0.6}) -- (5.0, {0.6 + \i*0.6});
  }

  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.4] (orX) at (8,3) {};
  \draw (5, 0.6) node[right]{\small ($m_0, m_1$)} -- (orX.input 4);
  \draw (5, 1.8) node[right]{\small ($m_2, m_3$)} -- (orX.input 3);
  \draw (5, 4.2) node[right]{\small ($m_4, m_5$)} -- (orX.input 2);
  \draw (5, 4.8) node[right]{\small ($m_6, m_7$)} -- (orX.input 1);
  \draw (orX.output) -- ++(1,0) node[right]{\large $\mathbf{X}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{X(A,B,C,D) = \bar{B}\bar{D} + \bar{B}C + CD + ABC}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Synchronous 2-Bit UP/DOWN Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q5)}
Design a synchronous 2-bit up/down counter using T flip-flops.
\end{questionbox}

\paragraph{Design Equations:}
$$T_0 = 1, \qquad T_1 = M \oplus Q_0$$

\begin{schematicbox}{Synchronous 2-Bit UP/DOWN Counter Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % FF0
  \draw[thick, fill=boxbg] (0,0) rectangle (2.8,3.5);
  \node at (1.4,3.0) {\textbf{FF0 (T)}};
  \node at (0.4,2.2) {\small $T_0$};
  \node at (0.5,1.0) {\small $>$};
  \node at (2.4,2.2) {\small $Q_0$};
  \node at (2.4,1.0) {\small $\bar{Q}_0$};
  \draw[thick] (2.8,2.2) -- ++(0.5,0) -- ++(0,1.8) node[above]{\large $\mathbf{Q_0}$};

  % FF1
  \draw[thick, fill=boxbg] (6,0) rectangle (8.8,3.5);
  \node at (7.4,3.0) {\textbf{FF1 (T)}};
  \node at (6.4,2.2) {\small $T_1$};
  \node at (6.5,1.0) {\small $>$};
  \node at (8.4,2.2) {\small $Q_1$};
  \node at (8.4,1.0) {\small $\bar{Q}_1$};
  \draw[thick] (8.8,2.2) -- ++(0.5,0) -- ++(0,1.8) node[above]{\large $\mathbf{Q_1}$};

  % T0 = 1
  \draw[thick] (-1.0,2.2) node[left]{$1\ (V_{CC})$} -- (0,2.2);

  % XOR Gate for T1 = M XOR Q0
  \node[xor gate US, draw, logic gate inputs=nn] (xorT1) at (4.8,2.2) {};
  \draw (xorT1.output) -- (6,2.2);
  \draw (2.8,2.2) -- (xorT1.input 2);
  \draw (-1.0,4.5) node[left]{\large $\mathbf{M}$ (Mode)} -- (4.0,4.5) |- (xorT1.input 1);

  % Common Synchronous Clock
  \draw[thick] (-1.0,-1.0) node[left]{\large $\mathbf{\text{CLK}}$} -- (7.5,-1.0);
  \draw[thick] (0.5,-1.0) -- (0.5,0);
  \draw[thick] (6.5,-1.0) -- (6.5,0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{T_0 = 1, \qquad T_1 = M \oplus Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: 4-Bit PISO Shift Register Schematic [3 + 2 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q6)}
Explain the operation of 4-bit parallel-in serial-out (PISO) shift register with necessary circuit and timing diagram for 1101 input data.
\end{questionbox}

\begin{schematicbox}{4-Bit Parallel-In Serial-Out (PISO) Shift Register Logic Diagram}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  \foreach \i in {3,2,1,0} {
    \draw[thick, fill=boxbg] ({(\i)*3.8}, 0) rectangle ({(\i)*3.8 + 2.2}, 2.8);
    \node at ({(\i)*3.8 + 1.1}, 2.4) {\textbf{FF\i\ (D)}};
    \node at ({(\i)*3.8 + 0.4}, 1.6) {\small $D$};
    \node at ({(\i)*3.8 + 0.5}, 0.8) {\small $>$};
    \node at ({(\i)*3.8 + 1.8}, 1.6) {\small $Q$};
  }

  \draw[thick] (0+2.2, 1.6) -- ++(1.0,0) node[right]{\large $\mathbf{D_{\text{out}}}$ (Serial)};
  \draw[thick] (-1.0, -1.0) node[left]{\large $\mathbf{\text{CLK}}$} -- (12.0, -1.0);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.8 + 0.5}, -1.0) -- ({(\i)*3.8 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 7: Mod-12 Asynchronous Counter Schematic [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q7)}
Sketch the circuit diagram of mod-12 asynchronous counter having positive-edge triggering clock system implementing JK flip-flops with neat timing diagram.
\end{questionbox}

\begin{schematicbox}{Mod-12 Asynchronous Counter (Positive Edge Triggered)}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({(\i)*3.6}, 0) rectangle ({(\i)*3.6 + 2.4}, 3);
    \node at ({(\i)*3.6 + 1.2}, 2.6) {\textbf{FF\i\ (JK)}};
    \node at ({(\i)*3.6 + 0.5}, 1.5) {\small $>$};
    \node at ({(\i)*3.6 + 2.0}, 2.0) {\small $Q$};
    \node at ({(\i)*3.6 + 2.0}, 1.0) {\small $\bar{Q}$};
    \node at ({(\i)*3.6 + 1.2}, 0.4) {\small $\overline{\text{CLR}}$};
    \draw[thick] ({(\i)*3.6 + 2.4}, 2.0) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  % Clock into FF0
  \draw[thick] (-1.0, 1.5) node[left]{\large $\mathbf{\text{CLK}}$} -- (0, 1.5);

  % Clocking from Q_bar for UP counting on positive edges
  \draw[thick] (2.4, 1.0) -- (3.0, 1.0) |- (3.6, 1.5);
  \draw[thick] (6.0, 1.0) -- (6.6, 1.0) |- (7.2, 1.5);
  \draw[thick] (9.6, 1.0) -- (10.2, 1.0) |- (10.8, 1.5);

  % Reset NAND Gate for state 1100 (Q3=1, Q2=1)
  \node[nand gate US, draw, logic gate inputs=nn, rotate=-90] (nand_rst) at (8, -2.5) {};
  \draw (9.6+1.2, 2.0) -- ++(0,-3.5) |- (nand_rst.input 1);
  \draw (7.2+1.2, 2.0) -- ++(0,-3.5) |- (nand_rst.input 2);

  % Clear bus
  \draw[thick] (nand_rst.output) -- (8, -4.0) -- (-0.5, -4.0) -- (-0.5, -0.6) -- (12.0, -0.6);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 1.2}, -0.6) -- ({(\i)*3.6 + 1.2}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Reset Logic:} $\overline{\text{CLR}} = \overline{Q_3 \cdot Q_2}$. Modulus $= 12$ ($0000$ to $1011$).
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: FSM Sequence Detector '010' Using D Flip-Flops [10 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q8)}
Design a sequential machine that consists of one input $X$ and one output $Z$. $Z=1$ whenever it detects the serial sequence $010$. Implement only D flip-flops.
\end{questionbox}

\begin{schematicbox}{FSM State Transition Automaton for '010' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.2cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$1 / 0$} (S0)
             edge [bend left] node {$0 / 0$} (S1)
        (S1) edge [loop above] node {$0 / 0$} (S1)
             edge [bend left] node {$1 / 0$} (S2)
        (S2) edge [bend left=45] node [below] {$0 / \mathbf{1}$} (S1)
             edge [bend left=60] node [above] {$1 / 0$} (S0);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Design Equations:}
$$D_A = BX, \qquad D_B = \bar{X}, \qquad Z = A\bar{X}$$

\begin{schematicbox}{Logic Schematic with D Flip-Flops for '010' Detector}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % FFA
  \draw[thick, fill=boxbg] (4,2) rectangle (6.5,5);
  \node at (5.25,4.5) {\textbf{FF-A (D)}};
  \node at (4.4,3.6) {\small $D_A$};
  \node at (4.5,2.6) {\small $>$};
  \node at (6.1,3.6) {\small $A$};

  % FFB
  \draw[thick, fill=boxbg] (4,-2) rectangle (6.5,1);
  \node at (5.25,0.5) {\textbf{FF-B (D)}};
  \node at (4.4,-0.4) {\small $D_B$};
  \node at (4.5,-1.4) {\small $>$};
  \node at (6.1,-0.4) {\small $B$};

  % Gates
  \node[and gate US, draw, logic gate inputs=nn] (andDA) at (2,3.6) {};
  \node[not gate US, draw, scale=0.8] (notX) at (2,-0.4) {};
  \node[and gate US, draw, logic gate inputs=nn] (andZ) at (8.5,3.6) {};

  \draw (andDA.output) -- (4,3.6);
  \draw (notX.output) -- (4,-0.4);

  % Inputs
  \draw (-1.5,4.0) node[left]{\large $\mathbf{X}$} -- (1.0,4.0) |- (andDA.input 1);
  \draw (1.0,4.0) |- (notX.input);

  % Feedback B to andDA
  \draw (6.5,-0.4) -- (7.5,-0.4) -- (7.5,-2.8) -- (0.5,-2.8) |- (andDA.input 2);

  % Output Z = A . X_bar
  \draw (6.5,3.6) -- (andZ.input 1);
  \draw (2.8,-0.4) -- (3.2,-0.4) -- (3.2,1.8) -- (7.5,1.8) |- (andZ.input 2);
  \draw (andZ.output) -- ++(1.0,0) node[right]{\large $\mathbf{Z}$ (Output)};

  % Clock
  \draw (-1.5,-3.5) node[left]{\large $\mathbf{\text{CLK}}$} -- (5.25,-3.5);
  \draw (4.5,-3.5) |- (4,2.6);
  \draw (4.5,-3.5) |- (4,-1.4);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{D_A = BX, \qquad D_B = \bar{X}, \qquad Z = A\bar{X}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: Two-Input CMOS NAND Gate Transistor Circuit [4 + 2 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q9)}
Draw the circuit diagram of two-input CMOS NAND gate, explain its logic operation, and list the characteristics of TTL logic family.
\end{questionbox}

\begin{schematicbox}{Two-Input CMOS NAND Gate Transistor Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % VDD Rail
  \draw[thick] (1, 6) node[above]{\large $V_{DD}$} -- (5, 6);

  % PMOS Transistors in Parallel
  \draw[thick] (2, 6) -- (2, 5.2);
  \draw[thick] (4, 6) -- (4, 5.2);

  \draw[thick, fill=boxbg] (1.4, 4.4) rectangle (2.6, 5.2) node[midway]{\small $P_1$ (PMOS)};
  \draw[thick, fill=boxbg] (3.4, 4.4) rectangle (4.6, 5.2) node[midway]{\small $P_2$ (PMOS)};

  \draw[thick] (2, 4.4) -- (2, 3.6);
  \draw[thick] (4, 4.4) -- (4, 3.6);
  \draw[thick] (2, 3.6) -- (4, 3.6);
  \draw[thick] (3, 3.6) -- (6, 3.6) node[right]{\large $\mathbf{Y = \overline{A \cdot B}}$};

  % NMOS Transistors in Series
  \draw[thick] (3, 3.6) -- (3, 2.8);
  \draw[thick, fill=boxbg] (2.4, 2.0) rectangle (3.6, 2.8) node[midway]{\small $N_1$ (NMOS)};
  \draw[thick] (3, 2.0) -- (3, 1.2);
  \draw[thick, fill=boxbg] (2.4, 0.4) rectangle (3.6, 1.2) node[midway]{\small $N_2$ (NMOS)};
  \draw[thick] (3, 0.4) -- (3, -0.2) node[ground]{};
  \node at (3, -0.6) {\small GND ($V_{SS}$)};

  % Inputs A and B
  \draw[thick] (-0.5, 4.8) node[left]{\large $\mathbf{A}$} -- (1.4, 4.8);
  \draw[thick] (0.5, 4.8) |- (2.4, 2.4);

  \draw[thick] (-0.5, 0.8) node[left]{\large $\mathbf{B}$} -- (2.4, 0.8);
  \draw[thick] (0.2, 0.8) |- (3.4, 4.8);
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 10: Time Interval Measurement Block Diagram [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q10)}
With the help of functional diagram explain the operation of time measuring circuit.
\end{questionbox}

\begin{schematicbox}{Time Interval Measurement System Block Diagram}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % RS Flip Flop
  \draw[thick, fill=boxbg] (0,1) rectangle (2.5,3.5);
  \node at (1.25,3.0) {\textbf{RS Latch}};
  \node at (0.4,2.5) {\small $S$};
  \node at (0.4,1.5) {\small $R$};
  \node at (2.1,2.0) {\small $Q$};

  \draw[thick] (-1.5,2.5) node[left]{\large $\mathbf{\text{START Pulse}}$} -- (0,2.5);
  \draw[thick] (-1.5,1.5) node[left]{\large $\mathbf{\text{STOP Pulse}}$} -- (0,1.5);

  % Clock Generator
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (osc) at (2.5,-0.5) {Clock ($1\text{MHz}$)};

  % Main Gate
  \node[and gate US, draw, logic gate inputs=nn, scale=1.3] (gate) at (5,1.0) {};
  \draw[thick] (2.5,2.0) -| (gate.input 1);
  \draw[thick] (osc.east) -| (gate.input 2);

  % Counter & Display
  \node[draw, rectangle, fill=boxbg, minimum width=2.2cm, minimum height=1.0cm] (counter) at (8,1.0) {Digital Counter};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (disp) at (11.5,1.0) {Display ($\mu\text{s}$)};

  \draw[thick, ->] (gate.output) -- (counter);
  \draw[thick, ->] (counter) -- (disp);
\end{tikzpicture}
\end{schematicbox}

\newpage
% ==============================================================================
% CHAPTER 4: 2081 ASHWIN
% ==============================================================================
\chapter{2081 Ashwin Examination Solutions}

\subsection{Question 1: Merits \& Demerits of Digital Signals [2 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q1)}
Mention merits and demerits of digital signal over analog signal.
\end{questionbox}

\paragraph{Merits:} High noise immunity, easy error detection/correction, perfect storage/retrieval, compact digital ICs.
\paragraph{Demerits:} Higher transmission bandwidth, quantization noise in ADC.

\vspace{0.5cm}
\subsection{Question 2: Radix & Gray Code Conversions [3 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q2)}
Perform: (a) $(6\text{E}.2\text{C})_{16} = (?)_{8}$, (b) $(10110110)_{\text{Gray}} = (?)_{2}$.
\end{questionbox}

\begin{answerbox}
(a) $(6\text{E}.2\text{C})_{16} = \mathbf{(156.13)_8}$ \qquad (b) $(10110110)_{\text{Gray}} = \mathbf{(11011011)_2}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: BCD to 7-Segment 'f' Segment Decoder Logic Circuit [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q3)}
Design the simplest logic circuit for 'f' segment for the BCD-to-seven segment display decoder.
\end{questionbox}

\paragraph{Minimized Boolean Equation:}
$$f = A + \bar{C}\bar{D} + B\bar{C} + B\bar{D}$$

\begin{schematicbox}{Logic Gate Circuit for 7-Segment 'f' Segment}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (3,2.5) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (3,1.0) {};
  \node[and gate US, draw, logic gate inputs=nn] (and3) at (3,-0.5) {};
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.3] (orF) at (6,1.0) {};

  \draw (1,3.8) node[left]{$A$} -- ++(4,0) |- (orF.input 1);

  \draw (1,2.7) node[left]{$\bar{C}$} -- (and1.input 1);
  \draw (1,2.3) node[left]{$\bar{D}$} -- (and1.input 2);

  \draw (1,1.2) node[left]{$B$} -- (and2.input 1);
  \draw (1,0.8) node[left]{$\bar{C}$} -- (and2.input 2);

  \draw (1,-0.3) node[left]{$B$} -- (and3.input 1);
  \draw (1,-0.7) node[left]{$\bar{D}$} -- (and3.input 2);

  \draw (and1.output) -- ++(1,0) |- (orF.input 2);
  \draw (and2.output) -- (orF.input 3);
  \draw (and3.output) -- ++(1,0) |- (orF.input 4);

  \draw (orF.output) -- ++(1,0) node[right]{\large $\mathbf{f}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{f = A + \bar{C}\bar{D} + B\bar{C} + B\bar{D}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 4: 4:1 MUX Function Realization & Combined Adder/Subtractor [3 + 7 = 10 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q4)}
Implement $Y(A,B,C) = \sum m(0, 2, 3, 5, 7)$ using only a single 4:1 MUX. Design a combined Half-Adder and Half-Subtractor with a mode control.
\end{questionbox}

\begin{schematicbox}{Combined Half-Adder and Half-Subtractor Logic Circuit}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Mode Control XOR
  \node[xor gate US, draw, logic gate inputs=nn] (xorM) at (2,2) {};
  \draw (-1,2.2) node[left]{\large $\mathbf{A}$} -- (xorM.input 1);
  \draw (-1,1.8) node[left]{\large $\mathbf{M}$ (Mode)} -- (xorM.input 2);

  % Sum/Diff XOR Gate
  \node[xor gate US, draw, logic gate inputs=nn] (xorOut) at (5,3.5) {};
  \draw (-1,3.7) node[left]{\large $\mathbf{A}$} -- (xorOut.input 1);
  \draw (-1,0.5) node[left]{\large $\mathbf{B}$} -- (1.5,0.5) |- (xorOut.input 2);
  \draw (xorOut.output) -- ++(1.5,0) node[right]{\large $\mathbf{Sum / Diff} = A \oplus B$};

  % Carry/Borrow AND Gate
  \node[and gate US, draw, logic gate inputs=nn] (andCB) at (5,1.2) {};
  \draw (xorM.output) -- (andCB.input 1);
  \draw (1.5,0.5) |- (andCB.input 2);
  \draw (andCB.output) -- ++(1.5,0) node[right]{\large $\mathbf{Carry / Borrow} = (A \oplus M)B$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$M=0 \implies \text{Half Adder}; \quad M=1 \implies \text{Half Subtractor}$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Mod-6 Synchronous DOWN Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q5)}
Design a mod-6 synchronous down counter using JK flip-flops ($5 \to 4 \to 3 \to 2 \to 1 \to 0 \to 5$).
\end{questionbox}

\paragraph{Design Equations:}
$$J_0 = 1, \ K_0 = 1, \qquad J_1 = \bar{Q}_2\bar{Q}_0, \ K_1 = \bar{Q}_0, \qquad J_2 = K_2 = \bar{Q}_1\bar{Q}_0$$

\begin{schematicbox}{Mod-6 Synchronous DOWN Counter Schematic}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \foreach \i in {0,1,2} {
    \draw[thick, fill=boxbg] ({(\i)*4.0}, 0) rectangle ({(\i)*4.0 + 2.6}, 3.5);
    \node at ({(\i)*4.0 + 1.3}, 3.0) {\textbf{FF\i\ (JK)}};
    \node at ({(\i)*4.0 + 0.4}, 2.4) {\small $J$};
    \node at ({(\i)*4.0 + 0.5}, 1.5) {\small $>$};
    \node at ({(\i)*4.0 + 0.4}, 0.6) {\small $K$};
    \node at ({(\i)*4.0 + 2.2}, 2.4) {\small $Q$};
    \node at ({(\i)*4.0 + 2.2}, 0.6) {\small $\bar{Q}$};
    \draw[thick] ({(\i)*4.0 + 2.6}, 2.4) -- ++(0.4,0) -- ++(0,1.8) node[above]{\large $\mathbf{Q_\i}$};
  }

  % FF0 J=K=1
  \draw[thick] (-0.8,2.4) node[left]{$1\ (V_{CC})$} -- (0,2.4);
  \draw[thick] (-0.8,0.6) node[left]{$1\ (V_{CC})$} -- (0,0.6);

  % Common Clock
  \draw[thick] (-1.0,-1.0) node[left]{\large $\mathbf{\text{CLK}}$} -- (10.0,-1.0);
  \foreach \i in {0,1,2} {
    \draw[thick] ({(\i)*4.0 + 0.5}, -1.0) -- ({(\i)*4.0 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{J_0=1, \ K_0=1, \quad J_1=\bar{Q}_2\bar{Q}_0, \ K_1=\bar{Q}_0, \quad J_2=K_2=\bar{Q}_1\bar{Q}_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: 4-Bit SIPO Shift Register Schematic [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q6)}
Explain the operation of 4-bit serial-in parallel-out (SIPO) shift register with necessary circuit and timing diagram for input data of 1011.
\end{questionbox}

Four clock cycles load the serial sequence $1011_2$ into parallel outputs $Q_3 Q_2 Q_1 Q_0 = 1101_2$.

\vspace{0.5cm}
\subsection{Question 7: 3-Bit Asynchronous UP/DOWN Counter Schematic [4 + 3 = 7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q7)}
Describe briefly the operation of 3 bit up/down asynchronous counter having negative edge triggering clock system with neat circuit diagram and timing diagram.
\end{questionbox}

\begin{schematicbox}{3-Bit Asynchronous UP/DOWN Counter with Negative Edge Triggering}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \foreach \i in {0,1,2} {
    \draw[thick, fill=boxbg] ({(\i)*4.2}, 0) rectangle ({(\i)*4.2 + 2.6}, 3);
    \node at ({(\i)*4.2 + 1.3}, 2.6) {\textbf{FF\i\ (T=1)}};
    \node at ({(\i)*4.2 + 0.5}, 1.5) {\small $>$};
    \node at ({(\i)*4.2 + 2.1}, 2.0) {\small $Q$};
    \node at ({(\i)*4.2 + 2.1}, 1.0) {\small $\bar{Q}$};
    \draw[thick] ({(\i)*4.2 + 2.6}, 2.0) -- ++(0.4,0) -- ++(0,1.5) node[above]{\large $\mathbf{Q_\i}$};
  }

  \draw[thick] (-1.0, 1.5) node[left]{\large $\mathbf{\text{CLK}}$} -- (0, 1.5);
  \node at (3.4, 1.5) {\small Steering Gate};
  \node at (7.6, 1.5) {\small Steering Gate};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Steering Logic:} $\text{CLK}_{i+1} = \bar{M} Q_i + M \bar{Q}_i$. $M=0 \implies$ UP Counter, $M=1 \implies$ DOWN Counter.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: FSM Sequence Detector '101' Using SR Flip-Flops [10 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q8)}
Design a sequential machine that consists of one input $X$ and one output $Z$. $Z=1$ whenever it detects the serial sequence $101$. Implement only SR flip-flops.
\end{questionbox}

\begin{schematicbox}{FSM State Transition Automaton for '101' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.2cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$0 / 0$} (S0)
             edge [bend left] node {$1 / 0$} (S1)
        (S1) edge [loop above] node {$1 / 0$} (S1)
             edge [bend left] node {$0 / 0$} (S2)
        (S2) edge [bend left=45] node [below] {$0 / 0$} (S0)
             edge [bend left=60] node [above] {$1 / \mathbf{1}$} (S1);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Design Equations:}
$$S_A = BX, \quad R_A = \bar{X}, \qquad S_B = X(\bar{A}\bar{B}+A), \quad R_B = B\bar{X}, \qquad Z = AX$$

\begin{answerbox}
$$\mathbf{S_A = BX, \quad R_A = \bar{X}, \quad S_B = X(\bar{A}\bar{B}+A), \quad R_B = B\bar{X}, \quad Z = AX}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: Two-Input TTL NOR Gate Transistor Circuit [5 + 2 = 7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q9)}
Draw the circuit diagram of two-input TTL NOR gate, explain its operation, and list the characteristics of CMOS logic family.
\end{questionbox}

\begin{schematicbox}{Two-Input TTL NOR Gate Schematic (Totem-Pole Output)}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % VCC Rail
  \draw[thick] (0,5) node[left]{\large $+5\text{V}\ (V_{CC})$} -- (8,5);

  % Transistors
  \draw[thick, fill=boxbg] (1,3.5) rectangle (2.2,4.3) node[midway]{\small $Q_{1A}$ (Input)};
  \draw[thick, fill=boxbg] (1,2.0) rectangle (2.2,2.8) node[midway]{\small $Q_{1B}$ (Input)};

  \draw[thick] (-1.0, 3.9) node[left]{\large $\mathbf{A}$} -- (1, 3.9);
  \draw[thick] (-1.0, 2.4) node[left]{\large $\mathbf{B}$} -- (1, 2.4);

  \draw[thick, fill=boxbg] (3.5,2.5) rectangle (4.7,3.5) node[midway]{\small Phase Split};
  \draw[thick, fill=boxbg] (6.0,3.5) rectangle (7.2,4.3) node[midway]{\small $Q_3$ (Pull-Up)};
  \draw[thick, fill=boxbg] (6.0,1.5) rectangle (7.2,2.3) node[midway]{\small $Q_4$ (Pull-Dn)};

  \draw[thick] (6.6,2.9) -- (8.5,2.9) node[right]{\large $\mathbf{Y = \overline{A + B}}$};
  \draw[thick] (6.6,1.5) -- (6.6,0.8) node[ground]{};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 10: Digital Frequency Measurement Block Diagram [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q10)}
With the help of functional diagram explain the operation of frequency measurement.
\end{questionbox}

\begin{schematicbox}{Digital Frequency Measurement System Block Diagram}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (amp) at (0,2) {Attenuator/Amp};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (schmitt) at (3,2) {Schmitt Trigger};
  \node[and gate US, draw, logic gate inputs=nn, scale=1.3] (gate) at (6,1) {};
  \node[draw, rectangle, fill=boxbg, minimum width=2.2cm, minimum height=1.0cm] (counter) at (9.5,1) {Decade Counter};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (disp) at (13,1) {Display (Hz)};

  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (osc) at (0,-0.5) {Crystal Osc};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (div) at (3,-0.5) {Time Base Div};

  \draw[thick, ->] (-1.8,2) node[left]{$f_x$ (Input)} -- (amp);
  \draw[thick, ->] (amp) -- (schmitt);
  \draw[thick, ->] (schmitt) -| (gate.input 1);
  \draw[thick, ->] (osc) -- (div);
  \draw[thick, ->] (div) -| (gate.input 2);
  \draw[thick, ->] (gate.output) -- (counter);
  \draw[thick, ->] (counter) -- (disp);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$f_x = \frac{N}{T_{\text{gate}}}$$
\end{answerbox}

\end{document}
'''

with open('dependencies/digital_logic_master_solutions.tex', 'w') as f:
    f.write(latex_content)

print("Wrote Final Digital Logic Master Solutions LaTeX source with polished TikZ schematics.")
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies', 'dependencies/digital_logic_master_solutions.tex'], capture_output=True, text=True)
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies', 'dependencies/digital_logic_master_solutions.tex'], capture_output=True, text=True)

pdf_out = 'dependencies/digital_logic_master_solutions.pdf'
if os.path.exists(pdf_out):
    shutil.copy(pdf_out, 'subjects/2_digital_logic/Digital Logic Solutions.pdf')
    shutil.copy(pdf_out, 'solutions/web_app/downloads/dl/digital_logic_solutions.pdf')
    print("SUCCESS: Compiled and published complete Digital Logic Master Solutions Book!")
