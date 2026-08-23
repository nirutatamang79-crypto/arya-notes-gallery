# dl_ch3_2082_baishakh.py
# Chapter 3: 2082 Baishakh Examination Master Solutions

def get_chapter_2082_baishakh():
    return r"""
\chapter{2082 Baishakh Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BCT, BEI & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Digital Logic (EX 152) & \textbf{Examination Type:} Back (New Course) \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: ASCII Code \& 2's Complement Addition [1 + 3 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q1)}
Define an ASCII code. Use 2's complement method to perform the following addition $(-28 + 12)_{10}$ in 8-bit signed number representation.
\end{questionbox}

\paragraph{Part (a): Definition of ASCII Code [1 Mark]}
\textbf{ASCII} (\textit{American Standard Code for Information Interchange}) is a standardized alphanumeric character encoding scheme:
\begin{itemize}
  \item Standard ASCII uses a \textbf{7-bit binary code} to represent $2^7 = 128$ distinct characters, including English alphabets ($A-Z, a-z$), numerals ($0-9$), punctuation symbols, and non-printable control characters (e.g., CR, LF, ESC).
  \item Extended ASCII uses an \textbf{8-bit code} ($2^8 = 256$ characters) to accommodate graphical symbols and international characters.
\end{itemize}

\paragraph{Part (b): 2's Complement Addition of $(-28 + 12)_{10}$ in 8 Bits [3 Marks]}
\begin{enumerate}
  \item \textbf{Representation of $+12_{10}$ in 8-bit binary:}
  \[
  +12_{10} = \mathbf{0000\ 1100_2}
  \]
  \item \textbf{Representation of $-28_{10}$ in 8-bit 2's complement form:}
  \[
  +28_{10} = 0001\ 1100_2
  \]
  Take 1's complement: $\text{1's comp}(0001\ 1100) = 1110\ 0011_2$. \\
  Add 1:
  \[
  -28_{10} = 1110\ 0011 + 1 = \mathbf{1110\ 0100_2}
  \]
  \item \textbf{Perform 8-bit Binary Addition:}
  \[
  \begin{array}{r@{\quad}l}
    1110\ 0100 & (-28_{10}) \\
  +\ 0000\ 1100 & (+12_{10}) \\
  \hline
    \mathbf{1111\ 0000_2} & \text{(Result in 2's complement form)}
  \end{array}
  \]
  \item \textbf{Verification and Decimal Interpretation:}
  \begin{itemize}
    \item MSB $= 1 \implies$ Result is \textbf{negative}.
    \item Magnitude $= \text{2's complement of } 1111\ 0000_2 = (0000\ 1111)_2 + 1 = 0001\ 0000_2 = \mathbf{16_{10}}$.
    \item Therefore, result is $\mathbf{-16_{10}}$, which matches $-28 + 12 = -16$.
  \end{itemize}
\end{enumerate}

\begin{answerbox}
$$(-28 + 12)_{10} = \mathbf{(1111\ 0000)_2} = -16_{10}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: Boolean Algebra Proofs [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q2)}
Prove the following Boolean identities algebraically:
\begin{enumerate}[label=(\alph*)]
  \item $AB + \bar{A}C + BC = AB + \bar{A}C$
  \item $AB + C(A \oplus B) = BC + A(B+C)$
\end{enumerate}
\end{questionbox}

\paragraph{Part (a): Consensus Theorem Proof [2 Marks]}
To prove: $AB + \bar{A}C + BC = AB + \bar{A}C$.
\begin{align*}
\text{LHS} &= AB + \bar{A}C + BC \\
&= AB + \bar{A}C + BC(1) && \text{(Identity Law: } X \cdot 1 = X\text{)} \\
&= AB + \bar{A}C + BC(A + \bar{A}) && \text{(Complementarity Law: } A + \bar{A} = 1\text{)} \\
&= AB + \bar{A}C + ABC + \bar{A}BC && \text{(Distributive Law)} \\
&= (AB + ABC) + (\bar{A}C + \bar{A}BC) && \text{(Associative \& Commutative Laws)} \\
&= AB(1 + C) + \bar{A}C(1 + B) && \text{(Distributive Law)} \\
&= AB(1) + \bar{A}C(1) && \text{(Dominance Law: } 1 + X = 1\text{)} \\
&= AB + \bar{A}C = \text{RHS} \quad \blacksquare
\end{align*}

\paragraph{Part (b): Identity Proof [2 Marks]}
To prove: $AB + C(A \oplus B) = BC + A(B+C)$.
\begin{align*}
\text{LHS} &= AB + C(A \oplus B) \\
&= AB + C(A\bar{B} + \bar{A}B) && \text{(Definition of XOR: } A \oplus B = A\bar{B} + \bar{A}B\text{)} \\
&= AB + A\bar{B}C + \bar{A}BC \\
&= AB(1 + C) + A\bar{B}C + \bar{A}BC && \text{(Since } AB = AB(1+C) = AB + ABC\text{)} \\
&= AB + ABC + A\bar{B}C + \bar{A}BC \\
&= AB + AC(B + \bar{B}) + BC(A + \bar{A}) \\
&= AB + AC(1) + BC(1) \\
&= AB + AC + BC
\end{align*}
Now expanding the Right Hand Side (RHS):
\begin{align*}
\text{RHS} &= BC + A(B + C) \\
&= BC + AB + AC \\
&= AB + AC + BC
\end{align*}
Since $\text{LHS} = \text{RHS} = AB + AC + BC$, the identity is proved. $\blacksquare$

\begin{answerbox}
Both Boolean identities are formally verified using fundamental axioms and laws of Boolean algebra.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: Octal Priority Encoder Schematic [2 + 6 = 8 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q3)}
What is a decoder? Design an octal priority encoder with neat circuit diagram.
\end{questionbox}

\paragraph{Part (a): Definition of Decoder [2 Marks]}
A \textbf{decoder} is a combinational logic circuit with $n$ input lines and $2^n$ unique output lines. It decodes an $n$-bit binary code word by asserting exactly one output line HIGH (or active LOW) corresponding to the decimal equivalent of the input binary code.

\paragraph{Part (b): Design of Octal Priority Encoder (8-to-3) [6 Marks]}
An \textbf{Octal Priority Encoder} accepts 8 input lines $D_0, D_1, \dots, D_7$ where input $D_7$ has the highest priority and $D_0$ has the lowest priority. If multiple inputs are HIGH simultaneously, the output binary code $A_2 A_1 A_0$ reflects the highest-indexed active input. A \textbf{Valid Output} bit ($V$) indicates whether any input is active.

\paragraph{Truth Table:}
\begin{center}
\small
\begin{tabular}{|cccccccc||ccc|c|}
\hline
$D_7$ & $D_6$ & $D_5$ & $D_4$ & $D_3$ & $D_2$ & $D_1$ & $D_0$ & $\mathbf{A_2}$ & $\mathbf{A_1}$ & $\mathbf{A_0}$ & $\mathbf{V\ (Valid)}$ \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & $X$ & $X$ & $X$ & 0 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 1 & $X$ & 0 & 0 & 1 & 1 \\ \hline
0 & 0 & 0 & 0 & 0 & 1 & $X$ & $X$ & 0 & 1 & 0 & 1 \\ \hline
0 & 0 & 0 & 0 & 1 & $X$ & $X$ & $X$ & 0 & 1 & 1 & 1 \\ \hline
0 & 0 & 0 & 1 & $X$ & $X$ & $X$ & $X$ & 1 & 0 & 0 & 1 \\ \hline
0 & 0 & 1 & $X$ & $X$ & $X$ & $X$ & $X$ & 1 & 0 & 1 & 1 \\ \hline
0 & 1 & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ & 1 & 1 & 0 & 1 \\ \hline
1 & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ & $X$ & 1 & 1 & 1 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{Minimized Boolean Output Equations:}
\begin{align*}
A_2 &= D_4 + D_5 + D_6 + D_7 \\
A_1 &= D_6 + D_7 + \bar{D}_6 \bar{D}_5 (D_2 + D_3) = D_6 + D_7 + D_2 \bar{D}_4 \bar{D}_5 + D_3 \bar{D}_4 \bar{D}_5 \\
A_0 &= D_7 + D_5 \bar{D}_6 + D_3 \bar{D}_4 \bar{D}_6 + D_1 \bar{D}_2 \bar{D}_4 \bar{D}_6 \\
V &= D_0 + D_1 + D_2 + D_3 + D_4 + D_5 + D_6 + D_7
\end{align*}

\begin{schematicbox}{Octal (8-to-3) Priority Encoder Circuit Schematic}
\centering
\begin{tikzpicture}[scale=0.88, transform shape]
  % Inputs vertical rails
  \foreach \i in {0,1,...,7} {
    \draw[thick] ({1.3*\i}, 6.0) -- ({1.3*\i}, 0.5);
    \node[above] at ({1.3*\i}, 6.0) {$\mathbf{D_\i}$};
  }

  % Output OR Gates
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.1] (orA2) at (12.5, 4.8) {};
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.1] (orA1) at (12.5, 3.2) {};
  \node[or gate US, draw, logic gate inputs=nnnn, scale=1.1] (orA0) at (12.5, 1.6) {};
  \node[or gate US, draw, logic gate inputs=nnnnnnnn, scale=1.1] (orV) at (12.5, 0.0) {};

  % Output lines
  \draw[thick] (orA2.output) -- ++(1.0, 0) node[right] {\large $\mathbf{A_2}$};
  \draw[thick] (orA1.output) -- ++(1.0, 0) node[right] {\large $\mathbf{A_1}$};
  \draw[thick] (orA0.output) -- ++(1.0, 0) node[right] {\large $\mathbf{A_0}$};
  \draw[thick] (orV.output) -- ++(1.0, 0) node[right] {\large $\mathbf{V}$};

  % Wire OR A2 (D4, D5, D6, D7)
  \filldraw[black] ({1.3*4}, 5.1) circle (2pt); \draw[thick] ({1.3*4}, 5.1) -- (orA2.input 4);
  \filldraw[black] ({1.3*5}, 4.9) circle (2pt); \draw[thick] ({1.3*5}, 4.9) -- (orA2.input 3);
  \filldraw[black] ({1.3*6}, 4.7) circle (2pt); \draw[thick] ({1.3*6}, 4.7) -- (orA2.input 2);
  \filldraw[black] ({1.3*7}, 4.5) circle (2pt); \draw[thick] ({1.3*7}, 4.5) -- (orA2.input 1);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{A_2 = D_4 + D_5 + D_6 + D_7, \quad A_1 = D_6 + D_7 + \bar{D}_4\bar{D}_5(D_2 + D_3), \quad V = \sum_{i=0}^7 D_i}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: 3x8 Decoder Function Realization \& K-Map [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q4)}
Realize the Boolean function $X(A, B, C, D) = \sum m(0, 2, 3, 7, 8, 10, 11, 14, 15)$ using a single $3 \times 8$ decoder. Also simplify the logic function implementing K-map method.
\end{questionbox}

\paragraph{Part (a): Realization Using a Single $3 \times 8$ Decoder [3 Marks]}
Let variables $A, B, C$ be connected to decoder select inputs $S_2, S_1, S_0$, and let variable $D$ serve as external data input:
\begin{itemize}
  \item $Y_0 = \bar{A}\bar{B}\bar{C}$: includes $m_0(\bar{D}), m_1(D) \implies$ function has $m_0 \implies \mathbf{Y_0 \bar{D}}$.
  \item $Y_1 = \bar{A}\bar{B}C$: includes $m_2(\bar{D}), m_3(D) \implies$ function has both $m_2, m_3 \implies \mathbf{Y_1}$.
  \item $Y_2 = \bar{A}B\bar{C}$: includes $m_4, m_5 \implies 0$.
  \item $Y_3 = \bar{A}BC$: includes $m_6(\bar{D}), m_7(D) \implies$ function has $m_7 \implies \mathbf{Y_3 D}$.
  \item $Y_4 = A\bar{B}\bar{C}$: includes $m_8(\bar{D}), m_9(D) \implies$ function has $m_8 \implies \mathbf{Y_4 \bar{D}}$.
  \item $Y_5 = A\bar{B}C$: includes $m_{10}(\bar{D}), m_{11}(D) \implies$ function has both $m_{10}, m_{11} \implies \mathbf{Y_5}$.
  \item $Y_6 = AB\bar{C}$: includes $m_{12}, m_{13} \implies 0$.
  \item $Y_7 = ABC$: includes $m_{14}(\bar{D}), m_{15}(D) \implies$ function has both $m_{14}, m_{15} \implies \mathbf{Y_7}$.
\end{itemize}
Combining terms:
\[
X = (Y_0 + Y_4)\bar{D} + Y_1 + Y_3 D + Y_5 + Y_7
\]

\begin{schematicbox}{Function Realization Using Single 3x8 Decoder and Gates}
\centering
\begin{tikzpicture}[scale=0.9, transform shape]
  % 3x8 Decoder Box
  \draw[thick, fill=boxbg] (0, 0) rectangle (3.5, 6.0);
  \node at (1.75, 5.5) {\textbf{3x8 Decoder}};
  \node[anchor=west] at (0.2, 4.2) {\small $A\ (S_2)$};
  \node[anchor=west] at (0.2, 3.0) {\small $B\ (S_1)$};
  \node[anchor=west] at (0.2, 1.8) {\small $C\ (S_0)$};

  \foreach \i in {0,1,...,7} {
    \node[anchor=east] at (3.3, {0.6 + \i*0.6}) {\small $Y_\i$};
    \draw[thick] (3.5, {0.6 + \i*0.6}) -- (4.2, {0.6 + \i*0.6});
  }

  % Combinational Gates on right
  \node[or gate US, draw, logic gate inputs=nn] (or04) at (5.5, 1.8) {};
  \node[and gate US, draw, logic gate inputs=nn] (and04D) at (7.5, 1.8) {};
  \node[and gate US, draw, logic gate inputs=nn] (and3D) at (7.5, 3.6) {};

  % Final 5-input OR Gate
  \node[or gate US, draw, logic gate inputs=nnnnn, scale=1.3] (orOut) at (10.5, 3.5) {};

  % Connections
  \draw[thick] (4.2, 0.6) |- (or04.input 2); % Y0
  \draw[thick] (4.2, 3.0) |- (or04.input 1); % Y4
  \draw[thick] (or04.output) -- (and04D.input 1);
  \draw[thick] (6.0, 1.4) node[left] {$\bar{D}$} -- (and04D.input 2);

  \draw[thick] (4.2, 2.4) |- (and3D.input 1); % Y3
  \draw[thick] (6.0, 3.2) node[left] {$D$} -- (and3D.input 2);

  % Feeds into OR Out
  \draw[thick] (and04D.output) -- ++(1.0, 0) |- (orOut.input 5);
  \draw[thick] (4.2, 1.2) -- ++(3.5, 0) |- (orOut.input 4); % Y1
  \draw[thick] (and3D.output) -- (orOut.input 3);
  \draw[thick] (4.2, 3.6) -- ++(3.5, 0) |- (orOut.input 2); % Y5
  \draw[thick] (4.2, 4.8) -- ++(3.5, 0) |- (orOut.input 1); % Y7

  \draw[thick] (orOut.output) -- ++(1.0, 0) node[right] {\large $\mathbf{X}$};
\end{tikzpicture}
\end{schematicbox}

\paragraph{Part (b): K-Map Minimization [3 Marks]}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
$AB \ \backslash \ CD$ & \textbf{00} & \textbf{01} & \textbf{11} & \textbf{10} \\ \hline
\textbf{00} & $\mathbf{1}\ (m_0)$ & $0\ (m_1)$ & $\mathbf{1}\ (m_3)$ & $\mathbf{1}\ (m_2)$ \\ \hline
\textbf{01} & $0\ (m_4)$ & $0\ (m_5)$ & $\mathbf{1}\ (m_7)$ & $0\ (m_6)$ \\ \hline
\textbf{11} & $0\ (m_{12})$ & $0\ (m_{13})$ & $\mathbf{1}\ (m_{15})$ & $\mathbf{1}\ (m_{14})$ \\ \hline
\textbf{10} & $\mathbf{1}\ (m_8)$ & $0\ (m_9)$ & $\mathbf{1}\ (m_{11})$ & $\mathbf{1}\ (m_{10})$ \\ \hline
\end{tabular}
\end{center}
\begin{enumerate}
  \item \textbf{Quad 1 (Four Corners):} $(m_0, m_2, m_8, m_{10}) \implies \mathbf{\bar{B}\bar{D}}$.
  \item \textbf{Quad 2 (Column 11):} $(m_3, m_7, m_{15}, m_{11}) \implies \mathbf{CD}$.
  \item \textbf{Quad 3 (Rows 11 and 10, Cols 11 and 10):} $(m_{15}, m_{14}, m_{11}, m_{10}) \implies \mathbf{AC}$.
\end{enumerate}

\begin{answerbox}
$$\mathbf{X(A,B,C,D) = \bar{B}\bar{D} + CD + AC}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: Synchronous 2-Bit UP/DOWN Counter Schematic [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q5)}
Design a synchronous 2-bit up/down counter using T flip-flops.
\end{questionbox}

Let mode control input be $M$:
\begin{itemize}
  \item $M = 0 \implies$ \textbf{UP Counting Sequence:} $00 \to 01 \to 10 \to 11 \to 00$.
  \item $M = 1 \implies$ \textbf{DOWN Counting Sequence:} $00 \to 11 \to 10 \to 01 \to 00$.
\end{itemize}

\paragraph{1. State Transition and T Excitation Table ($T = Q_n \oplus Q_{n+1}$):}
\begin{center}
\begin{tabular}{|c|cc|cc|cc|}
\hline
\textbf{Mode} & \multicolumn{2}{c|}{\textbf{Present State}} & \multicolumn{2}{c|}{\textbf{Next State}} & \multicolumn{2}{c|}{\textbf{T Inputs}} \\
$M$ & $Q_1$ & $Q_0$ & $Q_1^+$ & $Q_0^+$ & $\mathbf{T_1}$ & $\mathbf{T_0}$ \\ \hline
0 & 0 & 0 & 0 & 1 & 0 & 1 \\ \hline
0 & 0 & 1 & 1 & 0 & 1 & 1 \\ \hline
0 & 1 & 0 & 1 & 1 & 0 & 1 \\ \hline
0 & 1 & 1 & 0 & 0 & 1 & 1 \\ \hline
1 & 0 & 0 & 1 & 1 & 1 & 1 \\ \hline
1 & 0 & 1 & 0 & 0 & 0 & 1 \\ \hline
1 & 1 & 0 & 0 & 1 & 1 & 1 \\ \hline
1 & 1 & 1 & 1 & 0 & 0 & 1 \\ \hline
\end{tabular}
\end{center}

\paragraph{2. Minimized T Equations via K-Maps:}
\begin{itemize}
  \item $T_0 = 1$ (LSB flip-flop toggles on every single clock edge regardless of mode).
  \item For $T_1(M, Q_1, Q_0)$:
  \[
  T_1 = \bar{M}Q_0 + M\bar{Q}_0 = \mathbf{M \oplus Q_0}
  \]
\end{itemize}

\begin{schematicbox}{Synchronous 2-Bit UP/DOWN Counter Circuit Schematic}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % FF0 and FF1
  \draw[thick, fill=boxbg] (1.0, 0) rectangle (3.6, 3.4);
  \node at (2.3, 2.9) {\textbf{FF0 (T)}};
  \node[anchor=west] at (1.2, 2.0) {\small $T_0$};
  \node[anchor=west] at (1.2, 0.8) {\small $>$};
  \node[anchor=east] at (3.4, 2.0) {\small $Q_0$};
  \node[anchor=east] at (3.4, 0.8) {\small $\bar{Q}_0$};

  \draw[thick, fill=boxbg] (7.5, 0) rectangle (10.1, 3.4);
  \node at (8.8, 2.9) {\textbf{FF1 (T)}};
  \node[anchor=west] at (7.7, 2.0) {\small $T_1$};
  \node[anchor=west] at (7.7, 0.8) {\small $>$};
  \node[anchor=east] at (9.9, 2.0) {\small $Q_1$};
  \node[anchor=east] at (9.9, 0.8) {\small $\bar{Q}_1$};

  % Output lines
  \draw[thick] (3.6, 2.0) -- ++(0.6, 0) -- ++(0, 2.0) node[above] {\large $\mathbf{Q_0}$};
  \draw[thick] (10.1, 2.0) -- ++(0.6, 0) -- ++(0, 2.0) node[above] {\large $\mathbf{Q_1}$};

  % T0 = 1
  \draw[thick] (-0.8, 2.0) node[left] {\large $\mathbf{1\ (V_{CC})}$} -- (1.0, 2.0);

  % T1 XOR Gate (M XOR Q0)
  \node[xor gate US, draw, logic gate inputs=nn] (xor1) at (5.8, 2.0) {};
  \draw[thick] (3.6, 2.0) -- (xor1.input 2);
  \draw[thick] (-0.8, 3.8) node[left] {\large $\mathbf{M\ (\text{Mode})}$} -- (5.0, 3.8) |- (xor1.input 1);
  \draw[thick] (xor1.output) -- (7.5, 2.0);

  % Common Synchronous Clock
  \draw[thick] (-0.8, -0.8) node[left] {\large $\mathbf{\text{CLK}}$} -- (9.0, -0.8);
  \draw[thick] (2.0, -0.8) -- (2.0, 0.8) -- (1.2, 0.8);
  \draw[thick] (8.5, -0.8) -- (8.5, 0.8) -- (7.7, 0.8);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{T_0 = 1, \qquad T_1 = \bar{M}Q_0 + M\bar{Q}_0 = M \oplus Q_0}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: 4-Bit PISO Shift Register Schematic [3 + 2 = 5 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q6)}
Explain the operation of 4-bit parallel-in serial-out (PISO) shift register with necessary circuit and timing diagram for $1101_2$ input data.
\end{questionbox}

A \textbf{Parallel-In Serial-Out (PISO)} shift register loads 4 bits of parallel data simultaneously on a single clock pulse when the mode control line $\text{Shift}/\overline{\text{Load}} = 0$, and shifts data out serially bit-by-bit when $\text{Shift}/\overline{\text{Load}} = 1$.

\paragraph{Steering Logic Equation for Flip-Flop Data Inputs:}
\[
D_i = (\text{Shift} \cdot Q_{i+1}) + (\overline{\text{Load}} \cdot \text{Parallel In}_i)
\]

\begin{schematicbox}{4-Bit Parallel-In Serial-Out (PISO) Shift Register}
\centering
\begin{tikzpicture}[scale=0.85, transform shape]
  % 4 D Flip Flops
  \foreach \i in {3,2,1,0} {
    \draw[thick, fill=boxbg] ({3.8*(3 - \i)}, 0) rectangle ({3.8*(3 - \i) + 2.2}, 3.0);
    \node at ({3.8*(3 - \i) + 1.1}, 2.6) {\textbf{FF\i\ (D)}};
    \node[anchor=west] at ({3.8*(3 - \i) + 0.2}, 1.6) {\small $D$};
    \node[anchor=west] at ({3.8*(3 - \i) + 0.2}, 0.6) {\small $>$};
    \node[anchor=east] at ({3.8*(3 - \i) + 2.0}, 1.6) {\small $Q$};
  }

  % Serial Output from FF0
  \draw[thick] (13.6, 1.6) -- ++(1.2, 0) node[right] {\large $\mathbf{\text{Serial Out}}$};

  % Steering Multiplexers / AND-OR gates
  \foreach \i in {2,1,0} {
    \node[draw, thick, fill=boxbg, minimum width=0.8cm, minimum height=1.2cm] (mux\i) at ({3.8*(3 - \i) - 0.7}, 1.6) {\small MUX};
    \draw[thick] (mux\i.east) -- ({3.8*(3 - \i)}, 1.6);
  }

  % Parallel inputs D3, D2, D1, D0
  \draw[thick] (-0.8, 1.6) node[left] {\large $\mathbf{P_3}$} -- (0, 1.6);
  \draw[thick] (2.4, 4.0) node[above] {\large $\mathbf{P_2}$} |- (mux2.north west);
  \draw[thick] (6.2, 4.0) node[above] {\large $\mathbf{P_1}$} |- (mux1.north west);
  \draw[thick] (10.0, 4.0) node[above] {\large $\mathbf{P_0}$} |- (mux0.north west);

  % Common Clock and Mode Lines
  \draw[thick] (-1.0, -0.8) node[left] {\large $\mathbf{\text{CLK}}$} -- (12.5, -0.8);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({3.8*\i + 0.4}, -0.8) -- ({3.8*\i + 0.4}, 0.6) -- ({3.8*\i + 0.2}, 0.6);
  }
\end{tikzpicture}
\end{schematicbox}

\paragraph{Cycle-by-Cycle Shifting of Data $1101_2$ ($P_3=1, P_2=1, P_1=0, P_0=1$):}
\begin{center}
\begin{tabular}{|c|c|cccc|c|}
\hline
\textbf{Clock Cycle} & $\mathbf{\text{Shift}/\overline{\text{Load}}}$ & $\mathbf{Q_3}$ & $\mathbf{Q_2}$ & $\mathbf{Q_1}$ & $\mathbf{Q_0}$ & \textbf{Serial Output} \\ \hline
\textbf{Parallel Load} & 0 & 1 & 1 & 0 & 1 & $\mathbf{1}$ (Bit 0 available immediately) \\ \hline
\textbf{Shift 1} & 1 & 0 & 1 & 1 & 0 & $\mathbf{0}$ (Bit 1) \\ \hline
\textbf{Shift 2} & 1 & 0 & 0 & 1 & 1 & $\mathbf{1}$ (Bit 2) \\ \hline
\textbf{Shift 3} & 1 & 0 & 0 & 0 & 1 & $\mathbf{1}$ (Bit 3) \\ \hline
\end{tabular}
\end{center}

\begin{answerbox}
The data word $1101_2$ is loaded in parallel on $\text{Shift}/\overline{\text{Load}}=0$ and shifted out serially as bits $1 \to 0 \to 1 \to 1$ across 3 consecutive shift clock cycles.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: Mod-12 Asynchronous Counter Schematic [3 + 3 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q7)}
Sketch the circuit diagram of mod-12 asynchronous counter having positive-edge triggering clock system implementing JK flip-flops with neat timing diagram.
\end{questionbox}

A \textbf{Mod-12 Asynchronous Counter} counts 12 states from $0000_2$ ($0_{10}$) to $1011_2$ ($11_{10}$). On the 12th count ($1100_2$, where $Q_3=1, Q_2=1$), an asynchronous active-low clear pulse resets all flip-flops to $0000_2$:
\[
\overline{\text{CLR}} = \overline{Q_3 \cdot Q_2}
\]
With positive-edge triggered flip-flops, UP counting requires ripple clocking via complementary outputs: $\text{CLK}_{i+1} = \bar{Q}_i$.

\begin{schematicbox}{Mod-12 Positive-Edge Triggered Asynchronous Counter}
\centering
\begin{tikzpicture}[scale=0.88, transform shape]
  % 4 JK Flip Flops
  \foreach \i in {0,1,2,3} {
    \draw[thick, fill=boxbg] ({3.6*\i}, 0) rectangle ({3.6*\i + 2.4}, 3.4);
    \node at ({3.6*\i + 1.2}, 2.9) {\textbf{FF\i\ (JK)}};
    \node[anchor=west] at ({3.6*\i + 0.2}, 2.2) {\small $J=1$};
    \node[anchor=west] at ({3.6*\i + 0.2}, 1.5) {\small $>$};
    \node[anchor=west] at ({3.6*\i + 0.2}, 0.8) {\small $K=1$};
    \node[anchor=east] at ({3.6*\i + 2.2}, 2.2) {\small $Q$};
    \node[anchor=east] at ({3.6*\i + 2.2}, 0.8) {\small $\bar{Q}$};
    \node[anchor=south] at ({3.6*\i + 1.2}, 0.1) {\small $\overline{\text{CLR}}$};

    % Output lines
    \filldraw[black] ({3.6*\i + 2.8}, 2.2) circle (2pt);
    \draw[thick] ({3.6*\i + 2.4}, 2.2) -- ({3.6*\i + 2.8}, 2.2) -- ({3.6*\i + 2.8}, 4.2) node[above] {\large $\mathbf{Q_\i}$};
  }

  % External Clock
  \draw[thick] (-1.2, 1.5) node[left] {\large $\mathbf{\text{CLK}}$} -- (0, 1.5);

  % Ripple connections (Q_bar_i -> CLK_{i+1})
  \draw[thick] (2.4, 0.8) -- (3.0, 0.8) |- (3.6, 1.5);
  \draw[thick] (6.0, 0.8) -- (6.6, 0.8) |- (7.2, 1.5);
  \draw[thick] (9.6, 0.8) -- (10.2, 0.8) |- (10.8, 1.5);

  % Reset NAND Gate: Q3 and Q2
  \node[nand gate US, draw, logic gate inputs=nn, rotate=-90] (nandRst) at (8.5, -2.0) {};
  \draw[thick] (13.6, 2.2) -- (13.6, -1.2) |- (nandRst.input 1); % Q3
  \draw[thick] (10.0, 2.2) -- (10.0, -1.2) |- (nandRst.input 2); % Q2

  % Clear Rail
  \draw[thick] (nandRst.output) -- (8.5, -3.2) -- (-0.5, -3.2) -- (-0.5, -0.4) -- (12.0, -0.4);
  \foreach \i in {0,1,2,3} {
    \draw[thick] ({3.6*\i + 1.2}, -0.4) -- ({3.6*\i + 1.2}, 0);
  }
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
Reset condition: $\mathbf{\overline{\text{CLR}} = \overline{Q_3 \cdot Q_2}}$, providing exactly 12 stable counting states from $0000_2$ to $1011_2$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: FSM Sequence Detector '010' Using D Flip-Flops [10 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q8)}
Design a sequential machine that consists of one input $X$ and one output $Z$. The machine is required to give output high ($Z=1$) whenever it detects the serial sequence of `010' from its input data stream $X$. Implement only D flip-flops for the designed circuit realization.
\end{questionbox}

\paragraph{1. State Definitions (Mealy Model with Overlapping Detection):}
\begin{itemize}
  \item $S_0 (00)$: Reset state / No matching prefix.
  \item $S_1 (01)$: Detected pattern `0'.
  \item $S_2 (10)$: Detected pattern `01'.
  \item When in $S_2$ and next bit is $X=0 \implies$ `010' detected $\implies Z=1$, next state $S_1$ (since trailing `0' can start the next sequence).
\end{itemize}

\begin{schematicbox}{State Diagram for '010' Sequence Detector}
\centering
\begin{tikzpicture}[->, >=Stealth, auto, node distance=3.2cm, thick]
  \node[state, initial] (S0) {$S_0 (00)$};
  \node[state] (S1) [right of=S0] {$S_1 (01)$};
  \node[state] (S2) [right of=S1] {$S_2 (10)$};

  \path (S0) edge [loop above] node {$X=1 / 0$} (S0)
             edge [bend left] node {$X=0 / 0$} (S1)
        (S1) edge [loop above] node {$X=0 / 0$} (S1)
             edge [bend left] node {$X=1 / 0$} (S2)
        (S2) edge [bend left=45] node {$X=1 / 0$} (S0)
             edge [bend left] node {$X=0 / 1$} (S1);
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. State Transition and D Excitation Table ($D_1 = Q_1^+, D_0 = Q_0^+$):}
\begin{center}
\begin{tabular}{|cc|c|cc|c|cc|}
\hline
\multicolumn{2}{|c|}{\textbf{Present State}} & \textbf{Input} & \multicolumn{2}{c|}{\textbf{Next State}} & \textbf{Output} & \multicolumn{2}{c|}{\textbf{D Inputs}} \\
$Q_1$ & $Q_0$ & $X$ & $Q_1^+$ & $Q_0^+$ & $\mathbf{Z}$ & $\mathbf{D_1}$ & $\mathbf{D_0}$ \\ \hline
0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\ \hline
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
0 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\ \hline
0 & 1 & 1 & 1 & 0 & 0 & 1 & 0 \\ \hline
1 & 0 & 0 & 0 & 1 & 1 & 0 & 1 \\ \hline
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ \hline
1 & 1 & 0 & $X$ & $X$ & $X$ & $X$ & $X$ \\ \hline
1 & 1 & 1 & $X$ & $X$ & $X$ & $X$ & $X$ \\ \hline
\end{tabular}
\end{center}

\paragraph{3. Minimized Equations via K-Maps:}
\begin{align*}
D_1 &= \bar{Q}_1 Q_0 X \\
D_0 &= \bar{X} \\
Z &= Q_1 \bar{X}
\end{align*}

\begin{schematicbox}{Complete Logic Circuit Realization Using D Flip-Flops}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % 2 D Flip Flops
  \draw[thick, fill=boxbg] (1.0, 0) rectangle (3.6, 3.4);
  \node at (2.3, 2.9) {\textbf{FF1 (D)}};
  \node[anchor=west] at (1.2, 2.0) {\small $D_1$};
  \node[anchor=west] at (1.2, 0.8) {\small $>$};
  \node[anchor=east] at (3.4, 2.0) {\small $Q_1$};
  \node[anchor=east] at (3.4, 0.8) {\small $\bar{Q}_1$};

  \draw[thick, fill=boxbg] (6.5, 0) rectangle (9.1, 3.4);
  \node at (7.8, 2.9) {\textbf{FF0 (D)}};
  \node[anchor=west] at (6.7, 2.0) {\small $D_0$};
  \node[anchor=west] at (6.7, 0.8) {\small $>$};
  \node[anchor=east] at (8.9, 2.0) {\small $Q_0$};
  \node[anchor=east] at (8.9, 0.8) {\small $\bar{Q}_0$};

  % Input X and Inverter
  \draw[thick] (-1.5, 2.0) node[left] {\large $\mathbf{X}$} -- (-0.8, 2.0);
  \node[not gate US, draw, scale=0.8] (notX) at (-0.2, 2.0) {};
  \draw[thick] (-0.8, 2.0) -- (notX.input);

  % D0 = X_bar
  \draw[thick] (notX.output) -- (0.5, 2.0) -- (0.5, -0.4) -- (6.0, -0.4) |- (6.7, 2.0);

  % D1 = Q1_bar . Q0 . X
  \node[and gate US, draw, logic gate inputs=nnn] (andD1) at (-0.2, 3.2) {};
  \draw[thick] (-1.2, 3.4) node[left] {\footnotesize $\bar{Q}_1$} -- (andD1.input 1);
  \draw[thick] (-1.2, 3.2) node[left] {\footnotesize $Q_0$} -- (andD1.input 2);
  \draw[thick] (-1.2, 3.0) node[left] {\footnotesize $X$} -- (andD1.input 3);
  \draw[thick] (andD1.output) |- (1.0, 2.0);

  % Output Z = Q1 . X_bar
  \node[and gate US, draw, logic gate inputs=nn] (andZ) at (11.0, 2.0) {};
  \draw[thick] (3.6, 2.0) -- (andZ.input 1);
  \draw[thick] (0.5, -0.4) -- (10.0, -0.4) |- (andZ.input 2);
  \draw[thick] (andZ.output) -- ++(1.0, 0) node[right] {\large $\mathbf{Z}$};

  % Clock
  \draw[thick] (-1.5, -1.0) node[left] {\large $\mathbf{\text{CLK}}$} -- (8.0, -1.0);
  \draw[thick] (1.8, -1.0) -- (1.8, 0.8) -- (1.2, 0.8);
  \draw[thick] (7.3, -1.0) -- (7.3, 0.8) -- (6.7, 0.8);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{D_1 = \bar{Q}_1 Q_0 X, \qquad D_0 = \bar{X}, \qquad Z = Q_1 \bar{X}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: Two-Input CMOS NAND Gate Transistor Circuit [4 + 2 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q9)}
Draw the circuit diagram of two-input CMOS NAND gate and explain its logic operation briefly and list the characteristics of TTL logic family.
\end{questionbox}

\paragraph{Part (a): 2-Input CMOS NAND Gate Circuit and Operation [4 Marks]}
A CMOS logic gate consists of a \textbf{Pull-Up Network (PUN)} made of PMOS transistors and a \textbf{Pull-Down Network (PDN)} made of NMOS transistors:
\begin{itemize}
  \item \textbf{PUN:} Two PMOS transistors ($M_1, M_2$) connected in \textbf{parallel} between $V_{DD}$ and Output $Y$.
  \item \textbf{PDN:} Two NMOS transistors ($M_3, M_4$) connected in \textbf{series} between Output $Y$ and Ground.
\end{itemize}

\begin{schematicbox}{Transistor-Level Schematic of 2-Input CMOS NAND Gate}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % VDD rail
  \draw[thick] (2.0, 5.5) -- (6.0, 5.5);
  \node[above] at (4.0, 5.5) {\large $\mathbf{V_{DD}\ (+5\text{V})}$};

  % PMOS M1 (left) and M2 (right)
  \draw[thick, fill=boxbg] (2.2, 3.8) rectangle (3.4, 4.8);
  \node at (2.8, 4.3) {\small $\mathbf{M_1}$ (PMOS)};
  \draw[thick, fill=boxbg] (4.6, 3.8) rectangle (5.8, 4.8);
  \node at (5.2, 4.3) {\small $\mathbf{M_2}$ (PMOS)};

  \draw[thick] (2.8, 5.5) -- (2.8, 4.8);
  \draw[thick] (5.2, 5.5) -- (5.2, 4.8);

  % Common output Y
  \draw[thick] (2.8, 3.8) -- (2.8, 3.0) -- (5.2, 3.0) -- (5.2, 3.8);
  \draw[thick] (4.0, 3.0) -- (7.5, 3.0) node[right] {\large $\mathbf{Y = \overline{A \cdot B}}$};

  % NMOS M3 (top) and M4 (bottom) in series
  \draw[thick, fill=boxbg] (3.4, 1.6) rectangle (4.6, 2.6);
  \node at (4.0, 2.1) {\small $\mathbf{M_3}$ (NMOS)};
  \draw[thick, fill=boxbg] (3.4, 0.0) rectangle (4.6, 1.0);
  \node at (4.0, 0.5) {\small $\mathbf{M_4}$ (NMOS)};

  \draw[thick] (4.0, 3.0) -- (4.0, 2.6);
  \draw[thick] (4.0, 1.6) -- (4.0, 1.0);
  \draw[thick] (4.0, 0.0) -- (4.0, -0.6);

  % Ground
  \draw[thick] (3.4, -0.6) -- (4.6, -0.6);
  \draw[thick] (3.6, -0.8) -- (4.4, -0.8);
  \draw[thick] (3.8, -1.0) -- (4.2, -1.0);
  \node[below] at (4.0, -1.0) {\textbf{GND}};

  % Inputs A and B
  \draw[thick] (0.8, 4.3) node[left] {$\mathbf{A}$} -- (2.2, 4.3);
  \draw[thick] (0.8, 4.3) -- (1.5, 4.3) |- (3.4, 2.1); % A to M3

  \draw[thick] (7.0, 4.3) node[right] {$\mathbf{B}$} -- (5.8, 4.3);
  \draw[thick] (7.0, 4.3) -- (6.3, 4.3) |- (4.6, 0.5); % B to M4
\end{tikzpicture}
\end{schematicbox}

\paragraph{Operation Truth Table:}
\begin{center}
\begin{tabular}{|cc||cc|cc||c|l|}
\hline
$\mathbf{A}$ & $\mathbf{B}$ & $\mathbf{M_1\ (P)}$ & $\mathbf{M_2\ (P)}$ & $\mathbf{M_3\ (N)}$ & $\mathbf{M_4\ (N)}$ & $\mathbf{Y}$ & \textbf{State} \\ \hline
0 & 0 & ON & ON & OFF & OFF & $\mathbf{1}\ (V_{DD})$ & PUN conducts to $V_{DD}$ \\ \hline
0 & 1 & ON & OFF & OFF & ON & $\mathbf{1}\ (V_{DD})$ & $M_1$ pulls output HIGH \\ \hline
1 & 0 & OFF & ON & ON & OFF & $\mathbf{1}\ (V_{DD})$ & $M_2$ pulls output HIGH \\ \hline
1 & 1 & OFF & OFF & ON & ON & $\mathbf{0}\ (\text{GND})$ & PDN pulls output to Ground \\ \hline
\end{tabular}
\end{center}

\paragraph{Part (b): Characteristics of TTL Logic Family [2 Marks]}
\begin{enumerate}
  \item \textbf{Supply Voltage:} Standard $V_{CC} = +5.0\text{V} \pm 5\%$.
  \item \textbf{Power Dissipation:} $\approx 10\text{ mW}$ per gate (Standard 7400 TTL).
  \item \textbf{Propagation Delay:} $\approx 10\text{ ns}$ (high speed bipolar technology).
  \item \textbf{Noise Margin:} $NM_H = 0.4\text{V}, NM_L = 0.4\text{V}$.
  \item \textbf{Fan-Out:} 10 standard 7400 TTL loads.
\end{enumerate}

\begin{answerbox}
CMOS NAND uses parallel PMOS pull-up and series NMOS pull-down transistors, providing near-zero static power dissipation and full rail-to-rail voltage swing.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: Time Interval Measurement Block Diagram [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q10)}
With the help of functional diagram explain the operation of time measuring circuit.
\end{questionbox}

A \textbf{Digital Time Interval Meter} measures the elapsed time $\Delta T$ between a START trigger event and a STOP trigger event by counting the number of precision clock pulses of known period $T_0$:
\[
\Delta T = N \times T_0 = \frac{N}{f_{\text{osc}}}
\]

\paragraph{Operational Sequence:}
\begin{enumerate}
  \item \textbf{Start Pulse Conditioning:} The START signal passes through an input amplifier and Schmitt trigger, setting the \textbf{Gate Control Flip-Flop (RS Latch)}.
  \item \textbf{Gating Period:} While the latch is SET ($Q=1$), the \textbf{Main AND Gate} opens, allowing clock pulses from the crystal oscillator time base to flow into the decade counters.
  \item \textbf{Stop Pulse Conditioning:} The arrival of the STOP event resets the latch ($Q=0$), closing the AND gate and freezing the count.
  \item \textbf{Display:} The accumulated count $N$ is displayed directly on 7-segment digital readouts in microseconds ($\mu$s), milliseconds (ms), or seconds (s).
\end{enumerate}

\begin{schematicbox}{Functional Block Diagram of Digital Time Interval Measurement Circuit}
\centering
\begin{tikzpicture}[scale=0.88, transform shape, >=Stealth]
  % Start / Stop input blocks
  \node[draw, thick, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm, align=center] (start) at (0, 3.5) {START Input\\Conditioner};
  \node[draw, thick, fill=boxbg, minimum width=2.4cm, minimum height=1.0cm, align=center] (stop) at (0, 1.5) {STOP Input\\Conditioner};

  % RS Flip Flop
  \draw[thick, fill=boxbg] (3.5, 1.2) rectangle (5.5, 3.8);
  \node at (4.5, 3.3) {\textbf{RS Latch}};
  \node[anchor=west] at (3.6, 2.8) {\small $S$};
  \node[anchor=west] at (3.6, 1.8) {\small $R$};
  \node[anchor=east] at (5.4, 2.5) {\small $Q$};

  \draw[thick, ->] (start.east) -- (3.5, 2.8);
  \draw[thick, ->] (stop.east) -- (3.5, 1.8);

  % Main AND Gate
  \node[and gate US, draw, logic gate inputs=nn, scale=1.2] (mainGate) at (7.5, 2.5) {};
  \draw[thick, ->] (5.5, 2.5) -- (mainGate.input 1);

  % Time base oscillator
  \node[draw, thick, fill=boxbg, minimum width=2.2cm, minimum height=1.0cm, align=center] (osc) at (7.5, 0.0) {Precision Clock\\Oscillator ($T_0$)};
  \draw[thick, ->] (osc.north) -- (mainGate.input 2);

  % Counter and Display
  \node[draw, thick, fill=boxbg, minimum width=2.4cm, minimum height=1.2cm, align=center] (counter) at (10.5, 2.5) {Decade\\Counters ($N$)};
  \node[draw, thick, fill=boxbg, minimum width=2.2cm, minimum height=1.2cm, align=center] (disp) at (13.8, 2.5) {Digital Display\\($\Delta T = N \cdot T_0$)};

  \draw[thick, ->] (mainGate.output) -- (counter.west);
  \draw[thick, ->] (counter.east) -- (disp.west);
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
The time interval measurement system gates standard clock pulses between START and STOP triggers, computing time elapsed as $\mathbf{\Delta T = N \times T_0}$.
\end{answerbox}
"""
