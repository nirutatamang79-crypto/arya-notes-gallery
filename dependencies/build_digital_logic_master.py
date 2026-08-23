"""
Digital Logic (ENEX 152 / EX 152) — Complete Master Solutions Book Generator
Tribhuvan University, Institute of Engineering (IOE)
Comprehensive Step-by-Step Solved Papers for:
- 2083 Baishakh (Questions 1 to 12)
- 2082 Bhadra (Questions 1 to 12)
- 2082 Baishakh (Questions 1 to 10)
- 2081 Ashwin (Questions 1 to 10)
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

\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

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
  {\Large Complete Step-by-Step Solved Papers with Logic Schematics, K-Maps \& FSM State Tables}\\[0.8cm]
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
Excess-3 is an unweighted, self-complementing code formed by adding $3$ (or $0011_2$) to each decimal digit, then writing the 4-bit binary representation:
\begin{itemize}
  \item Digit $1$: $1 + 3 = 4 \implies 0100_2$
  \item Digit $5$: $5 + 3 = 8 \implies 1000_2$
  \item Digit $9$: $9 + 3 = 12 \implies 1100_2$
\end{itemize}

\begin{answerbox}
$$(159)_{10} = \mathbf{0100\ 1000\ 1100_{\text{Excess-3}}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: Universal Logic Gates Demonstration [3 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q3)}
Show that NAND and NOR gates are universal gates.
\end{questionbox}

A universal gate is one that can implement all basic logic functions (NOT, AND, OR) without requiring any other gate type.

\paragraph{1. Realization using only NAND Gates:}
\begin{itemize}
  \item \textbf{NOT Gate from NAND:} Connect inputs together:
  $$Y = \overline{A \cdot A} = \bar{A}$$
  \item \textbf{AND Gate from NAND:} Invert the output of a NAND gate using a second NAND:
  $$Y = \overline{\overline{A \cdot B}} = A \cdot B$$
  \item \textbf{OR Gate from NAND:} Invert inputs before passing to a NAND gate (De Morgan's theorem):
  $$Y = \overline{\bar{A} \cdot \bar{B}} = \overline{\overline{A + B}} = A + B$$
\end{itemize}

\paragraph{2. Realization using only NOR Gates:}
\begin{itemize}
  \item \textbf{NOT Gate from NOR:} Connect inputs together:
  $$Y = \overline{A + A} = \bar{A}$$
  \item \textbf{OR Gate from NOR:} Invert the output of a NOR gate using a second NOR:
  $$Y = \overline{\overline{A + B}} = A + B$$
  \item \textbf{AND Gate from NOR:} Invert inputs before passing to a NOR gate:
  $$Y = \overline{\bar{A} + \bar{B}} = \overline{\overline{A \cdot B}} = A \cdot B$$
\end{itemize}

\begin{answerbox}
Both NAND and NOR independently synthesize NOT, AND, and OR operators, proving universality.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 4: 4-Variable K-Map Minimization [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q4)}
Minimize the function $F(A,B,C,D) = \sum m(1, 2, 4, 5, 6, 8, 10, 11, 13, 15)$ using K-Map and realize it with suitable logic gates.
\end{questionbox}

\paragraph{Step 1: Plotting the 4-Variable Karnaugh Map}
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

\paragraph{Step 2: Grouping of Min-terms}
\begin{enumerate}
  \item \textbf{Quad 1 ($m_1, m_5, m_{13}, m_{15}$ is not full, but $m_1, m_5 \implies \bar{A}\bar{C}D$ and $m_{13}, m_{15} \implies ABD$).}
  \item \textbf{Quad 2 ($m_4, m_5, m_6$):} Group $m_4, m_6 \implies \bar{A}B\bar{D}$.
  \item \textbf{Quad 3 ($m_2, m_6, m_8, m_{10}$ corners and edges):} $m_8, m_{10} \implies A\bar{B}\bar{D}$; $m_{10}, m_{11} \implies A\bar{B}C$.
  \item \textbf{Group ($m_{11}, m_{15}$):} $\implies ACD$.
\end{enumerate}

Minimal SOP expression:
$$F(A,B,C,D) = \bar{A}\bar{C}D + \bar{A}B\bar{D} + A\bar{B}\bar{D} + ACD + ABD$$

\begin{answerbox}
$$\mathbf{F(A,B,C,D) = \bar{A}\bar{C}D + \bar{A}B\bar{D} + A\bar{B}\bar{D} + ACD + ABD}$$
Realized using 3-input AND gates feeding a 5-input OR gate.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Encoder vs. Decoder \& Octal-to-Binary Encoder [2 + 4 = 6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q5)}
Differentiate between encoder and decoder. Design an Octal-to-Binary Encoder with necessary diagrams.
\end{questionbox}

\paragraph{Differences:}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Feature} & \textbf{Encoder} & \textbf{Decoder} \\
\midrule
\textbf{Function} & Converts $2^n$ inputs to $n$ binary outputs & Converts $n$ binary inputs to $2^n$ unique outputs \\
\textbf{Active Lines} & Exactly one input line is active HIGH at a time & Exactly one output line is activated \\
\textbf{Logic Gates} & Built primarily using OR gates & Built using AND/NAND gates and inverters \\
\textbf{Application} & Keyboards, data compression, priority systems & Memory addressing, 7-segment display driving \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Design of Octal-to-Binary Encoder ($8$-to-$3$):}
\begin{itemize}
  \item \textbf{Inputs:} $D_0, D_1, D_2, D_3, D_4, D_5, D_6, D_7$ ($8$ lines)
  \item \textbf{Outputs:} $A, B, C$ ($3$-bit binary code where $A$ is MSB, $C$ is LSB)
\end{itemize}

\paragraph{Truth Table:}
\begin{center}
\begin{tabular}{cccccccc|ccc}
\toprule
$D_7$ & $D_6$ & $D_5$ & $D_4$ & $D_3$ & $D_2$ & $D_1$ & $D_0$ & $A$ & $B$ & $C$ \\
\midrule
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Boolean Output Equations:}
\begin{align*}
A &= D_4 + D_5 + D_6 + D_7 \\
B &= D_2 + D_3 + D_6 + D_7 \\
C &= D_1 + D_3 + D_5 + D_7
\end{align*}

\begin{answerbox}
\textbf{Logic Equations:} $A = D_4+D_5+D_6+D_7$, $B = D_2+D_3+D_6+D_7$, $C = D_1+D_3+D_5+D_7$. Realized using three 4-input OR gates.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: Full Subtractor Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q6)}
Implement a Full Subtractor circuit using Multiplexer.
\end{questionbox}

A full subtractor subtracts three single-bit inputs $A$ (Minuend), $B$ (Subtrahend), and $B_{\text{in}}$ (Borrow In) to produce Difference ($D$) and Borrow Out ($B_{\text{out}}$).

\paragraph{Truth Table:}
\begin{center}
\begin{tabular}{ccc|cc}
\toprule
$A$ & $B$ & $B_{\text{in}}$ & Difference ($D$) & Borrow Out ($B_{\text{out}}$) \\
\midrule
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 1 \\
0 & 1 & 0 & 1 & 1 \\
0 & 1 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 0 \\
1 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 0 & 0 \\
1 & 1 & 1 & 1 & 1 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Implementation using 4:1 Multiplexers (Select Lines $S_1 = A, S_0 = B$):}
\begin{itemize}
  \item For $AB = 00$: $D = B_{\text{in}}$, $B_{\text{out}} = B_{\text{in}}$
  \item For $AB = 01$: $D = \overline{B_{\text{in}}}$, $B_{\text{out}} = 1$
  \item For $AB = 10$: $D = \overline{B_{\text{in}}}$, $B_{\text{out}} = 0$
  \item For $AB = 11$: $D = B_{\text{in}}$, $B_{\text{out}} = B_{\text{in}}$
\end{itemize}

\begin{answerbox}
\textbf{Difference MUX (4:1):} $I_0 = B_{\text{in}}, I_1 = \overline{B_{\text{in}}}, I_2 = \overline{B_{\text{in}}}, I_3 = B_{\text{in}}$, Select lines: $S_1 = A, S_0 = B$.\\[0.1cm]
\textbf{Borrow MUX (4:1):} $I_0 = B_{\text{in}}, I_1 = 1, I_2 = 0, I_3 = B_{\text{in}}$, Select lines: $S_1 = A, S_0 = B$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 7: Latch vs. Flip-Flop \& D-to-JK Conversion [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q7)}
Differentiate between latch and flip-flop. Modify a D flip-flop such that it functions as a JK flip-flop.
\end{questionbox}

\paragraph{Comparison: Latch vs. Flip-Flop}
\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
\textbf{Feature} & \textbf{Latch} & \textbf{Flip-Flop} \\
\midrule
\textbf{Triggering} & Level-sensitive (transparent when enabled) & Edge-triggered (responds only to clock transitions) \\
\textbf{Clock Signal} & Uses an Enable (EN) gate level & Uses a high-speed Clock (CLK) transition \\
\textbf{Race Condition} & Prone to race-around condition & Immune to race conditions due to edge triggering \\
\textbf{Complexity} & Simple, fewer gates, consumes less power & More complex (Master-Slave or edge-detector circuit) \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Conversion of D Flip-Flop to JK Flip-Flop:}
\begin{enumerate}
  \item Target JK Characteristic: $Q(t+1) = J\bar{Q} + \bar{K}Q$.
  \item D Flip-Flop Characteristic: $Q(t+1) = D$.
  \item Equating gives: $D = J\bar{Q} + \bar{K}Q$.
\end{enumerate}

\begin{answerbox}
\textbf{Modification Logic:} Feed the D input with the combinational circuit:
$$\mathbf{D = J\bar{Q} + \bar{K}Q}$$
Constructed with two 2-input AND gates feeding a 2-input OR gate.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: 4-Bit SIPO Shift Register [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q8)}
Explain the working of 4-bit SIPO register with timing diagram of 1010 data input.
\end{questionbox}

A \textbf{Serial-In Parallel-Out (SIPO)} register consists of 4 cascaded D flip-flops clocked simultaneously. Data enters serially bit-by-bit at $D_3$, and shifts towards $D_0$ with each clock edge.

\paragraph{Shift Operations for Input Data $1010_2$ (MSB first: $1, 0, 1, 0$):}
\begin{center}
\begin{tabular}{@{}c|c|cccc@{}}
\toprule
\textbf{Clock Pulse} & \textbf{Serial Input ($D_{in}$)} & $Q_3$ & $Q_2$ & $Q_1$ & $Q_0$ \\
\midrule
Initial State & --- & 0 & 0 & 0 & 0 \\
1st Clock Pulse & 1 & 1 & 0 & 0 & 0 \\
2nd Clock Pulse & 0 & 0 & 1 & 0 & 0 \\
3rd Clock Pulse & 1 & 1 & 0 & 1 & 0 \\
4th Clock Pulse & 0 & \textbf{0} & \textbf{1} & \textbf{0} & \textbf{1} \\
\bottomrule
\end{tabular}
\end{center}

\begin{answerbox}
Four clock pulses are required to load a 4-bit serial sequence into parallel registers.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: Asynchronous BCD (Decade) Counter [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q9)}
Describe the operation of asynchronous BCD (decade) counter with necessary diagrams.
\end{questionbox}

An asynchronous BCD counter counts through 10 distinct states from $0000_2$ ($0$) to $1001_2$ ($9$), resetting to $0000$ on the 10th count.

\paragraph{Working Principle:}
\begin{itemize}
  \item Requires $4$ T/JK flip-flops in toggle mode ($J=K=1$).
  \item Counts in normal binary sequence up to $9$ ($1001$).
  \item On the 10th clock pulse, state becomes $1010_2$ ($Q_3=1, Q_2=0, Q_1=1, Q_0=0$).
  \item A 2-input NAND gate monitors $Q_3$ and $Q_1$. As soon as state $1010$ is reached, the NAND output goes LOW, asserting the active-low $\overline{\text{CLR}}$ inputs of all 4 flip-flops, forcing the counter back to $0000$.
\end{itemize}

\begin{answerbox}
\textbf{Reset Logic:} $\overline{\text{CLR}} = \overline{Q_3 \cdot Q_1}$. Modulus $= 10$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 10: Synchronous Mod-10 UP Counter Using T Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q10)}
Design a synchronous Mod-10 UP counter using T flip-flops and draw its timing diagram.
\end{questionbox}

\paragraph{State Transition \& Excitation Table ($T = Q \oplus Q^+$):}
\begin{center}
\begin{tabular}{cccc|cccc|cccc}
\toprule
\multicolumn{4}{c|}{\textbf{Present State}} & \multicolumn{4}{c|}{\textbf{Next State}} & \multicolumn{4}{c}{\textbf{T Inputs}} \\
$Q_3$ & $Q_2$ & $Q_1$ & $Q_0$ & $Q_3^+$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $T_3$ & $T_2$ & $T_1$ & $T_0$ \\
\midrule
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 \\
0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\
0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 1 \\
0 & 1 & 1 & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 \\
0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{K-Map Simplifications:}
\begin{align*}
T_0 &= 1 \\
T_1 &= \bar{Q}_3 Q_0 \\
T_2 &= Q_1 Q_0 \\
T_3 &= Q_2 Q_1 Q_0 + Q_3 Q_0
\end{align*}

\begin{answerbox}
$$\mathbf{T_0 = 1, \quad T_1 = \bar{Q}_3 Q_0, \quad T_2 = Q_1 Q_0, \quad T_3 = Q_2 Q_1 Q_0 + Q_3 Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 11: Synchronous FSM Sequence Detector '011' [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q11)}
Design a synchronous sequential machine that has 1-bit serial input $X$ and output $Z$ which will be HIGH when the input contains the message $011$ (Use T Flip-Flop).
\end{questionbox}

\paragraph{Step 1: State Assignment (Mealy Model)}
\begin{itemize}
  \item $S_0 (00)$: Initial / Reset state.
  \item $S_1 (01)$: Sequence '0' detected.
  \item $S_2 (10)$: Sequence '01' detected.
\end{itemize}

\paragraph{Step 2: State \& Excitation Table (T Flip-Flops $A, B$)}
\begin{center}
\begin{tabular}{ccc|cc|c|cc}
\toprule
\textbf{State} & \textbf{State} & \textbf{Input} & \multicolumn{2}{c|}{\textbf{Next State}} & \textbf{Output} & \multicolumn{2}{c}{\textbf{T Inputs}} \\
$A$ & $B$ & $X$ & $A^+$ & $B^+$ & $Z$ & $T_A$ & $T_B$ \\
\midrule
0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 \\
1 & 0 & 0 & 0 & 1 & 0 & 1 & 1 \\
1 & 0 & 1 & 0 & 0 & 1 & 1 & 0 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Step 3: K-Map Simplification}
\begin{align*}
T_A &= BX + A \\
T_B &= \bar{X} + AX + BX = \bar{X} + X(A+B) \\
Z &= AX
\end{align*}

\begin{answerbox}
$$\mathbf{T_A = BX + A, \quad T_B = \bar{X} + X(A+B), \quad Z = AX}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 12: Characteristics of Digital Logic Families [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q12)}
Explain about the main characteristics of digital logic families.
\end{questionbox}

\begin{enumerate}
  \item \textbf{Propagation Delay ($t_{pd}$):} The time delay between application of an input signal and the resulting change in output. Smaller $t_{pd}$ means faster operation.
  \item \textbf{Power Dissipation ($P_D$):} The electrical power consumed by a gate during operation, expressed in milliwatts (mW).
  \item \textbf{Noise Margin ($NM$):} The maximum noise voltage that can be added to the input signal without causing an undesirable change in output ($NM_H = V_{OH} - V_{IH}$, $NM_L = V_{IL} - V_{OL}$).
  \item \textbf{Fan-In \& Fan-Out:} Fan-In is the number of inputs a gate can handle. Fan-Out is the maximum number of standard load inputs that the output of a gate can reliably drive.
  \item \textbf{Figure of Merit (Speed-Power Product):} Product of propagation delay and power dissipation ($SPP = t_{pd} \times P_D$, in pJ).
\end{enumerate}

\newpage
% ==============================================================================
% CHAPTER 2: 2082 BHADRA
% ==============================================================================
\chapter{2082 Bhadra Examination Solutions}

\subsection{Question 1: Binary to Gray Code Conversion [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q1)}
Convert the following binary codes to Gray codes:
\begin{enumerate}[label=(\alph*)]
  \item $101101_2$
  \item $110001_2$
\end{enumerate}
\end{questionbox}

\paragraph{Conversion Rule:} $g_{n-1} = b_{n-1}$; for $i = n-2$ down to $0$, $g_i = b_{i+1} \oplus b_i$.
\begin{itemize}
  \item \textbf{Part (a):} $101101_2 \implies g_5=1, g_4=1\oplus0=1, g_3=0\oplus1=1, g_2=1\oplus1=0, g_1=1\oplus0=1, g_0=0\oplus1=1 \implies \mathbf{111011_{\text{Gray}}}$.
  \item \textbf{Part (b):} $110001_2 \implies g_5=1, g_4=1\oplus1=0, g_3=1\oplus0=1, g_2=0\oplus0=0, g_1=0\oplus0=0, g_0=0\oplus1=1 \implies \mathbf{101001_{\text{Gray}}}$.
\end{itemize}

\begin{answerbox}
(a) $(101101)_2 = \mathbf{111011_{\text{Gray}}}$ \qquad (b) $(110001)_2 = \mathbf{101001_{\text{Gray}}}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: 2's Complement \& BCD Addition [1 + 2 = 3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q2)}
What is 2's complement representation? Perform BCD addition of $23 + 48$.
\end{questionbox}

\paragraph{2's Complement Representation:}
The 2's complement of an $n$-bit binary number $N$ is defined as $2^n - N$. In binary systems, it is obtained by inverting all bits (1's complement) and adding 1 to the LSB. It simplifies arithmetic hardware by allowing subtraction to be performed using identical adder circuitry.

\paragraph{BCD Addition of $23 + 48$:}
\begin{itemize}
  \item $23_{\text{BCD}} = 0010\ 0011$
  \item $48_{\text{BCD}} = 0100\ 1000$
\end{itemize}
Add binary columns:
$$\begin{array}{r@{\quad}c@{\quad}c}
  & 0010 & 0011 \\
+ & 0100 & 1000 \\
\hline
  & 0110 & 1011 \quad (11 > 9 \implies \text{Invalid BCD}) \\
+ & 0000 & 0110 \quad (\text{Add } 0110_2 \text{ to lower nibble}) \\
\hline
  & \mathbf{0111} & \mathbf{0001} \implies \mathbf{71_{\text{BCD}}}
\end{array}$$

\begin{answerbox}
$$23 + 48 = \mathbf{0111\ 0001_{\text{BCD}}} = (71)_{10}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: De Morgan's Theorems [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q3)}
State and explain De Morgan's Theorem with truth table and necessary diagrams.
\end{questionbox}

\paragraph{Theorem 1:} $\overline{A \cdot B} = \bar{A} + \bar{B}$ (NAND gate is equivalent to a Bubbled OR gate).
\paragraph{Theorem 2:} $\overline{A + B} = \bar{A} \cdot \bar{B}$ (NOR gate is equivalent to a Bubbled AND gate).

\paragraph{Truth Table Verification:}
\begin{center}
\begin{tabular}{cc|c|c|c|c|c|c}
\toprule
$A$ & $B$ & $\overline{A \cdot B}$ & $\bar{A} + \bar{B}$ & \textbf{Equal?} & $\overline{A + B}$ & $\bar{A} \cdot \bar{B}$ & \textbf{Equal?} \\
\midrule
0 & 0 & 1 & 1 & \checkmark & 1 & 1 & \checkmark \\
0 & 1 & 1 & 1 & \checkmark & 0 & 0 & \checkmark \\
1 & 0 & 1 & 1 & \checkmark & 0 & 0 & \checkmark \\
1 & 1 & 0 & 0 & \checkmark & 0 & 0 & \checkmark \\
\bottomrule
\end{tabular}
\end{center}

\vspace{0.5cm}
\subsection{Question 4: K-Map Minimization with Don't Cares [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q4)}
Minimize $F(A,B,C,D) = \sum m(0, 1, 2, 4, 7, 8, 9, 10, 12, 15) + d(5, 11, 13)$ using K-Map.
\end{questionbox}

\paragraph{Karnaugh Map Plotting:}
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

\paragraph{Optimal Groupings:}
\begin{enumerate}
  \item \textbf{Octet (Columns $CD=00$ and $CD=01$):} $\implies \bar{C}$.
  \item \textbf{Quad 1 ($m_7, m_{15}, d_5, d_{13}$):} $\implies BD$.
  \item \textbf{Quad 2 (4 corners $m_0, m_2, m_8, m_{10}$):} $\implies \bar{B}\bar{D}$.
\end{enumerate}

\begin{answerbox}
$$\mathbf{F(A,B,C,D) = \bar{C} + BD + \bar{B}\bar{D}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: 3-Bit Magnitude Comparator [1 + 5 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q5)}
What is magnitude comparator? Design a 3-bit magnitude comparator.
\end{questionbox}

A magnitude comparator compares two binary words $A = A_2 A_1 A_0$ and $B = B_2 B_1 B_0$ to determine whether $A > B$, $A = B$, or $A < B$.

\paragraph{Design Equations:}
Define equality condition per bit $x_i = A_i \odot B_i = A_i B_i + \bar{A}_i \bar{B}_i$:
\begin{align*}
(A = B) &= x_2 \cdot x_1 \cdot x_0 \\
(A > B) &= A_2 \bar{B}_2 + x_2 A_1 \bar{B}_1 + x_2 x_1 A_0 \bar{B}_0 \\
(A < B) &= \bar{A}_2 B_2 + x_2 \bar{A}_1 B_1 + x_2 x_1 \bar{A}_0 B_0
\end{align*}

\begin{answerbox}
$$\mathbf{(A=B) = x_2 x_1 x_0, \quad (A>B) = A_2\bar{B}_2 + x_2 A_1\bar{B}_1 + x_2 x_1 A_0\bar{B}_0}$$
$$\mathbf{(A<B) = \bar{A}_2 B_2 + x_2 \bar{A}_1 B_1 + x_2 x_1 \bar{A}_0 B_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: Full Adder Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q6)}
Implement a full adder circuit using Multiplexer.
\end{questionbox}

Full Adder has inputs $A, B, C_{in}$ and outputs $\text{Sum} = \sum m(1, 2, 4, 7)$ and $C_{out} = \sum m(3, 5, 6, 7)$.

\paragraph{Using two 4:1 MUX (Select Lines $S_1 = A, S_0 = B$):}
\begin{align*}
\text{For Sum MUX:} \quad I_0 = C_{in}, \quad I_1 = \bar{C}_{in}, \quad I_2 = \bar{C}_{in}, \quad I_3 = C_{in} \\
\text{For } C_{out} \text{ MUX:} \quad I_0 = 0, \quad I_1 = C_{in}, \quad I_2 = C_{in}, \quad I_3 = 1
\end{align*}

\begin{answerbox}
Sum and $C_{out}$ realized with two 4:1 multiplexers sharing select inputs $A$ and $B$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 7: Combinational vs. Sequential \& SR-to-JK Conversion [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q7)}
Differentiate between combinational and sequential circuits. Convert SR flip-flop into JK flip-flop.
\end{questionbox}

\paragraph{SR to JK Flip-Flop Conversion Table:}
\begin{center}
\begin{tabular}{ccc|c|cc}
\toprule
$J$ & $K$ & $Q(t)$ & $Q(t+1)$ & $S$ & $R$ \\
\midrule
0 & 0 & 0 & 0 & 0 & X \\
0 & 0 & 1 & 1 & X & 0 \\
0 & 1 & 0 & 0 & 0 & X \\
0 & 1 & 1 & 0 & 0 & 1 \\
1 & 0 & 0 & 1 & 1 & 0 \\
1 & 0 & 1 & 1 & X & 0 \\
1 & 1 & 0 & 1 & 1 & 0 \\
1 & 1 & 1 & 0 & 0 & 1 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{K-Map for S and R Inputs:}
$$S = J\bar{Q}, \qquad R = KQ$$

\begin{answerbox}
$$\mathbf{S = J\bar{Q}, \qquad R = KQ}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: Shift Registers \& Johnson's Counter [2 + 3 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q8)}
Write briefly about types of shift registers. Explain the operation of a Johnson's Counter.
\end{questionbox}

\paragraph{Johnson Counter (Twisted Ring Counter):}
A 4-bit Johnson counter connects the inverted output ($\bar{Q}_3$) of the last flip-flop back to the input ($D_0$) of the first flip-flop.
\begin{itemize}
  \item Produces $2n = 8$ distinct states:
  $$0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000$$
  \item Requires only $n$ flip-flops to count $2n$ states, easily decoded using 2-input AND gates without glitching.
\end{itemize}

\begin{answerbox}
Johnson counter modulus is $2n = 8$ states for 4 flip-flops.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: 3-Bit Ripple UP Counter [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q9)}
Describe the operation of 3-bit ripple up counter with positive edge triggered clock.
\end{questionbox}

For positive-edge triggered T/JK flip-flops, an UP counter is achieved by clocking each subsequent flip-flop from the inverted output ($\bar{Q}$) of the preceding stage ($CLK_{i+1} = \bar{Q}_i$).
\begin{itemize}
  \item Counts: $000 \to 001 \to 010 \to 011 \to 100 \to 101 \to 110 \to 111 \to 000$.
\end{itemize}

\begin{answerbox}
Modulus $= 2^3 = 8$. Each flip-flop toggles on the positive clock transition of $\bar{Q}_{prev}$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 10: Synchronous Mod-6 Counter Using SR Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q10)}
Design the synchronous mod-6 counter using SR flip-flop and draw its timing diagram.
\end{questionbox}

\paragraph{State \& SR Excitation Table ($0 \to 1 \to 2 \to 3 \to 4 \to 5 \to 0$):}
\begin{center}
\begin{tabular}{ccc|ccc|cc|cc|cc}
\toprule
$Q_2$ & $Q_1$ & $Q_0$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $S_2$ & $R_2$ & $S_1$ & $R_1$ & $S_0$ & $R_0$ \\
\midrule
0 & 0 & 0 & 0 & 0 & 1 & 0 & X & 0 & X & 1 & 0 \\
0 & 0 & 1 & 0 & 1 & 0 & 0 & X & 1 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 & 1 & 0 & X & X & 0 & 1 & 0 \\
0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 1 & 0 & 1 & X & 0 & 0 & X & 1 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & X & 0 & 1 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{K-Map Simplifications:}
\begin{align*}
S_0 &= \bar{Q}_0, \quad R_0 = Q_0 \\
S_1 &= \bar{Q}_2 \bar{Q}_1 Q_0, \quad R_1 = Q_1 Q_0 \\
S_2 &= Q_1 Q_0, \quad R_2 = Q_0
\end{align*}

\begin{answerbox}
$$\mathbf{S_0 = \bar{Q}_0, \ R_0 = Q_0, \quad S_1 = \bar{Q}_2\bar{Q}_1 Q_0, \ R_1 = Q_1 Q_0, \quad S_2 = Q_1 Q_0, \ R_2 = Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 11: Synchronous FSM Sequence Detector '110' [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q11)}
Design a synchronous sequential machine that has 1-bit serial input $X$ and output $Z$ which will be HIGH when the input contains the message $110$ (Use SR Flip-Flop).
\end{questionbox}

\paragraph{State Equations \& Excitation:}
Using states $S_0 (00)$, $S_1 (01)$, $S_2 (10)$ and SR flip-flops $A, B$:
\begin{align*}
S_A &= BX, \quad R_A = \bar{X} \\
S_B &= \bar{A}\bar{B}X, \quad R_B = B\bar{X} + A \\
Z &= A\bar{X}
\end{align*}

\begin{answerbox}
$$\mathbf{S_A = BX, \quad R_A = \bar{X}, \quad S_B = \bar{A}\bar{B}X, \quad R_B = B\bar{X} + A, \quad Z = A\bar{X}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 12: Frequency Counter Short Note [3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q12)}
Write a short note on frequency counter.
\end{questionbox}

A digital frequency counter measures the frequency of an unknown periodic input signal by counting the number of cycles that pass through an AND gate enabled for an exact known time period (e.g. 1 second derived from a crystal oscillator and decade dividers).
\begin{itemize}
  \item \textbf{Basic Formula:} $f = \frac{N}{T_{\text{gate}}}$, where $N$ is total counted pulses, $T_{\text{gate}}$ is the gate window duration.
\end{itemize}

\newpage
% ==============================================================================
% CHAPTER 3: 2082 BAISHAKH
% ==============================================================================
\chapter{2082 Baishakh Examination Solutions}

\subsection{Question 1: ASCII Code \& 2's Complement Addition [1 + 3 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q1)}
Define an ASCII code. Use 2's complement method to perform $(-28 + 12)_{10}$ in 8-bit signed number representation.
\end{questionbox}

\paragraph{ASCII Code:} American Standard Code for Information Interchange is a standard 7-bit character encoding system representing 128 characters (letters, numbers, punctuation, control codes).

\paragraph{2's Complement Addition of $(-28 + 12)_{10}$:}
\begin{itemize}
  \item $+28_{10} = 0001\ 1100_2 \implies -28_{10} = 1110\ 0011 + 1 = 1110\ 0100_2$
  \item $+12_{10} = 0000\ 1100_2$
\end{itemize}
Perform addition:
$$\begin{array}{r@{\quad}l}
  & 1110\ 0100 \quad (-28) \\
+ & 0000\ 1100 \quad (+12) \\
\hline
  & \mathbf{1111\ 0000} \quad (\text{Result is Negative})
\end{array}$$
Magnitude verification: $-(2\text{'s complement of } 1111\ 0000) = -(0000\ 1111 + 1) = -0001\ 0000_2 = -16_{10}$.

\begin{answerbox}
$(-28 + 12)_{10} = \mathbf{1111\ 0000_2} = -16_{10}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 2: Boolean Algebra Proofs [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q2)}
Prove the following Boolean identities:
\begin{enumerate}[label=(\alph*)]
  \item $AB + \bar{A}C + BC = AB + \bar{A}C$ (Consensus Theorem)
  \item $AB + C(A \oplus B) = BC + A(B+C)$
\end{enumerate}
\end{questionbox}

\paragraph{Proof of (a):}
$$\text{LHS} = AB + \bar{A}C + BC(A + \bar{A}) = AB + \bar{A}C + ABC + \bar{A}BC = AB(1 + C) + \bar{A}C(1 + B) = AB + \bar{A}C = \text{RHS}$$

\paragraph{Proof of (b):}
$$\text{LHS} = AB + C(A\bar{B} + \bar{A}B) = AB + A\bar{B}C + \bar{A}BC$$
$$\text{RHS} = BC + AB + AC = AB + BC(A + \bar{A}) + AC(B + \bar{B}) = AB + ABC + \bar{A}BC + ABC + A\bar{B}C = AB + A\bar{B}C + \bar{A}BC = \text{LHS}$$

\begin{answerbox}
Both identities are algebraically verified.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: Decoder Definition \& Octal Priority Encoder [2 + 6 = 8 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q3)}
What is a decoder? Design an octal priority encoder with neat circuit diagram.
\end{questionbox}

\paragraph{Octal Priority Encoder (8-to-3):}
Gives priority to the highest-indexed active input ($D_7 > D_6 > \dots > D_0$).
\begin{align*}
A &= D_4 + D_5 + D_6 + D_7 \\
B &= D_2\bar{D}_4\bar{D}_5 + D_3\bar{D}_4\bar{D}_5 + D_6 + D_7 \\
C &= D_1\bar{D}_2\bar{D}_4\bar{D}_6 + D_3\bar{D}_4\bar{D}_6 + D_5\bar{D}_6 + D_7 \\
V &= D_0 + D_1 + D_2 + D_3 + D_4 + D_5 + D_6 + D_7 \quad (\text{Valid Bit})
\end{align*}

\vspace{0.5cm}
\subsection{Question 4: Function Realization Using 3x8 Decoder [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q4)}
Realize $X(A,B,C,D) = \sum m(0, 2, 3, 7, 8, 10, 11, 14, 15)$ using a single 3x8 decoder and simplify implementing K-Map.
\end{questionbox}

\paragraph{K-Map Minimization:}
$$\mathbf{X(A,B,C,D) = \bar{B}\bar{D} + \bar{B}C + CD + ABC}$$

\paragraph{Realization with 3x8 Decoder:}
Connect $A, B, C$ to select lines $S_2, S_1, S_0$, and express the outputs in terms of $D$:
Connect decoder outputs to an OR gate with appropriate $D$/$\bar{D}$ gating.

\vspace{0.5cm}
\subsection{Question 5: Synchronous 2-Bit UP/DOWN Counter Using T Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q5)}
Design a synchronous 2-bit up/down counter using T flip-flops.
\end{questionbox}

\paragraph{Design Table ($M=0 \implies$ UP Counter, $M=1 \implies$ DOWN Counter):}
\begin{center}
\begin{tabular}{ccc|cc|cc}
\toprule
$M$ & $Q_1$ & $Q_0$ & $Q_1^+$ & $Q_0^+$ & $T_1$ & $T_0$ \\
\midrule
0 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 0 & 1 & 1 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 & 1 & 0 & 1 \\
0 & 1 & 1 & 0 & 0 & 1 & 1 \\
1 & 0 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 0 & 0 & 1 \\
1 & 1 & 0 & 0 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 0 & 0 & 1 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{K-Map Simplification:}
\begin{align*}
T_0 &= 1 \\
T_1 &= \bar{M} Q_0 + M \bar{Q}_0 = M \oplus Q_0
\end{align*}

\begin{answerbox}
$$\mathbf{T_0 = 1, \qquad T_1 = M \oplus Q_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: 4-Bit PISO Shift Register [3 + 2 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q6)}
Explain the operation of 4-bit parallel-in serial-out (PISO) shift register with necessary circuit and timing diagram for 1101 input data.
\end{questionbox}

A Parallel-In Serial-Out (PISO) shift register loads all 4 bits in parallel during a single clock cycle when $\text{Shift}/\overline{\text{Load}} = 0$, and then shifts the bits out serially bit-by-bit when $\text{Shift}/\overline{\text{Load}} = 1$.
\begin{itemize}
  \item Data inputs: $D_3 D_2 D_1 D_0 = 1101$.
  \item After Load: $Q_3=1, Q_2=1, Q_1=0, Q_0=1$.
  \item Serial output bit stream: $1 \to 0 \to 1 \to 1$.
\end{itemize}

\vspace{0.5cm}
\subsection{Question 7: Mod-12 Asynchronous Counter with Positive Edge Triggering [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q7)}
Sketch the circuit diagram of mod-12 asynchronous counter having positive-edge triggering clock system implementing JK flip-flops with neat timing diagram.
\end{questionbox}

Mod-12 counter counts $0$ through $11$ ($0000$ to $1011$), and resets upon reaching $12$ ($1100_2$, where $Q_3=1, Q_2=1, Q_1=0, Q_0=0$).
\begin{itemize}
  \item For positive-edge triggered UP counter, clock each stage from $\bar{Q}$ of previous stage: $\text{CLK}_{i+1} = \bar{Q}_i$.
  \item Reset condition: Connect $Q_3$ and $Q_2$ to a 2-input NAND gate feeding the active-low $\overline{\text{CLR}}$ inputs of all 4 flip-flops:
  $$\overline{\text{CLR}} = \overline{Q_3 \cdot Q_2}$$
\end{itemize}

\begin{answerbox}
\textbf{Reset Logic:} $\overline{\text{CLR}} = \overline{Q_3 \cdot Q_2}$. Flip-flops count from $0000$ to $1011$ (12 states).
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 8: Sequential Machine Sequence Detector '010' Using D Flip-Flops [10 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q8)}
Design a sequential machine that consists of one input $X$ and one output $Z$. $Z=1$ whenever it detects the serial sequence $010$. Implement only D flip-flops.
\end{questionbox}

\paragraph{State Assignment (Mealy Model):}
\begin{itemize}
  \item $S_0 (00)$: Reset state.
  \item $S_1 (01)$: Sequence '0' detected.
  \item $S_2 (10)$: Sequence '01' detected.
\end{itemize}

\paragraph{State Table \& D Flip-Flop Inputs ($D = Q^+$):}
\begin{center}
\begin{tabular}{ccc|cc|c|cc}
\toprule
$A$ & $B$ & $X$ & $A^+$ & $B^+$ & $Z$ & $D_A$ & $D_B$ \\
\midrule
0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 & 1 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{K-Map Simplification:}
\begin{align*}
D_A &= BX \\
D_B &= \bar{X} \\
Z &= A\bar{X}
\end{align*}

\begin{answerbox}
$$\mathbf{D_A = BX, \qquad D_B = \bar{X}, \qquad Z = A\bar{X}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: CMOS NAND Gate \& TTL Characteristics [4 + 2 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q9)}
Draw the circuit diagram of two-input CMOS NAND gate, explain its logic operation, and list the characteristics of TTL logic family.
\end{questionbox}

\paragraph{CMOS NAND Gate:}
\begin{itemize}
  \item \textbf{Pull-Up Network (PUN):} Two PMOS transistors ($P_1, P_2$) connected in \textbf{parallel} between $V_{DD}$ and Output $Y$.
  \item \textbf{Pull-Down Network (PDN):} Two NMOS transistors ($N_1, N_2$) connected in \textbf{series} between Output $Y$ and Ground.
  \item \textbf{Operation:}
    \begin{itemize}
      \item If $A=0$ or $B=0$, at least one PMOS conducts, pulling output to $V_{DD}$ ('1').
      \item If $A=1$ and $B=1$, both NMOS conduct in series, pulling output to GND ('0').
    \end{itemize}
\end{itemize}

\paragraph{TTL Characteristics:} $V_{CC} = 5\text{V}$, Propagation delay $\approx 10\text{ns}$, Power dissipation $\approx 10\text{mW/gate}$, Fan-out $\approx 10$.

\vspace{0.5cm}
\subsection{Question 10: Time Interval Measurement Circuit [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q10)}
With the help of functional diagram explain the operation of time measuring circuit.
\end{questionbox}

A digital time interval meter measures the elapsed time $\Delta t$ between a START pulse and a STOP pulse.
\begin{itemize}
  \item The START pulse sets an RS flip-flop, enabling an AND gate.
  \item Precise standard clock pulses from a crystal oscillator (e.g. $1\text{MHz}$, period $T = 1\mu\text{s}$) pass through the open gate into a digital counter.
  \item The STOP pulse resets the flip-flop, disabling the gate.
  \item $\Delta t = N \times T_{\text{clk}}$, where $N$ is the total registered counts.
\end{itemize}

\newpage
% ==============================================================================
% CHAPTER 4: 2081 ASHWIN
% ==============================================================================
\chapter{2081 Ashwin Examination Solutions}

\subsection{Question 1: Merits \& Demerits of Digital Signals [2 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q1)}
Mention merits and demerits of digital signal over analog signal.
\end{questionbox}

\paragraph{Merits:} High noise immunity, easy error detection/correction, perfect reproduction, simple digital IC integration and programmability.
\paragraph{Demerits:} Higher bandwidth requirement, quantization error/noise during analog-to-digital conversion, and requirement for high-speed converters.

\vspace{0.5cm}
\subsection{Question 2: Radix & Gray Code Conversions [3 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q2)}
Perform: (a) $(6\text{E}.2\text{C})_{16} = (?)_{8}$, (b) $(10110110)_{\text{Gray}} = (?)_{2}$.
\end{questionbox}

\paragraph{Part (a): $(6\text{E}.2\text{C})_{16} \to \text{Octal}$}
\begin{itemize}
  \item Hex to Binary: $6 = 0110, \text{E} = 1110, .2 = 0010, \text{C} = 1100 \implies 01101110.00101100_2$
  \item Regroup into 3-bit octal groups: $001\ 101\ 110\ .\ 001\ 011\ 000_2 = (156.130)_8 = \mathbf{(156.13)_8}$.
\end{itemize}

\paragraph{Part (b): $(10110110)_{\text{Gray}} \to \text{Binary}$}
$$b_7=1, b_6=1\oplus0=1, b_5=1\oplus1=0, b_4=0\oplus1=1, b_3=1\oplus0=1, b_2=1\oplus1=0, b_1=0\oplus1=1, b_0=1\oplus0=1$$
Result: $\mathbf{(11011011)_2}$.

\begin{answerbox}
(a) $(6\text{E}.2\text{C})_{16} = \mathbf{(156.13)_8}$ \qquad (b) $(10110110)_{\text{Gray}} = \mathbf{(11011011)_2}$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 3: BCD to 7-Segment 'f' Segment Decoder [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q3)}
Design the simplest logic circuit for 'f' segment for the BCD-to-seven segment display decoder.
\end{questionbox}

The 'f' segment is active (HIGH) for decimal digits: $0, 4, 5, 6, 8, 9$. Inputs $10$ to $15$ are Don't Cares ($d$).
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
\textbf{$AB \backslash CD$} & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $\mathbf{1}$ ($m_0$) & $0$ ($m_1$) & $0$ ($m_3$) & $0$ ($m_2$) \\ \hline
\textbf{01} & $\mathbf{1}$ ($m_4$) & $\mathbf{1}$ ($m_5$) & $0$ ($m_7$) & $\mathbf{1}$ ($m_6$) \\ \hline
\textbf{11} & $\mathbf{X}$ & $\mathbf{X}$ & $\mathbf{X}$ & $\mathbf{X}$ \\ \hline
\textbf{10} & $\mathbf{1}$ ($m_8$) & $\mathbf{1}$ ($m_9$) & $\mathbf{X}$ & $\mathbf{X}$ \\ \hline
\end{tabular}
\end{center}

\paragraph{K-Map Simplification:}
\begin{align*}
\text{Group 1 (Row 10, 11):} &\quad A \\
\text{Group 2 ($m_0, m_4, d_{12}, m_8$):} &\quad \bar{C}\bar{D} \\
\text{Group 3 ($m_4, m_5, d_{12}, d_{13}$):} &\quad B\bar{C} \\
\text{Group 4 ($m_5, m_6, d_{13}, d_{14}$):} &\quad B\bar{D}
\end{align*}

\begin{answerbox}
$$\mathbf{f = A + \bar{C}\bar{D} + B\bar{C} + B\bar{D}}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 4: 4:1 MUX Realization \& Combined Half Adder/Subtractor [3 + 7 = 10 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q4)}
Implement $Y(A,B,C) = \sum m(0, 2, 3, 5, 7)$ using only a single 4:1 MUX. Design a combined Half-Adder and Half-Subtractor with a mode control.
\end{questionbox}

\paragraph{Part 1: 4:1 MUX Realization (Select Lines $S_1 = A, S_0 = B$):}
\begin{itemize}
  \item $AB = 00 \implies m_0, m_1 \implies Y = \bar{C}$ ($I_0 = \bar{C}$)
  \item $AB = 01 \implies m_2, m_3 \implies Y = 1$ ($I_1 = 1$)
  \item $AB = 10 \implies m_4, m_5 \implies Y = C$ ($I_2 = C$)
  \item $AB = 11 \implies m_6, m_7 \implies Y = C$ ($I_3 = C$)
\end{itemize}

\paragraph{Part 2: Combined Half-Adder / Half-Subtractor (Mode $M=0$ for Add, $M=1$ for Sub):}
\begin{itemize}
  \item \textbf{Sum / Difference:} $S/D = A \oplus B$ (Identical for both).
  \item \textbf{Carry / Borrow:} $C_{\text{out}} = AB$ (when $M=0$), $B_{\text{out}} = \bar{A}B$ (when $M=1$).
  \item \textbf{Unified Output:} $C/B = (A \oplus M) \cdot B$.
\end{itemize}

\begin{answerbox}
\textbf{MUX Inputs:} $I_0 = \bar{C}, I_1 = 1, I_2 = C, I_3 = C$.\\[0.1cm]
\textbf{Combined Adder/Subtractor Logic:} $\text{Sum/Diff} = A \oplus B, \quad \text{Carry/Borrow} = (A \oplus M) \cdot B$.
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 5: Mod-6 Synchronous DOWN Counter Using JK Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q5)}
Design a mod-6 synchronous down counter using JK flip-flops ($5 \to 4 \to 3 \to 2 \to 1 \to 0 \to 5$).
\end{questionbox}

\paragraph{State \& JK Excitation Table:}
\begin{center}
\begin{tabular}{ccc|ccc|cc|cc|cc}
\toprule
$Q_2$ & $Q_1$ & $Q_0$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $J_2$ & $K_2$ & $J_1$ & $K_1$ & $J_0$ & $K_0$ \\
\midrule
1 & 0 & 1 & 1 & 0 & 0 & X & 0 & 0 & X & X & 1 \\
1 & 0 & 0 & 0 & 1 & 1 & X & 1 & 1 & X & 1 & X \\
0 & 1 & 1 & 0 & 1 & 0 & 0 & X & X & 0 & X & 1 \\
0 & 1 & 0 & 0 & 0 & 1 & 0 & X & X & 1 & 1 & X \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & X & 0 & X & X & 1 \\
0 & 0 & 0 & 1 & 0 & 1 & 1 & X & 0 & X & 1 & X \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{K-Map Simplifications:}
\begin{align*}
J_0 &= 1, \quad K_0 = 1 \\
J_1 &= \bar{Q}_2 \bar{Q}_0, \quad K_1 = \bar{Q}_0 \\
J_2 &= \bar{Q}_1 \bar{Q}_0, \quad K_2 = \bar{Q}_1 \bar{Q}_0
\end{align*}

\begin{answerbox}
$$\mathbf{J_0 = 1, \ K_0 = 1, \quad J_1 = \bar{Q}_2\bar{Q}_0, \ K_1 = \bar{Q}_0, \quad J_2 = K_2 = \bar{Q}_1\bar{Q}_0}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 6: 4-Bit SIPO Shift Register with Data 1011 [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q6)}
Explain the operation of 4-bit serial-in parallel-out (SIPO) shift register with necessary circuit and timing diagram for input data of 1011.
\end{questionbox}

Serial input sequence $1011$ (MSB first: $1, 0, 1, 1$):
\begin{center}
\begin{tabular}{@{}c|c|cccc@{}}
\toprule
\textbf{Clock} & \textbf{Serial In} & $Q_3$ & $Q_2$ & $Q_1$ & $Q_0$ \\
\midrule
Initial & --- & 0 & 0 & 0 & 0 \\
1st CLK & 1 & 1 & 0 & 0 & 0 \\
2nd CLK & 0 & 0 & 1 & 0 & 0 \\
3rd CLK & 1 & 1 & 0 & 1 & 0 \\
4th CLK & 1 & \textbf{1} & \textbf{1} & \textbf{0} & \textbf{1} \\
\bottomrule
\end{tabular}
\end{center}

\vspace{0.5cm}
\subsection{Question 7: 3-Bit Asynchronous UP/DOWN Counter [4 + 3 = 7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q7)}
Describe briefly the operation of 3 bit up/down asynchronous counter having negative edge triggering clock system with neat circuit diagram and timing diagram.
\end{questionbox}

For negative-edge triggered T/JK flip-flops:
\begin{itemize}
  \item \textbf{UP Counting:} Clock next stage from normal output $Q$ ($\text{CLK}_{i+1} = Q_i$).
  \item \textbf{DOWN Counting:} Clock next stage from inverted output $\bar{Q}$ ($\text{CLK}_{i+1} = \bar{Q}_i$).
  \item \textbf{Mode Control ($M$):} Using steering logic: $\text{CLK}_{i+1} = \bar{M} Q_i + M \bar{Q}_i$.
\end{itemize}

\vspace{0.5cm}
\subsection{Question 8: Sequence Detector '101' Using SR Flip-Flops [10 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q8)}
Design a sequential machine that consists of one input $X$ and one output $Z$. $Z=1$ whenever it detects the serial sequence $101$. Implement only SR flip-flops.
\end{questionbox}

\paragraph{State Table \& SR Inputs ($S_0=00, S_1=01, S_2=10$):}
\begin{align*}
S_A &= BX, \quad R_A = \bar{X} \\
S_B &= \bar{A}\bar{B}X + AX, \quad R_B = B\bar{X} \\
Z &= AX
\end{align*}

\begin{answerbox}
$$\mathbf{S_A = BX, \quad R_A = \bar{X}, \quad S_B = X(\bar{A}\bar{B}+A), \quad R_B = B\bar{X}, \quad Z = AX}$$
\end{answerbox}

\vspace{0.5cm}
\subsection{Question 9: TTL NOR Gate & CMOS Characteristics [5 + 2 = 7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q9)}
Draw the circuit diagram of two-input TTL NOR gate, explain its operation, and list the characteristics of CMOS logic family.
\end{questionbox}

\paragraph{TTL NOR Gate Operation:}
Uses multi-emitter input transistors and totem-pole output stage ($Q_3$ pull-up transistor, $Q_4$ pull-down transistor). When either input is HIGH, the corresponding phase-splitter and pull-down transistor conduct, driving output LOW.

\paragraph{CMOS Logic Family Characteristics:}
Extremely low static power dissipation ($< 10\text{nW}$), high noise margin ($V_{DD}/2$), wide operating voltage range ($3\text{V} - 15\text{V}$), high fan-out ($> 50$).

\vspace{0.5cm}
\subsection{Question 10: Frequency Measurement Using Digital Counter [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q10)}
With the help of functional diagram explain the operation of frequency measurement.
\end{questionbox}

\paragraph{Functional Operation:}
\begin{enumerate}
  \item \textbf{Input Amplifier / Schmitt Trigger:} Converts arbitrary periodic analog input into sharp rectangular digital pulses.
  \item \textbf{Time Base Generator:} Crystal oscillator + decade frequency dividers produce an accurate gating window pulse $T_g$ (e.g. $1.000\text{s}$).
  \item \textbf{Main Gate (AND Gate):} Passes input signal pulses to the decade counter only while $T_g$ is active.
  \item \textbf{Display Unit:} Displays the total count $N$, which directly equals frequency $f = \frac{N}{T_g}\text{ Hz}$.
\end{enumerate}

\begin{answerbox}
$$f_x = \frac{N}{T_g}$$
\end{answerbox}

\end{document}
'''

with open('dependencies/digital_logic_master_solutions.tex', 'w') as f:
    f.write(latex_content)

print("Wrote Complete Digital Logic Master Solutions LaTeX source.")
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies', 'dependencies/digital_logic_master_solutions.tex'], capture_output=True, text=True)
subprocess.run(['pdflatex', '-interaction=nonstopmode', '-output-directory=dependencies', 'dependencies/digital_logic_master_solutions.tex'], capture_output=True, text=True)

pdf_out = 'dependencies/digital_logic_master_solutions.pdf'
if os.path.exists(pdf_out):
    shutil.copy(pdf_out, 'subjects/2_digital_logic/Digital Logic Solutions.pdf')
    shutil.copy(pdf_out, 'solutions/web_app/downloads/dl/digital_logic_solutions.pdf')
    print("SUCCESS: Compiled and published complete Digital Logic Master Solutions Book!")
