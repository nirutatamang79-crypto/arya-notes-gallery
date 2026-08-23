# dl_ch1_2083_baishakh.py
# Chapter 1: 2083 Baishakh Examination Master Solutions

def get_chapter_2083_baishakh():
    return r"""
\chapter{2083 Baishakh Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BCT, BEI & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Digital Logic (ENEX 152) & \textbf{Examination Type:} Regular \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: Gray Code to Binary Conversion [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q1)}
Convert the following gray codes to binary codes:
\begin{enumerate}[label=(\alph*)]
  \item $(10011)_{\text{Gray}}$
  \item $(110001)_{\text{Gray}}$
\end{enumerate}
\end{questionbox}

\paragraph{Conversion Principle and Algorithm:}
Let an $n$-bit Gray code word be $G = g_{n-1} g_{n-2} \dots g_1 g_0$ and the corresponding binary code word be $B = b_{n-1} b_{n-2} \dots b_1 b_0$.
\begin{enumerate}
  \item The Most Significant Bit (MSB) of the binary code is identical to the MSB of the Gray code:
  \[
  b_{n-1} = g_{n-1}
  \]
  \item Each subsequent binary bit $b_i$ (for $i = n-2$ down to $0$) is obtained by XORing the previously determined binary bit $b_{i+1}$ with the current Gray code bit $g_i$:
  \[
  b_i = b_{i+1} \oplus g_i \quad \text{for } i = n-2, n-3, \dots, 0
  \]
\end{enumerate}

\paragraph{Part (a): Conversion of $(10011)_{\text{Gray}}$ ($5$-bit code)}
Given $g_4 g_3 g_2 g_1 g_0 = 10011_2$:
\begin{itemize}
  \item $b_4 = g_4 = 1$
  \item $b_3 = b_4 \oplus g_3 = 1 \oplus 0 = 1$
  \item $b_2 = b_3 \oplus g_2 = 1 \oplus 0 = 1$
  \item $b_1 = b_2 \oplus g_1 = 1 \oplus 1 = 0$
  \item $b_0 = b_1 \oplus g_0 = 0 \oplus 1 = 1$
\end{itemize}
Thus, $(10011)_{\text{Gray}} = (11101)_2$.

\paragraph{Part (b): Conversion of $(110001)_{\text{Gray}}$ ($6$-bit code)}
Given $g_5 g_4 g_3 g_2 g_1 g_0 = 110001_2$:
\begin{itemize}
  \item $b_5 = g_5 = 1$
  \item $b_4 = b_5 \oplus g_4 = 1 \oplus 1 = 0$
  \item $b_3 = b_4 \oplus g_3 = 0 \oplus 0 = 0$
  \item $b_2 = b_3 \oplus g_2 = 0 \oplus 0 = 0$
  \item $b_1 = b_2 \oplus g_1 = 0 \oplus 0 = 0$
  \item $b_0 = b_1 \oplus g_0 = 0 \oplus 1 = 1$
\end{itemize}
Thus, $(110001)_{\text{Gray}} = (100001)_2$.

\begin{answerbox}
\begin{align*}
\text{(a)}\quad (10011)_{\text{Gray}} &= \mathbf{(11101)_2} = (29)_{10} \\
\text{(b)}\quad (110001)_{\text{Gray}} &= \mathbf{(100001)_2} = (33)_{10}
\end{align*}
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: Analog vs. Digital Signals \& Excess-3 Code [1 + 2 = 3 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q2)}
Differentiate between analog and digital signal. Convert $(159)_{10}$ to excess-3 code.
\end{questionbox}

\paragraph{Part (a): Comparison between Analog and Digital Signals [1 Mark]}
\begin{center}
\small
\begin{tabular}{@{}p{3.2cm}p{6.8cm}p{6.8cm}@{}}
\toprule
\textbf{Parameter} & \textbf{Analog Signal} & \textbf{Digital Signal} \\
\midrule
\textbf{Definition} & Continuous in both time and amplitude over a continuous range. & Discrete in time and quantized into distinct binary logic levels (`0' and `1'). \\
\textbf{Information Representation} & Expressed as continuous physical variations (voltage, current, pressure). & Expressed as discrete binary words / pulses. \\
\textbf{Noise Immunity} & Low; noise and distortion add directly to the signal and accumulate. & High; noise margins allow threshold regeneration via digital buffers without degradation. \\
\textbf{Storage \& Processing} & Bulky magnetic tape, analog filters; prone to aging and drift. & Stored compactly in semiconductor memory / disk; easily processed by microprocessors and DSPs. \\
\textbf{Error Correction} & Extremely difficult to detect and correct transmission errors. & Error detection and correction codes (Parity, CRC, Hamming codes) easily implemented. \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Part (b): Conversion of $(159)_{10}$ to Excess-3 Code [2 Marks]}
The \textbf{Excess-3 (XS-3)} code is an unweighted, self-complementing binary-coded decimal code. To convert a decimal number to Excess-3:
\begin{enumerate}
  \item Add $3$ ($0011_2$) to each decimal digit individually.
  \item Convert each resulting sum ($0$ to $12$) into its $4$-bit binary representation.
\end{enumerate}
For $(159)_{10}$:
\begin{itemize}
  \item \textbf{Hundreds digit ($1$):} $1 + 3 = 4 \implies 0100_2$
  \item \textbf{Tens digit ($5$):} $5 + 3 = 8 \implies 1000_2$
  \item \textbf{Units digit ($9$):} $9 + 3 = 12 \implies 1100_2$
\end{itemize}

\begin{answerbox}
$$(159)_{10} = \mathbf{(0100\ 1000\ 1100)_{\text{Excess-3}}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: Universal Logic Gates Schematics [3 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q3)}
Show that NAND and NOR gates are universal gates.
\end{questionbox}

A logic gate is termed \textbf{universal} if any arbitrary Boolean function (or the complete set of primitive logic operations $\{\text{NOT}, \text{AND}, \text{OR}\}$) can be synthesized solely using that gate type without requiring any additional gates.

\paragraph{1. Realization of Basic Gates Using NAND Gates Only:}
\begin{itemize}
  \item \textbf{NOT Gate:} Tie both inputs together: $Y = \overline{A \cdot A} = \bar{A}$.
  \item \textbf{AND Gate:} A NAND gate followed by a NAND-inverter: $Y = \overline{\overline{A \cdot B}} = A \cdot B$.
  \item \textbf{OR Gate:} By De Morgan's Law, $A + B = \overline{\bar{A} \cdot \bar{B}}$. Invert $A$ and $B$ with NAND inverters, then apply to a NAND gate: $Y = \overline{\bar{A} \cdot \bar{B}} = A + B$.
\end{itemize}

\begin{schematicbox}{Basic Logic Gates Synthesized from NAND Gates}
\centering
\begin{tikzpicture}[scale=0.78, transform shape]
  % (a) NOT from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (n1) at (1.8, 0) {};
  \draw[thick] (0.2, 0) -- (0.8, 0) node[left, at start] {$A$};
  \draw[thick] (0.8, 0) |- (n1.input 1);
  \draw[thick] (0.8, 0) |- (n1.input 2);
  \draw[thick] (n1.output) -- ++(0.6, 0) node[right, xshift=1mm] {$Y = \bar{A}$};
  \node[below=0.7cm of n1] {\small \textbf{(a) NOT Gate}};

  % (b) AND from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (n2) at (6.8, 0) {};
  \node[nand gate US, draw, logic gate inputs=nn] (n3) at (9.2, 0) {};
  \draw[thick] (5.2, 0.25) -- (n2.input 1) node[left, at start] {$A$};
  \draw[thick] (5.2, -0.25) -- (n2.input 2) node[left, at start] {$B$};
  \draw[thick] (n2.output) -- (8.2, 0);
  \draw[thick] (8.2, 0) |- (n3.input 1);
  \draw[thick] (8.2, 0) |- (n3.input 2);
  \draw[thick] (n3.output) -- ++(0.6, 0) node[right, xshift=1mm] {$Y = A \cdot B$};
  \node[below=0.7cm of n2, xshift=1.2cm] {\small \textbf{(b) AND Gate}};

  % (c) OR from NAND
  \node[nand gate US, draw, logic gate inputs=nn] (n4) at (13.8, 0.9) {};
  \node[nand gate US, draw, logic gate inputs=nn] (n5) at (13.8, -0.9) {};
  \node[nand gate US, draw, logic gate inputs=nn] (n6) at (16.5, 0) {};
  \draw[thick] (12.4, 0.9) -- (12.9, 0.9) node[left, at start] {$A$};
  \draw[thick] (12.9, 0.9) |- (n4.input 1); \draw[thick] (12.9, 0.9) |- (n4.input 2);
  \draw[thick] (12.4, -0.9) -- (12.9, -0.9) node[left, at start] {$B$};
  \draw[thick] (12.9, -0.9) |- (n5.input 1); \draw[thick] (12.9, -0.9) |- (n5.input 2);
  \draw[thick] (n4.output) -- ++(0.5, 0) |- (n6.input 1);
  \draw[thick] (n5.output) -- ++(0.5, 0) |- (n6.input 2);
  \draw[thick] (n6.output) -- ++(0.6, 0) node[right, xshift=1mm] {$Y = A + B$};
  \node[below=1.6cm of n6] {\small \textbf{(c) OR Gate}};
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. Realization of Basic Gates Using NOR Gates Only:}
\begin{itemize}
  \item \textbf{NOT Gate:} Tie both inputs together: $Y = \overline{A + A} = \bar{A}$.
  \item \textbf{OR Gate:} A NOR gate followed by a NOR-inverter: $Y = \overline{\overline{A + B}} = A + B$.
  \item \textbf{AND Gate:} By De Morgan's Law, $A \cdot B = \overline{\bar{A} + \bar{B}}$. Invert $A$ and $B$ with NOR inverters, then apply to a NOR gate: $Y = \overline{\bar{A} + \bar{B}} = A \cdot B$.
\end{itemize}

\begin{schematicbox}{Basic Logic Gates Synthesized from NOR Gates}
\centering
\begin{tikzpicture}[scale=0.78, transform shape]
  % (a) NOT from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (r1) at (1.8, 0) {};
  \draw[thick] (0.2, 0) -- (0.8, 0) node[left, at start] {$A$};
  \draw[thick] (0.8, 0) |- (r1.input 1);
  \draw[thick] (0.8, 0) |- (r1.input 2);
  \draw[thick] (r1.output) -- ++(0.6, 0) node[right, xshift=1mm] {$Y = \bar{A}$};
  \node[below=0.7cm of r1] {\small \textbf{(a) NOT Gate}};

  % (b) OR from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (r2) at (6.8, 0) {};
  \node[nor gate US, draw, logic gate inputs=nn] (r3) at (9.2, 0) {};
  \draw[thick] (5.2, 0.25) -- (r2.input 1) node[left, at start] {$A$};
  \draw[thick] (5.2, -0.25) -- (r2.input 2) node[left, at start] {$B$};
  \draw[thick] (r2.output) -- (8.2, 0);
  \draw[thick] (8.2, 0) |- (r3.input 1);
  \draw[thick] (8.2, 0) |- (r3.input 2);
  \draw[thick] (r3.output) -- ++(0.6, 0) node[right, xshift=1mm] {$Y = A + B$};
  \node[below=0.7cm of r2, xshift=1.2cm] {\small \textbf{(b) OR Gate}};

  % (c) AND from NOR
  \node[nor gate US, draw, logic gate inputs=nn] (r4) at (13.8, 0.9) {};
  \node[nor gate US, draw, logic gate inputs=nn] (r5) at (13.8, -0.9) {};
  \node[nor gate US, draw, logic gate inputs=nn] (r6) at (16.5, 0) {};
  \draw[thick] (12.4, 0.9) -- (12.9, 0.9) node[left, at start] {$A$};
  \draw[thick] (12.9, 0.9) |- (r4.input 1); \draw[thick] (12.9, 0.9) |- (r4.input 2);
  \draw[thick] (12.4, -0.9) -- (12.9, -0.9) node[left, at start] {$B$};
  \draw[thick] (12.9, -0.9) |- (r5.input 1); \draw[thick] (12.9, -0.9) |- (r5.input 2);
  \draw[thick] (r4.output) -- ++(0.5, 0) |- (r6.input 1);
  \draw[thick] (r5.output) -- ++(0.5, 0) |- (r6.input 2);
  \draw[thick] (r6.output) -- ++(0.6, 0) node[right, xshift=1mm] {$Y = A \cdot B$};
  \node[below=1.6cm of r6] {\small \textbf{(c) AND Gate}};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Since both NAND and NOR gates can independently synthesize the complete set of Boolean operators $\{\text{NOT}, \text{AND}, \text{OR}\}$, they are universally complete logic gates.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: 4-Variable K-Map Minimization \& Circuit [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q4)}
Minimize the function $F(A, B, C, D) = \sum m(1, 2, 4, 5, 6, 8, 10, 11, 13, 15)$ using K-Map and realize it with suitable logic gates.
\end{questionbox}

\paragraph{1. Karnaugh Map Plotting (4-Variable K-Map):}
The given minterms are plotted into the $4 \times 4$ Gray-coded map:
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
$AB \ \backslash \ CD$ & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $0\ (m_0)$ & $\mathbf{1}\ (m_1)$ & $0\ (m_3)$ & $\mathbf{1}\ (m_2)$ \\ \hline
\textbf{01} & $\mathbf{1}\ (m_4)$ & $\mathbf{1}\ (m_5)$ & $0\ (m_7)$ & $\mathbf{1}\ (m_6)$ \\ \hline
\textbf{11} & $0\ (m_{12})$ & $\mathbf{1}\ (m_{13})$ & $\mathbf{1}\ (m_{15})$ & $0\ (m_{14})$ \\ \hline
\textbf{10} & $\mathbf{1}\ (m_8)$ & $0\ (m_9)$ & $\mathbf{1}\ (m_{11})$ & $\mathbf{1}\ (m_{10})$ \\ \hline
\end{tabular}
\end{center}

\paragraph{2. Systematic Grouping (Prime Implicants):}
\begin{enumerate}
  \item \textbf{Group 1 (Quad in column 01):} Minterms $(m_1, m_5, m_{13}, m_{15}) \implies \mathbf{\bar{C}D}$.
  \item \textbf{Group 2 (Pair in row 01):} Minterms $(m_4, m_6) \implies \mathbf{\bar{A}B\bar{D}}$.
  \item \textbf{Group 3 (Pair in column 10):} Minterms $(m_2, m_6) \implies \mathbf{\bar{A}C\bar{D}}$.
  \item \textbf{Group 4 (Pair in row 10):} Minterms $(m_8, m_{10}) \implies \mathbf{A\bar{B}\bar{D}}$.
  \item \textbf{Group 5 (Pair in column 11):} Minterms $(m_{11}, m_{15}) \implies \mathbf{ACD}$.
  \item \textbf{Group 6 (Pair in row 11):} Minterms $(m_{13}, m_{15}) \implies \mathbf{ABD}$.
\end{enumerate}
The minimal Sum of Products (SOP) expression is:
\[
F(A,B,C,D) = \bar{A}\bar{C}D + \bar{A}B\bar{D} + \bar{A}C\bar{D} + A\bar{B}\bar{D} + ACD + ABD
\]

\begin{schematicbox}{Two-Level AND-OR Logic Realization for Minimized $F(A,B,C,D)$}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % 6 AND Gates
  \foreach \i/\label/\inA/\inB/\inC in {
    1/{$\bar{A}\bar{C}D$}/$\bar{A}$/$\bar{C}$/$D$,
    2/{$\bar{A}B\bar{D}$}/$\bar{A}$/$B$/$\bar{D}$,
    3/{$\bar{A}C\bar{D}$}/$\bar{A}$/$C$/$\bar{D}$,
    4/{\smash{$A\bar{B}\bar{D}$}}/$A$/$\bar{B}$/$\bar{D}$,
    5/{$ACD$}/$A$/$C$/$D$,
    6/{$ABD$}/$A$/$B$/$D$
  } {
    \node[and gate US, draw, logic gate inputs=nnn] (and\i) at (4, {4.5 - (\i - 1)*1.5}) {};
    \draw[thick] (1.8, {4.5 - (\i - 1)*1.5 + 0.3}) node[left] {\small \inA} -- (and\i.input 1);
    \draw[thick] (1.8, {4.5 - (\i - 1)*1.5}) node[left] {\small \inB} -- (and\i.input 2);
    \draw[thick] (1.8, {4.5 - (\i - 1)*1.5 - 0.3}) node[left] {\small \inC} -- (and\i.input 3);
  }

  % 6-input OR Gate
  \node[or gate US, draw, logic gate inputs=nnnnnn, scale=1.4] (orgate) at (10, 0.75) {};
  
  \draw[thick] (and1.output) -- ++(1.5, 0) |- (orgate.input 1);
  \draw[thick] (and2.output) -- ++(1.1, 0) |- (orgate.input 2);
  \draw[thick] (and3.output) -- ++(0.7, 0) |- (orgate.input 3);
  \draw[thick] (and4.output) -- ++(0.7, 0) |- (orgate.input 4);
  \draw[thick] (and5.output) -- ++(1.1, 0) |- (orgate.input 5);
  \draw[thick] (and6.output) -- ++(1.5, 0) |- (orgate.input 6);
  
  \draw[thick] (orgate.output) -- ++(1.2, 0) node[right] {\large $\mathbf{F}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{F(A,B,C,D) = \bar{A}\bar{C}D + \bar{A}B\bar{D} + \bar{A}C\bar{D} + A\bar{B}\bar{D} + ACD + ABD}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: Octal-to-Binary Encoder Logic Circuit [2 + 4 = 6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q5)}
Differentiate between encoder and decoder. Design an octal-to-binary encoder with necessary diagrams.
\end{questionbox}

\paragraph{Part (a): Comparison between Encoder and Decoder [2 Marks]}
\begin{center}
\small
\begin{tabular}{@{}p{3.2cm}p{6.8cm}p{6.8cm}@{}}
\toprule
\textbf{Feature} & \textbf{Encoder} & \textbf{Decoder} \\
\midrule
\textbf{Functional Operation} & Converts $2^n$ (or fewer) input active lines into an $n$-bit coded binary output. & Converts an $n$-bit coded binary input into $2^n$ unique active output lines. \\
\textbf{Inputs / Outputs} & $2^n$ input lines, $n$ output lines. & $n$ input lines, $2^n$ output lines. \\
\textbf{Internal Logic Gate} & Constructed using \textbf{OR} gates. & Constructed using \textbf{AND} / \textbf{NAND} gates. \\
\textbf{Typical Applications} & Keyboards, priority encoders, Flash Analog-to-Digital Converters (ADCs). & Memory address decoding, 7-segment display drivers, demultiplexers. \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Part (b): Design of Octal-to-Binary Encoder (8-to-3 Encoder) [4 Marks]}
An octal-to-binary encoder accepts 8 active-high input lines $D_0, D_1, \dots, D_7$ (where exactly one input is HIGH at any instant) and produces a 3-bit binary equivalent $A, B, C$ ($A$ is MSB, $C$ is LSB).

\paragraph{Truth Table:}
\begin{center}
\begin{tabular}{|cccccccc||ccc|}
\hline
$D_7$ & $D_6$ & $D_5$ & $D_4$ & $D_3$ & $D_2$ & $D_1$ & $D_0$ & $\mathbf{A\ (MSB)}$ & $\mathbf{B}$ & $\mathbf{C\ (LSB)}$ \\ \hline
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
Output bits are HIGH whenever any input corresponding to that binary position is active:
\begin{align*}
A &= D_4 + D_5 + D_6 + D_7 \\
B &= D_2 + D_3 + D_6 + D_7 \\
C &= D_1 + D_3 + D_5 + D_7
\end{align*}
(Note: $D_0$ is not required in the equations since $A=B=C=0$ when $D_0=1$.)

\begin{schematicbox}{Octal-to-Binary (8-to-3) Encoder Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Vertical input lines D0 to D7
  \foreach \i in {0,1,...,7} {
    \draw[thick] ({1.2*\i}, 5.5) -- ({1.2*\i}, 0.5);
    \node[above] at ({1.2*\i}, 5.5) {$\mathbf{D_\i}$};
  }

  % Horizontal OR gates on the right
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.1] (orA) at (12.0, 4.2) {};
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.1] (orB) at (12.0, 2.7) {};
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.1] (orC) at (12.0, 1.2) {};

  % Output lines
  \draw[thick] (orA.output) -- ++(1.0, 0) node[right] {\large $\mathbf{A\ (MSB)}$};
  \draw[thick] (orB.output) -- ++(1.0, 0) node[right] {\large $\mathbf{B}$};
  \draw[thick] (orC.output) -- ++(1.0, 0) node[right] {\large $\mathbf{C\ (LSB)}$};

  % Wiring for OR A: D4, D5, D6, D7
  \filldraw[black] ({1.2*4}, 4.5) circle (2pt); \draw[thick] ({1.2*4}, 4.5) -- ++(1.0, 0) |- (orA.input 4);
  \filldraw[black] ({1.2*5}, 4.3) circle (2pt); \draw[thick] ({1.2*5}, 4.3) -- ++(0.5, 0) |- (orA.input 3);
  \filldraw[black] ({1.2*6}, 4.1) circle (2pt); \draw[thick] ({1.2*6}, 4.1) -- ++(0.5, 0) |- (orA.input 2);
  \filldraw[black] ({1.2*7}, 3.9) circle (2pt); \draw[thick] ({1.2*7}, 3.9) -- ++(0.5, 0) |- (orA.input 1);

  % Wiring for OR B: D2, D3, D6, D7
  \filldraw[black] ({1.2*2}, 3.0) circle (2pt); \draw[thick] ({1.2*2}, 3.0) -- ++(1.0, 0) |- (orB.input 4);
  \filldraw[black] ({1.2*3}, 2.8) circle (2pt); \draw[thick] ({1.2*3}, 2.8) -- ++(0.5, 0) |- (orB.input 3);
  \filldraw[black] ({1.2*6}, 2.6) circle (2pt); \draw[thick] ({1.2*6}, 2.6) -- ++(0.5, 0) |- (orB.input 2);
  \filldraw[black] ({1.2*7}, 2.4) circle (2pt); \draw[thick] ({1.2*7}, 2.4) -- ++(0.5, 0) |- (orB.input 1);

  % Wiring for OR C: D1, D3, D5, D7
  \filldraw[black] ({1.2*1}, 1.5) circle (2pt); \draw[thick] ({1.2*1}, 1.5) -- ++(1.0, 0) |- (orC.input 4);
  \filldraw[black] ({1.2*3}, 1.3) circle (2pt); \draw[thick] ({1.2*3}, 1.3) -- ++(0.5, 0) |- (orC.input 3);
  \filldraw[black] ({1.2*5}, 1.1) circle (2pt); \draw[thick] ({1.2*5}, 1.1) -- ++(0.5, 0) |- (orC.input 2);
  \filldraw[black] ({1.2*7}, 0.9) circle (2pt); \draw[thick] ({1.2*7}, 0.9) -- ++(0.5, 0) |- (orC.input 1);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{A = D_4 + D_5 + D_6 + D_7, \quad B = D_2 + D_3 + D_6 + D_7, \quad C = D_1 + D_3 + D_5 + D_7}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: Full Subtractor Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q6)}
Implement a full subtractor circuit using multiplexer.
\end{questionbox}

A full subtractor performs subtraction on three 1-bit inputs: Minuend ($A$), Subtrahend ($B$), and Borrow In ($B_{\text{in}}$). It generates Difference ($D$) and Borrow Out ($B_{\text{out}}$).

\paragraph{Truth Table:}
\begin{center}
\begin{tabular}{|ccc||cc|}
\hline
$A$ & $B$ & $B_{\text{in}}$ & $\mathbf{D\ (Difference)}$ & $\mathbf{B_{\text{out}}\ (Borrow)}$ \\ \hline
0 & 0 & 0 & 0 & 0 \\ \hline
0 & 0 & 1 & 1 & 1 \\ \hline
0 & 1 & 0 & 1 & 1 \\ \hline
0 & 1 & 1 & 0 & 1 \\ \hline
1 & 0 & 0 & 1 & 0 \\ \hline
1 & 0 & 1 & 0 & 0 \\ \hline
1 & 1 & 0 & 0 & 0 \\ \hline
1 & 1 & 1 & 1 & 1 \\ \hline
\end{tabular}
\end{center}
Minterm canonical forms:
\[
D(A,B,B_{\text{in}}) = \sum m(1, 2, 4, 7), \qquad B_{\text{out}}(A,B,B_{\text{in}}) = \sum m(1, 2, 3, 7)
\]

\paragraph{Multiplexer Implementation using Two $4:1$ MUXes:}
Let select lines be $S_1 = A$ and $S_0 = B$, and data inputs be expressed in terms of $B_{\text{in}}$:
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Select Inputs} $(A, B)$ & \textbf{Data Channel} & \textbf{Difference ($D$)} & \textbf{Borrow Out ($B_{\text{out}}$)} \\ \hline
$00$ & $I_0$ & $B_{\text{in}}$ & $B_{\text{in}}$ \\ \hline
$01$ & $I_1$ & $\bar{B}_{\text{in}}$ & $1\ (V_{CC})$ \\ \hline
$10$ & $I_2$ & $\bar{B}_{\text{in}}$ & $0\ (\text{GND})$ \\ \hline
$11$ & $I_3$ & $B_{\text{in}}$ & $B_{\text{in}}$ \\ \hline
\end{tabular}
\end{center}

\begin{schematicbox}{Full Subtractor Implementation Using Two 4:1 Multiplexers}
\centering
\begin{tikzpicture}[scale=0.88, transform shape]
  % MUX 1: Difference (x: 0 to 3.2)
  \draw[thick, fill=boxbg] (0, 0) rectangle (3.2, 5.0);
  \node at (1.6, 4.5) {\textbf{4:1 MUX}};
  \node at (1.6, 4.0) {\small (Difference)};
  \node[anchor=west] at (0.2, 3.2) {\small $I_0$};
  \node[anchor=west] at (0.2, 2.4) {\small $I_1$};
  \node[anchor=west] at (0.2, 1.6) {\small $I_2$};
  \node[anchor=west] at (0.2, 0.8) {\small $I_3$};
  \node[anchor=north] at (1.0, 0) {\small $S_1$};
  \node[anchor=north] at (2.2, 0) {\small $S_0$};
  \draw[thick] (3.2, 2.5) -- ++(1.4, 0) node[right, xshift=1mm] {\large $\mathbf{D}$};

  % MUX 2: Borrow Out (x: 9.0 to 12.2)
  \draw[thick, fill=boxbg] (9.0, 0) rectangle (12.2, 5.0);
  \node at (10.6, 4.5) {\textbf{4:1 MUX}};
  \node at (10.6, 4.0) {\small (Borrow Out)};
  \node[anchor=west] at (9.2, 3.2) {\small $I_0$};
  \node[anchor=west] at (9.2, 2.4) {\small $I_1$};
  \node[anchor=west] at (9.2, 1.6) {\small $I_2$};
  \node[anchor=west] at (9.2, 0.8) {\small $I_3$};
  \node[anchor=north] at (10.0, 0) {\small $S_1$};
  \node[anchor=north] at (11.2, 0) {\small $S_0$};
  \draw[thick] (12.2, 2.5) -- ++(1.4, 0) node[right, xshift=1mm] {\large $\mathbf{B_{\text{out}}}$};

  % Input Rails on Left for MUX 1
  \draw[thick] (-2.8, 3.2) node[left] {$\mathbf{B_{\text{in}}}$} -- (-1.8, 3.2);
  \node[not gate US, draw, scale=0.8] (not1) at (-1.0, 2.0) {};
  \draw[thick] (-1.8, 3.2) -- (-0.2, 3.2) -- (0, 3.2);
  \draw[thick] (-1.8, 3.2) |- (not1.input);
  \draw[thick] (not1.output) -- (-0.4, 2.0);
  \draw[thick] (-0.4, 2.0) |- (0, 2.4);
  \draw[thick] (-0.4, 2.0) |- (0, 1.6);
  \draw[thick] (-0.2, 3.2) |- (0, 0.8);

  % Inputs for MUX 2
  \draw[thick] (7.2, 3.2) node[left] {$\mathbf{B_{\text{in}}}$} -- (9.0, 3.2);
  \draw[thick] (7.2, 2.4) node[left] {$\mathbf{1\ (V_{CC})}$} -- (9.0, 2.4);
  \draw[thick] (7.2, 1.6) node[left] {$\mathbf{0\ (\text{GND})}$} -- (9.0, 1.6);
  \draw[thick] (7.2, 0.8) node[left] {$\mathbf{B_{\text{in}}}$} -- (9.0, 0.8);

  % Common Select lines A, B
  \draw[thick] (-2.0, -1.0) node[left] {$\mathbf{A}$} -- (1.0, -1.0) -- (1.0, 0);
  \draw[thick] (1.0, -1.0) -- (10.0, -1.0) -- (10.0, 0);
  \draw[thick] (-2.0, -1.6) node[left] {$\mathbf{B}$} -- (2.2, -1.6) -- (2.2, 0);
  \draw[thick] (2.2, -1.6) -- (11.2, -1.6) -- (11.2, 0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Difference ($D$):} $I_0 = B_{\text{in}}, I_1 = \bar{B}_{\text{in}}, I_2 = \bar{B}_{\text{in}}, I_3 = B_{\text{in}}$.\\
\textbf{Borrow Out ($B_{\text{out}}$):} $I_0 = B_{\text{in}}, I_1 = 1, I_2 = 0, I_3 = B_{\text{in}}$, with select lines $S_1 = A, S_0 = B$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: D Flip-Flop to JK Flip-Flop Conversion Schematic [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q7)}
Differentiate between latch and flipflop. Modify a D flip-flop such that it functions as a JK flip-flop.
\end{questionbox}

\paragraph{Part (a): Comparison between Latch and Flip-Flop [2 Marks]}
\begin{center}
\small
\begin{tabular}{@{}p{3.2cm}p{6.8cm}p{6.8cm}@{}}
\toprule
\textbf{Parameter} & \textbf{Latch} & \textbf{Flip-Flop} \\
\midrule
\textbf{Triggering Method} & \textbf{Level-triggered}: transparent to input changes as long as Enable (EN) is active HIGH/LOW. & \textbf{Edge-triggered}: state transition occurs only during an active clock transition ($\uparrow$ positive or $\downarrow$ negative edge). \\
\textbf{Clock Requirement} & Does not require a periodic clock signal; operates on control/enable gates. & Requires a synchronous periodic clock signal for synchronized state updates. \\
\textbf{Race Condition} & Highly susceptible to race-around conditions when pulse width exceeds propagation delay. & Immune to race-around condition because input sampling occurs only during infinitesimal clock edges. \\
\textbf{Circuit Role} & Asynchronous registers, temporary storage buffers. & Synchronous counters, state machines, pipelines, CPU registers. \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Part (b): Conversion of D Flip-Flop to JK Flip-Flop [5 Marks]}
\begin{enumerate}
  \item \textbf{Target Behavior:} JK Flip-Flop with inputs $J, K$, present state $Q_n$, and next state $Q_{n+1}$.
  \item \textbf{Available Device:} D Flip-Flop whose characteristic equation is $Q_{n+1} = D$. Thus, $D = Q_{n+1}$.
\end{enumerate}

\paragraph{Conversion Table:}
\begin{center}
\begin{tabular}{|ccc||c||c|}
\hline
$\mathbf{J}$ & $\mathbf{K}$ & $\mathbf{Q_n}$ & $\mathbf{Q_{n+1}}$ & $\mathbf{D\ \text{Input}\ (D = Q_{n+1})}$ \\ \hline
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

\paragraph{K-Map for Input $D(J, K, Q_n)$:}
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
$JK \ \backslash \ Q_n$ & $\mathbf{0}$ & $\mathbf{1}$ \\ \hline
\textbf{00} & $0$ & $1$ \\ \hline
\textbf{01} & $0$ & $0$ \\ \hline
\textbf{11} & $1$ & $0$ \\ \hline
\textbf{10} & $1$ & $1$ \\ \hline
\end{tabular}
\end{center}
\begin{itemize}
  \item Group 1: Minterms for $Q_n=0$ where $J=1 \implies \mathbf{J\bar{Q}_n}$
  \item Group 2: Minterms for $Q_n=1$ where $K=0 \implies \mathbf{\bar{K}Q_n}$
\end{itemize}
\[
D = J\bar{Q} + \bar{K}Q
\]

\begin{schematicbox}{JK Flip-Flop Realized by Modifying a D Flip-Flop}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % D Flip Flop Box
  \draw[thick, fill=boxbg] (7.0, 0) rectangle (10.5, 4.0);
  \node at (8.75, 3.4) {\textbf{D Flip-Flop}};
  \node[anchor=west] at (7.2, 2.5) {\small $D$};
  \node[anchor=west] at (7.2, 1.0) {\small $>$ \text{CLK}};
  \node[anchor=east] at (10.3, 2.5) {\small $Q$};
  \node[anchor=east] at (10.3, 1.0) {\small $\bar{Q}$};

  % Clock line
  \draw[thick] (5.5, 1.0) -- (7.0, 1.0) node[left, at start] {\large $\mathbf{\text{CLK}}$};

  % Logic gates on the left
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (2.5, 3.0) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (2.5, 1.2) {};
  \node[not gate US, draw, scale=0.8] (notK) at (0.8, 1.4) {};
  \node[or gate US, draw, logic gate inputs=nn] (orgate) at (5.0, 2.5) {};

  % Inputs J and K
  \draw[thick] (-0.8, 3.2) -- (and1.input 1) node[left, at start] {\large $\mathbf{J}$};
  \draw[thick] (-0.8, 1.4) -- (notK.input) node[left, at start] {\large $\mathbf{K}$};
  \draw[thick] (notK.output) -- (and2.input 1);

  % OR gate to D input
  \draw[thick] (and1.output) -- ++(0.8, 0) |- (orgate.input 1);
  \draw[thick] (and2.output) -- ++(0.8, 0) |- (orgate.input 2);
  \draw[thick] (orgate.output) -- (7.0, 2.5);

  % Feedback paths Q and Q_bar
  \draw[thick] (10.5, 2.5) -- ++(1.5, 0) node[right] {\large $\mathbf{Q}$};
  \draw[thick] (10.5, 1.0) -- ++(1.5, 0) node[right] {\large $\mathbf{\bar{Q}}$};

  % Feedback Q to and2.input 2
  \filldraw[black] (11.2, 2.5) circle (2pt);
  \draw[thick] (11.2, 2.5) -- (11.2, -0.8) -- (1.5, -0.8) |- (and2.input 2);

  % Feedback Q_bar to and1.input 2
  \filldraw[black] (11.6, 1.0) circle (2pt);
  \draw[thick] (11.6, 1.0) -- (11.6, 4.6) -- (1.5, 4.6) |- (and1.input 2);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{D = J\bar{Q} + \bar{K}Q}$$
A D flip-flop is transformed into a JK flip-flop by driving its $D$ input with the combinational network $J\bar{Q} + \bar{K}Q$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: 4-Bit SIPO Shift Register Schematic \& Timing Diagram [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q8)}
Explain the working of 4-bit SIPO register with timing diagram of 1010 data input.
\end{questionbox}

A \textbf{Serial-In Parallel-Out (SIPO)} shift register accepts binary data sequentially (bit-by-bit) over a single input line, shifting it through cascaded flip-flops on each clock edge. After 4 clock cycles, all 4 bits are simultaneously accessible on parallel output pins $Q_3, Q_2, Q_1, Q_0$.

\begin{schematicbox}{4-Bit Serial-In Parallel-Out (SIPO) Shift Register}
\centering
\begin{tikzpicture}[scale=0.88, transform shape]
  % 4 D Flip-Flops
  \foreach \i/\ffname in {3/FF3 ($Q_3$), 2/FF2 ($Q_2$), 1/FF1 ($Q_1$), 0/FF0 ($Q_0$)} {
    \draw[thick, fill=boxbg] ({3.6*(3 - \i)}, 0) rectangle ({3.6*(3 - \i) + 2.4}, 3.2);
    \node at ({3.6*(3 - \i) + 1.2}, 2.7) {\textbf{\ffname}};
    \node[anchor=west] at ({3.6*(3 - \i) + 0.2}, 1.8) {\small $D$};
    \node[anchor=west] at ({3.6*(3 - \i) + 0.2}, 0.8) {\small $>$};
    \node[anchor=east] at ({3.6*(3 - \i) + 2.2}, 1.8) {\small $Q$};
    
    % Parallel output taps
    \filldraw[black] ({3.6*(3 - \i) + 2.8}, 1.8) circle (2pt);
    \draw[thick] ({3.6*(3 - \i) + 2.8}, 1.8) -- ({3.6*(3 - \i) + 2.8}, 4.2) node[above] {\large $\mathbf{Q_\i}$};
  }

  % Serial Input to FF3
  \draw[thick] (-1.5, 1.8) node[left] {\large $\mathbf{D_{\text{in}}\ (\text{Serial In})}$} -- (0, 1.8);

  % Inter-stage connections
  \draw[thick] (2.4, 1.8) -- (3.6, 1.8);
  \draw[thick] (6.0, 1.8) -- (7.2, 1.8);
  \draw[thick] (9.6, 1.8) -- (10.8, 1.8);
  \draw[thick] (13.2, 1.8) -- (13.6, 1.8);

  % Common Clock Rail
  \draw[thick] (-1.5, -0.8) node[left] {\large $\mathbf{\text{CLK}}$} -- (12.0, -0.8);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({3.6*\i + 0.4}, -0.8) -- ({3.6*\i + 0.4}, 0.8) -- ({3.6*\i + 0.2}, 0.8);
  }
\end{tikzpicture}
\end{schematicbox}

\paragraph{Step-by-Step Operation for Input Sequence $1010_2$ (MSB entered first):}
Assume initial contents are $Q_3 Q_2 Q_1 Q_0 = 0000_2$.
\begin{center}
\begin{tabular}{|c|c|cccc|l|}
\hline
\textbf{Clock Pulse} & \textbf{Serial Input ($D_{\text{in}}$)} & $\mathbf{Q_3}$ & $\mathbf{Q_2}$ & $\mathbf{Q_1}$ & $\mathbf{Q_0}$ & \textbf{Remarks} \\ \hline
\textbf{Initial} & $-$ & 0 & 0 & 0 & 0 & Cleared state \\ \hline
\textbf{CLK 1} & $1$ (MSB) & 1 & 0 & 0 & 0 & First bit enters FF3 \\ \hline
\textbf{CLK 2} & $0$ & 0 & 1 & 0 & 0 & Shift right, second bit enters \\ \hline
\textbf{CLK 3} & $1$ & 1 & 0 & 1 & 0 & Shift right, third bit enters \\ \hline
\textbf{CLK 4} & $0$ (LSB) & 0 & 1 & 0 & 1 & Complete word loaded ($1010_2$) \\ \hline
\end{tabular}
\end{center}

\begin{schematicbox}{Timing Waveforms for 4-Bit SIPO Shift Register Loading $1010_2$}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % Vertical grid lines
  \foreach \x in {0, 2.5, 5.0, 7.5, 10.0, 12.5} {
    \draw[dotted, gray!60] (\x, 1.2) -- (\x, -6.5);
  }
  
  % Clock Waveform
  \node[left] at (-0.3, 0.5) {\textbf{CLK}};
  \draw[thick, blue] (0,0) -- (1.25,0) -- (1.25,1) -- (2.5,1) -- (2.5,0) -- (3.75,0) -- (3.75,1) -- (5.0,1) -- (5.0,0) -- (6.25,0) -- (6.25,1) -- (7.5,1) -- (7.5,0) -- (8.75,0) -- (8.75,1) -- (10.0,1) -- (10.0,0) -- (11.25,0) -- (11.25,1) -- (12.5,1);
  \node at (1.87, 1.3) {\small Pulse 1};
  \node at (4.37, 1.3) {\small Pulse 2};
  \node at (6.87, 1.3) {\small Pulse 3};
  \node at (9.37, 1.3) {\small Pulse 4};

  % Serial In (1, 0, 1, 0)
  \node[left] at (-0.3, -0.8) {\textbf{$D_{\text{in}}$}};
  \draw[thick, red] (0, -0.3) -- (2.5, -0.3) -- (2.5, -1.3) -- (5.0, -1.3) -- (5.0, -0.3) -- (7.5, -0.3) -- (7.5, -1.3) -- (12.5, -1.3);
  \node at (1.25, -0.1) {\small '1'}; \node at (3.75, -1.5) {\small '0'}; \node at (6.25, -0.1) {\small '1'}; \node at (8.75, -1.5) {\small '0'};

  % Q3
  \node[left] at (-0.3, -2.3) {\textbf{$Q_3$}};
  \draw[thick, teal] (0, -2.8) -- (2.5, -2.8) -- (2.5, -1.8) -- (5.0, -1.8) -- (5.0, -2.8) -- (7.5, -2.8) -- (7.5, -1.8) -- (10.0, -1.8) -- (10.0, -2.8) -- (12.5, -2.8);

  % Q2
  \node[left] at (-0.3, -3.7) {\textbf{$Q_2$}};
  \draw[thick, teal] (0, -4.2) -- (5.0, -4.2) -- (5.0, -3.2) -- (7.5, -3.2) -- (7.5, -4.2) -- (10.0, -4.2) -- (10.0, -3.2) -- (12.5, -3.2);

  % Q1
  \node[left] at (-0.3, -5.1) {\textbf{$Q_1$}};
  \draw[thick, teal] (0, -5.6) -- (7.5, -5.6) -- (7.5, -4.6) -- (10.0, -4.6) -- (10.0, -5.6) -- (12.5, -5.6);

  % Q0
  \node[left] at (-0.3, -6.3) {\textbf{$Q_0$}};
  \draw[thick, teal] (0, -6.5) -- (10.0, -6.5) -- (10.0, -5.8) -- (12.5, -5.8);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
After 4 clock pulses, serial word $1010_2$ is converted to parallel outputs: $\mathbf{Q_3 Q_2 Q_1 Q_0 = 0101_2}$ (or $1010_2$ when read in arrival sequence $Q_0 Q_1 Q_2 Q_3$).
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: Asynchronous BCD (Decade) Counter Schematic [5 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q9)}
Describe the operation of asynchronous BCD (decade) counter with necessary diagrams.
\end{questionbox}

An \textbf{Asynchronous BCD (Decade) Counter} (Mod-10 ripple counter) counts through $10$ discrete binary states from $0000_2$ ($0_{10}$) up to $1001_2$ ($9_{10}$) and automatically recycles to $0000_2$ on the tenth clock pulse.

\paragraph{Design Principle:}
\begin{itemize}
  \item 4 negative edge-triggered JK (or T) flip-flops are connected in toggle mode ($J=K=1$).
  \item Ripple clocking: $Q_0 \to \text{CLK}_1$, $Q_1 \to \text{CLK}_2$, $Q_2 \to \text{CLK}_3$.
  \item Modulo reset: At the 10th clock pulse, the count momentarily enters transient state $1010_2$ ($Q_3=1, Q_2=0, Q_1=1, Q_0=0$).
  \item A 2-input NAND gate detects $Q_3 \cdot Q_1 = 1$ and outputs an active-LOW reset pulse ($\overline{\text{CLR}} = 0$) to all flip-flops:
  \[
  \overline{\text{CLR}} = \overline{Q_3 \cdot Q_1}
  \]
\end{itemize}

\begin{schematicbox}{Asynchronous BCD (Decade) Counter Logic Circuit}
\centering
\begin{tikzpicture}[scale=0.88, transform shape]
  % 4 JK Flip Flops
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({3.6*\i}, 0) rectangle ({3.6*\i + 2.4}, 3.4);
    \node at ({3.6*\i + 1.2}, 2.9) {\textbf{FF\i\ (JK)}};
    \node[anchor=west] at ({3.6*\i + 0.2}, 2.2) {\small $J=1$};
    \node[anchor=west] at ({3.6*\i + 0.2}, 1.5) {\small $\circ>$};
    \node[anchor=west] at ({3.6*\i + 0.2}, 0.8) {\small $K=1$};
    \node[anchor=east] at ({3.6*\i + 2.2}, 2.2) {\small $Q$};
    \node[anchor=east] at ({3.6*\i + 2.2}, 0.8) {\small $\bar{Q}$};
    \node[anchor=south] at ({3.6*\i + 1.2}, 0.1) {\small $\overline{\text{CLR}}$};

    % Output lines
    \filldraw[black] ({3.6*\i + 2.8}, 2.2) circle (2pt);
    \draw[thick] ({3.6*\i + 2.4}, 2.2) -- ({3.6*\i + 2.8}, 2.2) -- ({3.6*\i + 2.8}, 4.2) node[above] {\large $\mathbf{Q_\i}$};
  }

  % External Clock to FF0
  \draw[thick] (-1.2, 1.5) node[left] {\large $\mathbf{\text{CLK}}$} -- (0, 1.5);

  % Ripple clock connections (Q_i -> CLK_{i+1})
  \draw[thick] (2.8, 2.2) -- (3.2, 2.2) |- (3.6, 1.5);
  \draw[thick] (6.4, 2.2) -- (6.8, 2.2) |- (7.2, 1.5);
  \draw[thick] (10.0, 2.2) -- (10.4, 2.2) |- (10.8, 1.5);

  % NAND Reset Gate
  \node[nand gate US, draw, logic gate inputs=nn, rotate=-90] (nandRst) at (7.0, -2.0) {};
  \draw[thick] (13.6, 2.2) -- (13.6, -1.2) |- (nandRst.input 1); % Q3
  \draw[thick] (6.4, 2.2) -- (6.4, -1.2) |- (nandRst.input 2);  % Q1

  % Reset Bus to CLR pins
  \draw[thick] (nandRst.output) -- (7.0, -3.2) -- (-0.5, -3.2) -- (-0.5, -0.4) -- (12.0, -0.4);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({3.6*\i + 1.2}, -0.4) -- ({3.6*\i + 1.2}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
The asynchronous BCD counter cycles through states $0000 \to 0001 \to \dots \to 1001 \to (1010 \text{ glitch}) \xrightarrow{\overline{\text{CLR}}=0} 0000$, implementing a stable Mod-10 frequency divider.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: Synchronous Mod-10 UP Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q10)}
Design the synchronous mod-10 up counter using T flip-flop and draw its timing diagram also.
\end{questionbox}

\paragraph{1. State Transition and T Excitation Table ($T = Q_n \oplus Q_{n+1}$):}
\begin{center}
\begin{tabular}{|c|cccc|cccc|cccc|}
\hline
\textbf{State} & \multicolumn{4}{c|}{\textbf{Present State}} & \multicolumn{4}{c|}{\textbf{Next State}} & \multicolumn{4}{c|}{\textbf{T Inputs}} \\
& $Q_3$ & $Q_2$ & $Q_1$ & $Q_0$ & $Q_3^+$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $\mathbf{T_3}$ & $\mathbf{T_2}$ & $\mathbf{T_1}$ & $\mathbf{T_0}$ \\ \hline
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
(Unused states 10 to 15 are treated as Don't Cares $X$).

\paragraph{2. K-Map Derivations for T Inputs:}
\begin{itemize}
  \item $\mathbf{T_0 = 1}$ ($Q_0$ toggles on every single clock pulse).
  \item $\mathbf{T_1 = \bar{Q}_3 Q_0}$ ($Q_1$ toggles when $Q_0=1$ except when transitioning from 9 to 0).
  \item $\mathbf{T_2 = Q_1 Q_0}$ ($Q_2$ toggles when $Q_1 Q_0 = 1$).
  \item $\mathbf{T_3 = Q_2 Q_1 Q_0 + Q_3 Q_0}$ ($Q_3$ toggles at state 7 to become 1, and at state 9 to reset to 0).
\end{itemize}

\begin{schematicbox}{Synchronous Mod-10 UP Counter Logic Circuit}
\centering
\begin{tikzpicture}[scale=0.65, transform shape]
  % 4 T Flip Flops (Width 2.0 each, wide inter-stage gaps)
  % FF0: x in [0, 2.0]
  % FF1: x in [5.6, 7.6]
  % FF2: x in [11.2, 13.2]
  % FF3: x in [19.5, 21.5]
  
  \foreach \i/\xpos in {0/0, 1/5.6, 2/11.2, 3/19.5} {
    \draw[thick, fill=boxbg] (\xpos, 0) rectangle (\xpos + 2.0, 3.4);
    \node at (\xpos + 1.0, 2.9) {\textbf{FF\i\ (T)}};
    \node[anchor=west] at (\xpos + 0.2, 2.2) {\small $T$};
    \node[anchor=west] at (\xpos + 0.2, 1.0) {\small $>$};
    \node[anchor=east] at (\xpos + 1.8, 2.2) {\small $Q$};
    \node[anchor=east] at (\xpos + 1.8, 1.0) {\small $\bar{Q}$};

    % Output pins Q_i
    \filldraw[black] (\xpos + 2.5, 2.2) circle (2pt);
    \draw[thick] (\xpos + 2.0, 2.2) -- (\xpos + 2.5, 2.2) -- (\xpos + 2.5, 4.4) node[above] {\large $\mathbf{Q_\i}$};
  }

  % T0 = 1 (VCC)
  \draw[thick] (-1.2, 2.2) node[left] {\large $\mathbf{1\ (V_{CC})}$} -- (0, 2.2);

  % Common Synchronous Clock Rail
  \draw[thick] (-1.2, -1.0) node[left] {\large $\mathbf{\text{CLK}}$} -- (21.0, -1.0);
  \foreach \xpos in {0, 5.6, 11.2, 19.5} {
    \draw[thick] (\xpos + 0.5, -1.0) -- (\xpos + 0.5, 1.0) -- (\xpos + 0.2, 1.0);
  }

  % T1 Gate = Q0 . Q3_bar (placed at x = 4.6 in gap [2.0, 5.6])
  \node[and gate US, draw, logic gate inputs=nn] (andT1) at (4.6, 2.2) {};
  \draw[thick] (3.6, 2.35) node[left] {\footnotesize $Q_0$} -- (andT1.input 1);
  \draw[thick] (3.6, 2.05) node[left] {\footnotesize $\bar{Q}_3$} -- (andT1.input 2);
  \draw[thick] (andT1.output) -- (5.6, 2.2);

  % T2 Gate = Q1 . Q0 (placed at x = 10.2 in gap [7.6, 11.2])
  \node[and gate US, draw, logic gate inputs=nn] (andT2) at (10.2, 2.2) {};
  \draw[thick] (9.2, 2.35) node[left] {\footnotesize $Q_1$} -- (andT2.input 1);
  \draw[thick] (9.2, 2.05) node[left] {\footnotesize $Q_0$} -- (andT2.input 2);
  \draw[thick] (andT2.output) -- (11.2, 2.2);

  % T3 Gates: andT3a, andT3b + orT3 (placed in wide gap [13.2, 19.5])
  \node[and gate US, draw, logic gate inputs=nnn] (andT3a) at (16.5, 2.6) {};
  \node[and gate US, draw, logic gate inputs=nn] (andT3b) at (16.5, 1.7) {};
  \node[or gate US, draw, logic gate inputs=nn] (orT3) at (18.2, 2.2) {};
  
  \draw[thick] (15.2, 2.8) node[left] {\footnotesize $Q_2$} -- (andT3a.input 1);
  \draw[thick] (15.2, 2.6) node[left] {\footnotesize $Q_1$} -- (andT3a.input 2);
  \draw[thick] (15.2, 2.4) node[left] {\footnotesize $Q_0$} -- (andT3a.input 3);
  
  \draw[thick] (15.2, 1.85) node[left] {\footnotesize $Q_3$} -- (andT3b.input 1);
  \draw[thick] (15.2, 1.55) node[left] {\footnotesize $Q_0$} -- (andT3b.input 2);
  
  \draw[thick] (andT3a.output) -- (orT3.input 1);
  \draw[thick] (andT3b.output) -- (orT3.input 2);
  \draw[thick] (orT3.output) -- (19.5, 2.2);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{T_0 = 1, \quad T_1 = \bar{Q}_3 Q_0, \quad T_2 = Q_1 Q_0, \quad T_3 = Q_2 Q_1 Q_0 + Q_3 Q_0}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 11
% =========================================================================
\subsection{Question 11: Synchronous FSM Sequence Detector '011' [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q11)}
Design a synchronous sequential machine that has 1-bit serial input $X$ and output $Z$ which will be high when the input contains the message `011' (Use T Flip-Flop).
\end{questionbox}

\paragraph{1. State Definitions and State Diagram (Mealy Model):}
\begin{itemize}
  \item $S_0 (00)$: Reset state / No relevant bit detected.
  \item $S_1 (01)$: Sequence `0' detected.
  \item $S_2 (10)$: Sequence `01' detected.
  \item When in $S_2$ and next bit $X=1 \implies$ `011' detected $\implies Z=1$, next state $S_0$.
\end{itemize}

\begin{schematicbox}{State Transition Automaton for '011' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.6cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$X=1 / 0$} (S0)
             edge [bend left] node {$X=0 / 0$} (S1)
        (S1) edge [loop above] node {$X=0 / 0$} (S1)
             edge [bend left] node {$X=1 / 0$} (S2)
        (S2) edge [bend left=55] node[below=2mm] {$X=1 / 1$} (S0)
             edge [bend left] node[below=1mm] {$X=0 / 0$} (S1);
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. State Transition and Excitation Table for T Flip-Flops ($A, B$):}
\begin{center}
\begin{tabular}{|cc|c|cc|c|cc|}
\hline
\multicolumn{2}{|c|}{\textbf{Present State}} & \textbf{Input} & \multicolumn{2}{c|}{\textbf{Next State}} & \textbf{Output} & \multicolumn{2}{c|}{\textbf{T Inputs}} \\
$A$ & $B$ & $X$ & $A^+$ & $B^+$ & $\mathbf{Z}$ & $\mathbf{T_A}$ & $\mathbf{T_B}$ \\ \hline
0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\ \hline
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 \\ \hline
0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 \\ \hline
1 & 0 & 0 & 0 & 1 & 0 & 1 & 1 \\ \hline
1 & 0 & 1 & 0 & 0 & 1 & 1 & 0 \\ \hline
1 & 1 & 0 & $X$ & $X$ & $X$ & $X$ & $X$ \\ \hline
1 & 1 & 1 & $X$ & $X$ & $X$ & $X$ & $X$ \\ \hline
\end{tabular}
\end{center}

\paragraph{3. Minimized Equations via K-Maps:}
\begin{align*}
T_A &= A + BX \\
T_B &= \bar{A}\bar{B}\bar{X} + BX + A\bar{X} \\
Z &= AX
\end{align*}

\begin{schematicbox}{Synchronous FSM Circuit Realization Using T Flip-Flops}
\centering
\begin{tikzpicture}[scale=0.82, transform shape]
  % Flip-Flop A (x in [0.5, 3.0]) and Flip-Flop B (x in [9.5, 12.0]) -> 6.5cm wide gap in middle!
  \draw[thick, fill=boxbg] (0.5, 0) rectangle (3.0, 3.2);
  \node at (1.75, 2.7) {\textbf{FF-A (T)}};
  \node[anchor=west] at (0.7, 2.0) {\small $T_A$};
  \node[anchor=west] at (0.7, 0.8) {\small $>$};
  \node[anchor=east] at (2.8, 2.0) {\small $A$};
  \node[anchor=east] at (2.8, 0.8) {\small $\bar{A}$};

  \draw[thick, fill=boxbg] (9.5, 0) rectangle (12.0, 3.2);
  \node at (10.75, 2.7) {\textbf{FF-B (T)}};
  \node[anchor=west] at (9.7, 2.0) {\small $T_B$};
  \node[anchor=west] at (9.7, 0.8) {\small $>$};
  \node[anchor=east] at (11.8, 2.0) {\small $B$};
  \node[anchor=east] at (11.8, 0.8) {\small $\bar{B}$};

  % Common Clock
  \draw[thick] (-2.2, -0.8) node[left] {\large $\mathbf{\text{CLK}}$} -- (11.0, -0.8);
  \draw[thick] (1.3, -0.8) -- (1.3, 0.8) -- (0.7, 0.8);
  \draw[thick] (10.3, -0.8) -- (10.3, 0.8) -- (9.7, 0.8);

  % Combinational Gates for T_A = A + BX (on the left, x in [-2.0, 0.5])
  \node[and gate US, draw, logic gate inputs=nn] (andTA) at (-1.2, 2.6) {};
  \node[or gate US, draw, logic gate inputs=nn] (orTA) at (-0.2, 2.0) {};
  \draw[thick] (-2.0, 2.75) node[left] {\footnotesize $B$} -- (andTA.input 1);
  \draw[thick] (-2.0, 2.45) node[left] {\footnotesize $X$} -- (andTA.input 2);
  \draw[thick] (andTA.output) |- (orTA.input 1);
  \draw[thick] (-1.2, 1.7) node[left] {\footnotesize $A$} -- (orTA.input 2);
  \draw[thick] (orTA.output) -- (0.5, 2.0);

  % Combinational Gates for T_B = \bar{A}\bar{B}\bar{X} + BX + A\bar{X} (centered in the wide 6.5cm gap at x=6.0 to 8.5)
  \node[and gate US, draw, logic gate inputs=nnn] (andTB1) at (6.5, 2.6) {};
  \node[and gate US, draw, logic gate inputs=nn] (andTB2) at (6.5, 1.9) {};
  \node[and gate US, draw, logic gate inputs=nn] (andTB3) at (6.5, 1.2) {};
  \node[or gate US, draw, logic gate inputs=nnn] (orTB) at (8.0, 2.0) {};
  
  \draw[thick] (5.4, 2.8) node[left] {\footnotesize $\bar{A}$} -- (andTB1.input 1);
  \draw[thick] (5.4, 2.6) node[left] {\footnotesize $\bar{B}$} -- (andTB1.input 2);
  \draw[thick] (5.4, 2.4) node[left] {\footnotesize $\bar{X}$} -- (andTB1.input 3);
  
  \draw[thick] (5.4, 2.05) node[left] {\footnotesize $B$} -- (andTB2.input 1);
  \draw[thick] (5.4, 1.75) node[left] {\footnotesize $X$} -- (andTB2.input 2);
  
  \draw[thick] (5.4, 1.35) node[left] {\footnotesize $A$} -- (andTB3.input 1);
  \draw[thick] (5.4, 1.05) node[left] {\footnotesize $\bar{X}$} -- (andTB3.input 2);
  
  \draw[thick] (andTB1.output) |- (orTB.input 1);
  \draw[thick] (andTB2.output) -- (orTB.input 2);
  \draw[thick] (andTB3.output) |- (orTB.input 3);
  \draw[thick] (orTB.output) -- (9.5, 2.0);

  % Output Z = A . X (placed to the right of FF-B at x=13.8)
  \node[and gate US, draw, logic gate inputs=nn] (andZ) at (13.8, 2.0) {};
  \draw[thick] (3.0, 2.0) -- (3.6, 2.0) -- (3.6, 4.0) -- (12.8, 4.0) |- (andZ.input 1);
  \draw[thick] (12.5, 1.2) node[left] {$X$} -- (andZ.input 2);
  \draw[thick] (andZ.output) -- ++(1.0, 0) node[right] {\large $\mathbf{Z}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{T_A = A + BX, \quad T_B = \bar{A}\bar{B}\bar{X} + BX + A\bar{X}, \quad Z = AX}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 12
% =========================================================================
\subsection{Question 12: Characteristics of Digital Logic Families [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q12)}
Explain about the main characteristics of digital logic families.
\end{questionbox}

The performance and suitability of digital integrated circuit (IC) families are evaluated based on the following key operational parameters:

\begin{enumerate}[leftmargin=*]
  \item \textbf{Propagation Delay ($t_{pd}$):} The average time elapsed between the application of an input logic transition and the resulting output logic transition:
  \[
  t_{pd} = \frac{t_{pLH} + t_{pHL}}{2}
  \]
  where $t_{pLH}$ is the low-to-high delay and $t_{pHL}$ is the high-to-low delay. Lower propagation delay indicates higher operating speed.

  \item \textbf{Power Dissipation ($P_D$):} The DC power consumed by the logic gate during static and dynamic operation, expressed in milliwatts (mW) or microwatts ($\mu$W):
  \[
  P_D = V_{CC} \times I_{CC(\text{avg})}
  \]

  \item \textbf{Speed-Power Product (Figure of Merit):} The product of propagation delay and power dissipation:
  \[
  \text{SPP} = t_{pd} \times P_D \quad (\text{expressed in picojoules, pJ})
  \]
  A lower SPP value signifies superior overall technological performance.

  \item \textbf{Noise Margins ($NM_H$ and $NM_L$):} The maximum allowable unwanted noise voltage superimposed on the input without causing an erroneous output change:
  \[
  NM_H = V_{OH(\min)} - V_{IH(\min)}, \qquad NM_L = V_{IL(\max)} - V_{OL(\max)}
  \]

  \item \textbf{Fan-Out and Fan-In:}
  \begin{itemize}
    \item \textbf{Fan-Out:} Maximum number of standard logic gate inputs of the same family that an output can reliably drive without exceeding current limits.
    \item \textbf{Fan-In:} Number of independent input signals that a single gate can accommodate without degradation.
  \end{itemize}

  \item \textbf{Operating Temperature Range:} Standard commercial grade ($0^\circ\text{C}$ to $70^\circ\text{C}$) versus military grade ($-55^\circ\text{C}$ to $+125^\circ\text{C}$).
\end{enumerate}

\paragraph{Comparative Summary of Major Digital Logic Families:}
\begin{center}
\small
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Parameter} & \textbf{Standard TTL (7400)} & \textbf{Schottky TTL (74S)} & \textbf{CMOS (74HC)} & \textbf{ECL (10K)} \\
\midrule
\textbf{Propagation Delay ($t_{pd}$)} & $10\text{ ns}$ & $3\text{ ns}$ & $8\text{ ns}$ & $1\text{ ns}$ \\
\textbf{Power Dissipation / Gate} & $10\text{ mW}$ & $20\text{ mW}$ & $0.001\text{ mW (static)}$ & $25\text{ mW}$ \\
\textbf{Speed-Power Product (SPP)} & $100\text{ pJ}$ & $60\text{ pJ}$ & $0.008\text{ pJ}$ & $25\text{ pJ}$ \\
\textbf{Noise Margin ($NM$)} & $0.4\text{ V}$ & $0.3\text{ V}$ & $> 1.0\text{ V}$ & $0.25\text{ V}$ \\
\textbf{Fan-Out} & 10 & 20 & $> 50$ & 25 \\
\bottomrule
\end{tabular}
\end{center}

\begin{answerbox}
Digital logic families are comprehensively characterized by speed ($t_{pd}$), power consumption ($P_D$), noise margins ($NM_H, NM_L$), fan-out, and the Speed-Power Product figure of merit.
\end{answerbox}
"""
