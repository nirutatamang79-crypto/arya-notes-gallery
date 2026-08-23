# dl_ch2_2082_bhadra.py
# Chapter 2: 2082 Bhadra Examination Master Solutions

def get_chapter_2082_bhadra():
    return r"""
\chapter{2082 Bhadra Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BEI, BCT & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Digital Logic (ENEX 152 / EX 152) & \textbf{Examination Type:} Regular / Back \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: Binary to Gray Code Conversion [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q1)}
Convert the following binary codes to gray codes:
\begin{enumerate}[label=(\alph*)]
  \item $(101101)_2$
  \item $(110001)_2$
\end{enumerate}
\end{questionbox}

\paragraph{Conversion Algorithm:}
Given an $n$-bit binary word $B = b_{n-1} b_{n-2} \dots b_1 b_0$ and target Gray code $G = g_{n-1} g_{n-2} \dots g_1 g_0$:
\begin{enumerate}
  \item $g_{n-1} = b_{n-1}$ (The Most Significant Bit remains unchanged).
  \item $g_i = b_{i+1} \oplus b_i$ for each subsequent bit position $i = n-2, n-3, \dots, 0$.
\end{enumerate}

\paragraph{Part (a): Conversion of $(101101)_2$}
Given $b_5 b_4 b_3 b_2 b_1 b_0 = 101101_2$:
\begin{itemize}
  \item $g_5 = b_5 = 1$
  \item $g_4 = b_5 \oplus b_4 = 1 \oplus 0 = 1$
  \item $g_3 = b_4 \oplus b_3 = 0 \oplus 1 = 1$
  \item $g_2 = b_3 \oplus b_2 = 1 \oplus 1 = 0$
  \item $g_1 = b_2 \oplus b_1 = 1 \oplus 0 = 1$
  \item $g_0 = b_1 \oplus b_0 = 0 \oplus 1 = 1$
\end{itemize}
Thus, $(101101)_2 = (111011)_{\text{Gray}}$.

\paragraph{Part (b): Conversion of $(110001)_2$}
Given $b_5 b_4 b_3 b_2 b_1 b_0 = 110001_2$:
\begin{itemize}
  \item $g_5 = b_5 = 1$
  \item $g_4 = b_5 \oplus b_4 = 1 \oplus 1 = 0$
  \item $g_3 = b_4 \oplus b_3 = 1 \oplus 0 = 1$
  \item $g_2 = b_3 \oplus b_2 = 0 \oplus 0 = 0$
  \item $g_1 = b_2 \oplus b_1 = 0 \oplus 0 = 0$
  \item $g_0 = b_1 \oplus b_0 = 0 \oplus 1 = 1$
\end{itemize}
Thus, $(110001)_2 = (101001)_{\text{Gray}}$.

\begin{answerbox}
\begin{align*}
\text{(a)}\quad (101101)_2 &= \mathbf{(111011)_{\text{Gray}}} \\
\text{(b)}\quad (110001)_2 &= \mathbf{(101001)_{\text{Gray}}}
\end{align*}
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: 2's Complement \& BCD Addition [1 + 2 = 3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q2)}
What is 2's complement representation? Perform BCD addition of $(23)_{10} + (48)_{10}$.
\end{questionbox}

\paragraph{Part (a): 2's Complement Representation [1 Mark]}
2's complement is the standard system used in digital computers to represent signed integers. For an $n$-bit binary number $X$:
\[
\text{2's Complement of } X = 2^n - X = (\text{1's Complement of } X) + 1
\]
\textbf{Key Advantages:}
\begin{itemize}
  \item Unambiguous representation of zero (single representation $0000_2$, unlike 1's complement which has $+0$ and $-0$).
  \item Simplifies hardware arithmetic: subtraction $A - B$ is performed as addition $A + (\text{2's comp of } B)$ using standard binary adder circuits.
\end{itemize}

\paragraph{Part (b): BCD Addition of $23_{10} + 48_{10}$ [2 Marks]}
In BCD (8421 code), each decimal digit is encoded into 4 bits ($0000_2$ to $1001_2$). If the sum of any decade exceeds $9$ ($1001_2$) or produces a carry, a correction factor of $+6$ ($0110_2$) must be added.
\begin{itemize}
  \item Represent numbers in BCD:
  \[
  23_{10} = \mathbf{0010\ 0011}_{\text{BCD}}, \qquad 48_{10} = \mathbf{0100\ 1000}_{\text{BCD}}
  \]
  \item \textbf{Step 1: Add Lower Decade (Units):}
  \[
  \begin{array}{r@{\quad}l}
    0011 & (3_{10}) \\
  +\ 1000 & (8_{10}) \\
  \hline
    1011_2 & (11_{10} > 9 \implies \text{Invalid BCD})
  \end{array}
  \]
  \item \textbf{Step 2: Add Correction Factor ($+0110_2$):}
  \[
  \begin{array}{r@{\quad}l}
    1011 & \\
  +\ 0110 & (+6_{10}) \\
  \hline
    \mathbf{0001}_2 & \text{with Carry Out } C_{\text{out}} = 1 \text{ to Upper Decade}
  \end{array}
  \]
  \item \textbf{Step 3: Add Upper Decade (Tens) including Carry In:}
  \[
  \begin{array}{r@{\quad}l}
    0010 & (2_{10}) \\
    0100 & (4_{10}) \\
  +\ 0001 & (\text{Carry in} = 1) \\
  \hline
    \mathbf{0111}_2 & (7_{10} \le 9 \implies \text{Valid BCD})
  \end{array}
  \]
\end{itemize}

\begin{answerbox}
$$(23)_{10} + (48)_{10} = \mathbf{0111\ 0001_{\text{BCD}}} = (71)_{10}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: De Morgan's Theorem with Diagrams [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q3)}
State and explain De Morgan's Theorem with truth table and necessary diagrams.
\end{questionbox}

\paragraph{1. First Theorem (NAND-to-Inverted-OR Equivalence):}
The complement of a product of variables is equal to the sum of the complements of the variables:
\[
\overline{A \cdot B} = \bar{A} + \bar{B}
\]

\paragraph{2. Second Theorem (NOR-to-Inverted-AND Equivalence):}
The complement of a sum of variables is equal to the product of the complements of the variables:
\[
\overline{A + B} = \bar{A} \cdot \bar{B}
\]

\paragraph{Truth Table Verification:}
\begin{center}
\begin{tabular}{|cc|cc|c|c||c|c|}
\hline
$A$ & $B$ & $\bar{A}$ & $\bar{B}$ & $\overline{A \cdot B}$ & $\bar{A} + \bar{B}$ & $\overline{A + B}$ & $\bar{A} \cdot \bar{B}$ \\ \hline
0 & 0 & 1 & 1 & \textbf{1} & \textbf{1} & \textbf{1} & \textbf{1} \\ \hline
0 & 1 & 1 & 0 & \textbf{1} & \textbf{1} & \textbf{0} & \textbf{0} \\ \hline
1 & 0 & 0 & 1 & \textbf{1} & \textbf{1} & \textbf{0} & \textbf{0} \\ \hline
1 & 1 & 0 & 0 & \textbf{0} & \textbf{0} & \textbf{0} & \textbf{0} \\ \hline
\end{tabular}
\end{center}
Columns 5 and 6 are identical, verifying Theorem 1. Columns 7 and 8 are identical, verifying Theorem 2.

\begin{schematicbox}{De Morgan's Equivalent Logic Gate Pairs}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Theorem 1: NAND == Bubbled OR
  \node[nand gate US, draw, logic gate inputs=nn] (nand1) at (2.5, 2.2) {};
  \draw[thick] (0.8, 2.45) node[left] {$A$} -- (nand1.input 1);
  \draw[thick] (0.8, 1.95) node[left] {$B$} -- (nand1.input 2);
  \draw[thick] (nand1.output) -- ++(1.0, 0) node[right] {$\overline{A \cdot B}$};

  \node at (5.5, 2.2) {\LARGE $\equiv$};

  \node[or gate US, draw, logic gate inputs=ii, scale=1.0] (bubOR) at (8.5, 2.2) {};
  \draw[thick] (6.8, 2.45) node[left] {$A$} -- (bubOR.input 1);
  \draw[thick] (6.8, 1.95) node[left] {$B$} -- (bubOR.input 2);
  \draw[thick] (bubOR.output) -- ++(1.0, 0) node[right] {$\bar{A} + \bar{B}$};
  \node[above] at (5.5, 3.2) {\textbf{Theorem 1:} $\overline{A \cdot B} = \bar{A} + \bar{B}$ (NAND $\equiv$ Inverted-Input OR)};

  % Theorem 2: NOR == Bubbled AND
  \node[nor gate US, draw, logic gate inputs=nn] (nor1) at (2.5, -0.8) {};
  \draw[thick] (0.8, -0.55) node[left] {$A$} -- (nor1.input 1);
  \draw[thick] (0.8, -1.05) node[left] {$B$} -- (nor1.input 2);
  \draw[thick] (nor1.output) -- ++(1.0, 0) node[right] {$\overline{A + B}$};

  \node at (5.5, -0.8) {\LARGE $\equiv$};

  \node[and gate US, draw, logic gate inputs=ii, scale=1.0] (bubAND) at (8.5, -0.8) {};
  \draw[thick] (6.8, -0.55) node[left] {$A$} -- (bubAND.input 1);
  \draw[thick] (6.8, -1.05) node[left] {$B$} -- (bubAND.input 2);
  \draw[thick] (bubAND.output) -- ++(1.0, 0) node[right] {$\bar{A} \cdot \bar{B}$};
  \node[above] at (5.5, 0.2) {\textbf{Theorem 2:} $\overline{A + B} = \bar{A} \cdot \bar{B}$ (NOR $\equiv$ Inverted-Input AND)};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
De Morgan's Laws establish dual relationships between AND and OR operations through inversion: $\mathbf{\overline{A \cdot B} = \bar{A} + \bar{B}}$ and $\mathbf{\overline{A + B} = \bar{A} \cdot \bar{B}}$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: K-Map with Don't Cares \& Circuit [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q4)}
Minimize the function $F(A, B, C, D) = \sum m(0,1,2,4,7,8,9,10,12,15) + d(5,11,13)$ using K-Map and realize it with suitable logic gates.
\end{questionbox}

\paragraph{1. K-Map Plotting (4-Variable K-Map):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
$AB \ \backslash \ CD$ & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $\mathbf{1}\ (m_0)$ & $\mathbf{1}\ (m_1)$ & $0\ (m_3)$ & $\mathbf{1}\ (m_2)$ \\ \hline
\textbf{01} & $\mathbf{1}\ (m_4)$ & $\mathbf{X}\ (d_5)$ & $\mathbf{1}\ (m_7)$ & $0\ (m_6)$ \\ \hline
\textbf{11} & $\mathbf{1}\ (m_{12})$ & $\mathbf{X}\ (d_{13})$ & $\mathbf{1}\ (m_{15})$ & $0\ (m_{14})$ \\ \hline
\textbf{10} & $\mathbf{1}\ (m_8)$ & $\mathbf{1}\ (m_9)$ & $\mathbf{X}\ (d_{11})$ & $\mathbf{1}\ (m_{10})$ \\ \hline
\end{tabular}
\end{center}

\paragraph{2. Grouping Analysis:}
\begin{enumerate}
  \item \textbf{Octet 1 (Columns $CD=00$ and $CD=01$):} \\
  Cells $(m_0, m_1, m_4, d_5, m_{12}, d_{13}, m_8, m_9) \implies \mathbf{\bar{C}}$.
  \item \textbf{Quad 2 (Center and Column 11):} \\
  Cells $(d_5, m_7, d_{13}, m_{15}) \implies \mathbf{BD}$.
  \item \textbf{Quad 3 (Four Corners):} \\
  Cells $(m_0, m_2, m_8, m_{10}) \implies \mathbf{\bar{B}\bar{D}}$.
\end{enumerate}

\paragraph{Minimal Sum of Products (SOP):}
\[
F(A,B,C,D) = \bar{C} + BD + \bar{B}\bar{D}
\]
(Note that $BD + \bar{B}\bar{D} = \overline{B \oplus D} = B \odot D$, the XNOR equivalence).

\begin{schematicbox}{Logic Circuit Realization for Minimized $F(A,B,C,D) = \bar{C} + BD + \bar{B}\bar{D}$}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Gates
  \node[and gate US, draw, logic gate inputs=nn] (and1) at (3.5, 2.5) {};
  \node[and gate US, draw, logic gate inputs=nn] (and2) at (3.5, 0.8) {};
  \node[or gate US, draw, logic gate inputs=nnn, scale=1.2] (orgate) at (7.5, 1.65) {};

  % Input connections to AND1 (B, D)
  \draw[thick] (1.2, 2.75) node[left] {$B$} -- (and1.input 1);
  \draw[thick] (1.2, 2.25) node[left] {$D$} -- (and1.input 2);

  % Input connections to AND2 (\bar{B}, \bar{D})
  \draw[thick] (1.2, 1.05) node[left] {$\bar{B}$} -- (and2.input 1);
  \draw[thick] (1.2, 0.55) node[left] {$\bar{D}$} -- (and2.input 2);

  % Direct \bar{C} line
  \draw[thick] (1.2, 3.8) node[left] {$\bar{C}$} -- (5.5, 3.8) |- (orgate.input 1);

  % AND outputs to OR
  \draw[thick] (and1.output) -- ++(1.0, 0) |- (orgate.input 2);
  \draw[thick] (and2.output) -- ++(1.0, 0) |- (orgate.input 3);

  % Final Output
  \draw[thick] (orgate.output) -- ++(1.2, 0) node[right] {\large $\mathbf{F}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{F(A,B,C,D) = \bar{C} + BD + \bar{B}\bar{D} = \bar{C} + (B \odot D)}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: 3-Bit Magnitude Comparator Schematic [1 + 5 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q5)}
What is a magnitude comparator? Design a 3-bit magnitude comparator.
\end{questionbox}

\paragraph{Part (a): Definition of Magnitude Comparator [1 Mark]}
A \textbf{magnitude comparator} is a combinational logic circuit that compares two binary numbers $A$ and $B$, generating three mutually exclusive digital outputs indicating whether $A > B$, $A = B$, or $A < B$.

\paragraph{Part (b): Design of 3-Bit Magnitude Comparator [5 Marks]}
Let the two 3-bit input numbers be:
\[
A = (A_2 A_1 A_0)_2, \qquad B = (B_2 B_1 B_0)_2
\]
where $A_2, B_2$ are the Most Significant Bits (MSBs) and $A_0, B_0$ are the Least Significant Bits (LSBs).

\paragraph{1. Equality Condition ($A = B$):}
Two numbers are equal if and only if all corresponding bits are identical:
\[
x_i = A_i \odot B_i = A_i B_i + \bar{A}_i \bar{B}_i \quad \text{for } i = 0, 1, 2
\]
Therefore, the equality output $(A = B)$ is:
\[
\mathbf{(A = B) = x_2 \cdot x_1 \cdot x_0}
\]

\paragraph{2. Greater Than Condition ($A > B$):}
$A$ is strictly greater than $B$ if:
\begin{itemize}
  \item The MSB of $A$ is 1 and MSB of $B$ is 0 ($A_2 > B_2 \implies A_2 \bar{B}_2$), OR
  \item MSBs are equal ($x_2=1$) and $A_1 > B_1$ ($A_1 \bar{B}_1$), OR
  \item MSBs and middle bits are equal ($x_2 x_1 = 1$) and $A_0 > B_0$ ($A_0 \bar{B}_0$).
\end{itemize}
\[
\mathbf{(A > B) = A_2 \bar{B}_2 + x_2 A_1 \bar{B}_1 + x_2 x_1 A_0 \bar{B}_0}
\]

\paragraph{3. Less Than Condition ($A < B$):}
By symmetric logic:
\[
\mathbf{(A < B) = \bar{A}_2 B_2 + x_2 \bar{A}_1 B_1 + x_2 x_1 \bar{A}_0 B_0}
\]

\begin{schematicbox}{3-Bit Magnitude Comparator Logic Schematic}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % XNOR gates for x2, x1, x0
  \node[xnor gate US, draw, logic gate inputs=nn] (xnor2) at (3.0, 5.0) {};
  \draw[thick] (1.0, 5.25) node[left] {$A_2$} -- (xnor2.input 1);
  \draw[thick] (1.0, 4.75) node[left] {$B_2$} -- (xnor2.input 2);
  \draw[thick] (xnor2.output) -- ++(0.8, 0) node[right] {$x_2$};

  \node[xnor gate US, draw, logic gate inputs=nn] (xnor1) at (3.0, 3.5) {};
  \draw[thick] (1.0, 3.75) node[left] {$A_1$} -- (xnor1.input 1);
  \draw[thick] (1.0, 3.25) node[left] {$B_1$} -- (xnor1.input 2);
  \draw[thick] (xnor1.output) -- ++(0.8, 0) node[right] {$x_1$};

  \node[xnor gate US, draw, logic gate inputs=nn] (xnor0) at (3.0, 2.0) {};
  \draw[thick] (1.0, 2.25) node[left] {$A_0$} -- (xnor0.input 1);
  \draw[thick] (1.0, 1.75) node[left] {$B_0$} -- (xnor0.input 2);
  \draw[thick] (xnor0.output) -- ++(0.8, 0) node[right] {$x_0$};

  % A = B AND Gate
  \node[and gate US, draw, logic gate inputs=nnn] (andEQ) at (7.0, 3.5) {};
  \draw[thick] (4.2, 5.0) |- (andEQ.input 1);
  \draw[thick] (4.2, 3.5) -- (andEQ.input 2);
  \draw[thick] (4.2, 2.0) |- (andEQ.input 3);
  \draw[thick] (andEQ.output) -- ++(1.0, 0) node[right] {\large $\mathbf{(A = B)}$};

  % A > B OR Gate and AND stages
  \node[or gate US, draw, logic gate inputs=nnn] (orGT) at (12.0, 5.0) {};
  \node[and gate US, draw, logic gate inputs=nn] (andGT1) at (9.5, 4.8) {};
  \node[and gate US, draw, logic gate inputs=nnn] (andGT2) at (9.5, 3.8) {};

  \draw[thick] (7.5, 5.8) node[left] {$A_2 \bar{B}_2$} -- ++(2.5, 0) |- (orGT.input 1);
  \draw[thick] (andGT1.output) -- (orGT.input 2);
  \draw[thick] (andGT2.output) -- ++(0.5, 0) |- (orGT.input 3);
  \draw[thick] (orGT.output) -- ++(1.0, 0) node[right] {\large $\mathbf{(A > B)}$};

  % A < B OR Gate and AND stages
  \node[or gate US, draw, logic gate inputs=nnn] (orLT) at (12.0, 1.5) {};
  \node[and gate US, draw, logic gate inputs=nn] (andLT1) at (9.5, 1.3) {};
  \node[and gate US, draw, logic gate inputs=nnn] (andLT2) at (9.5, 0.3) {};

  \draw[thick] (7.5, 2.3) node[left] {$\bar{A}_2 B_2$} -- ++(2.5, 0) |- (orLT.input 1);
  \draw[thick] (andLT1.output) -- (orLT.input 2);
  \draw[thick] (andLT2.output) -- ++(0.5, 0) |- (orLT.input 3);
  \draw[thick] (orLT.output) -- ++(1.0, 0) node[right] {\large $\mathbf{(A < B)}$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\begin{align*}
(A = B) &= x_2 x_1 x_0 \\
(A > B) &= A_2 \bar{B}_2 + x_2 A_1 \bar{B}_1 + x_2 x_1 A_0 \bar{B}_0 \\
(A < B) &= \bar{A}_2 B_2 + x_2 \bar{A}_1 B_1 + x_2 x_1 \bar{A}_0 B_0
\end{align*}
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: Full Adder Using Multiplexers [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q6)}
Implement a full adder circuit using Multiplexer.
\end{questionbox}

A full adder adds three 1-bit binary inputs: Augend ($A$), Addend ($B$), and Carry In ($C_{\text{in}}$). It generates Sum ($S$) and Carry Out ($C_{\text{out}}$).

\paragraph{Truth Table:}
\begin{center}
\begin{tabular}{|ccc||cc|}
\hline
$A$ & $B$ & $C_{\text{in}}$ & $\mathbf{S\ (Sum)}$ & $\mathbf{C_{\text{out}}\ (Carry)}$ \\ \hline
0 & 0 & 0 & 0 & 0 \\ \hline
0 & 0 & 1 & 1 & 0 \\ \hline
0 & 1 & 0 & 1 & 0 \\ \hline
0 & 1 & 1 & 0 & 1 \\ \hline
1 & 0 & 0 & 1 & 0 \\ \hline
1 & 0 & 1 & 0 & 1 \\ \hline
1 & 1 & 0 & 0 & 1 \\ \hline
1 & 1 & 1 & 1 & 1 \\ \hline
\end{tabular}
\end{center}
\[
S(A,B,C_{\text{in}}) = \sum m(1, 2, 4, 7), \qquad C_{\text{out}}(A,B,C_{\text{in}}) = \sum m(3, 5, 6, 7)
\]

\paragraph{Multiplexer Implementation using Two $4:1$ MUXes:}
Let select lines be $S_1 = A, S_0 = B$:
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Select Inputs} $(A, B)$ & \textbf{Data Channel} & \textbf{Sum ($S$)} & \textbf{Carry Out ($C_{\text{out}}$)} \\ \hline
$00$ & $I_0$ & $C_{\text{in}}$ & $0\ (\text{GND})$ \\ \hline
$01$ & $I_1$ & $\bar{C}_{\text{in}}$ & $C_{\text{in}}$ \\ \hline
$10$ & $I_2$ & $\bar{C}_{\text{in}}$ & $C_{\text{in}}$ \\ \hline
$11$ & $I_3$ & $C_{\text{in}}$ & $1\ (V_{CC})$ \\ \hline
\end{tabular}
\end{center}

\begin{schematicbox}{Full Adder Implementation Using Two 4:1 Multiplexers}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % MUX 1: Sum
  \draw[thick, fill=boxbg] (0, 0) rectangle (3.2, 5.0);
  \node at (1.6, 4.5) {\textbf{4:1 MUX}};
  \node at (1.6, 4.0) {\small (Sum)};
  \node[anchor=west] at (0.2, 3.2) {\small $I_0$};
  \node[anchor=west] at (0.2, 2.4) {\small $I_1$};
  \node[anchor=west] at (0.2, 1.6) {\small $I_2$};
  \node[anchor=west] at (0.2, 0.8) {\small $I_3$};
  \node[anchor=north] at (1.0, 0) {\small $S_1$};
  \node[anchor=north] at (2.2, 0) {\small $S_0$};
  \draw[thick] (3.2, 2.5) -- ++(1.0, 0) node[right] {\large $\mathbf{S}$};

  % MUX 2: Carry Out
  \draw[thick, fill=boxbg] (7.5, 0) rectangle (10.7, 5.0);
  \node at (9.1, 4.5) {\textbf{4:1 MUX}};
  \node at (9.1, 4.0) {\small (Carry Out)};
  \node[anchor=west] at (7.7, 3.2) {\small $I_0$};
  \node[anchor=west] at (7.7, 2.4) {\small $I_1$};
  \node[anchor=west] at (7.7, 1.6) {\small $I_2$};
  \node[anchor=west] at (7.7, 0.8) {\small $I_3$};
  \node[anchor=north] at (8.5, 0) {\small $S_1$};
  \node[anchor=north] at (9.7, 0) {\small $S_0$};
  \draw[thick] (10.7, 2.5) -- ++(1.0, 0) node[right] {\large $\mathbf{C_{\text{out}}}$};

  % Input Rails on Left
  \draw[thick] (-3.0, 3.2) -- (-2.2, 3.2) node[left, at start] {$\mathbf{C_{\text{in}}}$};
  \node[not gate US, draw, scale=0.8] (not1) at (-1.4, 2.0) {};
  \draw[thick] (-2.2, 3.2) -- (-0.2, 3.2) -- (0, 3.2);
  \draw[thick] (-2.2, 3.2) |- (not1.input);
  \draw[thick] (not1.output) -- (-0.4, 2.0);
  \draw[thick] (-0.4, 2.0) |- (0, 2.4);
  \draw[thick] (-0.4, 2.0) |- (0, 1.6);
  \draw[thick] (-0.2, 3.2) |- (0, 0.8);

  % MUX 2 inputs
  \draw[thick] (5.5, 3.2) node[left] {$\mathbf{0\ (\text{GND})}$} -- (7.5, 3.2);
  \draw[thick] (5.5, 2.4) node[left] {$\mathbf{C_{\text{in}}}$} -- (7.5, 2.4);
  \draw[thick] (5.5, 1.6) node[left] {$\mathbf{C_{\text{in}}}$} -- (7.5, 1.6);
  \draw[thick] (5.5, 0.8) node[left] {$\mathbf{1\ (V_{CC})}$} -- (7.5, 0.8);

  % Common Select lines A, B
  \draw[thick] (-2.0, -1.0) node[left] {$\mathbf{A}$} -- (1.0, -1.0) -- (1.0, 0);
  \draw[thick] (1.0, -1.0) -- (8.5, -1.0) -- (8.5, 0);
  \draw[thick] (-2.0, -1.6) node[left] {$\mathbf{B}$} -- (2.2, -1.6) -- (2.2, 0);
  \draw[thick] (2.2, -1.6) -- (9.7, -1.6) -- (9.7, 0);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
\textbf{Sum ($S$):} $I_0 = C_{\text{in}}, I_1 = \bar{C}_{\text{in}}, I_2 = \bar{C}_{\text{in}}, I_3 = C_{\text{in}}$.\\
\textbf{Carry Out ($C_{\text{out}}$):} $I_0 = 0, I_1 = C_{\text{in}}, I_2 = C_{\text{in}}, I_3 = 1$, with select lines $S_1 = A, S_0 = B$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: SR to JK Flip-Flop Conversion Schematic [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q7)}
Differentiate between combinational circuit and sequential circuit. With necessary steps and implementation, convert an SR flip-flop into a JK flip-flop.
\end{questionbox}

\paragraph{Part (a): Combinational vs. Sequential Circuits [2 Marks]}
\begin{center}
\small
\begin{tabular}{@{}p{3.2cm}p{6.8cm}p{6.8cm}@{}}
\toprule
\textbf{Parameter} & \textbf{Combinational Circuit} & \textbf{Sequential Circuit} \\
\midrule
\textbf{Output Dependence} & Depends strictly on the present inputs at that instant. & Depends on both present inputs and the past history (internal stored state). \\
\textbf{Memory Elements} & Contains no memory elements or feedback paths. & Contains memory elements (flip-flops, latches) with feedback loops. \\
\textbf{Clock Synchronization} & Clock signal is not required; operates asynchronously. & Usually driven by a synchronous master clock signal. \\
\textbf{Design Complexity} & Simple (Boolean algebraic minimization, K-maps). & Complex (State tables, state diagrams, FSM models). \\
\textbf{Examples} & Adders, Subtractors, Multiplexers, Decoders. & Flip-flops, Counters, Shift registers, CPUs. \\
\bottomrule
\end{tabular}
\end{center}

\paragraph{Part (b): Conversion of SR Flip-Flop into JK Flip-Flop [5 Marks]}
\begin{enumerate}
  \item \textbf{Target:} JK Flip-Flop with inputs $J, K$, present state $Q_n$, next state $Q_{n+1}$.
  \item \textbf{Available:} SR Flip-Flop with excitation requirements:
  \[
  \begin{array}{cc|cc}
  Q_n & Q_{n+1} & S & R \\ \hline
  0 & 0 & 0 & X \\
  0 & 1 & 1 & 0 \\
  1 & 0 & 0 & 1 \\
  1 & 1 & X & 0
  \end{array}
  \]
\end{enumerate}

\paragraph{Conversion Table:}
\begin{center}
\begin{tabular}{|ccc||c||cc|}
\hline
$\mathbf{J}$ & $\mathbf{K}$ & $\mathbf{Q_n}$ & $\mathbf{Q_{n+1}}$ & $\mathbf{S}$ & $\mathbf{R}$ \\ \hline
0 & 0 & 0 & 0 & 0 & $X$ \\ \hline
0 & 0 & 1 & 1 & $X$ & 0 \\ \hline
0 & 1 & 0 & 0 & 0 & $X$ \\ \hline
0 & 1 & 1 & 0 & 0 & 1 \\ \hline
1 & 0 & 0 & 1 & 1 & 0 \\ \hline
1 & 0 & 1 & 1 & $X$ & 0 \\ \hline
1 & 1 & 0 & 1 & 1 & 0 \\ \hline
1 & 1 & 1 & 0 & 0 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{K-Map Minimization for $S$ and $R$:}
\begin{itemize}
  \item For $S(J, K, Q_n)$: Minterms are $m_4, m_6$; Don't cares are $d_1, d_5 \implies \mathbf{S = J\bar{Q}_n}$.
  \item For $R(J, K, Q_n)$: Minterms are $m_3, m_7$; Don't cares are $d_0, d_2 \implies \mathbf{R = KQ_n}$.
\end{itemize}

\begin{schematicbox}{SR Flip-Flop Converted to JK Flip-Flop}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % SR Flip Flop Box
  \draw[thick, fill=boxbg] (7.0, 0) rectangle (10.5, 4.0);
  \node at (8.75, 3.4) {\textbf{SR Flip-Flop}};
  \node[anchor=west] at (7.2, 2.8) {\small $S$};
  \node[anchor=west] at (7.2, 2.0) {\small $>$ \text{CLK}};
  \node[anchor=west] at (7.2, 1.2) {\small $R$};
  \node[anchor=east] at (10.3, 2.8) {\small $Q$};
  \node[anchor=east] at (10.3, 1.2) {\small $\bar{Q}$};

  % Clock line
  \draw[thick] (5.5, 2.0) -- (7.0, 2.0) node[left, at start] {\large $\mathbf{\text{CLK}}$};

  % AND gates on Left
  \node[and gate US, draw, logic gate inputs=nn] (andS) at (4.5, 2.8) {};
  \node[and gate US, draw, logic gate inputs=nn] (andR) at (4.5, 1.2) {};

  \draw[thick] (andS.output) -- (7.0, 2.8);
  \draw[thick] (andR.output) -- (7.0, 1.2);

  % Inputs J and K
  \draw[thick] (1.5, 3.0) node[left] {\large $\mathbf{J}$} -- (andS.input 1);
  \draw[thick] (1.5, 1.0) node[left] {\large $\mathbf{K}$} -- (andR.input 2);

  % Outputs Q and Q_bar
  \draw[thick] (10.5, 2.8) -- ++(1.5, 0) node[right] {\large $\mathbf{Q}$};
  \draw[thick] (10.5, 1.2) -- ++(1.5, 0) node[right] {\large $\mathbf{\bar{Q}}$};

  % Feedback Q to andR.input 1
  \filldraw[black] (11.2, 2.8) circle (2pt);
  \draw[thick] (11.2, 2.8) -- (11.2, -0.6) -- (3.2, -0.6) |- (andR.input 1);

  % Feedback Q_bar to andS.input 2
  \filldraw[black] (11.6, 1.2) circle (2pt);
  \draw[thick] (11.6, 1.2) -- (11.6, 4.4) -- (3.2, 4.4) |- (andS.input 2);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{S = J\bar{Q}, \qquad R = KQ}$$
An SR flip-flop is converted into a JK flip-flop by connecting $S = J\bar{Q}$ and $R = KQ$. This eliminates the invalid state ($S=R=1$) and enables toggling ($J=K=1$).
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: Types of Shift Registers \& 4-Bit Johnson Counter [2 + 3 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q8)}
Write briefly about different types of shift registers. With necessary circuit and timing diagrams, explain the operation of how the shift register is used as a Johnson's Counter.
\end{questionbox}

\paragraph{Part (a): Classification of Shift Registers [2 Marks]}
\begin{enumerate}
  \item \textbf{SISO (Serial-In Serial-Out):} Data loaded and retrieved serially. Used for time delay generation.
  \item \textbf{SIPO (Serial-In Parallel-Out):} Data loaded serially and read out in parallel. Used for serial-to-parallel data conversion.
  \item \textbf{PISO (Parallel-In Serial-Out):} Data loaded simultaneously in parallel and shifted out serially. Used in serial transmitters (e.g. UART).
  \item \textbf{PIPO (Parallel-In Parallel-Out):} Data loaded and read out simultaneously. Used as general-purpose internal CPU registers.
  \item \textbf{Bidirectional / Universal Shift Register:} Can shift data left, right, load parallel data, or hold state based on mode select lines.
\end{enumerate}

\paragraph{Part (b): 4-Bit Johnson (Twisted Ring) Counter [3 Marks]}
A \textbf{Johnson Counter} (or Moebius Counter) is constructed from an $n$-bit shift register by connecting the inverted output of the last stage ($\bar{Q}_3$) back to the data input of the first stage ($D_0$):
\[
D_0 = \bar{Q}_3
\]
An $n$-bit Johnson counter yields $2n$ unique states ($2 \times 4 = 8$ states for a 4-bit register), compared to $n$ states for a standard ring counter.

\begin{schematicbox}{4-Bit Johnson (Twisted-Ring) Counter Circuit Schematic}
\centering
\begin{tikzpicture}[scale=0.88, transform shape]
  % 4 D Flip Flops
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({3.6*\i}, 0) rectangle ({3.6*\i + 2.4}, 3.2);
    \node at ({3.6*\i + 1.2}, 2.7) {\textbf{FF\i\ (D)}};
    \node[anchor=west] at ({3.6*\i + 0.2}, 1.8) {\small $D$};
    \node[anchor=west] at ({3.6*\i + 0.2}, 0.8) {\small $>$};
    \node[anchor=east] at ({3.6*\i + 2.2}, 1.8) {\small $Q_\i$};
    \node[anchor=east] at ({3.6*\i + 2.2}, 0.8) {\small $\bar{Q}_\i$};
  }

  % Forward Shift Connections
  \draw[thick] (2.4, 1.8) -- (3.6, 1.8);
  \draw[thick] (6.0, 1.8) -- (7.2, 1.8);
  \draw[thick] (9.6, 1.8) -- (10.8, 1.8);

  % Inverted Feedback from FF3 Q_bar to FF0 D
  \draw[thick] (13.2, 0.8) -- (13.8, 0.8) -- (13.8, -1.2) -- (-0.6, -1.2) |- (0, 1.8);

  % Common Synchronous Clock
  \draw[thick] (-1.0, -0.5) node[left] {\large $\mathbf{\text{CLK}}$} -- (12.0, -0.5);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({3.6*\i + 0.4}, -0.5) -- ({3.6*\i + 0.4}, 0.8) -- ({3.6*\i + 0.2}, 0.8);
  }
\end{tikzpicture}
\end{schematicbox}

\paragraph{State Sequence Table (8 Distinct States):}
\begin{center}
\begin{tabular}{|c|cccc|l|}
\hline
\textbf{Clock Pulse} & $\mathbf{Q_0}$ & $\mathbf{Q_1}$ & $\mathbf{Q_2}$ & $\mathbf{Q_3}$ & \textbf{Next Input $D_0 = \bar{Q}_3$} \\ \hline
0 (Initial) & 0 & 0 & 0 & 0 & $D_0 = \bar{0} = 1$ \\ \hline
1 & 1 & 0 & 0 & 0 & $D_0 = \bar{0} = 1$ \\ \hline
2 & 1 & 1 & 0 & 0 & $D_0 = \bar{0} = 1$ \\ \hline
3 & 1 & 1 & 1 & 0 & $D_0 = \bar{0} = 1$ \\ \hline
4 & 1 & 1 & 1 & 1 & $D_0 = \bar{1} = 0$ \\ \hline
5 & 0 & 1 & 1 & 1 & $D_0 = \bar{1} = 0$ \\ \hline
6 & 0 & 0 & 1 & 1 & $D_0 = \bar{1} = 0$ \\ \hline
7 & 0 & 0 & 0 & 1 & $D_0 = \bar{1} = 0$ \\ \hline
8 (Recycles) & 0 & 0 & 0 & 0 & Recycles to state 0 \\ \hline
\end{tabular}
\end{center}

\begin{answerbox}
A 4-bit Johnson counter provides $\mathbf{2n = 8}$ decoding states with adjacent states differing by only a single bit (Gray-code property), operating as a divide-by-8 frequency scaler.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: 3-Bit Ripple UP Counter with Positive Edge Triggering [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q9)}
Describe the operation of 3-bit ripple up counter with positive edge triggered clock.
\end{questionbox}

A \textbf{3-Bit Ripple UP Counter} counts through 8 binary states from $000_2$ to $111_2$. 

\paragraph{Clocking Principle for Positive-Edge Triggered Flip-Flops:}
\begin{itemize}
  \item In a ripple UP counter, the next higher bit $Q_{i+1}$ must toggle whenever the current bit $Q_i$ transitions from $\mathbf{1 \to 0}$.
  \item Since the flip-flops are \textbf{positive edge-triggered} ($\uparrow$, triggering on $0 \to 1$), the transition $Q_i: 1 \to 0$ corresponds to inverted output $\bar{Q}_i: 0 \to 1$.
  \item Therefore, to achieve UP counting with positive-edge triggered flip-flops, the clock input of each subsequent flip-flop must be driven by the \textbf{complementary output $\bar{Q}$} of the preceding stage:
  \[
  \text{CLK}_{i+1} = \bar{Q}_i
  \]
\end{itemize}

\begin{schematicbox}{3-Bit Positive-Edge Triggered Ripple UP Counter}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % 3 JK Flip Flops
  \foreach \i in {0,1,2} {
    \draw[thick, fill=boxbg] ({4.0*\i}, 0) rectangle ({4.0*\i + 2.6}, 3.4);
    \node at ({4.0*\i + 1.3}, 2.9) {\textbf{FF\i\ (T/JK)}};
    \node[anchor=west] at ({4.0*\i + 0.2}, 2.2) {\small $J=1$};
    \node[anchor=west] at ({4.0*\i + 0.2}, 1.5) {\small $>$};
    \node[anchor=west] at ({4.0*\i + 0.2}, 0.8) {\small $K=1$};
    \node[anchor=east] at ({4.0*\i + 2.4}, 2.2) {\small $Q$};
    \node[anchor=east] at ({4.0*\i + 2.4}, 0.8) {\small $\bar{Q}$};

    % Output pins
    \filldraw[black] ({4.0*\i + 3.0}, 2.2) circle (2pt);
    \draw[thick] ({4.0*\i + 2.6}, 2.2) -- ({4.0*\i + 3.0}, 2.2) -- ({4.0*\i + 3.0}, 4.2) node[above] {\large $\mathbf{Q_\i}$};
  }

  % External Clock to FF0
  \draw[thick] (-1.2, 1.5) node[left] {\large $\mathbf{\text{CLK}}$} -- (0, 1.5);

  % Ripple Connections: Q_bar_i -> CLK_{i+1}
  \draw[thick] (2.6, 0.8) -- (3.2, 0.8) |- (4.0, 1.5);
  \draw[thick] (6.6, 0.8) -- (7.2, 0.8) |- (8.0, 1.5);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
By connecting $\text{CLK}_{i+1} = \bar{Q}_i$, the positive-edge triggered flip-flops toggle on every $1 \to 0$ transition of $Q_i$, producing the standard binary UP counting sequence: $\mathbf{000 \to 001 \to 010 \to 011 \to 100 \to 101 \to 110 \to 111 \to 000}$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: Synchronous Mod-6 Counter Using SR Flip-Flops [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q10)}
Design the synchronous mod-6 counter using S-R flip-flop and draw its timing diagram also.
\end{questionbox}

A \textbf{Synchronous Mod-6 Counter} counts through 6 states: $000 \to 001 \to 010 \to 011 \to 100 \to 101 \to 000$. Requires $N = 3$ flip-flops ($2^2 < 6 \le 2^3$). Unused states: $110, 111$ (Don't Cares).

\paragraph{1. State Transition and SR Excitation Table:}
\begin{center}
\begin{tabular}{|c|ccc|ccc|cccccc|}
\hline
\textbf{State} & \multicolumn{3}{c|}{\textbf{Present State}} & \multicolumn{3}{c|}{\textbf{Next State}} & \multicolumn{6}{c|}{\textbf{SR Flip-Flop Inputs}} \\
& $Q_2$ & $Q_1$ & $Q_0$ & $Q_2^+$ & $Q_1^+$ & $Q_0^+$ & $\mathbf{S_2}$ & $\mathbf{R_2}$ & $\mathbf{S_1}$ & $\mathbf{R_1}$ & $\mathbf{S_0}$ & $\mathbf{R_0}$ \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & $X$ & 0 & $X$ & 1 & 0 \\ \hline
1 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & $X$ & 1 & 0 & 0 & 1 \\ \hline
2 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & $X$ & $X$ & 0 & 1 & 0 \\ \hline
3 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 \\ \hline
4 & 1 & 0 & 0 & 1 & 0 & 1 & $X$ & 0 & 0 & $X$ & 1 & 0 \\ \hline
5 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & $X$ & 0 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{2. Minimized Equations via K-Maps:}
\begin{align*}
S_0 &= \bar{Q}_0, \qquad R_0 = Q_0 \\
S_1 &= \bar{Q}_2 \bar{Q}_1 Q_0, \qquad R_1 = Q_1 Q_0 \\
S_2 &= Q_1 Q_0, \qquad R_2 = Q_2 Q_0
\end{align*}

\paragraph{3. Self-Starting \& Lock-out Verification:}
\begin{itemize}
  \item If in state $110_2$: $S_0=1, R_0=0 \implies Q_0^+=1$; $S_1=0, R_1=0 \implies Q_1^+=1$; $S_2=0, R_2=0 \implies Q_2^+=1 \implies \text{Next State } 111_2$.
  \item If in state $111_2$: $S_0=0, R_0=1 \implies Q_0^+=0$; $S_1=0, R_1=1 \implies Q_1^+=0$; $S_2=0, R_2=1 \implies Q_2^+=0 \implies \text{Next State } 000_2$ (Valid state!).
\end{itemize}
Thus, the counter is completely self-starting and cannot get trapped in unused states.

\begin{schematicbox}{Synchronous Mod-6 Counter Logic Circuit Using SR Flip-Flops}
\centering
\begin{tikzpicture}[scale=0.70, transform shape]
  % 3 SR Flip Flops (Width 2.0 each, wide 3.6cm inter-stage gaps)
  % FF0: x in [0, 2.0]
  % FF1: x in [5.6, 7.6]
  % FF2: x in [11.2, 13.2]
  \foreach \i/\xpos in {0/0, 1/5.6, 2/11.2} {
    \draw[thick, fill=boxbg] (\xpos, 0) rectangle (\xpos + 2.0, 3.6);
    \node at (\xpos + 1.0, 3.1) {\textbf{FF\i\ (SR)}};
    \node[anchor=west] at (\xpos + 0.2, 2.4) {\small $S$};
    \node[anchor=west] at (\xpos + 0.2, 1.6) {\small $>$};
    \node[anchor=west] at (\xpos + 0.2, 0.8) {\small $R$};
    \node[anchor=east] at (\xpos + 1.8, 2.4) {\small $Q_\i$};
    \node[anchor=east] at (\xpos + 1.8, 0.8) {\small $\bar{Q}_\i$};

    \filldraw[black] (\xpos + 2.4, 2.4) circle (2pt);
    \draw[thick] (\xpos + 2.0, 2.4) -- (\xpos + 2.4, 2.4) -- (\xpos + 2.4, 4.4) node[above] {\large $\mathbf{Q_\i}$};
  }

  % Common Synchronous Clock
  \draw[thick] (-1.0, -1.0) node[left] {\large $\mathbf{\text{CLK}}$} -- (12.5, -1.0);
  \foreach \xpos in {0, 5.6, 11.2} {
    \draw[thick] (\xpos + 0.5, -1.0) -- (\xpos + 0.5, 1.6) -- (\xpos + 0.2, 1.6);
  }

  % FF0 Connections: S0 = Q0_bar (over top), R0 = Q0 (under bottom)
  \draw[thick] (2.0, 0.8) -- (2.3, 0.8) -- (2.3, 4.2) -- (-0.4, 4.2) |- (0, 2.4); % S0 = Q0_bar
  \draw[thick] (2.0, 2.4) -- (2.3, 2.4) -- (2.3, -0.5) -- (-0.4, -0.5) |- (0, 0.8); % R0 = Q0

  % Logic for S1 = Q2_bar . Q1_bar . Q0 (centered in gap [2.3, 5.6])
  \node[and gate US, draw, logic gate inputs=nnn] (andS1) at (4.7, 2.4) {};
  \draw[thick] (3.8, 2.6) node[left] {\footnotesize $\bar{Q}_2$} -- (andS1.input 1);
  \draw[thick] (3.8, 2.4) node[left] {\footnotesize $\bar{Q}_1$} -- (andS1.input 2);
  \draw[thick] (3.8, 2.2) node[left] {\footnotesize $Q_0$} -- (andS1.input 3);
  \draw[thick] (andS1.output) -- (5.6, 2.4);

  % AND Gate for S2 = Q1.Q0 and R1 = Q1.Q0 (in gap [7.6, 11.2])
  \node[and gate US, draw, logic gate inputs=nn] (andQ1Q0) at (10.2, 2.4) {};
  \draw[thick] (9.3, 2.55) node[left] {\footnotesize $Q_1$} -- (andQ1Q0.input 1);
  \draw[thick] (9.3, 2.25) node[left] {\footnotesize $Q_0$} -- (andQ1Q0.input 2);
  \draw[thick] (andQ1Q0.output) -- (11.2, 2.4); % S2
  \draw[thick] (10.7, 2.4) -- (10.7, -0.4) -- (5.1, -0.4) |- (5.6, 0.8); % R1

  % Logic for R2 = Q2 . Q0 (in gap [7.6, 11.2])
  \node[and gate US, draw, logic gate inputs=nn] (andR2) at (10.2, 0.8) {};
  \draw[thick] (9.3, 0.95) node[left] {\footnotesize $Q_2$} -- (andR2.input 1);
  \draw[thick] (9.3, 0.65) node[left] {\footnotesize $Q_0$} -- (andR2.input 2);
  \draw[thick] (andR2.output) -- (11.2, 0.8);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{S_0 = \bar{Q}_0, \ R_0 = Q_0, \quad S_1 = \bar{Q}_2 \bar{Q}_1 Q_0, \ R_1 = Q_1 Q_0, \quad S_2 = Q_1 Q_0, \ R_2 = Q_2 Q_0}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 11
% =========================================================================
\subsection{Question 11: Synchronous FSM Sequence Detector '110' [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q11)}
Design a synchronous sequential machine that has 1-bit serial input $X$ and output $Z$ which will be high when the input contains the message `110' (Use SR Flip-Flop).
\end{questionbox}

\paragraph{1. State Definitions (Mealy Model):}
\begin{itemize}
  \item $S_0 (00)$: Reset state / No relevant bit detected.
  \item $S_1 (01)$: Pattern `1' detected.
  \item $S_2 (10)$: Pattern `11' detected.
  \item When in $S_2$ and $X=0 \implies$ `110' detected $\implies Z=1$, next state $S_0$.
\end{itemize}

\begin{schematicbox}{State Diagram for '110' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.2cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$X=0 / 0$} (S0)
             edge [bend left] node {$X=1 / 0$} (S1)
        (S1) edge [loop above] node {$X=1 / 0$} (S2)
             edge [bend left] node {$X=0 / 0$} (S0)
        (S2) edge [loop above] node {$X=1 / 0$} (S2)
             edge [bend left=45] node {$X=0 / 1$} (S0);
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. State Transition \& SR Excitation Table (Flip-Flops $A, B$):}
\begin{center}
\begin{tabular}{|cc|c|cc|c|cccc|}
\hline
\multicolumn{2}{|c|}{\textbf{Present State}} & \textbf{Input} & \multicolumn{2}{c|}{\textbf{Next State}} & \textbf{Output} & \multicolumn{4}{c|}{\textbf{SR Inputs}} \\
$A$ & $B$ & $X$ & $A^+$ & $B^+$ & $\mathbf{Z}$ & $\mathbf{S_A}$ & $\mathbf{R_A}$ & $\mathbf{S_B}$ & $\mathbf{R_B}$ \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & $X$ & 0 & $X$ \\ \hline
0 & 0 & 1 & 0 & 1 & 0 & 0 & $X$ & 1 & 0 \\ \hline
0 & 1 & 0 & 0 & 0 & 0 & 0 & $X$ & 0 & 1 \\ \hline
0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\ \hline
1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & $X$ \\ \hline
1 & 0 & 1 & 1 & 0 & 0 & $X$ & 0 & 0 & $X$ \\ \hline
1 & 1 & 0 & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ \\ \hline
1 & 1 & 1 & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ \\ \hline
\end{tabular}
\end{center}

\paragraph{3. Minimized Equations via K-Maps:}
\begin{align*}
S_A &= BX, \qquad R_A = \bar{X} \\
S_B &= \bar{A}\bar{B}X, \qquad R_B = \bar{X} + B \\
Z &= A\bar{X}
\end{align*}

\begin{answerbox}
$$\mathbf{S_A = BX, \quad R_A = \bar{X}, \quad S_B = \bar{A}\bar{B}X, \quad R_B = \bar{X} + B, \quad Z = A\bar{X}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 12
% =========================================================================
\subsection{Question 12: Frequency Counter Block Diagram [3 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q12)}
Write a short note on frequency counter.
\end{questionbox}

A \textbf{Digital Frequency Counter} is an electronic test instrument that accurately measures the frequency of an unknown periodic input signal by counting the number of cycles ($N$) that occur during a precisely controlled time window ($T_{\text{gate}}$):
\[
f_x = \frac{N}{T_{\text{gate}}}
\]

\paragraph{Core Functional Subsystems:}
\begin{enumerate}
  \item \textbf{Input Attenuator \& Amplifier:} Scales input voltage to safe operational levels.
  \item \textbf{Schmitt Trigger (Wave Shaper):} Converts arbitrary input waveforms (sinusoidal, triangular) into sharp, clean digital rectangular pulses.
  \item \textbf{Crystal Oscillator \& Time Base Generator:} Highly stable quartz crystal oscillator (e.g. 1 MHz or 10 MHz) paired with decade frequency dividers to produce accurate gate periods ($1\text{ ms}, 10\text{ ms}, 0.1\text{ s}, 1\text{ s}$).
  \item \textbf{Main Gate (AND Gate):} Enabled for exactly $T_{\text{gate}}$, passing $N$ input pulses to the counter.
  \item \textbf{Decade Counter, Latch, \& Display:} Counts incoming pulses, latches the result, and drives 7-segment digital displays.
\end{enumerate}

\begin{schematicbox}{Functional Block Diagram of a Digital Frequency Counter}
\centering
\begin{tikzpicture}[scale=0.88, transform shape, >=Stealth]
  % Input blocks
  \node[draw, thick, fill=boxbg, minimum width=2.0cm, minimum height=1.2cm, align=center] (amp) at (0, 3) {Input\\Amplifier};
  \node[draw, thick, fill=boxbg, minimum width=2.2cm, minimum height=1.2cm, align=center] (schmitt) at (3.2, 3) {Schmitt\\Trigger};
  \node[draw, thick, fill=boxbg, minimum width=1.6cm, minimum height=1.2cm, align=center] (gate) at (6.5, 3) {Main AND\\Gate};
  \node[draw, thick, fill=boxbg, minimum width=2.4cm, minimum height=1.2cm, align=center] (counter) at (10.0, 3) {Decade\\Counters};
  \node[draw, thick, fill=boxbg, minimum width=2.2cm, minimum height=1.2cm, align=center] (disp) at (13.5, 3) {Latch \&\\Display};

  \draw[thick, ->] (-2.0, 3) node[left] {Input $f_x$} -- (amp.west);
  \draw[thick, ->] (amp.east) -- (schmitt.west);
  \draw[thick, ->] (schmitt.east) -- (gate.west);
  \draw[thick, ->] (gate.east) -- (counter.west);
  \draw[thick, ->] (counter.east) -- (disp.west);

  % Time base blocks
  \node[draw, thick, fill=boxbg, minimum width=2.2cm, minimum height=1.2cm, align=center] (osc) at (0, 0) {Crystal\\Oscillator};
  \node[draw, thick, fill=boxbg, minimum width=2.4cm, minimum height=1.2cm, align=center] (div) at (3.2, 0) {Time Base\\Dividers};
  \node[draw, thick, fill=boxbg, minimum width=2.2cm, minimum height=1.2cm, align=center] (gctrl) at (6.5, 0) {Gate Control\\Flip-Flop};

  \draw[thick, ->] (osc.east) -- (div.west);
  \draw[thick, ->] (div.east) -- (gctrl.west);
  \draw[thick, ->] (gctrl.north) -- (gate.south) node[midway, right] {Gate Enable ($T_{\text{gate}}$)};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
A frequency counter counts incoming signal transitions over a precision gate window $T_{\text{gate}}$, calculating frequency via $\mathbf{f = N / T_{\text{gate}}}$.
\end{answerbox}
"""
