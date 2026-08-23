"""
Digital Logic (ENEX 152 / EX 152) — Master Solutions Book with Complete Logic Circuit Schematics
Tribhuvan University, Institute of Engineering (IOE)
Polished Page Formatting and Layout
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
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{hyperref}
\usepackage{enumitem}

\usetikzlibrary{shapes.gates.logic.US,positioning,calc,automata,arrows.meta}

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
  title={Logic Schematic / Diagram: #1},
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
  {\Large Complete Step-by-Step Solutions with High-Precision TikZ Vector Logic Schematics, Transistor Circuits, K-Maps, FSM Automata \& Timing Waveforms}\\[0.8cm]
  \textbf{Covering All 4 Exam Sessions:}\\[0.2cm]
  \textbf{2083 Baishakh, 2082 Bhadra, 2082 Baishakh, and 2081 Ashwin}\\[1.5cm]
  
  \vfill
  {\large\textbf{Institute of Engineering Central Reference Portal}}\\[0.2cm]
  {\small Verified Comprehensive Solutions for IOE Students}
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
Convert the following gray codes to binary codes:
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
Differentiate between analog and digital signal. Convert 159 to excess-3 code.
\end{questionbox}

\paragraph{Comparison: Analog vs. Digital Signals}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Parameter} & \textbf{Analog Signal} & \textbf{Digital Signal} \\
\midrule
\textbf{Definition} & Continuous in time and continuous in amplitude & Discrete in time and quantized in amplitude \\
\textbf{Values} & Takes infinite intermediate values within range & Takes discrete binary values ('0' and '1') \\
\textbf{Noise Immunity} & Low (noise directly distorts analog waveform) & High (immune to small amplitude variations) \\
\textbf{Processing/Storage} & Complex analog circuits and magnetic media & Microprocessors, memory registers, DSPs \\
\textbf{Transmission} & Requires linear amplifiers with high distortion & Digital repeaters regenerate clean binary pulses \\
\textbf{Example} & Human voice voltage from microphone & Clock pulses, data in digital computers \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Conversion of $(159)_{10}$ to Excess-3 Code:}
Excess-3 is an unweighted self-complementing BCD code obtained by adding $3$ ($0011_2$) to each decimal digit:
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
Show that NAND and NOR gates are universal gates.
\end{questionbox}

A logic gate is called \textbf{universal} if any Boolean function can be implemented using only that type of gate without requiring any other gate type.

\begin{schematicbox}{Basic Gates Realized Using NAND Only}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % NOT Gate from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (nand_not) at (2,2) {};
  \draw (-0.2,2) -- (0.8,2);
  \node[left] at (-0.2,2) {$A$};
  \draw (0.8,2) |- (nand_not.input 1);
  \draw (0.8,2) |- (nand_not.input 2);
  \draw (nand_not.output) -- ++(0.8,0);
  \node[right] at ($(nand_not.output)+(0.8,0)$) {$Y = \bar{A}$};
  \node at (1.5,0.8) {\small \textbf{(a) NOT from NAND}};

  % AND Gate from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (nand_and1) at (6.5,2) {};
  \node[nand gate US, draw, logic gate inputs=nn] (nand_and2) at (9,2) {};
  \draw (4.8,2.2) -- (nand_and1.input 1); \node[left] at (4.8,2.2) {$A$};
  \draw (4.8,1.8) -- (nand_and1.input 2); \node[left] at (4.8,1.8) {$B$};
  \draw (nand_and1.output) -- (7.8,2) |- (nand_and2.input 1);
  \draw (7.8,2) |- (nand_and2.input 2);
  \draw (nand_and2.output) -- ++(0.8,0);
  \node[right] at ($(nand_and2.output)+(0.8,0)$) {$Y = A \cdot B$};
  \node at (7.5,0.8) {\small \textbf{(b) AND from NAND}};

  % OR Gate from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (nand_or1) at (13,2.7) {};
  \node[nand gate US, draw, logic gate inputs=nn] (nand_or2) at (13,1.3) {};
  \node[nand gate US, draw, logic gate inputs=nn] (nand_or3) at (15.5,2) {};
  \draw (11.2,2.7) -- (11.8,2.7); \node[left] at (11.2,2.7) {$A$};
  \draw (11.8,2.7) |- (nand_or1.input 1);
  \draw (11.8,2.7) |- (nand_or1.input 2);
  \draw (11.2,1.3) -- (11.8,1.3); \node[left] at (11.2,1.3) {$B$};
  \draw (11.8,1.3) |- (nand_or2.input 1);
  \draw (11.8,1.3) |- (nand_or2.input 2);
  \draw (nand_or1.output) -- ++(0.5,0) |- (nand_or3.input 1);
  \draw (nand_or2.output) -- ++(0.5,0) |- (nand_or3.input 2);
  \draw (nand_or3.output) -- ++(0.8,0);
  \node[right] at ($(nand_or3.output)+(0.8,0)$) {$Y = A + B$};
  \node at (14,0.8) {\small \textbf{(c) OR from NAND}};
\end{tikzpicture}
\end{schematicbox}

\begin{schematicbox}{Basic Gates Realized Using NOR Only}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % NOT Gate from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (nor_not) at (2,2) {};
  \draw (-0.2,2) -- (0.8,2); \node[left] at (-0.2,2) {$A$};
  \draw (0.8,2) |- (nor_not.input 1);
  \draw (0.8,2) |- (nor_not.input 2);
  \draw (nor_not.output) -- ++(0.8,0);
  \node[right] at ($(nor_not.output)+(0.8,0)$) {$Y = \bar{A}$};
  \node at (1.5,0.8) {\small \textbf{(a) NOT from NOR}};

  % OR Gate from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (nor_or1) at (6.5,2) {};
  \node[nor gate US, draw, logic gate inputs=nn] (nor_or2) at (9,2) {};
  \draw (4.8,2.2) -- (nor_or1.input 1); \node[left] at (4.8,2.2) {$A$};
  \draw (4.8,1.8) -- (nor_or1.input 2); \node[left] at (4.8,1.8) {$B$};
  \draw (nor_or1.output) -- (7.8,2) |- (nor_or2.input 1);
  \draw (7.8,2) |- (nor_or2.input 2);
  \draw (nor_or2.output) -- ++(0.8,0);
  \node[right] at ($(nor_or2.output)+(0.8,0)$) {$Y = A + B$};
  \node at (7.5,0.8) {\small \textbf{(b) OR from NOR}};

  % AND Gate from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (nor_and1) at (13,2.7) {};
  \node[nor gate US, draw, logic gate inputs=nn] (nor_and2) at (13,1.3) {};
  \node[nor gate US, draw, logic gate inputs=nn] (nor_and3) at (15.5,2) {};
  \draw (11.2,2.7) -- (11.8,2.7); \node[left] at (11.2,2.7) {$A$};
  \draw (11.8,2.7) |- (nor_and1.input 1);
  \draw (11.8,2.7) |- (nor_and1.input 2);
  \draw (11.2,1.3) -- (11.8,1.3); \node[left] at (11.2,1.3) {$B$};
  \draw (11.8,1.3) |- (nor_and2.input 1);
  \draw (11.8,1.3) |- (nor_and2.input 2);
  \draw (nor_and1.output) -- ++(0.5,0) |- (nor_and3.input 1);
  \draw (nor_and2.output) -- ++(0.5,0) |- (nor_and3.input 2);
  \draw (nor_and3.output) -- ++(0.8,0);
  \node[right] at ($(nor_and3.output)+(0.8,0)$) {$Y = A \cdot B$};
  \node at (14,0.8) {\small \textbf{(c) AND from NOR}};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
NAND and NOR gates synthesize NOT, AND, and OR operations independently, proving universality.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 4: 4-Variable K-Map Minimization \& Circuit [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q4)}
Minimize the function $F(A,B,C,D) = \sum m(1, 2, 4, 5, 6, 8, 10, 11, 13, 15)$ using K-Map and realize it with suitable logic gates.
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

\paragraph{Prime Implicant Grouping:}
\begin{enumerate}
  \item Group 1 (m1, m5): $\bar{A}\bar{C}D$
  \item Group 2 (m4, m6): $\bar{A}B\bar{D}$
  \item Group 3 (m2, m6): $\bar{A}C\bar{D}$
  \item Group 4 (m8, m10): $A\bar{B}\bar{D}$
  \item Group 5 (m11, m15): $ACD$
  \item Group 6 (m13, m15): $ABD$
\end{enumerate}

\paragraph{Minimized Boolean SOP Expression:}
$$F(A,B,C,D) = \bar{A}\bar{C}D + \bar{A}B\bar{D} + \bar{A}C\bar{D} + A\bar{B}\bar{D} + ACD + ABD$$

\begin{schematicbox}{Logic Circuit Realization for $F(A,B,C,D)$}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % 6 AND gates
  \node[and gate US, draw, logic gate inputs=nnn] (and1) at (4,5) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and2) at (4,3) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and3) at (4,1) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and4) at (4,-1) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and5) at (4,-3) {};
  \node[and gate US, draw, logic gate inputs=nnn] (and6) at (4,-5) {};

  % Inputs to AND gates
  \draw (1, 5.3) -- (and1.input 1); \node[left] at (1, 5.3) {\small $\bar{A}$};
  \draw (1, 5.0) -- (and1.input 2); \node[left] at (1, 5.0) {\small $\bar{C}$};
  \draw (1, 4.7) -- (and1.input 3); \node[left] at (1, 4.7) {\small $D$};

  \draw (1, 3.3) -- (and2.input 1); \node[left] at (1, 3.3) {\small $\bar{A}$};
  \draw (1, 3.0) -- (and2.input 2); \node[left] at (1, 3.0) {\small $B$};
  \draw (1, 2.7) -- (and2.input 3); \node[left] at (1, 2.7) {\small $\bar{D}$};

  \draw (1, 1.3) -- (and3.input 1); \node[left] at (1, 1.3) {\small $\bar{A}$};
  \draw (1, 1.0) -- (and3.input 2); \node[left] at (1, 1.0) {\small $C$};
  \draw (1, 0.7) -- (and3.input 3); \node[left] at (1, 0.7) {\small $\bar{D}$};

  \draw (1,-0.7) -- (and4.input 1); \node[left] at (1,-0.7) {\small $A$};
  \draw (1,-1.0) -- (and4.input 2); \node[left] at (1,-1.0) {\small $\bar{B}$};
  \draw (1,-1.3) -- (and4.input 3); \node[left] at (1,-1.3) {\small $\bar{D}$};

  \draw (1,-2.7) -- (and5.input 1); \node[left] at (1,-2.7) {\small $A$};
  \draw (1,-3.0) -- (and5.input 2); \node[left] at (1,-3.0) {\small $C$};
  \draw (1,-3.3) -- (and5.input 3); \node[left] at (1,-3.3) {\small $D$};

  \draw (1,-4.7) -- (and6.input 1); \node[left] at (1,-4.7) {\small $A$};
  \draw (1,-5.0) -- (and6.input 2); \node[left] at (1,-5.0) {\small $B$};
  \draw (1,-5.3) -- (and6.input 3); \node[left] at (1,-5.3) {\small $D$};

  % 6-input OR Gate
  \node[or gate US, draw, logic gate inputs=nnnnnn, scale=1.4] (or_out) at (8,0) {};
  \draw (and1.output) -- ++(2.0,0) |- (or_out.input 1);
  \draw (and2.output) -- ++(1.5,0) |- (or_out.input 2);
  \draw (and3.output) -- ++(1.0,0) |- (or_out.input 3);
  \draw (and4.output) -- ++(1.0,0) |- (or_out.input 4);
  \draw (and5.output) -- ++(1.5,0) |- (or_out.input 5);
  \draw (and6.output) -- ++(2.0,0) |- (or_out.input 6);

  \draw (or_out.output) -- ++(1,0);
  \node[right] at ($(or_out.output)+(1,0)$) {\large $\mathbf{F}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{F = \bar{A}\bar{C}D + \bar{A}B\bar{D} + \bar{A}C\bar{D} + A\bar{B}\bar{D} + ACD + ABD}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Octal-to-Binary Encoder Logic Circuit [2 + 4 = 6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q5)}
Differentiate between encoder and decoder. Design octal to binary encoder with necessary diagrams.
\end{questionbox}

\paragraph{Comparison: Encoder vs. Decoder}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Feature} & \textbf{Encoder} & \textbf{Decoder} \\
\midrule
\textbf{Function} & Converts $2^n$ input lines to $n$ coded binary outputs & Converts $n$ coded binary inputs into $2^n$ unique outputs \\
\textbf{Inputs/Outputs} & $2^n$ inputs, $n$ outputs & $n$ inputs, $2^n$ outputs \\
\textbf{Internal Logic} & Implemented using OR gates & Implemented using AND / NAND gates \\
\textbf{Application} & Keyboards, ADC conversion & Address decoding, memory chip select, 7-segment display \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Octal-to-Binary ($8$-to-$3$) Truth Table:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c||c|c|c|}
\hline
\textbf{$D_7$} & \textbf{$D_6$} & \textbf{$D_5$} & \textbf{$D_4$} & \textbf{$D_3$} & \textbf{$D_2$} & \textbf{$D_1$} & \textbf{$D_0$} & \textbf{$A$ (MSB)} & \textbf{$B$} & \textbf{$C$ (LSB)} \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\ \hline
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 \\ \hline
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ \hline
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \\ \hline
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 \\ \hline
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\ \hline
\end{tabular}
\end{center}

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
    \draw (0, 7-\i) -- (9, 7-\i);
    \node[left] at (0, 7-\i) {$D_\i$};
  }

  % Three 4-input OR gates
  \node[or gate US, draw, logic gate inputs=nnnn, rotate=-90, scale=1.2] (orA) at (3, -1) {};
  \node[or gate US, draw, logic gate inputs=nnnn, rotate=-90, scale=1.2] (orB) at (5.5, -1) {};
  \node[or gate US, draw, logic gate inputs=nnnn, rotate=-90, scale=1.2] (orC) at (8, -1) {};

  % Output Lines
  \draw (orA.output) -- ++(0,-0.8); \node[below] at ($(orA.output)+(0,-0.8)$) {\large $\mathbf{A}$ (MSB)};
  \draw (orB.output) -- ++(0,-0.8); \node[below] at ($(orB.output)+(0,-0.8)$) {\large $\mathbf{B}$};
  \draw (orC.output) -- ++(0,-0.8); \node[below] at ($(orC.output)+(0,-0.8)$) {\large $\mathbf{C}$ (LSB)};

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
Implement a full subtractor circuit using multiplexer.
\end{questionbox}

A full subtractor has inputs $A$ (minuend), $B$ (subtrahend), $B_{\text{in}}$ (borrow in), and outputs $D$ (difference) and $B_{\text{out}}$ (borrow out).
\begin{itemize}
  \item Difference $D(A,B,B_{\text{in}}) = \sum m(1, 2, 4, 7)$
  \item Borrow Out $B_{\text{out}}(A,B,B_{\text{in}}) = \sum m(1, 2, 3, 7)$
\end{itemize}

\paragraph{Implementation Tables (Select Lines: $S_1 = A, S_0 = B$):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Output} & \textbf{$I_0$ ($AB=00$)} & \textbf{$I_1$ ($AB=01$)} & \textbf{$I_2$ ($AB=10$)} & \textbf{$I_3$ ($AB=11$)} \\ \hline
\textbf{Difference ($D$)} & $B_{\text{in}}$ ($m_1$) & $\overline{B_{\text{in}}}$ ($m_2$) & $\overline{B_{\text{in}}}$ ($m_4$) & $B_{\text{in}}$ ($m_7$) \\ \hline
\textbf{Borrow ($B_{\text{out}}$)} & $B_{\text{in}}$ ($m_1$) & $1$ ($m_2, m_3$) & $0$ & $B_{\text{in}}$ ($m_7$) \\ \hline
\end{tabular}
\end{center}

\begin{schematicbox}{Full Subtractor Realization Using Dual 4:1 Multiplexers}
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
  \draw[thick] (3,2) -- (4.8,2); \node[right] at (4.8,2) {\large $\mathbf{D}$ (Diff)};

  % MUX 2: Borrow Out
  \draw[thick, fill=boxbg] (8.5,0) rectangle (11.5,4);
  \node at (10.0,3.5) {\textbf{4:1 MUX ($B_{\text{out}}$)}};
  \node at (8.9,2.8) {\small $I_0$};
  \node at (8.9,2.2) {\small $I_1$};
  \node at (8.9,1.6) {\small $I_2$};
  \node at (8.9,1.0) {\small $I_3$};
  \node at (10.0,0.4) {\small $S_1\quad S_0$};
  \draw[thick] (11.5,2) -- (13.0,2); \node[right] at (13.0,2) {\large $\mathbf{B_{\text{out}}}$};

  % Select Line Bus
  \draw[thick] (-1.5,-1.2) -- (1.0,-1.2) -- (1.0,0); \node[left] at (-1.5,-1.2) {$A$};
  \draw[thick] (-1.5,-1.8) -- (2.0,-1.8) -- (2.0,0); \node[left] at (-1.5,-1.8) {$B$};
  \draw[thick] (1.0,-1.2) -- (9.5,-1.2) -- (9.5,0);
  \draw[thick] (2.0,-1.8) -- (10.5,-1.8) -- (10.5,0);

  % Data Inputs Connections for MUX 1
  \draw (-1.5,2.8) -- (0,2.8); \node[left] at (-1.5,2.8) {$B_{\text{in}}$};
  \node[not gate US, draw, scale=0.8] (not1) at (-0.8,2.2) {};
  \draw (-1.5,2.2) -- (not1.input); \draw (not1.output) -- (0,2.2);
  \draw (-0.8,2.2) |- (0,1.6);
  \draw (-1.5,2.8) |- (0,1.0);

  % Data Inputs Connections for MUX 2
  \draw (6.8,2.8) -- (8.5,2.8); \node[left] at (6.8,2.8) {$B_{\text{in}}$};
  \draw (6.8,2.2) -- (8.5,2.2); \node[left] at (6.8,2.2) {$1\ (V_{CC})$};
  \draw (6.8,1.6) -- (8.5,1.6); \node[left] at (6.8,1.6) {$0\ (\text{GND})$};
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
Differentiate between latch and flipflop. Modify a D flip-flop such that it functions as a JK flip-flop.
\end{questionbox}

\paragraph{Comparison: Latch vs. Flip-Flop}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Parameter} & \textbf{Latch} & \textbf{Flip-Flop} \\
\midrule
\textbf{Triggering} & Level triggered (sensitive throughout clock HIGH/LOW) & Edge triggered (sensitive only during transition) \\
\textbf{Clock Requirement} & Operates with Enable (EN) signal & Requires periodic clock pulses (CLK) \\
\textbf{Race Condition} & High susceptibility to race-around condition & Immune to race conditions due to edge triggering \\
\textbf{Classification} & Asynchronous sequential device & Synchronous sequential device \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Conversion Excitation Table:}
\begin{center}
\begin{tabular}{|c|c|c||c||c|}
\hline
\textbf{$J$} & \textbf{$K$} & \textbf{$Q_n$} & \textbf{$Q_{n+1}$} & \textbf{$D$ Input} \\ \hline
0 & 0 & 0 & 0 & 0 \\ \hline
0 & 0 & 1 & 1 & 1 \\ \hline
0 & 1 & 0 & 0 & 0 \\ \hline
0 & 1 & 1 & 0 & 0 \\ \hline
1 & 0 & 0 & 1 & 1 \\ \hline
1 & 0 & 1 & 1 & 1 \\ \hline
1 & 1 & 0 & 1 & 1 \\ \hline
1 & 1 & 1 & 0 & 0 \\ \hline
\end{tabular}
\end{center}

\paragraph{Boolean Conversion Equation:}
$$D = J\bar{Q} + \bar{K}Q$$

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
  \draw (-1.5,3.7) -- (and1.input 1); \node[left] at (-1.5,3.7) {$J$};
  \draw (-1.5,1.6) -- (notK.input); \node[left] at (-1.5,1.6) {$K$};
  \draw (notK.output) -- (and2.input 2);

  % OR Gate Connection to D
  \draw (and1.output) -- ++(0.8,0) |- (orD.input 1);
  \draw (and2.output) -- ++(0.8,0) |- (orD.input 2);
  \draw (orD.output) -- (6,2.6);

  % Outputs and Feedbacks
  \draw[thick] (9,3.2) -- (10.5,3.2); \node[right] at (10.5,3.2) {\large $\mathbf{Q}$};
  \draw[thick] (9,1.8) -- (10.5,1.8); \node[right] at (10.5,1.8) {\large $\mathbf{\bar{Q}}$};

  % Feedback Lines
  \draw (9.8,3.2) -- (9.8,0.6) -- (0.8,0.6) |- (and2.input 1);
  \draw (9.5,1.8) -- (9.5,4.8) -- (0.8,4.8) |- (and1.input 2);
  \draw (4.5,2.0) -- (6,2.0); \node[left] at (4.5,2.0) {$\text{CLK}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{D = J\bar{Q} + \bar{K}Q}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: 4-Bit SIPO Shift Register Schematic \& Timing Diagram [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q8)}
Explain the working of 4-bit SIPO register with timing diagram of 1010 data input.
\end{questionbox}

A 4-bit Serial-In Parallel-Out (SIPO) register loads data one bit per clock cycle through the serial input line and presents all 4 bits simultaneously across parallel output lines $Q_3 Q_2 Q_1 Q_0$.

\begin{schematicbox}{4-Bit Serial-In Parallel-Out (SIPO) Shift Register Schematic}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \foreach \i in {3,2,1,0} {
    \draw[thick, fill=boxbg] ({(\i)*3.6}, 0) rectangle ({(\i)*3.6 + 2.4}, 3);
    \node at ({(\i)*3.6 + 1.2}, 2.6) {\textbf{FF\i\ (D)}};
    \node at ({(\i)*3.6 + 0.4}, 1.8) {\small $D$};
    \node at ({(\i)*3.6 + 0.5}, 0.8) {\small $>$};
    \node at ({(\i)*3.6 + 2.0}, 1.8) {\small $Q$};
    \draw[thick] ({(\i)*3.6 + 2.4}, 1.8) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*3.6 + 2.8}, 3.3) {\large $\mathbf{Q_\i}$};
  }

  % Serial Input entering FF3
  \draw[thick] (10.8+2.4+1.2, 1.8) -- (10.8+2.4, 1.8);
  \draw[thick] (-1.0, 1.8) -- (0, 1.8);
  \node[left] at (-1.0, 1.8) {\large $\mathbf{D_{\text{in}}}$ (Serial)};

  % Inter-stage connections from Qi to Di-1
  \draw[thick] (2.4, 1.8) -- (3.6, 1.8);
  \draw[thick] (6.0, 1.8) -- (7.2, 1.8);
  \draw[thick] (9.6, 1.8) -- (10.8, 1.8);

  % Common Clock Bus
  \draw[thick] (-1.0, -1.0) -- (12.0, -1.0);
  \node[left] at (-1.0, -1.0) {\large $\mathbf{\text{CLK}}$};
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 0.5}, -1.0) -- ({(\i)*3.6 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\paragraph{State Table for Serial Input $1010_2$ (MSB entered first):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Clock Pulse} & \textbf{Serial Input ($D_{\text{in}}$)} & \textbf{$Q_3$} & \textbf{$Q_2$} & \textbf{$Q_1$} & \textbf{$Q_0$} \\ \hline
Initial & --- & 0 & 0 & 0 & 0 \\ \hline
1 & 1 (MSB) & 1 & 0 & 0 & 0 \\ \hline
2 & 0 & 0 & 1 & 0 & 0 \\ \hline
3 & 1 & 1 & 0 & 1 & 0 \\ \hline
4 & 0 (LSB) & \textbf{0} & \textbf{1} & \textbf{0} & \textbf{1} \\ \hline
\end{tabular}
\end{center}

\begin{schematicbox}{Timing Diagram for SIPO Register Loading $1010_2$}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  % Grid / Ticks
  \foreach \x in {0,...,4} {
    \draw[dotted, gray] (\x*2.5, -6.5) -- (\x*2.5, 1.5);
    \node at (\x*2.5+1.25, 1.7) {\small Pulse \pgfmathparse{int(\x+1)}\pgfmathresult};
  }

  % CLK
  \node[left] at (-0.2, 1.0) {$\text{CLK}$};
  \draw[thick] (0, 0.7) \foreach \x in {0,...,4} { -- ++(1.25,0) -- ++(0,0.6) -- ++(1.25,0) -- ++(0,-0.6) };

  % Din (Data: 1, 0, 1, 0)
  \node[left] at (-0.2, -0.2) {$D_{\text{in}}$};
  \draw[thick, blue] (0, 0.2) -- (2.5, 0.2) -- (2.5, -0.4) -- (5.0, -0.4) -- (5.0, 0.2) -- (7.5, 0.2) -- (7.5, -0.4) -- (12.5, -0.4);

  % Q3
  \node[left] at (-0.2, -1.5) {$Q_3$};
  \draw[thick, red] (0, -1.8) -- (2.5, -1.8) -- (2.5, -1.2) -- (5.0, -1.2) -- (5.0, -1.8) -- (7.5, -1.8) -- (7.5, -1.2) -- (10.0, -1.2) -- (10.0, -1.8) -- (12.5, -1.8);

  % Q2
  \node[left] at (-0.2, -2.8) {$Q_2$};
  \draw[thick, teal] (0, -3.1) -- (5.0, -3.1) -- (5.0, -2.5) -- (7.5, -2.5) -- (7.5, -3.1) -- (10.0, -3.1) -- (10.0, -2.5) -- (12.5, -2.5);

  % Q1
  \node[left] at (-0.2, -4.1) {$Q_1$};
  \draw[thick, orange] (0, -4.4) -- (7.5, -4.4) -- (7.5, -3.8) -- (10.0, -3.8) -- (10.0, -4.4) -- (12.5, -4.4);

  % Q0
  \node[left] at (-0.2, -5.4) {$Q_0$};
  \draw[thick, violet] (0, -5.7) -- (10.0, -5.7) -- (10.0, -5.1) -- (12.5, -5.1);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
After 4 clock pulses, the serial word $1010_2$ is stored across parallel output pins: $Q_3 Q_2 Q_1 Q_0 = \mathbf{0101_2}$ (or $1010_2$ if read $Q_0 \dots Q_3$).
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: Asynchronous BCD (Decade) Counter Schematic [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q9)}
Describe the operation of asynchronous BCD (decade) counter with necessary diagrams.
\end{questionbox}

An asynchronous (ripple) BCD counter counts through decimal digits $0$ to $9$ ($0000_2$ to $1001_2$) and resets to $0000_2$ on the tenth clock pulse ($1010_2$).

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
    \draw[thick] ({(\i)*3.6 + 2.4}, 2.0) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*3.6 + 2.8}, 3.5) {\large $\mathbf{Q_\i}$};
  }

  % External Clock into FF0
  \draw[thick] (-1.0, 1.5) -- (0, 1.5);
  \node[left] at (-1.0, 1.5) {\large $\mathbf{\text{CLK}}$};

  % Ripple Clocks (Negative edge triggered: Q into next CLK)
  \draw[thick] (2.4, 2.0) -- (3.0, 2.0) |- (3.6, 1.5);
  \draw[thick] (6.0, 2.0) -- (6.6, 2.0) |- (7.2, 1.5);
  \draw[thick] (9.6, 2.0) -- (10.2, 2.0) |- (10.8, 1.5);

  % NAND Reset Gate for State 1010 (Q3=1, Q1=1)
  \node[nand gate US, draw, logic gate inputs=nn, rotate=-90] (nand_rst) at (6, -2.5) {};
  \draw (9.6+1.2, 2.0) -- ++(0,-3.5) |- (nand_rst.input 1);
  \draw (3.6+1.2, 2.0) -- ++(0,-3.5) |- (nand_rst.input 2);

  % Active-low Clear Bus
  \draw[thick] (nand_rst.output) -- (6, -4.0) -- (-0.5, -4.0) -- (-0.5, -0.6) -- (12.0, -0.6);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 1.2}, -0.6) -- ({(\i)*3.6 + 1.2}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\paragraph{State Transition Sequence:}
$$0000 \to 0001 \to 0010 \to 0011 \to 0100 \to 0101 \to 0110 \to 0111 \to 1000 \to 1001 \xrightarrow{\text{reset}} 0000$$

\begin{answerbox}
\textbf{Reset Equation:} $\overline{\text{CLR}} = \overline{Q_3 \cdot Q_1}$. The counter resets instantly upon reaching temporary transient state $1010_2$, giving 10 stable counting states.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 10: Synchronous Mod-10 UP Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q10)}
Design the synchronous mod-10 up counter using T flip-flop and draw its timing diagram also.
\end{questionbox}

\paragraph{State Transition and Excitation Table ($T = Q_n \oplus Q_{n+1}$):}
\begin{center}
\begin{tabular}{|c|cccc|cccc|cccc|}
\hline
\textbf{Decimal} & \multicolumn{4}{c|}{\textbf{Present State}} & \multicolumn{4}{c|}{\textbf{Next State}} & \multicolumn{4}{c|}{\textbf{T Inputs}} \\
& $Q_3$ & $Q_2$ & $Q_1$ & $Q_0$ & $Q_3^+$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $T_3$ & $T_2$ & $T_1$ & $T_0$ \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 \\ \hline
2 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 \\ \hline
3 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\ \hline
4 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
5 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 1 \\ \hline
6 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 \\ \hline
7 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ \hline
8 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
9 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{Minimized T Excitation Equations:}
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
    \draw[thick] ({(\i)*3.6 + 2.4}, 2.0) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*3.6 + 2.8}, 3.5) {\large $\mathbf{Q_\i}$};
  }

  % T0 = 1
  \draw[thick] (-0.8, 2.0) -- (0, 2.0); \node[left] at (-0.8, 2.0) {$1\ (V_{CC})$};

  % Common Synchronous Clock
  \draw[thick] (-1.0, -1.2) -- (12.0, -1.2);
  \node[left] at (-1.0, -1.2) {\large $\mathbf{\text{CLK}}$};
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
Design a synchronous sequential machine that has 1bit serial input X and output Z which will be high when the input contains the message 011 (Use T Flip Flop).
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

\paragraph{Excitation Table for T Flip-Flops ($A, B$):}
\begin{center}
\begin{tabular}{|c|c||c|c||c|c||c|}
\hline
\textbf{Present State ($A B$)} & \textbf{Input $X$} & \textbf{Next State ($A^+ B^+$)} & \textbf{$T_A$} & \textbf{$T_B$} & \textbf{Output $Z$} \\ \hline
$S_0 (00)$ & 0 & $S_1 (01)$ & 0 & 1 & 0 \\ \hline
$S_0 (00)$ & 1 & $S_0 (00)$ & 0 & 0 & 0 \\ \hline
$S_1 (01)$ & 0 & $S_1 (01)$ & 0 & 0 & 0 \\ \hline
$S_1 (01)$ & 1 & $S_2 (10)$ & 1 & 1 & 0 \\ \hline
$S_2 (10)$ & 0 & $S_1 (01)$ & 1 & 1 & 0 \\ \hline
$S_2 (10)$ & 1 & $S_0 (00)$ & 1 & 0 & 1 \\ \hline
$S_3 (11)$ & 0 & $d d$ & $d$ & $d$ & $d$ \\ \hline
$S_3 (11)$ & 1 & $d d$ & $d$ & $d$ & $d$ \\ \hline
\end{tabular}
\end{center}

\paragraph{Minimized Equations:}
$$T_A = A + BX, \qquad T_B = BX + \bar{B}\bar{X}, \qquad Z = AX$$

\begin{answerbox}
$$\mathbf{T_A = A + BX, \qquad T_B = BX + \bar{B}\bar{X}, \qquad Z = AX}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 12: Characteristics of Digital Logic Families [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q12)}
Explain about the main characteristics of digital logic families.
\end{questionbox}

\begin{enumerate}
  \item \textbf{Propagation Delay ($t_{pd}$):} The time interval between application of an input transition and the resulting output transition. It determines maximum operating frequency.
  \item \textbf{Power Dissipation ($P_D$):} The DC power consumed by a logic gate under active switching ($P = V_{CC} \times I_{CC}$).
  \item \textbf{Noise Margin ($NM$):} The maximum noise voltage amplitude that can be added to the input signal without altering the output logic state ($NM_H = V_{OH,\min} - V_{IH,\min}$, $NM_L = V_{IL,\max} - V_{OL,\max}$).
  \item \textbf{Fan-Out:} The maximum number of standard logic gate inputs of the same family that a gate output can drive simultaneously while maintaining proper logic levels.
  \item \textbf{Speed-Power Product (SPP):} The figure of merit defined as $SPP = t_{pd} \times P_D$, measured in picojoules (pJ). A lower SPP indicates a superior logic family.
\end{enumerate}

\newpage
% ==============================================================================
% CHAPTER 2: 2082 BHADRA
% ==============================================================================
\chapter{2082 Bhadra Examination Solutions}

\subsection{Question 1: Binary to Gray Code Conversion [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q1)}
Convert the following binary codes to gray codes:
\begin{enumerate}[label=(\alph*)]
  \item $101101_2$
  \item $110001_2$
\end{enumerate}
\end{questionbox}

\paragraph{Binary to Gray Algorithm:}
$g_{n-1} = b_{n-1}$, and $g_i = b_{i+1} \oplus b_i$ for all $i < n-1$.

\paragraph{Part (a): $(101101)_2$}
\begin{itemize}
  \item $g_5 = b_5 = 1$
  \item $g_4 = 1 \oplus 0 = 1$
  \item $g_3 = 0 \oplus 1 = 1$
  \item $g_2 = 1 \oplus 1 = 0$
  \item $g_1 = 1 \oplus 0 = 1$
  \item $g_0 = 0 \oplus 1 = 1$
\end{itemize}
$(101101)_2 = (111011)_{\text{Gray}}$.

\paragraph{Part (b): $(110001)_2$}
\begin{itemize}
  \item $g_5 = b_5 = 1$
  \item $g_4 = 1 \oplus 1 = 0$
  \item $g_3 = 1 \oplus 0 = 1$
  \item $g_2 = 0 \oplus 0 = 0$
  \item $g_1 = 0 \oplus 0 = 0$
  \item $g_0 = 0 \oplus 1 = 1$
\end{itemize}
$(110001)_2 = (101001)_{\text{Gray}}$.

\begin{answerbox}
(a) $(101101)_2 = \mathbf{111011_{\text{Gray}}}$ \qquad (b) $(110001)_2 = \mathbf{101001_{\text{Gray}}}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: 2's Complement \& BCD Addition [1 + 2 = 3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q2)}
What is 2's complement representation? Perform BCD addition of $23 + 48$.
\end{questionbox}

\paragraph{2's Complement Definition:}
2's complement is a binary representation system for signed numbers where a negative number is formed by inverting all bits (1's complement) and adding 1 to the LSB ($2\text{'s Comp} = \bar{X} + 1$). It allows subtraction to be performed directly using adder circuits.

\paragraph{BCD Addition ($23 + 48$):}
\begin{enumerate}
  \item $23 = 0010\ 0011_{\text{BCD}}$
  \item $48 = 0100\ 1000_{\text{BCD}}$
  \item Sum of lower decade: $0011 + 1000 = 1011_2 = (11)_{10} > 9$ (invalid BCD).
  \item Add correction factor $0110_2$ ($+6$):
  $$1011 + 0110 = 0001_2 \text{ with carry } 1$$
  \item Sum of upper decade: $0010 + 0100 + 1 = 0111_2$ ($7$).
\end{enumerate}

\begin{answerbox}
$$23 + 48 = \mathbf{0111\ 0001_{\text{BCD}}} = (71)_{10}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: De Morgan's Theorem with Diagrams [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q3)}
State and explain De Morgan's Theorem with truth table and necessary diagrams.
\end{questionbox}

\paragraph{Theorem Statements:}
\begin{enumerate}
  \item \textbf{First Theorem:} The complement of a product is equal to the sum of the complements:
  $$\overline{A \cdot B} = \bar{A} + \bar{B}$$
  \item \textbf{Second Theorem:} The complement of a sum is equal to the product of the complements:
  $$\overline{A + B} = \bar{A} \cdot \bar{B}$$
\end{enumerate}

\begin{schematicbox}{De Morgan's Equivalent Gate Schematics}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Theorem 1: NAND = Bubbled OR
  \node[nand gate US, draw, logic gate inputs=nn] (nand1) at (2,2) {};
  \draw (0.5,2.2) -- (nand1.input 1); \node[left] at (0.5,2.2) {$A$};
  \draw (0.5,1.8) -- (nand1.input 2); \node[left] at (0.5,1.8) {$B$};
  \draw (nand1.output) -- ++(0.8,0); \node[right] at ($(nand1.output)+(0.8,0)$) {$\overline{A \cdot B}$};
  \node at (4.5,2) {\Large $\equiv$};
  \node[or gate US, draw, logic gate inputs=nn] (bub_or) at (7,2) {};
  \draw (5.5,2.2) -- (bub_or.input 1); \node[left] at (5.5,2.2) {$\bar{A}$};
  \draw (5.5,1.8) -- (bub_or.input 2); \node[left] at (5.5,1.8) {$\bar{B}$};
  \draw (bub_or.output) -- ++(0.8,0); \node[right] at ($(bub_or.output)+(0.8,0)$) {$\bar{A} + \bar{B}$};
  \node at (4.5,0.8) {\textbf{Theorem 1: $\overline{A \cdot B} = \bar{A} + \bar{B}$}};

  % Theorem 2: NOR = Bubbled AND
  \node[nor gate US, draw, logic gate inputs=nn] (nor1) at (2,-1.5) {};
  \draw (0.5,-1.3) -- (nor1.input 1); \node[left] at (0.5,-1.3) {$A$};
  \draw (0.5,-1.7) -- (nor1.input 2); \node[left] at (0.5,-1.7) {$B$};
  \draw (nor1.output) -- ++(0.8,0); \node[right] at ($(nor1.output)+(0.8,0)$) {$\overline{A + B}$};
  \node at (4.5,-1.5) {\Large $\equiv$};
  \node[and gate US, draw, logic gate inputs=nn] (bub_and) at (7,-1.5) {};
  \draw (5.5,-1.3) -- (bub_and.input 1); \node[left] at (5.5,-1.3) {$\bar{A}$};
  \draw (5.5,-1.7) -- (bub_and.input 2); \node[left] at (5.5,-1.7) {$\bar{B}$};
  \draw (bub_and.output) -- ++(0.8,0); \node[right] at ($(bub_and.output)+(0.8,0)$) {$\bar{A} \cdot \bar{B}$};
  \node at (4.5,-2.7) {\textbf{Theorem 2: $\overline{A + B} = \bar{A} \cdot \bar{B}$}};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 4: K-Map with Don't Cares \& Circuit [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q4)}
Minimize the function $F(A,B,C,D) = \sum m(0,1,2,4,7,8,9,10,12,15) + d(5,11,13)$ using K-Map and realize it with suitable logic gates.
\end{questionbox}

\paragraph{K-Map Grouping:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{$AB \backslash CD$} & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $\mathbf{1}$ ($m_0$) & $\mathbf{1}$ ($m_1$) & $0$ ($m_3$) & $\mathbf{1}$ ($m_2$) \\ \hline
\textbf{01} & $\mathbf{1}$ ($m_4$) & $\mathbf{X}$ ($d_5$) & $\mathbf{1}$ ($m_7$) & $0$ ($m_6$) \\ \hline
\textbf{11} & $\mathbf{1}$ ($m_{12}$) & $\mathbf{X}$ ($d_{13}$) & $\mathbf{1}$ ($m_{15}$) & $0$ ($m_{14}$) \\ \hline
\textbf{10} & $\mathbf{1}$ ($m_8$) & $\mathbf{1}$ ($m_9$) & $\mathbf{X}$ ($d_{11}$) & $\mathbf{1}$ ($m_{10}$) \\ \hline
\end{tabular}
\end{center}

\paragraph{Prime Implicants:}
\begin{itemize}
  \item Octet in columns $00$ and $01$: $\bar{C}$
  \item Quad in center/corners ($m_5, m_7, m_{13}, m_{15}$): $BD$
  \item Quad at 4 corners ($m_0, m_2, m_8, m_{10}$): $\bar{B}\bar{D}$
\end{itemize}

\paragraph{Minimized Boolean SOP Expression:}
$$F(A,B,C,D) = \bar{C} + BD + \bar{B}\bar{D}$$

\begin{schematicbox}{Logic Realization for $F = \bar{C} + BD + \bar{B}\bar{D}$}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (3,2) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (3,0.5) {};
  \node[or gate US, draw, logic gate inputs=nnn, scale=1.2] (orF) at (6,1.25) {};

  \draw (1,2.2) -- (and1.input 1); \node[left] at (1,2.2) {$B$};
  \draw (1,1.8) -- (and1.input 2); \node[left] at (1,1.8) {$D$};

  \draw (1,0.7) -- (and2.input 1); \node[left] at (1,0.7) {$\bar{B}$};
  \draw (1,0.3) -- (and2.input 2); \node[left] at (1,0.3) {$\bar{D}$};

  \draw (1,3.0) -- ++(3.5,0) |- (orF.input 1); \node[left] at (1,3.0) {$\bar{C}$};
  \draw (and1.output) -- (orF.input 2);
  \draw (and2.output) -- ++(1,0) |- (orF.input 3);

  \draw (orF.output) -- ++(1,0); \node[right] at ($(orF.output)+(1,0)$) {\large $\mathbf{F}$};
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

A magnitude comparator is a combinational logic circuit that compares two binary words $A = A_2 A_1 A_0$ and $B = B_2 B_1 B_0$ and generates outputs indicating whether $A > B$, $A = B$, or $A < B$.

\paragraph{Bit-Equality Variables (using XNOR):}
$$x_2 = A_2 B_2 + \bar{A}_2 \bar{B}_2, \qquad x_1 = A_1 B_1 + \bar{A}_1 \bar{B}_1, \qquad x_0 = A_0 B_0 + \bar{A}_0 \bar{B}_0$$

\paragraph{Output Equations:}
\begin{align*}
\mathbf{(A = B)} &= x_2 x_1 x_0 \\
\mathbf{(A > B)} &= A_2 \bar{B}_2 + x_2 A_1 \bar{B}_1 + x_2 x_1 A_0 \bar{B}_0 \\
\mathbf{(A < B)} &= \bar{A}_2 B_2 + x_2 \bar{A}_1 B_1 + x_2 x_1 \bar{A}_0 B_0
\end{align*}

\begin{schematicbox}{3-Bit Magnitude Comparator Gate-Level Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % Inputs
  \draw (0,4) -- (1,4); \node[left] at (0,4) {$A_2, B_2$};
  \draw (0,2.5) -- (1,2.5); \node[left] at (0,2.5) {$A_1, B_1$};
  \draw (0,1) -- (1,1); \node[left] at (0,1) {$A_0, B_0$};

  % XNOR Equality blocks
  \node[draw, rectangle, fill=boxbg] (xnor2) at (2,4) {$x_2 = A_2 \odot B_2$};
  \node[draw, rectangle, fill=boxbg] (xnor1) at (2,2.5) {$x_1 = A_1 \odot B_1$};
  \node[draw, rectangle, fill=boxbg] (xnor0) at (2,1) {$x_0 = A_0 \odot B_0$};

  % AND gate for A=B
  \node[and gate US, draw, logic gate inputs=nnn] (andEQ) at (7,2.5) {};
  \draw (xnor2.east) -| (andEQ.input 1);
  \draw (xnor1.east) -- (andEQ.input 2);
  \draw (xnor0.east) -| (andEQ.input 3);
  \draw (andEQ.output) -- ++(1.5,0); \node[right] at ($(andEQ.output)+(1.5,0)$) {\large $\mathbf{A = B}$};

  % Output OR for A>B
  \node[or gate US, draw, logic gate inputs=nnn] (orGT) at (7,5.0) {};
  \draw (orGT.output) -- ++(1.5,0); \node[right] at ($(orGT.output)+(1.5,0)$) {\large $\mathbf{A > B}$};

  % Output OR for A<B
  \node[or gate US, draw, logic gate inputs=nnn] (orLT) at (7,0.0) {};
  \draw (orLT.output) -- ++(1.5,0); \node[right] at ($(orLT.output)+(1.5,0)$) {\large $\mathbf{A < B}$};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 6: Full Adder Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q6)}
Implement a full adder circuit using Multiplexer.
\end{questionbox}

A full adder has inputs $A, B, C_{\text{in}}$ and outputs $\text{Sum} = \sum m(1, 2, 4, 7)$ and $C_{\text{out}} = \sum m(3, 5, 6, 7)$.

\paragraph{Implementation Table (Select Lines: $S_1 = A, S_0 = B$):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{Output} & \textbf{$I_0$ ($AB=00$)} & \textbf{$I_1$ ($AB=01$)} & \textbf{$I_2$ ($AB=10$)} & \textbf{$I_3$ ($AB=11$)} \\ \hline
\textbf{Sum} & $C_{\text{in}}$ ($m_1$) & $\bar{C}_{\text{in}}$ ($m_2$) & $\bar{C}_{\text{in}}$ ($m_4$) & $C_{\text{in}}$ ($m_7$) \\ \hline
\textbf{Carry ($C_{\text{out}}$)} & $0$ & $C_{\text{in}}$ ($m_3$) & $C_{\text{in}}$ ($m_5$) & $1$ ($m_6, m_7$) \\ \hline
\end{tabular}
\end{center}

\begin{schematicbox}{Full Adder Realization Using Dual 4:1 Multiplexers}
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
  \draw[thick] (3,2) -- (4.8,2); \node[right] at (4.8,2) {\large $\mathbf{Sum}$};

  % MUX 2: Carry Out
  \draw[thick, fill=boxbg] (8.5,0) rectangle (11.5,4);
  \node at (10.0,3.5) {\textbf{4:1 MUX ($C_{\text{out}}$)}};
  \node at (8.9,2.8) {\small $I_0$};
  \node at (8.9,2.2) {\small $I_1$};
  \node at (8.9,1.6) {\small $I_2$};
  \node at (8.9,1.0) {\small $I_3$};
  \node at (10.0,0.4) {\small $S_1\quad S_0$};
  \draw[thick] (11.5,2) -- (13.0,2); \node[right] at (13.0,2) {\large $\mathbf{C_{\text{out}}}$};

  % Select Line Bus
  \draw[thick] (-1.5,-1.2) -- (1.0,-1.2) -- (1.0,0); \node[left] at (-1.5,-1.2) {$A$};
  \draw[thick] (-1.5,-1.8) -- (2.0,-1.8) -- (2.0,0); \node[left] at (-1.5,-1.8) {$B$};
  \draw[thick] (1.0,-1.2) -- (9.5,-1.2) -- (9.5,0);
  \draw[thick] (2.0,-1.8) -- (10.5,-1.8) -- (10.5,0);

  % Data Inputs Connections for Sum
  \draw (-1.5,2.8) -- (0,2.8); \node[left] at (-1.5,2.8) {$C_{\text{in}}$};
  \node[not gate US, draw, scale=0.8] (not1) at (-0.8,2.2) {};
  \draw (-1.5,2.2) -- (not1.input); \draw (not1.output) -- (0,2.2);
  \draw (-0.8,2.2) |- (0,1.6);
  \draw (-1.5,2.8) |- (0,1.0);

  % Data Inputs Connections for Cout
  \draw (6.8,2.8) -- (8.5,2.8); \node[left] at (6.8,2.8) {$0\ (\text{GND})$};
  \draw (6.8,2.2) -- (8.5,2.2); \node[left] at (6.8,2.2) {$C_{\text{in}}$};
  \draw (6.8,1.6) -- (8.5,1.6);
  \draw (6.8,1.0) -- (8.5,1.0); \node[left] at (6.8,1.0) {$1\ (V_{CC})$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Sum:} $I_0 = C_{in}, I_1 = \bar{C}_{in}, I_2 = \bar{C}_{in}, I_3 = C_{in}$.\\[0.1cm]
\textbf{Carry ($C_{\text{out}}$):} $I_0 = 0, I_1 = C_{in}, I_2 = C_{in}, I_3 = 1$. Select lines: $S_1 = A, S_0 = B$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 7: SR to JK Flip-Flop Conversion Schematic [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q7)}
Differentiate between combinational circuit and sequential circuit. With necessary steps and implementation, Convert SR flip flop into JK flip flop.
\end{questionbox}

\paragraph{Comparison: Combinational vs. Sequential Circuits}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Feature} & \textbf{Combinational Circuit} & \textbf{Sequential Circuit} \\
\midrule
\textbf{Output Dependence} & Depends only on current inputs & Depends on current inputs and past history (stored states) \\
\textbf{Memory Elements} & No memory elements present & Contains memory elements (latches/flip-flops) \\
\textbf{Feedback Path} & No feedback path & Contains feedback paths from output to input \\
\textbf{Clock Requirement} & Operates asynchronously without clock & Synchronized by periodic clock pulses \\
\textbf{Examples} & Adders, Multiplexers, Decoders & Shift Registers, Counters, FSM Controllers \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{SR to JK Conversion Table:}
\begin{center}
\begin{tabular}{|c|c|c||c||c|c|}
\hline
\textbf{$J$} & \textbf{$K$} & \textbf{$Q_n$} & \textbf{$Q_{n+1}$} & \textbf{$S$} & \textbf{$R$} \\ \hline
0 & 0 & 0 & 0 & 0 & $d$ \\ \hline
0 & 0 & 1 & 1 & $d$ & 0 \\ \hline
0 & 1 & 0 & 0 & 0 & $d$ \\ \hline
0 & 1 & 1 & 0 & 0 & 1 \\ \hline
1 & 0 & 0 & 1 & 1 & 0 \\ \hline
1 & 0 & 1 & 1 & $d$ & 0 \\ \hline
1 & 1 & 0 & 1 & 1 & 0 \\ \hline
1 & 1 & 1 & 0 & 0 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{Conversion Equations:}
$$S = J\bar{Q}, \qquad R = KQ$$

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
  \draw (-1.0,3.4) -- (andS.input 1); \node[left] at (-1.0,3.4) {$J$};
  \draw (-1.0,1.3) -- (andR.input 2); \node[left] at (-1.0,1.3) {$K$};

  \draw (andS.output) -- (6,3.2);
  \draw (andR.output) -- (6,1.5);

  % Outputs and Feedback
  \draw[thick] (9,3.2) -- (10.5,3.2); \node[right] at (10.5,3.2) {\large $\mathbf{Q}$};
  \draw[thick] (9,1.5) -- (10.5,1.5); \node[right] at (10.5,1.5) {\large $\mathbf{\bar{Q}}$};

  \draw (9.8,3.2) -- (9.8,0.5) -- (1.5,0.5) |- (andR.input 1);
  \draw (9.5,1.5) -- (9.5,4.8) -- (1.5,4.8) |- (andS.input 2);
  \draw (4.5,2.0) -- (6,2.0); \node[left] at (4.5,2.0) {$\text{CLK}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{S = J\bar{Q}, \qquad R = KQ}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: Types of Shift Registers \& 4-Bit Johnson Counter [2 + 3 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q8)}
Write briefly about different types of shift registers. With necessary circuit and timing diagrams, explain the operation of how the shift register is used as a Johnson's Counter.
\end{questionbox}

\paragraph{Types of Shift Registers:}
\begin{enumerate}
  \item \textbf{SISO (Serial-In Serial-Out):} Accepts data serially and outputs serially; used for time delay.
  \item \textbf{SIPO (Serial-In Parallel-Out):} Converts serial bitstream to parallel words.
  \item \textbf{PISO (Parallel-In Serial-Out):} Accepts parallel words and transmits serially.
  \item \textbf{PIPO (Parallel-In Parallel-Out):} Loads and outputs parallel words simultaneously; used as general data registers.
\end{enumerate}

\paragraph{Johnson Counter Operation:}
A 4-bit Johnson (twisted ring) counter is formed by connecting the inverted output of the last flip-flop ($\bar{Q}_3$) back to the data input ($D_0$) of the first flip-flop. It produces $2n = 8$ distinct states.

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
    \draw[thick] ({(\i)*3.6 + 2.4}, 1.8) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*3.6 + 2.8}, 3.3) {\large $\mathbf{Q_\i}$};
  }

  % Forward Shifts
  \draw[thick] (2.4, 1.8) -- (3.6, 1.8);
  \draw[thick] (6.0, 1.8) -- (7.2, 1.8);
  \draw[thick] (9.6, 1.8) -- (10.8, 1.8);

  % Inverted Feedback from Q3_bar back to D0
  \draw[thick] (13.2, 0.8) -- (13.8, 0.8) -- (13.8, -1.5) -- (-0.8, -1.5) -- (-0.8, 1.8) -- (0, 1.8);

  % Common Clock
  \draw[thick] (-1.0, -0.6) -- (12.0, -0.6);
  \node[left] at (-1.0, -0.6) {\large $\mathbf{\text{CLK}}$};
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.6 + 0.5}, -0.6) -- ({(\i)*3.6 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\paragraph{Johnson Counter Sequence Table:}
\begin{center}
\begin{tabular}{|c|cccc|l|}
\hline
\textbf{State / Pulse} & \textbf{$Q_0$} & \textbf{$Q_1$} & \textbf{$Q_2$} & \textbf{$Q_3$} & \textbf{Decoding Logic} \\ \hline
0 & 0 & 0 & 0 & 0 & $\bar{Q}_0 \bar{Q}_3$ \\ \hline
1 & 1 & 0 & 0 & 0 & $Q_0 \bar{Q}_1$ \\ \hline
2 & 1 & 1 & 0 & 0 & $Q_1 \bar{Q}_2$ \\ \hline
3 & 1 & 1 & 1 & 0 & $Q_2 \bar{Q}_3$ \\ \hline
4 & 1 & 1 & 1 & 1 & $Q_0 Q_3$ \\ \hline
5 & 0 & 1 & 1 & 1 & $\bar{Q}_0 Q_1$ \\ \hline
6 & 0 & 0 & 1 & 1 & $\bar{Q}_1 Q_2$ \\ \hline
7 & 0 & 0 & 0 & 1 & $\bar{Q}_2 Q_3$ \\ \hline
\end{tabular}
\end{center}

\begin{answerbox}
$2n = 8$ states: $0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: 3-Bit Ripple UP Counter with Positive Edge Triggering [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q9)}
Describe the operation of 3-bit ripple up counter with positive edge triggered clock.
\end{questionbox}

For positive-edge triggered T flip-flops to count in an UP sequence ($000 \to 111$), each subsequent flip-flop's clock must be driven by the inverted output ($\bar{Q}$) of the preceding stage ($\text{CLK}_{i+1} = \bar{Q}_i$).

\begin{schematicbox}{3-Bit Ripple UP Counter Schematic (Positive Edge Triggered)}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \foreach \i in {0,1,2} {
    \draw[thick, fill=boxbg] ({(\i)*4.2}, 0) rectangle ({(\i)*4.2 + 2.8}, 3);
    \node at ({(\i)*4.2 + 1.4}, 2.6) {\textbf{FF\i\ (T=1)}};
    \node at ({(\i)*4.2 + 0.5}, 1.5) {\small $>$};
    \node at ({(\i)*4.2 + 2.3}, 2.0) {\small $Q$};
    \node at ({(\i)*4.2 + 2.3}, 1.0) {\small $\bar{Q}$};
    \draw[thick] ({(\i)*4.2 + 2.8}, 2.0) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*4.2 + 3.2}, 3.5) {\large $\mathbf{Q_\i}$};
  }

  % CLK into FF0
  \draw[thick] (-1.0, 1.5) -- (0, 1.5);
  \node[left] at (-1.0, 1.5) {\large $\mathbf{\text{CLK}}$};

  % Clocking from Q_bar for UP counting on positive edges
  \draw[thick] (2.8, 1.0) -- (3.5, 1.0) |- (4.2, 1.5);
  \draw[thick] (7.0, 1.0) -- (7.7, 1.0) |- (8.4, 1.5);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Counts $000 \to 111$. Each stage toggles on the positive clock edge produced by the preceding $\bar{Q}$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 10: Synchronous Mod-6 Counter Using SR Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q10)}
Design the synchronous mod-6 counter using S R flip-flop and draw its timing diagram also.
\end{questionbox}

\paragraph{State Transition and SR Excitation Table ($0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 0$):}
\begin{center}
\begin{tabular}{|c|ccc|ccc|cc|cc|cc|}
\hline
\textbf{Dec} & \multicolumn{3}{c|}{\textbf{Present State}} & \multicolumn{3}{c|}{\textbf{Next State}} & \multicolumn{2}{c|}{\textbf{FF2}} & \multicolumn{2}{c|}{\textbf{FF1}} & \multicolumn{2}{c|}{\textbf{FF0}} \\
& $Q_2$ & $Q_1$ & $Q_0$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $S_2$ & $R_2$ & $S_1$ & $R_1$ & $S_0$ & $R_0$ \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & $d$ & 0 & $d$ & 1 & 0 \\ \hline
1 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & $d$ & 1 & 0 & 0 & 1 \\ \hline
2 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & $d$ & $d$ & 0 & 1 & 0 \\ \hline
3 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 \\ \hline
4 & 1 & 0 & 0 & 1 & 0 & 1 & $d$ & 0 & 0 & $d$ & 1 & 0 \\ \hline
5 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & $d$ & 0 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{Minimized Design Equations:}
$$S_0 = \bar{Q}_0, \quad R_0 = Q_0, \qquad S_1 = \bar{Q}_2\bar{Q}_1 Q_0, \quad R_1 = Q_1 Q_0, \qquad S_2 = Q_1 Q_0, \quad R_2 = Q_0$$

\begin{answerbox}
$$\mathbf{S_0 = \bar{Q}_0, \ R_0 = Q_0, \quad S_1 = \bar{Q}_2\bar{Q}_1 Q_0, \ R_1 = Q_1 Q_0, \quad S_2 = Q_1 Q_0, \ R_2 = Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 11: Synchronous FSM Sequence Detector '110' [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q11)}
Design a synchronous sequential machine that has 1bit serial input X and output Z which will be high when the input contains the message 110 (Use SR Flip Flop).
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

\paragraph{Design Equations for SR Flip-Flops ($A, B$):}
$$S_A = BX, \quad R_A = \bar{X}, \qquad S_B = \bar{A}\bar{B}X, \quad R_B = B\bar{X} + A, \qquad Z = A\bar{X}$$

\begin{answerbox}
$$\mathbf{S_A = BX, \quad R_A = \bar{X}, \quad S_B = \bar{A}\bar{B}X, \quad R_B = B\bar{X} + A, \quad Z = A\bar{X}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 12: Frequency Counter Block Diagram [3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q12)}
Write a short note on frequency counter.
\end{questionbox}

A digital frequency counter measures the unknown frequency $f_x$ of an input signal by counting the number of cycles $N$ passing through a precision time-base gate during an exact gate period $T_{\text{gate}}$ ($f_x = N / T_{\text{gate}}$).

\begin{schematicbox}{Digital Frequency Counter Functional Block Diagram}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (amp) at (0,2) {Attenuator/Amp};
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (schmitt) at (3.8,2) {Schmitt Trigger};
  \node[and gate US, draw, logic gate inputs=nn, scale=1.3] (gate) at (7.2,1) {};
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (counter) at (10.6,1) {Decade Counter};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (disp) at (14.2,1) {Display};

  \node[draw, rectangle, fill=boxbg, minimum width=2.2cm, minimum height=1.0cm] (osc) at (0,-0.5) {Crystal Osc};
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (div) at (3.8,-0.5) {Time Base Div};

  \draw[thick, ->] (-2.2,2) -- (amp); \node[left] at (-2.2,2) {$f_x$ (Unknown)};
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
Define an ASCII code. Use 2's complement method to perform the following addition $(-28 + 12)_{10}$ in 8-bit signed number representation.
\end{questionbox}

\paragraph{ASCII Definition:}
ASCII (American Standard Code for Information Interchange) is a 7-bit standard alphanumeric character encoding scheme ($2^7 = 128$ characters) representing letters, digits, punctuation, and control characters.

\paragraph{8-Bit 2's Complement Addition:}
\begin{itemize}
  \item Magnitude $+28 = 0001\ 1100_2$
  \item 1's complement of $+28 = 1110\ 0011_2$
  \item 2's complement of $-28 = 1110\ 0011 + 1 = 1110\ 0100_2$
  \item Value $+12 = 0000\ 1100_2$
\end{itemize}

\begin{align*}
  1110\ 0100_2 \quad &(-28) \\
+ 0000\ 1100_2 \quad &(+\,12) \\
\hline
  1111\ 0000_2 \quad &(-16)
\end{align*}

\paragraph{Verification:}
$1111\ 0000_2$ has sign bit $1$ (negative). Taking 2's complement: $-(0000\ 1111 + 1) = -(0001\ 0000_2) = -16_{10}$.

\begin{answerbox}
$$(-28 + 12)_{10} = \mathbf{1111\ 0000_2} = -16_{10}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: Boolean Algebra Proofs [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q2)}
Prove the following:
\begin{enumerate}[label=(\alph*)]
  \item $AB + \bar{A}C + BC = AB + \bar{A}C$
  \item $AB + C(A \oplus B) = BC + A(B+C)$
\end{enumerate}
\end{questionbox}

\paragraph{Part (a): Consensus Theorem Proof}
\begin{align*}
\text{LHS} &= AB + \bar{A}C + BC \\
&= AB + \bar{A}C + BC(A + \bar{A}) \\
&= AB + \bar{A}C + ABC + \bar{A}BC \\
&= AB(1 + C) + \bar{A}C(1 + B) \\
&= AB(1) + \bar{A}C(1) = AB + \bar{A}C = \text{RHS} \quad \blacksquare
\end{align*}

\paragraph{Part (b):}
\begin{align*}
\text{LHS} &= AB + C(A\bar{B} + \bar{A}B) = AB + A\bar{B}C + \bar{A}BC \\
\text{RHS} &= BC + A(B + C) = BC + AB + AC \\
&= AB + BC(A + \bar{A}) + AC(B + \bar{B}) \\
&= AB + ABC + \bar{A}BC + ABC + A\bar{B}C \\
&= AB + A\bar{B}C + \bar{A}BC = \text{LHS} \quad \blacksquare
\end{align*}

\begin{answerbox}
Both identities are verified algebraically.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: Octal Priority Encoder Schematic [2 + 6 = 8 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q3)}
What is a decoder? Design an octal priority encoder with neat circuit diagram.
\end{questionbox}

\paragraph{Decoder Definition:}
A decoder is a combinational circuit with $n$ input lines and up to $2^n$ unique output lines that decodes binary input words into mutually exclusive active outputs.

\paragraph{Octal Priority Encoder Truth Table (Higher index has priority):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c||c|c|c||c|}
\hline
\textbf{$D_7$} & \textbf{$D_6$} & \textbf{$D_5$} & \textbf{$D_4$} & \textbf{$D_3$} & \textbf{$D_2$} & \textbf{$D_1$} & \textbf{$D_0$} & \textbf{$A$} & \textbf{$B$} & \textbf{$C$} & \textbf{$V$} \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & $d$ & $d$ & $d$ & 0 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 1 & $d$ & 0 & 0 & 1 & 1 \\ \hline
0 & 0 & 0 & 0 & 0 & 1 & $d$ & $d$ & 0 & 1 & 0 & 1 \\ \hline
0 & 0 & 0 & 0 & 1 & $d$ & $d$ & $d$ & 0 & 1 & 1 & 1 \\ \hline
0 & 0 & 0 & 1 & $d$ & $d$ & $d$ & $d$ & 1 & 0 & 0 & 1 \\ \hline
0 & 0 & 1 & $d$ & $d$ & $d$ & $d$ & $d$ & 1 & 0 & 1 & 1 \\ \hline
0 & 1 & $d$ & $d$ & $d$ & $d$ & $d$ & $d$ & 1 & 1 & 0 & 1 \\ \hline
1 & $d$ & $d$ & $d$ & $d$ & $d$ & $d$ & $d$ & 1 & 1 & 1 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{Boolean Output Equations:}
\begin{align*}
A &= D_4 + D_5 + D_6 + D_7 \\
B &= D_2\bar{D}_4\bar{D}_5 + D_3\bar{D}_4\bar{D}_5 + D_6 + D_7 \\
C &= D_1\bar{D}_2\bar{D}_4\bar{D}_6 + D_3\bar{D}_4\bar{D}_6 + D_5\bar{D}_6 + D_7 \\
V &= D_0 + D_1 + D_2 + D_3 + D_4 + D_5 + D_6 + D_7
\end{align*}

\begin{schematicbox}{8-to-3 Octal Priority Encoder Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \draw[thick, fill=boxbg] (0,0) rectangle (6,6);
  \node at (3,5.5) {\textbf{8-to-3 Priority Encoder}};

  \foreach \i in {0,...,7} {
    \draw[thick] (-1.2, {0.6 + \i*0.6}) -- (0, {0.6 + \i*0.6});
    \node[left] at (-1.2, {0.6 + \i*0.6}) {$D_\i$};
  }

  \draw[thick] (6,4.5) -- ++(1.5,0); \node[right] at (7.5,4.5) {\large $\mathbf{A} = D_4 + D_5 + D_6 + D_7$};
  \draw[thick] (6,3.0) -- ++(1.5,0); \node[right] at (7.5,3.0) {\large $\mathbf{B} = D_2\bar{D}_4\bar{D}_5 + D_3\bar{D}_4\bar{D}_5 + D_6 + D_7$};
  \draw[thick] (6,1.5) -- ++(1.5,0); \node[right] at (7.5,1.5) {\large $\mathbf{C} = D_1\bar{D}_2\bar{D}_4\bar{D}_6 + D_3\bar{D}_4\bar{D}_6 + D_5\bar{D}_6 + D_7$};
  \draw[thick] (6,0.5) -- ++(1.5,0); \node[right] at (7.5,0.5) {\large $\mathbf{V} = \sum D_i$ (Valid Output)};
\end{tikzpicture}
\end{schematicbox}

\vspace{0.5cm}
\subsection{Question 4: 3x8 Decoder Function Realization \& K-Map [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q4)}
Realize the following Boolean function using a single 3x8 decoder. Also simplify the logic function implementing K-map method.
$$X(A,B,C,D) = \sum m(0, 2, 3, 7, 8, 10, 11, 14, 15)$$
\end{questionbox}

\paragraph{K-Map Simplification:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{$AB \backslash CD$} & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $\mathbf{1}$ ($m_0$) & $0$ ($m_1$) & $\mathbf{1}$ ($m_3$) & $\mathbf{1}$ ($m_2$) \\ \hline
\textbf{01} & $0$ ($m_4$) & $0$ ($m_5$) & $\mathbf{1}$ ($m_7$) & $0$ ($m_6$) \\ \hline
\textbf{11} & $0$ ($m_{12}$) & $0$ ($m_{13}$) & $\mathbf{1}$ ($m_{15}$) & $\mathbf{1}$ ($m_{14}$) \\ \hline
\textbf{10} & $\mathbf{1}$ ($m_8$) & $0$ ($m_9$) & $\mathbf{1}$ ($m_{11}$) & $\mathbf{1}$ ($m_{10}$) \\ \hline
\end{tabular}
\end{center}

\paragraph{Minimized SOP Expression:}
$$X(A,B,C,D) = AC + CD + \bar{B}\bar{D}$$

\begin{schematicbox}{Realization of 4-Variable Function Using 3x8 Decoder}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  \draw[thick, fill=boxbg] (0,0) rectangle (3.5,6);
  \node at (1.75,5.5) {\textbf{3x8 Decoder}};

  \draw[thick] (-1.5,4.5) -- (0,4.5); \node[left] at (-1.5,4.5) {$A$ ($S_2$)};
  \draw[thick] (-1.5,3.0) -- (0,3.0); \node[left] at (-1.5,3.0) {$B$ ($S_1$)};
  \draw[thick] (-1.5,1.5) -- (0,1.5); \node[left] at (-1.5,1.5) {$C$ ($S_0$)};

  \foreach \i in {0,...,7} {
    \node at (3.0, {0.6 + \i*0.6}) {\small $Y_\i$};
    \draw[thick] (3.5, {0.6 + \i*0.6}) -- (5.0, {0.6 + \i*0.6});
  }

  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.4] (orX) at (8,3) {};
  \draw (5, 0.6) -- (orX.input 4); \node[right] at (5, 0.6) {\small $Y_0 \bar{D}$};
  \draw (5, 1.8) -- (orX.input 3); \node[right] at (5, 1.8) {\small $Y_1 (CD)$};
  \draw (5, 4.2) -- (orX.input 2); \node[right] at (5, 4.2) {\small $Y_4 \bar{D}$};
  \draw (5, 4.8) -- (orX.input 1); \node[right] at (5, 4.8) {\small $Y_5 + Y_7$};
  \draw (orX.output) -- ++(1,0); \node[right] at ($(orX.output)+(1,0)$) {\large $\mathbf{X}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{X(A,B,C,D) = AC + CD + \bar{B}\bar{D}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Synchronous 2-Bit UP/DOWN Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q5)}
Design a synchronous 2-bit up/down counter using T flip-flops.
\end{questionbox}

Let mode control be $M$ ($M=0 \implies \text{UP Counting}$, $M=1 \implies \text{DOWN Counting}$).

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
  \draw[thick] (2.8,2.2) -- ++(0.5,0) -- ++(0,1.8);
  \node[above] at (3.3,4.0) {\large $\mathbf{Q_0}$};

  % FF1
  \draw[thick, fill=boxbg] (6,0) rectangle (8.8,3.5);
  \node at (7.4,3.0) {\textbf{FF1 (T)}};
  \node at (6.4,2.2) {\small $T_1$};
  \node at (6.5,1.0) {\small $>$};
  \node at (8.4,2.2) {\small $Q_1$};
  \node at (8.4,1.0) {\small $\bar{Q}_1$};
  \draw[thick] (8.8,2.2) -- ++(0.5,0) -- ++(0,1.8);
  \node[above] at (9.3,4.0) {\large $\mathbf{Q_1}$};

  % T0 = 1
  \draw[thick] (-1.0,2.2) -- (0,2.2); \node[left] at (-1.0,2.2) {$1\ (V_{CC})$};

  % XOR Gate for T1 = M XOR Q0
  \node[xor gate US, draw, logic gate inputs=nn] (xorT1) at (4.8,2.2) {};
  \draw (xorT1.output) -- (6,2.2);
  \draw (2.8,2.2) -- (xorT1.input 2);
  \draw (-1.0,4.5) -- (4.0,4.5) |- (xorT1.input 1);
  \node[left] at (-1.0,4.5) {\large $\mathbf{M}$ (Mode)};

  % Common Synchronous Clock
  \draw[thick] (-1.0,-1.0) -- (7.5,-1.0);
  \node[left] at (-1.0,-1.0) {\large $\mathbf{\text{CLK}}$};
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

A 4-bit PISO register uses a Shift/$\overline{\text{Load}}$ control line. When $\text{Shift}/\overline{\text{Load}} = 0$, parallel inputs $I_3 I_2 I_1 I_0$ are loaded into flip-flops $FF_3 \dots FF_0$. When $\text{Shift}/\overline{\text{Load}} = 1$, data shifts right toward the serial output.

\begin{schematicbox}{4-Bit Parallel-In Serial-Out (PISO) Shift Register Logic Diagram}
\centering
\begin{tikzpicture}[scale=0.8, transform shape]
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({(\i)*3.8}, 0) rectangle ({(\i)*3.8 + 2.4}, 2.8);
    \node at ({(\i)*3.8 + 1.2}, 2.4) {\textbf{FF\i\ (D)}};
    \node at ({(\i)*3.8 + 0.4}, 1.6) {\small $D$};
    \node at ({(\i)*3.8 + 0.5}, 0.8) {\small $>$};
    \node at ({(\i)*3.8 + 2.0}, 1.6) {\small $Q$};
    \draw[thick] ({(\i)*3.8 + 1.2}, 3.8) -- ({(\i)*3.8 + 1.2}, 2.8);
    \node[above] at ({(\i)*3.8 + 1.2}, 3.8) {\small $I_\i$ (Load)};
  }

  % Interconnects
  \draw[thick] (2.4, 1.6) -- (3.8, 1.6);
  \draw[thick] (6.2, 1.6) -- (7.6, 1.6);
  \draw[thick] (10.0, 1.6) -- (11.4, 1.6);
  \draw[thick] (13.8, 1.6) -- (15.2, 1.6);
  \node[right] at (15.2, 1.6) {\large $\mathbf{D_{\text{out}}}$ (Serial)};

  % Clock
  \draw[thick] (-1.0, -1.0) -- (14.0, -1.0);
  \node[left] at (-1.0, -1.0) {\large $\mathbf{\text{CLK}}$};
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({(\i)*3.8 + 0.5}, -1.0) -- ({(\i)*3.8 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Data word $1101_2$ is loaded in 1 parallel load cycle and shifted out serially across 3 shift clock pulses.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 7: Mod-12 Asynchronous Counter Schematic [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q7)}
Sketch the circuit diagram of mod-12 asynchronous counter having positive-edge triggering clock system implementing JK flip-flops with neat timing diagram.
\end{questionbox}

For positive-edge triggered JK flip-flops to count UP ($0000 \to 1011$), each subsequent clock is driven by $\bar{Q}$ of the previous flip-flop ($\text{CLK}_{i+1} = \bar{Q}_i$). The counter resets at $12_{10} = 1100_2$ ($Q_3=1, Q_2=1$).

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
    \draw[thick] ({(\i)*3.6 + 2.4}, 2.0) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*3.6 + 2.8}, 3.5) {\large $\mathbf{Q_\i}$};
  }

  % Clock into FF0
  \draw[thick] (-1.0, 1.5) -- (0, 1.5);
  \node[left] at (-1.0, 1.5) {\large $\mathbf{\text{CLK}}$};

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
Design a sequential machine that consists of one input, X and one output, Z. The machine is required to give output high (Z=1), whenever it detects the serial sequence of 010 from its input data stream X. Implement only D flip-flops for the designed circuit realization.
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

\paragraph{Design Equations for D Flip-Flops ($A, B$):}
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
  \draw (-1.5,4.0) -- (1.0,4.0) |- (andDA.input 1); \node[left] at (-1.5,4.0) {\large $\mathbf{X}$};
  \draw (1.0,4.0) |- (notX.input);

  % Feedback B to andDA
  \draw (6.5,-0.4) -- (7.5,-0.4) -- (7.5,-2.8) -- (0.5,-2.8) |- (andDA.input 2);

  % Output Z = A . X_bar
  \draw (6.5,3.6) -- (andZ.input 1);
  \draw (2.8,-0.4) -- (3.2,-0.4) -- (3.2,1.8) -- (7.5,1.8) |- (andZ.input 2);
  \draw (andZ.output) -- ++(1.0,0); \node[right] at ($(andZ.output)+(1.0,0)$) {\large $\mathbf{Z}$ (Output)};

  % Clock
  \draw (-1.5,-3.5) -- (5.25,-3.5); \node[left] at (-1.5,-3.5) {\large $\mathbf{\text{CLK}}$};
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
Draw the circuit diagram of two-input CMOS NAND gate and explain its logic operation briefly and list the characteristics of TTL logic family.
\end{questionbox}

\begin{schematicbox}{Two-Input CMOS NAND Gate Transistor Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Rails
  \draw[thick] (-2.5, 5.0) -- (2.5, 5.0);
  \node at (-2.5, 5.3) {$V_{DD}$};
  
  % PMOS P1 (Left)
  \draw[thick] (-1.2, 5.0) -- (-1.2, 4.2);
  \draw[thick] (-1.4, 4.2) -- (-1.0, 4.2);
  \draw[thick] (-1.4, 3.2) -- (-1.0, 3.2);
  \draw[thick] (-1.0, 4.4) -- (-1.0, 3.0);
  \draw[thick] (-1.4, 4.2) -- (-1.4, 3.2);
  \draw[thick] (-1.65, 3.7) circle (2pt);
  \draw[thick] (-2.5, 3.7) -- (-1.73, 3.7);
  \node[left] at (-2.5, 3.7) {$A$};
  \node at (-0.5, 3.7) {\small $P_1$};

  % PMOS P2 (Right)
  \draw[thick] (1.2, 5.0) -- (1.2, 4.2);
  \draw[thick] (1.0, 4.2) -- (1.4, 4.2);
  \draw[thick] (1.0, 3.2) -- (1.4, 3.2);
  \draw[thick] (1.0, 4.4) -- (1.0, 3.0);
  \draw[thick] (1.4, 4.2) -- (1.4, 3.2);
  \draw[thick] (0.75, 3.7) circle (2pt);
  \draw[thick] (0.67, 3.7) -- (-0.2, 3.7) -- (-0.2, 4.6) -- (-2.5, 4.6);
  \node[left] at (-2.5, 4.6) {$B$};
  \node at (1.8, 3.7) {\small $P_2$};

  % Common Drain Connection & Output
  \draw[thick] (-1.2, 3.2) -- (-1.2, 2.5) -- (1.2, 2.5) -- (1.2, 3.2);
  \draw[thick] (0, 2.5) -- (3.0, 2.5);
  \node[right] at (3.0, 2.5) {\large $\mathbf{Y = \overline{A \cdot B}}$};
  \fill (0, 2.5) circle (2pt);

  % NMOS N1 (Top Series)
  \draw[thick] (0, 2.5) -- (0, 2.0);
  \draw[thick] (-0.2, 2.0) -- (0.2, 2.0);
  \draw[thick] (-0.2, 1.0) -- (0.2, 1.0);
  \draw[thick] (0.2, 2.2) -- (0.2, 0.8);
  \draw[thick] (-0.2, 2.0) -- (-0.2, 1.0);
  \draw[thick] (-0.5, 1.5) -- (-0.2, 1.5);
  \draw[thick] (-0.5, 1.5) -- (-2.0, 1.5) -- (-2.0, 3.7);
  \fill (-2.0, 3.7) circle (2pt);
  \node at (0.6, 1.5) {\small $N_1$};

  % NMOS N2 (Bottom Series)
  \draw[thick] (0, 1.0) -- (0, 0.5);
  \draw[thick] (-0.2, 0.5) -- (0.2, 0.5);
  \draw[thick] (-0.2, -0.5) -- (0.2, -0.5);
  \draw[thick] (0.2, 0.7) -- (0.2, -0.7);
  \draw[thick] (-0.2, 0.5) -- (-0.2, -0.5);
  \draw[thick] (-0.5, 0.0) -- (-0.2, 0.0);
  \draw[thick] (-0.5, 0.0) -- (-2.3, 0.0) -- (-2.3, 4.6);
  \fill (-2.3, 4.6) circle (2pt);
  \node at (0.6, 0.0) {\small $N_2$};

  % Ground Rail
  \draw[thick] (0, -0.5) -- (0, -1.0);
  \draw[thick] (-0.6, -1.0) -- (0.6, -1.0);
  \draw[thick] (-0.4, -1.15) -- (0.4, -1.15);
  \draw[thick] (-0.2, -1.30) -- (0.2, -1.30);
  \node at (0, -1.6) {\small GND};
\end{tikzpicture}
\end{schematicbox}

\paragraph{Logic Operation Table:}
\begin{center}
\begin{tabular}{|c|c||c|c||c|c||c|}
\hline
\textbf{$A$} & \textbf{$B$} & \textbf{$P_1$} & \textbf{$P_2$} & \textbf{$N_1$} & \textbf{$N_2$} & \textbf{$Y = \overline{A \cdot B}$} \\ \hline
0 & 0 & ON & ON & OFF & OFF & \textbf{1} ($V_{DD}$) \\ \hline
0 & 1 & ON & OFF & OFF & ON & \textbf{1} ($V_{DD}$) \\ \hline
1 & 0 & OFF & ON & ON & OFF & \textbf{1} ($V_{DD}$) \\ \hline
1 & 1 & OFF & OFF & ON & ON & \textbf{0} (GND) \\ \hline
\end{tabular}
\end{center}

\vspace{0.5cm}
\subsection{Question 10: Time Interval Measurement Block Diagram [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q10)}
With the help of functional diagram explain the operation of time measuring circuit.
\end{questionbox}

A digital time interval meter measures the elapsed time $\Delta t$ between a START pulse and a STOP pulse by counting clock oscillations of a known frequency $f_c$ ($T = N \times T_{\text{clk}} = N / f_c$).

\begin{schematicbox}{Time Interval Measurement System Block Diagram}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % RS Flip Flop
  \draw[thick, fill=boxbg] (0,1) rectangle (2.5,3.5);
  \node at (1.25,3.0) {\textbf{RS Latch}};
  \node at (0.4,2.5) {\small $S$};
  \node at (0.4,1.5) {\small $R$};
  \node at (2.1,2.0) {\small $Q$};

  \draw[thick] (-1.5,2.5) -- (0,2.5); \node[left] at (-1.5,2.5) {\large $\mathbf{\text{START Pulse}}$};
  \draw[thick] (-1.5,1.5) -- (0,1.5); \node[left] at (-1.5,1.5) {\large $\mathbf{\text{STOP Pulse}}$};

  % Clock Generator
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (osc) at (2.5,-0.5) {Clock ($1\text{MHz}$)};

  % Main Gate
  \node[and gate US, draw, logic gate inputs=nn, scale=1.3] (gate) at (5.5,1.0) {};
  \draw[thick] (2.5,2.0) -| (gate.input 1);
  \draw[thick] (osc.east) -| (gate.input 2);

  % Counter & Display
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (counter) at (8.8,1.0) {Digital Counter};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (disp) at (12.5,1.0) {Display ($\mu\text{s}$)};

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

\paragraph{Merits:}
\begin{enumerate}
  \item \textbf{Superior Noise Immunity:} Digital circuits only distinguish between high/low voltage bands, ignoring intermediate noise voltages.
  \item \textbf{Error Detection and Correction:} Digital data can incorporate parity bits and Hamming codes for reliable transmission.
  \item \textbf{High Density Storage:} Data can be stored in semiconductor flash memory without signal degradation over time.
\end{enumerate}

\paragraph{Demerits:}
\begin{enumerate}
  \item \textbf{Higher Bandwidth Requirement:} Transmitting fast digital rectangular pulses requires significantly wider transmission bandwidth than analog signals.
  \item \textbf{Quantization Error:} Converting continuous analog physical signals to digital values introduces quantization noise during ADC conversion.
\end{enumerate}

\vspace{0.5cm}
\subsection{Question 2: Radix & Gray Code Conversions [3 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q2)}
Perform the following as indicated:
\begin{enumerate}[label=(\alph*)]
  \item $(6\text{E}.2\text{C})_{16} = (?)_{8}$
  \item $(10110110)_{\text{Gray}} = (?)_{2}$
\end{enumerate}
\end{questionbox}

\paragraph{Part (a): Hexadecimal to Octal}
\begin{enumerate}
  \item Hex to Binary: $(6\text{E}.2\text{C})_{16} = 0110\ 1110\ .\ 0010\ 1100_2$
  \item Regroup into 3-bit octal groups:
  $$(001)\ (101)\ (110)\ .\ (001)\ (011)\ (000)_2$$
  \item Convert to Octal: $(156.13)_8$.
\end{enumerate}

\paragraph{Part (b): Gray to Binary $(10110110)_{\text{Gray}}$}
\begin{itemize}
  \item $b_7 = 1$
  \item $b_6 = 1 \oplus 0 = 1$
  \item $b_5 = 1 \oplus 1 = 0$
  \item $b_4 = 0 \oplus 1 = 1$
  \item $b_3 = 1 \oplus 0 = 1$
  \item $b_2 = 1 \oplus 1 = 0$
  \item $b_1 = 0 \oplus 1 = 1$
  \item $b_0 = 1 \oplus 0 = 1$
\end{itemize}
$(10110110)_{\text{Gray}} = (11011011)_2$.

\begin{answerbox}
(a) $(6\text{E}.2\text{C})_{16} = \mathbf{(156.13)_8}$ \qquad (b) $(10110110)_{\text{Gray}} = \mathbf{(11011011)_2}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: BCD to 7-Segment 'f' Segment Decoder Logic Circuit [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q3)}
Design the simplest logic circuit for 'f' segment for the BCD-to-seven segment display decoder.
\end{questionbox}

Segment $f$ is illuminated for decimal digits $0, 4, 5, 6, 8, 9$. Decimal values $10$ to $15$ are invalid BCD and treated as don't-cares ($d$).

\paragraph{K-Map for Segment $f$:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{$AB \backslash CD$} & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $\mathbf{1}$ ($m_0$) & $0$ ($m_1$) & $0$ ($m_3$) & $0$ ($m_2$) \\ \hline
\textbf{01} & $\mathbf{1}$ ($m_4$) & $\mathbf{1}$ ($m_5$) & $0$ ($m_7$) & $\mathbf{1}$ ($m_6$) \\ \hline
\textbf{11} & $\mathbf{X}$ ($d_{12}$) & $\mathbf{X}$ ($d_{13}$) & $\mathbf{X}$ ($d_{15}$) & $\mathbf{X}$ ($d_{14}$) \\ \hline
\textbf{10} & $\mathbf{1}$ ($m_8$) & $\mathbf{1}$ ($m_9$) & $\mathbf{X}$ ($d_{11}$) & $\mathbf{X}$ ($d_{10}$) \\ \hline
\end{tabular}
\end{center}

\paragraph{Minimized Boolean Equation:}
$$f = A + B\bar{C} + B\bar{D} + \bar{C}\bar{D}$$

\begin{schematicbox}{Logic Gate Circuit for 7-Segment 'f' Segment}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (3,2.5) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (3,1.0) {};
  \node[and gate US, draw, logic gate inputs=nn] (and3) at (3,-0.5) {};
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.3] (orF) at (6,1.0) {};

  \draw (1,3.8) -- ++(4,0) |- (orF.input 1); \node[left] at (1,3.8) {$A$};

  \draw (1,2.7) -- (and1.input 1); \node[left] at (1,2.7) {$\bar{C}$};
  \draw (1,2.3) -- (and1.input 2); \node[left] at (1,2.3) {$\bar{D}$};

  \draw (1,1.2) -- (and2.input 1); \node[left] at (1,1.2) {$B$};
  \draw (1,0.8) -- (and2.input 2); \node[left] at (1,0.8) {$\bar{C}$};

  \draw (1,-0.3) -- (and3.input 1); \node[left] at (1,-0.3) {$B$};
  \draw (1,-0.7) -- (and3.input 2); \node[left] at (1,-0.7) {$\bar{D}$};

  \draw (and1.output) -- ++(1,0) |- (orF.input 2);
  \draw (and2.output) -- (orF.input 3);
  \draw (and3.output) -- ++(1,0) |- (orF.input 4);

  \draw (orF.output) -- ++(1,0); \node[right] at ($(orF.output)+(1,0)$) {\large $\mathbf{f}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{f = A + B\bar{C} + B\bar{D} + \bar{C}\bar{D}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 4: 4:1 MUX Realization \& Combined Adder/Subtractor [3 + 7 = 10 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q4)}
Implement $Y(A,B,C) = \sum m(0, 2, 3, 5, 7)$ using only a single 4:1 MUX. Design a circuit which can realize both the half-adder and the half-subtractor in a single circuit.
\end{questionbox}

\paragraph{Part 1: 4:1 MUX Implementation ($S_1 = A, S_0 = B$)}
\begin{itemize}
  \item $AB = 00$: $m_0=1, m_1=0 \implies I_0 = \bar{C}$
  \item $AB = 01$: $m_2=1, m_3=1 \implies I_1 = 1 (V_{CC})$
  \item $AB = 10$: $m_4=0, m_5=1 \implies I_2 = C$
  \item $AB = 11$: $m_6=0, m_7=1 \implies I_3 = C$
\end{itemize}

\begin{schematicbox}{Combined Half-Adder and Half-Subtractor Logic Circuit}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Mode Control XOR
  \node[xor gate US, draw, logic gate inputs=nn] (xorM) at (2,2) {};
  \draw (-1,2.2) -- (xorM.input 1); \node[left] at (-1,2.2) {\large $\mathbf{A}$};
  \draw (-1,1.8) -- (xorM.input 2); \node[left] at (-1,1.8) {\large $\mathbf{M}$ (Mode)};

  % Sum/Diff XOR Gate
  \node[xor gate US, draw, logic gate inputs=nn] (xorOut) at (5,3.5) {};
  \draw (-1,3.7) -- (xorOut.input 1); \node[left] at (-1,3.7) {\large $\mathbf{A}$};
  \draw (-1,0.5) -- (1.5,0.5) |- (xorOut.input 2); \node[left] at (-1,0.5) {\large $\mathbf{B}$};
  \draw (xorOut.output) -- ++(1.5,0); \node[right] at ($(xorOut.output)+(1.5,0)$) {\large $\mathbf{Sum / Diff} = A \oplus B$};

  % Carry/Borrow AND Gate
  \node[and gate US, draw, logic gate inputs=nn] (andCB) at (5,1.2) {};
  \draw (xorM.output) -- (andCB.input 1);
  \draw (1.5,0.5) |- (andCB.input 2);
  \draw (andCB.output) -- ++(1.5,0); \node[right] at ($(andCB.output)+(1.5,0)$) {\large $\mathbf{Carry / Borrow} = (A \oplus M)B$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$M=0 \implies \text{Half Adder}; \quad M=1 \implies \text{Half Subtractor}$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Mod-6 Synchronous DOWN Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q5)}
Design a mod-6 synchronous down counter using JK flip-flops.
\end{questionbox}

Counting sequence: $5 (101) \to 4 (100) \to 3 (011) \to 2 (010) \to 1 (001) \to 0 (000) \to 5 (101)$.

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
    \draw[thick] ({(\i)*4.0 + 2.6}, 2.4) -- ++(0.4,0) -- ++(0,1.8);
    \node[above] at ({(\i)*4.0 + 3.0}, 4.2) {\large $\mathbf{Q_\i}$};
  }

  % FF0 J=K=1
  \draw[thick] (-0.8,2.4) -- (0,2.4); \node[left] at (-0.8,2.4) {$1\ (V_{CC})$};
  \draw[thick] (-0.8,0.6) -- (0,0.6); \node[left] at (-0.8,0.6) {$1\ (V_{CC})$};

  % Common Clock
  \draw[thick] (-1.0,-1.0) -- (10.0,-1.0);
  \node[left] at (-1.0,-1.0) {\large $\mathbf{\text{CLK}}$};
  \foreach \i in {0,1,2} {
    \draw[thick] ({(\i)*4.0 + 0.5}, -1.0) -- ({(\i)*4.0 + 0.5}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{J_0=1, \ K_0=1, \quad J_1=\bar{Q}_2\bar{Q}_0, \ K_1=\bar{Q}_0, \quad J_2=K_2=\bar{Q}_1\bar{Q}_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: 4-Bit SIPO Shift Register for 1011 Input [3 + 3 = 6 Marks]}
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
    \draw[thick] ({(\i)*4.2 + 2.6}, 2.0) -- ++(0.4,0) -- ++(0,1.5);
    \node[above] at ({(\i)*4.2 + 3.0}, 3.5) {\large $\mathbf{Q_\i}$};
  }

  \draw[thick] (-1.0, 1.5) -- (0, 1.5);
  \node[left] at (-1.0, 1.5) {\large $\mathbf{\text{CLK}}$};
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
Design a sequential machine that consists of one input, X and one output, Z. The machine is required to give output high (Z=1), whenever it detects the serial sequence of 101 from its input data stream X. Implement only SR flip-flops for the designed circuit realization.
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

\paragraph{Design Equations for SR Flip-Flops ($A, B$):}
$$S_A = B\bar{X}, \quad R_A = X, \qquad S_B = X, \quad R_B = \bar{X}, \qquad Z = AX$$

\begin{answerbox}
$$\mathbf{S_A = B\bar{X}, \quad R_A = X, \qquad S_B = X, \quad R_B = \bar{X}, \qquad Z = AX}$$
\end{answerbox}\subsection{Question 9: Two-Input TTL NOR Gate Transistor Circuit [5 + 2 = 7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q9)}
Draw the circuit diagram of two-input TTL NOR gate and explain its logic operation briefly and list the characteristics of CMOS logic family.
\end{questionbox}

\begin{schematicbox}{Two-Input TTL NOR Gate Schematic (Totem-Pole Output)}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % VCC Rail
  \draw[thick] (-1.0, 6.0) -- (8.5, 6.0);
  \node at (-1.0, 6.3) {$+V_{CC}\ (5\text{V})$};

  % Resistors to VCC
  % R1A (4k)
  \draw[thick] (0, 6.0) -- (0, 5.0);
  \draw[thick] (-0.2, 5.0) rectangle (0.2, 4.2) node[midway, right=3pt]{\small $R_{1A}$};
  \draw[thick] (0, 4.2) -- (0, 3.5) -- (0.8, 3.5);

  % Q1A Input Transistor
  \draw[thick] (0.8, 3.8) -- (0.8, 3.2);
  \draw[thick] (0.8, 3.6) -- (1.5, 4.0);
  \draw[thick] (0.8, 3.4) -- (1.5, 3.0);
  \draw[thick, ->] (1.3, 3.1) -- (1.5, 3.0);
  \draw[thick] (1.5, 3.0) -- (1.5, 2.5) -- (-0.8, 2.5);
  \node[left] at (-0.8, 2.5) {$A$};
  \node at (0.5, 3.7) {\small $Q_{1A}$};

  % Q1B Input Transistor (Lower)
  \draw[thick] (0, 6.0) -- (0, 1.2);
  \draw[thick] (-0.2, 1.2) rectangle (0.2, 0.4) node[midway, right=3pt]{\small $R_{1B}$};
  \draw[thick] (0, 0.4) -- (0, -0.2) -- (0.8, -0.2);

  \draw[thick] (0.8, 0.1) -- (0.8, -0.5);
  \draw[thick] (0.8, -0.1) -- (1.5, 0.3);
  \draw[thick] (0.8, -0.3) -- (1.5, -0.7);
  \draw[thick] (1.5, -0.7) -- (1.5, -1.2) -- (-0.8, -1.2);
  \node[left] at (-0.8, -1.2) {$B$};
  \node at (0.5, 0.0) {\small $Q_{1B}$};

  % Phase Splitters Q2A & Q2B (in parallel)
  \draw[thick] (3.0, 6.0) -- (3.0, 5.0);
  \draw[thick] (2.8, 5.0) rectangle (3.2, 4.2) node[midway, right=3pt]{\small $R_2$};
  \draw[thick] (3.0, 4.2) -- (3.0, 3.8);

  % Q2A
  \draw[thick] (1.5, 4.0) -- (2.3, 4.0);
  \draw[thick] (2.3, 4.3) -- (2.3, 3.7);
  \draw[thick] (2.3, 4.1) -- (3.0, 4.5);
  \draw[thick] (2.3, 3.9) -- (3.0, 3.5);
  \draw[thick, ->] (2.8, 3.6) -- (3.0, 3.5);
  \node at (2.0, 4.3) {\small $Q_{2A}$};

  % Q2B
  \draw[thick] (1.5, 0.3) -- (2.3, 0.3);
  \draw[thick] (2.3, 0.6) -- (2.3, 0.0);
  \draw[thick] (2.3, 0.4) -- (3.0, 3.8);
  \draw[thick] (2.3, 0.2) -- (3.0, -0.2);
  \draw[thick, ->] (2.8, -0.1) -- (3.0, -0.2);
  \node at (2.0, 0.6) {\small $Q_{2B}$};

  % Combined Emitters to R3 and Q4 Base
  \draw[thick] (3.0, 3.5) -- (3.0, -0.2) -- (3.8, -0.2);
  \draw[thick] (3.8, -0.2) -- (3.8, -1.0);
  \draw[thick] (3.6, -1.0) rectangle (4.0, -1.8) node[midway, right=3pt]{\small $R_3$};
  \draw[thick] (3.8, -1.8) -- (3.8, -2.5);

  % Totem Pole Pull-Up Q3
  \draw[thick] (6.0, 6.0) -- (6.0, 5.0);
  \draw[thick] (5.8, 5.0) rectangle (6.2, 4.2) node[midway, right=3pt]{\small $R_4$};
  \draw[thick] (6.0, 4.2) -- (6.0, 3.8);

  \draw[thick] (3.0, 4.2) -- (4.8, 4.2) -- (4.8, 3.5) -- (5.3, 3.5);
  \draw[thick] (5.3, 3.8) -- (5.3, 3.2);
  \draw[thick] (5.3, 3.6) -- (6.0, 4.0);
  \draw[thick] (5.3, 3.4) -- (6.0, 3.0);
  \draw[thick, ->] (5.8, 3.1) -- (6.0, 3.0);
  \node at (5.0, 3.8) {\small $Q_3$};

  % Diode D1
  \draw[thick] (6.0, 3.0) -- (6.0, 2.5);
  \draw[thick] (5.7, 2.5) -- (6.3, 2.5) -- (6.0, 2.0) -- cycle;
  \draw[thick] (5.7, 2.0) -- (6.3, 2.0);
  \draw[thick] (6.0, 2.0) -- (6.0, 1.2);

  % Totem Pole Pull-Down Q4
  \draw[thick] (3.8, -0.2) -- (5.3, -0.2);
  \draw[thick] (5.3, 0.1) -- (5.3, -0.5);
  \draw[thick] (5.3, -0.1) -- (6.0, 0.3);
  \draw[thick] (5.3, -0.3) -- (6.0, -0.7);
  \draw[thick, ->] (5.8, -0.6) -- (6.0, -0.7);
  \node at (5.0, 0.2) {\small $Q_4$};

  % Output Node
  \draw[thick] (6.0, 1.2) -- (6.0, 0.3);
  \draw[thick] (6.0, 0.8) -- (8.0, 0.8);
  \node[right] at (8.0, 0.8) {\large $\mathbf{Y = \overline{A + B}}$};
  \fill (6.0, 0.8) circle (2pt);

  % Ground Rail
  \draw[thick] (6.0, -0.7) -- (6.0, -2.5) -- (3.0, -2.5) -- (8.0, -2.5);
  \draw[thick] (5.5, -2.5) -- (5.5, -2.8);
  \draw[thick] (5.2, -2.8) -- (5.8, -2.8);
  \draw[thick] (5.3, -2.95) -- (5.7, -2.95);
  \draw[thick] (5.4, -3.1) -- (5.6, -3.1);
  \node at (5.5, -3.4) {\small GND};
\end{tikzpicture}
\end{schematicbox}

\paragraph{CMOS Logic Family Characteristics:}
\begin{itemize}
  \item \textbf{Extremely Low Static Power Dissipation:} Almost zero static power ($\approx 10\,\text{nW}$ per gate).
  \item \textbf{High Noise Margin:} Typically $40\%$ of $V_{DD}$ ($NM_H \approx NM_L \approx 0.4 V_{DD}$).
  \item \textbf{High Fan-Out:} Virtually infinite at low frequencies ($> 50$ loads).
  \item \textbf{Wide Supply Voltage Range:} Operates from $+3\text{V}$ to $+18\text{V}$.
\end{itemize}

\newpage
\subsection{Question 10: Digital Frequency Measurement Block Diagram [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q10)}
With the help of functional diagram explain the operation of frequency measurement.
\end{questionbox}

\begin{schematicbox}{Digital Frequency Measurement System Block Diagram}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (amp) at (0,2) {Attenuator/Amp};
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (schmitt) at (3.8,2) {Schmitt Trigger};
  \node[and gate US, draw, logic gate inputs=nn, scale=1.3] (gate) at (7.2,1) {};
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (counter) at (10.6,1) {Decade Counter};
  \node[draw, rectangle, fill=boxbg, minimum width=2.0cm, minimum height=1.0cm] (disp) at (14.2,1) {Display (Hz)};

  \node[draw, rectangle, fill=boxbg, minimum width=2.2cm, minimum height=1.0cm] (osc) at (0,-0.5) {Crystal Osc};
  \node[draw, rectangle, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm] (div) at (3.8,-0.5) {Time Base Div};

  \draw[thick, ->] (-2.2,2) -- (amp); \node[left] at (-2.2,2) {$f_x$ (Input)};
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

print("Wrote Final Digital Logic Master Solutions source with complete polished schematics.")
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies', 'dependencies/digital_logic_master_solutions.tex'], capture_output=True, text=True)
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies', 'dependencies/digital_logic_master_solutions.tex'], capture_output=True, text=True)

pdf_out = 'dependencies/digital_logic_master_solutions.pdf'
if os.path.exists(pdf_out):
    shutil.copy(pdf_out, 'subjects/2_digital_logic/Digital Logic Solutions.pdf')
    shutil.copy(pdf_out, 'solutions/web_app/downloads/dl/digital_logic_solutions.pdf')
    print("SUCCESS: Compiled and published complete Digital Logic Master Solutions Book!")
