# edc_ch2_2082_bhadra.py
# Chapter 2: 2082 Bhadra Examination Master Solutions (Refined & Fully Verified)

def get_chapter_2082_bhadra():
    return r"""
\chapter{2082 Bhadra Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BEI, BCT & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Electronic Devices \& Circuits (ENEX 151) & \textbf{Examination Type:} Regular (New Course) \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: $\beta$-Independent Voltage Divider Bias Design [1 + 5 = 6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q1)}
What is the significance of $\beta$-independency in a voltage divider biasing circuit? Design a $\beta$-independent voltage divider bias circuit for the given parameters: $V_{CC} = 15\text{ V}, I_E = 1\text{ mA}$, and $\beta = 100$.
\end{questionbox}

\paragraph{Part (a): Significance of $\beta$-Independency [1 Mark]}
Transistor forward current gain $\beta$ ($h_{FE}$) exhibits wide manufacturing dispersions (typically ranging from 100 to 300 for the same transistor type) and strong temperature dependence ($+0.5\%/^\circ\text{C}$). A $\beta$-independent biasing circuit ensures that the quiescent operating point ($I_{CQ}, V_{CEQ}$) remains strictly invariant against device replacement and thermal drift, completely avoiding thermal runaway and waveform clipping.

\paragraph{Part (b): Step-by-Step Design [5 Marks]}
Design Specifications: $V_{CC} = 15\text{ V}, I_{E} \approx I_{CQ} = 1.0\text{ mA}, \beta = 100$, Silicon BJT ($V_{BE} = 0.7\text{ V}$).

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Emitter Voltage Allocation ($V_E$):}
  To ensure excellent temperature stability without compromising dynamic output voltage swing, allocate 10\% of $V_{CC}$:
  \[
  V_E = 0.10 \times V_{CC} = 0.10 \times 15\text{ V} = \mathbf{1.5\text{ V}}
  \]
  \item \textbf{Calculation of $R_E$:}
  \[
  R_E = \frac{V_E}{I_E} = \frac{1.5\text{ V}}{1.0\text{ mA}} = \mathbf{1.5\text{ k}\Omega}
  \]
  \item \textbf{Collector Voltage Allocation ($V_C$):}
  For maximum symmetrical undistorted output voltage swing:
  \[
  V_{CEQ} = \frac{V_{CC} - V_E}{2} = \frac{15\text{ V} - 1.5\text{ V}}{2} = 6.75\text{ V}
  \]
  \[
  V_C = V_E + V_{CEQ} = 1.5\text{ V} + 6.75\text{ V} = 8.25\text{ V}
  \]
  \[
  R_C = \frac{V_{CC} - V_C}{I_C} = \frac{15\text{ V} - 8.25\text{ V}}{1.0\text{ mA}} = 6.75\text{ k}\Omega \quad (\text{Select standard value } R_C = \mathbf{6.8\text{ k}\Omega})
  \]
  \item \textbf{Base Voltage ($V_B$):}
  \[
  V_B = V_E + V_{BE} = 1.5\text{ V} + 0.7\text{ V} = \mathbf{2.2\text{ V}}
  \]
  \item \textbf{Voltage Divider Resistors ($R_1, R_2$) via Bleeder Current Rule ($I_{\text{bleed}} \ge 10 I_B$):}
  \[
  I_B = \frac{I_C}{\beta} = \frac{1.0\text{ mA}}{100} = 0.01\text{ mA} = 10\ \mu\text{A} \implies I_{\text{bleed}} = 10 \times I_B = 0.10\text{ mA}
  \]
  \[
  R_2 = \frac{V_B}{I_{\text{bleed}}} = \frac{2.2\text{ V}}{0.10\text{ mA}} = \mathbf{22\text{ k}\Omega} \quad (\text{Standard } 5\% \text{ resistor})
  \]
  \[
  R_1 = \frac{V_{CC} - V_B}{I_{\text{bleed}} + I_B} = \frac{15\text{ V} - 2.2\text{ V}}{0.10\text{ mA} + 0.01\text{ mA}} = \frac{12.8\text{ V}}{0.11\text{ mA}} = 116.36\text{ k}\Omega \quad (\text{Select standard } R_1 = \mathbf{120\text{ k}\Omega})
  \]
\end{enumerate}

\begin{schematicbox}{Designed Common Emitter Amplifier Circuit ($V_{CC} = 15\text{V}$)}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.5, 5.2) node[right] {\large $\mathbf{V_{CC} = +15\text{V}}$};
  \draw[thick] (0, -0.8) -- (7.5, -0.8) node[right] {\textbf{GND}};

  % Divider R1 and R2
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 3.4) rectangle (2.2, 4.3) node[midway] {\small $R_1=120\text{k}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (vb) {};
  \draw[thick] (1.8, 2.5) -- (1.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 0.7) rectangle (2.2, 1.6) node[midway] {\small $R_2=22\text{k}$};
  \draw[thick] (1.8, 0.7) -- (1.8, -0.8);

  % Input coupling capacitor C1
  \draw[thick] (0.2, 2.5) node[left] {$V_{\text{in}}$} -- (0.8, 2.5);
  \draw[line width=1.4pt, line cap=round] (0.8, 2.1) -- (0.8, 2.9);
  \draw[line width=1.4pt, line cap=round] (1.0, 2.1) -- (1.0, 2.9);
  \node[above] at (0.9, 2.9) {$C_1$};
  \draw[thick] (1.0, 2.5) -- (vb);

  % Transistor Q1 (NPN)
  \draw[thick] (vb) -- (3.5, 2.5);
  \draw[draw=black!80, fill=white, thick] (4.0, 2.5) circle (0.55cm);
  \draw[line width=1.6pt] (3.65, 2.15) -- (3.65, 2.85); % Base
  \draw[thick] (3.5, 2.5) -- (3.65, 2.5);
  \draw[thick] (3.8, 2.7) -- (4.25, 3.05) -- (4.25, 3.4); % Collector
  \draw[thick, ->, >=latex] (3.8, 2.3) -- (4.1, 2.05); % Emitter
  \draw[thick] (4.1, 2.05) -- (4.25, 1.95) -- (4.25, 1.6) node[circle, fill, inner sep=1.8pt] (ve) {};
  \node[right=0.2cm] at (4.5, 2.5) {\large $\mathbf{Q_1}$};

  % Collector Resistor RC
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 3.4) rectangle (4.65, 4.3) node[midway] {\small $R_C=6.8\text{k}$};
  \draw[thick] (4.25, 4.3) -- (4.25, 5.2);

  % Emitter Resistor RE and Bypass CE
  \draw[thick] (ve) -- (4.25, 1.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 0.4) rectangle (4.65, 1.3) node[midway] {\small $R_E=1.5\text{k}$};
  \draw[thick] (4.25, 0.4) -- (4.25, -0.8);

  % Bypass Capacitor CE
  \draw[thick] (ve) -- (5.6, 1.6) -- (5.6, 1.0);
  \draw[line width=1.4pt, line cap=round] (5.2, 1.0) -- (6.0, 1.0);
  \draw[line width=1.4pt, line cap=round] (5.2, 0.8) -- (6.0, 0.8);
  \node[right] at (6.0, 0.9) {$C_E$};
  \draw[thick] (5.6, 0.8) -- (5.6, -0.8);

  % Output coupling capacitor C2
  \draw[thick] (4.25, 3.05) -- (5.8, 3.05);
  \draw[line width=1.4pt, line cap=round] (5.8, 2.65) -- (5.8, 3.45);
  \draw[line width=1.4pt, line cap=round] (6.0, 2.65) -- (6.0, 3.45);
  \node[above] at (5.9, 3.45) {$C_2$};
  \draw[thick] (6.0, 3.05) -- (7.0, 3.05) node[right] {\large $V_o$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{R_1 = 120\text{ k}\Omega, \quad R_2 = 22\text{ k}\Omega, \quad R_C = 6.8\text{ k}\Omega, \quad R_E = 1.5\text{ k}\Omega}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: Role of Coupling Capacitors \& CE Small Signal Parameters [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q2)}
Explain the role of coupling capacitors in amplifier circuits. Draw the small signal equivalent circuit of a common emitter amplifier circuit and find its input impedance, output impedance and voltage gain.
\end{questionbox}

\paragraph{Part (a): Role of Coupling Capacitors ($C_{\text{in}}, C_{\text{out}}$) [2 Marks]}
Coupling capacitors block DC operating voltages from entering the external AC signal source or load resistor, preventing quiescent operating point shifts while presenting a negligible impedance path ($X_C = \frac{1}{2\pi f C} \approx 0$) for signal frequencies.

\paragraph{Part (b): Common Emitter Parameter Derivations [5 Marks]}
\begin{schematicbox}{Small-Signal Model of Common Emitter BJT Amplifier}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Input
  \draw[thick] (0, 2.0) node[left] {$v_{\text{in}}$} -- (1.2, 2.0);
  % R_B (R1 || R2)
  \draw[thick] (0.8, 2.0) -- (0.8, 1.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.4, 0.5) rectangle (1.2, 1.4) node[midway] {\small $R_B$};
  \draw[thick] (0.8, 0.5) -- (0.8, 0);

  % Base resistance beta * re
  \draw[thick] (1.2, 2.0) -- (2.2, 2.0);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (2.2, 1.7) rectangle (3.4, 2.3) node[midway] {\small $\beta r_e$};
  \draw[thick] (3.4, 2.0) -- (4.2, 2.0) -- (4.2, 0);
  \draw[thick, ->, >=latex] (1.4, 2.2) -- (1.9, 2.2) node[midway, above] {$i_b$};

  % Dependent current source beta * ib
  \draw[thick] (5.5, 2.0) circle (0.45cm);
  \draw[thick, ->, >=latex] (5.5, 2.35) -- (5.5, 1.65);
  \node[left=0.15cm] at (4.85, 2.0) {\small $\mathbf{\beta i_b}$};
  \draw[thick] (5.5, 1.55) -- (5.5, 0);
  \draw[thick] (5.5, 2.45) -- (5.5, 2.7) -- (7.5, 2.7) node[circle, fill, inner sep=1.8pt] (c_node) {};

  % Output Resistance RC
  \draw[thick] (6.8, 2.7) -- (6.8, 2.0);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (6.4, 1.1) rectangle (7.2, 2.0) node[midway] {\small $R_C$};
  \draw[thick] (6.8, 1.1) -- (6.8, 0);

  % Ground Rail
  \draw[thick] (0, 0) -- (7.5, 0) node[right] {\textbf{Emitter (GND)}};

  % Output terminal
  \draw[thick] (c_node) -- (8.2, 2.7) node[right] {\large $v_o$};
\end{tikzpicture}
\end{schematicbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Input Impedance ($Z_{\text{in}}$):}
  \[
  \mathbf{Z_{\text{in}} = R_1 \parallel R_2 \parallel \beta r_e \approx \beta r_e} \quad (\text{moderate, } 1\text{ k}\Omega - 5\text{ k}\Omega)
  \]
  \item \textbf{Output Impedance ($Z_{\text{out}}$):}
  \[
  \mathbf{Z_{\text{out}} = R_C \parallel r_o \approx R_C}
  \]
  \item \textbf{Voltage Gain ($A_v$):}
  \[
  v_o = -(\beta i_b)(R_C \parallel R_L), \qquad v_{\text{in}} = i_b (\beta r_e)
  \]
  \[
  \mathbf{A_v = \frac{v_o}{v_{\text{in}}} = -\frac{\beta i_b (R_C \parallel R_L)}{i_b \beta r_e} = -\frac{R_C \parallel R_L}{r_e}} \quad (180^\circ \text{ phase inversion})
  \]
  \item \textbf{Current Gain ($A_i$):}
  \[
  \mathbf{A_i = \frac{i_o}{i_{\text{in}}} \approx -\beta \left(\frac{R_B}{R_B + \beta r_e}\right) \left(\frac{R_C}{R_C + R_L}\right)}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{Z_{\text{in}} \approx R_B \parallel \beta r_e, \qquad Z_{\text{out}} \approx R_C, \qquad A_v = -\frac{R_C \parallel R_L}{r_e}, \qquad A_i \approx -\beta}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: N-Channel JFET Construction and Characteristics [6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q3)}
Describe the construction and working principle of n-channel JFET with the help of characteristic curves and mathematical expressions.
\end{questionbox}

\paragraph{1. Physical Construction:}
An N-Channel Junction Field-Effect Transistor consists of an n-type semiconductor silicon bar with two ohmic contacts at the ends forming the \textbf{Drain} and \textbf{Source}. Two heavily doped $p^+$ regions are diffused on opposite sides of the bar and internally connected to form the \textbf{Gate}.

\begin{schematicbox}{Transfer Characteristics and Drain Output Curves of N-Channel JFET}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Transfer Characteristics (left)
  \draw[thick, ->, >=latex] (-4.5, 0) -- (1.0, 0) node[right] {$V_{GS}\ (\text{V})$};
  \draw[thick, ->, >=latex] (0, 0) -- (0, 4.2) node[above] {$I_D\ (\text{mA})$};
  \draw[domain=-3.5:0, smooth, variable=\x, line width=1.3pt, blue] plot ({\x}, {3.0*(1 + \x/3.5)^2});
  \node[below] at (-3.5, 0) {$V_P$};
  \node[left] at (0, 3.0) {$I_{DSS}$};
  \node[above] at (-1.8, 3.2) {\small\textbf{Shockley Locus}};

  % Drain Output Characteristics (right)
  \draw[thick, ->, >=latex] (3.0, 0) -- (10.5, 0) node[right] {$V_{DS}\ (\text{V})$};
  \draw[thick, ->, >=latex] (3.0, 0) -- (3.0, 4.2) node[above] {$I_D\ (\text{mA})$};

  % Family of Curves
  \draw[line width=1.2pt, teal] (3.0, 0) to[out=60, in=180] (5.5, 3.0) -- (9.8, 3.0) node[right] {\small $V_{GS} = 0\text{V}\ (I_{DSS})$};
  \draw[line width=1.2pt, teal] (3.0, 0) to[out=55, in=180] (5.0, 2.0) -- (9.8, 2.0) node[right] {\small $V_{GS} = -1\text{V}$};
  \draw[line width=1.2pt, teal] (3.0, 0) to[out=50, in=180] (4.5, 1.0) -- (9.8, 1.0) node[right] {\small $V_{GS} = -2\text{V}$};
  \draw[line width=1.2pt, teal] (3.0, 0) to[out=40, in=180] (3.8, 0.3) -- (9.8, 0.3) node[right] {\small $V_{GS} = -3\text{V}$};
  \draw[thick, red, dashed] (3.0, 0.05) -- (9.8, 0.05) node[right] {\small $V_{GS} \le V_P\ (I_D=0)$};

  % Pinch-off locus
  \draw[dashed, purple, line width=1.1pt] (3.0, 0) to[out=45, in=-140] (5.5, 3.0) node[above=0.1cm] {\small\textbf{Pinch-Off Boundary}};
  \node[above] at (4.0, 3.5) {\small\textbf{Ohmic}};
  \node[above] at (7.5, 3.5) {\small\textbf{Saturation (Pinch-off)}};
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. Conduction Equations:}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Ohmic Region ($V_{DS} < V_{GS} - V_P$):}
  \[
  I_D = I_{DSS} \left[ 2\left(1 - \frac{V_{GS}}{V_P}\right)\frac{V_{DS}}{|V_P|} - \left(\frac{V_{DS}}{V_P}\right)^2 \right]
  \]
  \item \textbf{Saturation Region ($V_{DS} \ge V_{GS} - V_P$):}
  \[
  \mathbf{I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2, \qquad g_m = \frac{2I_{DSS}}{|V_P|}\left(1 - \frac{V_{GS}}{V_P}\right)}
  \]
\end{itemize}

\begin{answerbox}
$$\mathbf{I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2, \qquad V_{DS(\text{sat})} = V_{GS} - V_P}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: N-Channel Enhancement-Type MOSFET Q-Point Calculation [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q4)}
Find $I_D$ and $V_{DS}$ for the circuit shown in the figure below. Given parameters are: $V_t = 1\text{ V}$ and $K = 0.48\text{ mA/V}^2$.
Circuit values: $V_{DD} = +10\text{ V}, R_1 = 11\text{ M}\Omega, R_2 = 11\text{ M}\Omega, R_D = 6\text{ k}\Omega, R_S = 6\text{ k}\Omega$.
\end{questionbox}

\begin{schematicbox}{N-Channel E-MOSFET Voltage Divider Bias Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (6.5, 5.2) node[right] {\large $\mathbf{V_{DD} = +10\text{V}}$};
  \draw[thick] (0, -0.8) -- (6.5, -0.8) node[right] {\textbf{GND}};

  % Divider R1 and R2
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.3, 3.4) rectangle (2.3, 4.3) node[midway] {\small $R_1=11\text{M}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (vg) {};
  \draw[thick] (1.8, 2.5) -- (1.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.3, 0.7) rectangle (2.3, 1.6) node[midway] {\small $R_2=11\text{M}$};
  \draw[thick] (1.8, 0.7) -- (1.8, -0.8);

  % Gate connection
  \draw[thick] (vg) -- (3.2, 2.5);

  % E-MOSFET Symbol (N-Channel)
  \draw[draw=black!80, fill=white, thick] (3.8, 2.5) circle (0.55cm);
  \draw[line width=1.4pt] (3.45, 2.05) -- (3.45, 2.95); % Gate plate
  \draw[thick] (3.2, 2.5) -- (3.45, 2.5);
  % 3 channel segments
  \draw[line width=1.6pt] (3.65, 2.7) -- (3.65, 2.95); % Drain segment
  \draw[line width=1.6pt] (3.65, 2.38) -- (3.65, 2.62); % Substrate segment
  \draw[line width=1.6pt] (3.65, 2.05) -- (3.65, 2.3); % Source segment
  % Terminals
  \draw[thick] (3.65, 2.85) -- (4.2, 2.85) -- (4.2, 3.4); % Drain
  \draw[thick] (3.65, 2.15) -- (4.2, 2.15) -- (4.2, 1.6) node[circle, fill, inner sep=1.8pt] (vs) {}; % Source
  \draw[thick, ->, >=latex] (4.2, 2.15) -- (3.65, 2.5); % Substrate arrow
  \node[right=0.2cm] at (4.4, 2.5) {\large $\mathbf{M_1}$};

  % Drain Resistor RD
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.8, 3.4) rectangle (4.6, 4.3) node[midway] {\small $R_D=6\text{k}$};
  \draw[thick] (4.2, 4.3) -- (4.2, 5.2);

  % Source Resistor RS
  \draw[thick] (vs) -- (4.2, 1.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.8, 0.4) rectangle (4.6, 1.3) node[midway] {\small $R_S=6\text{k}$};
  \draw[thick] (4.2, 0.4) -- (4.2, -0.8);
\end{tikzpicture}
\end{schematicbox}

\paragraph{1. Gate DC Voltage ($V_G$):}
Since the insulated gate draws zero current ($I_G = 0$):
\[
V_G = V_{DD} \left(\frac{R_2}{R_1 + R_2}\right) = 10\text{ V} \times \left(\frac{11\text{ M}\Omega}{11\text{ M}\Omega + 11\text{ M}\Omega}\right) = \mathbf{5.0\text{ V}}
\]

\paragraph{2. Equation for $V_{GS}$:}
Applying KVL in the gate-source loop:
\[
V_{GS} = V_G - I_D R_S = 5.0 - 6.0 I_D \quad (\text{with } I_D \text{ in mA and } R_S = 6\text{ k}\Omega)
\]

\paragraph{3. Saturation Region Characteristic Equation:}
\[
I_D = K(V_{GS} - V_t)^2 = 0.48 \left( (5.0 - 6.0 I_D) - 1.0 \right)^2 = 0.48 (4.0 - 6.0 I_D)^2
\]
\[
I_D = 0.48 (16.0 - 48.0 I_D + 36.0 I_D^2) = 7.68 - 23.04 I_D + 17.28 I_D^2
\]
\[
\mathbf{17.28 I_D^2 - 24.04 I_D + 7.68 = 0}
\]
Solving via the quadratic formula:
\[
\Delta = (-24.04)^2 - 4(17.28)(7.68) = 577.9216 - 530.8416 = 47.0800
\]
\[
\sqrt{\Delta} = \sqrt{47.0800} = \mathbf{6.8615}
\]
\[
I_D = \frac{24.04 \pm 6.8615}{2(17.28)} = \frac{24.04 \pm 6.8615}{34.56}
\]
Two mathematical roots:
\begin{itemize}[leftmargin=1.5em]
  \item $I_{D1} = \frac{30.9015}{34.56} = 0.8941\text{ mA} \implies V_{GS1} = 5.0 - 6(0.8941) = -0.365\text{ V} < V_t = 1.0\text{ V}$ (\textbf{Invalid, below threshold}).
  \item $I_{D2} = \frac{17.1785}{34.56} = \mathbf{0.4971\text{ mA}} \implies V_{GS2} = 5.0 - 6(0.4971) = \mathbf{2.017\text{ V}} > V_t = 1.0\text{ V}$ (\textbf{Valid, transistor ON}).
\end{itemize}

\paragraph{4. Calculation of Drain-to-Source Voltage ($V_{DS}$):}
\[
V_{DS} = V_{DD} - I_D(R_D + R_S) = 10\text{ V} - 0.4971\text{ mA} \times (6\text{ k}\Omega + 6\text{ k}\Omega) = 10 - 0.4971(12.0) = \mathbf{4.035\text{ V}}
\]
\textbf{Pinch-Off (Saturation) Verification:}
\[
V_{DS} = 4.035\text{ V} \ge V_{GS} - V_t = 2.017\text{ V} - 1.0\text{ V} = 1.017\text{ V} \implies \text{Confirmed in Saturation Region!} \quad \checkmark
\]

\begin{answerbox}
$$\mathbf{I_D = 0.497\text{ mA}, \qquad V_{GS} = 2.017\text{ V}, \qquad V_{DS} = 4.035\text{ V}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: Barkhausen Criteria \& RC Phase Shift Oscillator [6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q5)}
State Barkhausen criteria for sinusoidal oscillation. Explain the working principle of RC phase shift oscillator with necessary expression and circuit diagram.
\end{questionbox}

\paragraph{Part (a): Barkhausen Criteria for Sustained Sinusoidal Oscillation [2 Marks]}
For a closed-loop feedback amplifier to sustain stable sinusoidal oscillations without an external input:
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Loop Gain Magnitude Criterion:} The magnitude of the open-loop gain must be at least unity:
  \[
  |\mathbf{A \beta}| \ge 1
  \]
  \item \textbf{Loop Phase Shift Criterion:} The total phase shift around the closed loop must be an integer multiple of $360^\circ$ ($0^\circ$):
  \[
  \angle (\mathbf{A \beta}) = 0^\circ \quad \text{or} \quad 360^\circ
  \]
\end{enumerate}

\paragraph{Part (b): Working Principle of Op-Amp RC Phase Shift Oscillator [4 Marks]}
\begin{schematicbox}{Op-Amp RC Phase Shift Oscillator Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Op-Amp
  \draw[thick, fill=white] (5.5, 2.0) -- (5.5, 3.6) -- (7.0, 2.8) -- cycle;
  \node at (5.8, 3.2) {\large $-$};
  \node at (5.8, 2.4) {\large $+$};
  \draw[thick] (7.0, 2.8) -- (8.5, 2.8) node[right] {\large $v_o$};

  % Non-Inverting grounded
  \draw[thick] (5.5, 2.4) -- (4.8, 2.4) -- (4.8, 2.0);
  \draw[line width=1.2pt] (4.55, 2.0) -- (5.05, 2.0);
  \draw[line width=1.0pt] (4.64, 1.92) -- (4.96, 1.92);
  \draw[line width=0.8pt] (4.72, 1.84) -- (4.88, 1.84);

  % Inverting Feedback Resistor Rf
  \draw[thick] (5.5, 3.2) -- (4.8, 3.2) -- (4.8, 4.4) -- (5.6, 4.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.6, 4.1) rectangle (6.8, 4.7) node[midway] {\small $R_f$};
  \draw[thick] (6.8, 4.4) -- (7.8, 4.4) -- (7.8, 2.8);

  % 3-Stage RC Ladder from output vo
  \draw[thick] (7.8, 2.8) -- (7.8, 0.4) -- (4.8, 0.4);

  % Stage 3 (C3, R3)
  \draw[line width=1.4pt, line cap=round] (4.8, 0.0) -- (4.8, 0.8);
  \draw[line width=1.4pt, line cap=round] (4.6, 0.0) -- (4.6, 0.8);
  \node[above] at (4.7, 0.8) {\small $C$};
  \draw[thick] (4.6, 0.4) -- (3.6, 0.4) node[circle, fill, inner sep=1.8pt] (n3) {};
  \draw[thick] (n3) -- (3.6, -0.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.2, -1.3) rectangle (4.0, -0.4) node[midway] {\small $R$};
  \draw[thick] (3.6, -1.3) -- (3.6, -1.8);

  % Stage 2 (C2, R2)
  \draw[thick] (n3) -- (3.2, 0.4);
  \draw[line width=1.4pt, line cap=round] (3.2, 0.0) -- (3.2, 0.8);
  \draw[line width=1.4pt, line cap=round] (3.0, 0.0) -- (3.0, 0.8);
  \node[above] at (3.1, 0.8) {\small $C$};
  \draw[thick] (3.0, 0.4) -- (2.0, 0.4) node[circle, fill, inner sep=1.8pt] (n2) {};
  \draw[thick] (n2) -- (2.0, -0.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.6, -1.3) rectangle (2.4, -0.4) node[midway] {\small $R$};
  \draw[thick] (2.0, -1.3) -- (2.0, -1.8);

  % Stage 1 (C1, R1)
  \draw[thick] (n2) -- (1.6, 0.4);
  \draw[line width=1.4pt, line cap=round] (1.6, 0.0) -- (1.6, 0.8);
  \draw[line width=1.4pt, line cap=round] (1.4, 0.0) -- (1.4, 0.8);
  \node[above] at (1.5, 0.8) {\small $C$};
  \draw[thick] (1.4, 0.4) -- (0.5, 0.4) node[circle, fill, inner sep=1.8pt] (n1) {};
  \draw[thick] (n1) -- (0.5, -0.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.1, -1.3) rectangle (0.9, -0.4) node[midway] {\small $R$};
  \draw[thick] (0.5, -1.3) -- (0.5, -1.8);

  % Ground bus
  \draw[thick] (0, -1.8) -- (4.0, -1.8);
  \draw[thick] (2.0, -1.8) -- (2.0, -2.0);
  \draw[line width=1.2pt] (1.75, -2.0) -- (2.25, -2.0);
  \draw[line width=1.0pt] (1.84, -2.08) -- (2.16, -2.08);
  \draw[line width=0.8pt] (1.92, -2.16) -- (2.08, -2.16);

  % Feedback to inverting input via R1
  \draw[thick] (n1) -- (0.5, 3.2) -- (2.0, 3.2);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (2.0, 2.85) rectangle (3.4, 3.55) node[midway] {\small $R_1$};
  \draw[thick] (3.4, 3.2) -- (4.8, 3.2);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Mathematical Derivation of $f_0$ and Gain Requirement:}
The transfer function of the 3-stage high-pass RC ladder feedback network is:
\[
\beta(s) = \frac{v_f(s)}{v_o(s)} = \frac{s^3 R^3 C^3}{s^3 R^3 C^3 + 6s^2 R^2 C^2 + 5sRC + 1}
\]
Substituting $s = j\omega$:
\[
\beta(j\omega) = \frac{-j\omega^3 R^3 C^3}{(1 - 6\omega^2 R^2 C^2) + j(5\omega RC - \omega^3 R^3 C^3)}
\]
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Oscillation Frequency ($f_0$):} For the feedback network to produce a $180^\circ$ phase shift, the real part in the denominator must vanish:
  \[
  1 - 6\omega_0^2 R^2 C^2 = 0 \implies \omega_0 = \frac{1}{RC\sqrt{6}} \implies \mathbf{f_0 = \frac{1}{2\pi RC\sqrt{6}}}
  \]
  \item \textbf{Feedback Attenuation at $f_0$:}
  \[
  \beta(j\omega_0) = \frac{-j(1/6\sqrt{6})}{j(5/\sqrt{6} - 1/6\sqrt{6})} = \frac{-1/6}{29/6} = -\frac{1}{29} \implies |\beta| = \frac{1}{29}
  \]
  \item \textbf{Minimum Amplifier Gain ($|A_v \beta| \ge 1$):}
  \[
  |A_v| = \frac{R_f}{R_1} \ge \frac{1}{|\beta|} = 29 \implies \mathbf{R_f \ge 29 R_1}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{|\mathbf{A\beta}| \ge 1, \quad \angle(\mathbf{A\beta}) = 360^\circ, \qquad f_0 = \frac{1}{2\pi RC\sqrt{6}}, \qquad |A_v| \ge 29 \implies R_f \ge 29 R_1}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: Widlar Current Source Operation \& Advantages [5 + 2 = 7 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q6)}
With a neat circuit diagram and necessary mathematical expressions, explain the operation of Widlar current source. What is the advantage of Widlar current source over simple current source?
\end{questionbox}

\begin{schematicbox}{BJT Widlar Current Source Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.0, 5.2) node[right] {$V_{CC}$};
  \draw[thick] (0, 0) -- (7.0, 0) node[right] {GND};

  % Reference resistor R_REF
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 3.4) rectangle (2.2, 4.3) node[midway] {\small $R_{\text{REF}}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (n1) {};
  \node[left=0.1cm] at (1.8, 4.7) {$I_{\text{REF}} \downarrow$};

  % Transistor Q1 (Diode connected NPN)
  \draw[draw=black!80, fill=white, thick] (1.8, 1.5) circle (0.45cm);
  \draw[line width=1.4pt] (1.65, 1.25) -- (1.65, 1.75); % Base
  \draw[thick] (n1) -- (1.8, 1.95); % Collector
  \draw[thick, ->, >=latex] (1.75, 1.35) -- (1.95, 1.15); % Emitter
  \draw[thick] (1.95, 1.15) -- (1.95, 0); % To GND
  % Diode connection
  \draw[thick] (n1) -- (2.6, 2.5) -- (2.6, 1.5) -- (1.65, 1.5);
  \draw[thick] (2.6, 1.5) -- (5.05, 1.5); % Base of Q2
  \node[left=0.15cm] at (1.4, 1.5) {\small $\mathbf{Q_1}$};

  % Transistor Q2 (NPN with RE)
  \draw[draw=black!80, fill=white, thick] (5.2, 1.5) circle (0.45cm);
  \draw[line width=1.4pt] (5.05, 1.25) -- (5.05, 1.75); % Base
  \draw[thick, ->, >=latex] (5.15, 1.35) -- (5.35, 1.15); % Emitter
  \draw[thick] (5.35, 1.15) -- (5.35, 0.9);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.05, 0.2) rectangle (5.65, 0.9) node[midway] {\small $R_E$};
  \draw[thick] (5.35, 0.2) -- (5.35, 0);
  \draw[thick] (5.35, 1.95) -- (5.35, 4.2) node[circle, fill, inner sep=1.8pt] {};
  \node[right=0.1cm] at (5.35, 3.8) {$I_O \uparrow$ (To Load)};
  \node[right=0.15cm] at (5.6, 1.5) {\small $\mathbf{Q_2}$};
\end{tikzpicture}
\end{schematicbox}

\paragraph{Mathematical Analysis:}
\begin{enumerate}[leftmargin=1.5em]
  \item Applying KVL around the base-emitter loop of $Q_1$ and $Q_2$:
  \[
  V_{BE1} = V_{BE2} + I_{E2} R_E \approx V_{BE2} + I_O R_E \implies I_O R_E = V_{BE1} - V_{BE2}
  \]
  \item Expressing base-emitter voltages using the Ebers-Moll equation $I_C = I_S e^{V_{BE}/V_T}$:
  \[
  V_{BE1} = V_T \ln\left(\frac{I_{\text{REF}}}{I_{S1}}\right), \qquad V_{BE2} = V_T \ln\left(\frac{I_O}{I_{S2}}\right)
  \]
  Assuming matched transistors ($I_{S1} = I_{S2}$):
  \[
  \mathbf{I_O R_E = V_T \ln\left(\frac{I_{\text{REF}}}{I_O}\right) \implies R_E = \frac{V_T}{I_O} \ln\left(\frac{I_{\text{REF}}}{I_O}\right)}
  \]
\end{enumerate}

\paragraph{Part (b): Advantages over Simple Current Source [2 Marks]}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Micro-Ampere Current Generation ($I_O \ll I_{\text{REF}}$):} Enables setting small bias currents ($\mu\text{A}$ range) using small integrated resistors ($\sim \text{k}\Omega$) rather than huge, silicon-area-prohibitive mega-ohm resistors.
  \item \textbf{Ultra-High Output Resistance:} Negative current feedback across $R_E$ increases output impedance: $R_{\text{out}} \approx r_{o2}(1 + g_{m2} R_E)$.
\end{itemize}

\begin{answerbox}
$$\mathbf{I_O R_E = V_T \ln\left(\frac{I_{\text{REF}}}{I_O}\right), \qquad R_{\text{out}} \approx r_{o2}(1 + g_{m2} R_E)}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: Transformer-Coupled Class B Amplifier \& Minimum Efficiency [6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q7)}
Draw the circuit diagram of transformer coupled Class B amplifier. Determine the condition for minimum efficiency of Class B amplifier.
\end{questionbox}

\begin{schematicbox}{Transformer-Coupled Class B Push-Pull Amplifier Circuit}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (8.2, 5.2) node[right] {$+V_{CC}$};
  \draw[thick] (0, -1.2) -- (8.2, -1.2) node[right] {GND};

  % Input Transformer T1
  \draw[thick] (0.2, 3.5) node[left] {$v_{\text{in}}$} -- (1.0, 3.5);
  \draw[thick] (1.0, 3.5) to[out=-30, in=30] (1.0, 2.5) to[out=-30, in=30] (1.0, 1.5) to[out=-30, in=30] (1.0, 0.5);
  \draw[thick] (1.0, 0.5) -- (0.2, 0.5);
  \draw[line width=1.2pt] (-0.05, 0.5) -- (0.45, 0.5);

  % Core T1
  \draw[thick] (1.3, 3.5) -- (1.3, 0.5);
  \draw[thick] (1.4, 3.5) -- (1.4, 0.5);

  % Secondary T1 (Center Tapped)
  \draw[thick] (1.7, 3.5) to[out=150, in=-150] (1.7, 2.0) to[out=150, in=-150] (1.7, 0.5);
  \draw[thick] (1.7, 2.0) -- (2.3, 2.0) node[circle, fill, inner sep=1.8pt] {};
  \draw[thick] (2.3, 2.0) -- (2.3, -1.2); % Grounded center tap

  % Transistors Q1 and Q2 (NPN)
  \draw[thick] (1.7, 3.5) -- (3.2, 3.5);
  \draw[draw=black!80, fill=white, thick] (3.6, 3.5) circle (0.45cm);
  \draw[line width=1.4pt] (3.45, 3.25) -- (3.45, 3.75);
  \draw[thick] (3.2, 3.5) -- (3.45, 3.5);
  \draw[thick, ->, >=latex] (3.55, 3.35) -- (3.75, 3.15); % Emitter
  \draw[thick] (3.75, 3.15) -- (3.75, 2.0); % Grounded emitter
  \draw[thick] (3.75, 3.85) -- (3.75, 4.5) -- (5.6, 4.5); % Collector
  \node[left=0.15cm] at (3.2, 3.8) {\small $\mathbf{Q_1}$};

  \draw[thick] (1.7, 0.5) -- (3.2, 0.5);
  \draw[draw=black!80, fill=white, thick] (3.6, 0.5) circle (0.45cm);
  \draw[line width=1.4pt] (3.45, 0.25) -- (3.45, 0.75);
  \draw[thick] (3.2, 0.5) -- (3.45, 0.5);
  \draw[thick, ->, >=latex] (3.55, 0.35) -- (3.75, 0.15); % Emitter
  \draw[thick] (3.75, 0.15) -- (3.75, -1.2); % Grounded emitter
  \draw[thick] (3.75, 0.85) -- (3.75, 1.5) -- (5.6, 1.5); % Collector
  \node[left=0.15cm] at (3.2, 0.8) {\small $\mathbf{Q_2}$};

  % Output Transformer T2 Primary
  \draw[thick] (5.6, 4.5) to[out=-30, in=30] (5.6, 3.0) to[out=-30, in=30] (5.6, 1.5);
  \draw[thick] (5.6, 3.0) -- (6.2, 3.0) -- (6.2, 5.2); % Center tap to +VCC

  % Core T2
  \draw[thick] (5.9, 4.5) -- (5.9, 1.5);
  \draw[thick] (6.0, 4.5) -- (6.0, 1.5);

  % Secondary T2 and Load RL
  \draw[thick] (6.3, 4.5) to[out=150, in=-150] (6.3, 1.5);
  \draw[thick] (6.3, 4.5) -- (7.5, 4.5) -- (7.5, 3.5);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (7.1, 2.5) rectangle (7.9, 3.5) node[midway] {\small $R_L$};
  \draw[thick] (7.5, 2.5) -- (7.5, 1.5) -- (6.3, 1.5);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Efficiency Equation and Minimum Efficiency Condition:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{General Efficiency Expression:}
  \[
  P_{o(\text{ac})} = \frac{V_p^2}{2 R_L'}, \qquad P_{i(\text{dc})} = \frac{2}{\pi} \frac{V_{CC} V_p}{R_L'} \implies \mathbf{\eta = \frac{\pi}{4} \left(\frac{V_p}{V_{CC}}\right) \times 100\%}
  \]
  \item \textbf{Condition for Minimum Efficiency ($\eta_{\min}$):}
  Since efficiency is directly proportional to the output voltage amplitude $V_p$:
  \[
  \text{As } V_p \to 0 \implies \mathbf{\eta_{\min} = 0\%}
  \]
  Minimum conversion efficiency ($\eta = 0\%$) occurs at **zero input signal amplitude** (quiescent no-signal condition).
  \item \textbf{Condition for Maximum Efficiency ($\eta_{\max}$):}
  Occurs when the output signal reaches maximum undistorted swing ($V_p = V_{CC}$):
  \[
  \mathbf{\eta_{\max} = \frac{\pi}{4} \times 100\% \approx 78.54\%}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{\eta = \frac{\pi}{4} \left(\frac{V_p}{V_{CC}}\right) \times 100\%, \qquad \eta_{\min} = 0\% \quad (\text{at } V_p = 0), \qquad \eta_{\max} = 78.54\% \quad (\text{at } V_p = V_{CC})}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: Crossover Distortion \& Class AB Elimination [6 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q8)}
Define crossover distortion in a class B amplifier and explain how class AB operation can be used to eliminate it.
\end{questionbox}

\begin{schematicbox}{Class AB Complementary Push-Pull Amplifier with Diode Biasing}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.5, 5.2) node[right] {$+V_{CC}$};
  \draw[thick] (0, -1.2) -- (7.5, -1.2) node[right] {$-V_{CC}$};

  % Biasing branch
  \draw[thick] (2.0, 5.2) -- (2.0, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.6, 3.4) rectangle (2.4, 4.3) node[midway] {\small $R_1$};
  \draw[thick] (2.0, 3.4) -- (2.0, 3.0) node[circle, fill, inner sep=1.8pt] (nb1) {};

  % Diodes D1 and D2
  \draw[thick] (nb1) -- (2.0, 2.7);
  \draw[thick, fill=black] (1.8, 2.7) -- (2.2, 2.7) -- (2.0, 2.3) -- cycle;
  \draw[line width=1.2pt] (1.8, 2.3) -- (2.2, 2.3);
  \node[left] at (1.8, 2.5) {\small $D_1$};
  \draw[thick] (2.0, 2.3) -- (2.0, 1.7);
  \draw[thick, fill=black] (1.8, 1.7) -- (2.2, 1.7) -- (2.0, 1.3) -- cycle;
  \draw[line width=1.2pt] (1.8, 1.3) -- (2.2, 1.3);
  \node[left] at (1.8, 1.5) {\small $D_2$};
  \draw[thick] (2.0, 1.3) -- (2.0, 1.0) node[circle, fill, inner sep=1.8pt] (nb2) {};

  \draw[thick] (nb2) -- (2.0, 0.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.6, -0.3) rectangle (2.4, 0.6) node[midway] {\small $R_2$};
  \draw[thick] (2.0, -0.3) -- (2.0, -1.2);

  % Input signal with AC coupling capacitors C1 and C2
  \draw[thick] (0.2, 2.0) node[left] {$v_{\text{in}}$} -- (0.8, 2.0) node[circle, fill, inner sep=1.8pt] (vin_node) {};
  \draw[thick] (vin_node) -- (0.8, 3.0) -- (1.2, 3.0);
  \draw[line width=1.4pt, line cap=round] (1.2, 2.6) -- (1.2, 3.4);
  \draw[line width=1.4pt, line cap=round] (1.4, 2.6) -- (1.4, 3.4);
  \node[above] at (1.3, 3.4) {\small $C_1$};
  \draw[thick] (1.4, 3.0) -- (nb1);

  \draw[thick] (vin_node) -- (0.8, 1.0) -- (1.2, 1.0);
  \draw[line width=1.4pt, line cap=round] (1.2, 0.6) -- (1.2, 1.4);
  \draw[line width=1.4pt, line cap=round] (1.4, 0.6) -- (1.4, 1.4);
  \node[below] at (1.3, 0.6) {\small $C_2$};
  \draw[thick] (1.4, 1.0) -- (nb2);

  % Transistor Q1 (NPN)
  \draw[thick] (nb1) -- (3.65, 3.0);
  \draw[draw=black!80, fill=white, thick] (4.0, 3.0) circle (0.45cm);
  \draw[line width=1.4pt] (3.65, 2.75) -- (3.65, 3.25);
  \draw[thick] (3.85, 3.2) -- (4.25, 3.4) -- (4.25, 5.2); % Collector to +VCC
  \draw[thick, ->, >=latex] (3.85, 2.8) -- (4.1, 2.6); % Emitter
  \draw[thick] (4.1, 2.6) -- (4.25, 2.5) -- (4.25, 2.0) node[circle, fill, inner sep=1.8pt] (out_node) {};
  \node[right=0.15cm] at (4.4, 3.2) {\small $\mathbf{Q_1}$ (NPN)};

  % Transistor Q2 (PNP)
  \draw[thick] (nb2) -- (3.65, 1.0);
  \draw[draw=black!80, fill=white, thick] (4.0, 1.0) circle (0.45cm);
  \draw[line width=1.4pt] (3.65, 0.75) -- (3.65, 1.25);
  \draw[thick, <-, >=latex] (3.85, 1.2) -- (4.1, 1.4); % Emitter arrow in
  \draw[thick] (4.1, 1.4) -- (4.25, 1.5) -- (out_node);
  \draw[thick] (3.85, 0.8) -- (4.25, 0.6) -- (4.25, -1.2); % Collector to -VCC
  \node[right=0.15cm] at (4.4, 0.8) {\small $\mathbf{Q_2}$ (PNP)};

  % Output to Load RL
  \draw[thick] (out_node) -- (6.6, 2.0) -- (6.6, 1.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (6.2, 0.5) rectangle (7.0, 1.4) node[midway] {\small $R_L$};
  \draw[thick] (6.6, 0.5) -- (6.6, 0);
  \draw[line width=1.2pt] (6.35, 0) -- (6.85, 0);
\end{tikzpicture}
\end{schematicbox}

\paragraph{1. Definition of Crossover Distortion:}
In a standard Class B push-pull stage, transistors remain unconductive whenever the input signal magnitude is below the base-emitter cut-in voltage ($|v_{\text{in}}| < 0.7\text{ V}$). This causes a flat zero-crossing interval where both transistors are completely OFF, generating severe non-linear harmonic distortion termed **crossover distortion**.

\paragraph{2. Elimination Mechanism via Class AB Biasing:}
\begin{enumerate}[leftmargin=1.5em]
  \item Diodes $D_1$ and $D_2$ establish a constant forward bias voltage $V_{BB} = V_{D1} + V_{D2} \approx 1.4\text{ V} \approx 2V_{BE}$ across the bases of $Q_1$ and $Q_2$.
  \item This trickles a small quiescent collector current ($I_{CQ} \approx 5\text{ mA} - 20\text{ mA}$) through both transistors at $v_{\text{in}} = 0\text{ V}$.
  \item Consequently, transistors transition smoothly without any zero-crossing dead-band interval, completely eliminating crossover distortion.
\end{enumerate}

\begin{answerbox}
$$\mathbf{V_{BB} = V_{D1} + V_{D2} \approx 2V_{BE} \implies \text{Completely Eliminates Zero-Crossing Dead-Band Distortion}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: Series Transistor Regulator with Current Limiting [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q9)}
Explain the working principle of a series transistor voltage regulator, accompanied by short-circuit/overload protection.
\end{questionbox}

\begin{schematicbox}{Series Transistor Voltage Regulator with Short-Circuit Current Limiting Protection}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 4.5) node[left] {$V_{\text{in}}$} -- (1.2, 4.5);
  \draw[thick] (0, 0) -- (8.5, 0) node[right] {GND};

  % Pass Transistor Q1 (NPN)
  \draw[draw=black!80, fill=white, thick] (1.8, 4.5) circle (0.55cm);
  \draw[line width=1.6pt] (1.8, 4.15) -- (1.8, 4.85); % Base
  \draw[thick] (1.2, 4.5) -- (1.45, 4.7); % Collector
  \draw[thick, ->, >=latex] (1.8, 4.3) -- (2.15, 4.5); % Emitter
  \draw[thick] (2.15, 4.5) -- (3.0, 4.5) node[circle, fill, inner sep=1.8pt] (n_sense) {};
  \node[above=0.2cm] at (1.8, 5.05) {\small $\mathbf{Q_1}$ (Pass)};

  % Current Sensing Resistor R_sense
  \draw[thick] (n_sense) -- (3.3, 4.5);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.3, 4.1) rectangle (4.5, 4.9) node[midway] {\small $R_{\text{sense}}$};
  \draw[thick] (4.5, 4.5) -- (5.2, 4.5) node[circle, fill, inner sep=1.8pt] (n_out) {};
  \draw[thick] (n_out) -- (7.8, 4.5) node[right] {\large $V_o$};

  % Current Limiting Transistor Q2 (NPN)
  \draw[draw=black!80, fill=white, thick] (4.1, 2.5) circle (0.45cm);
  \draw[line width=1.4pt] (3.85, 2.25) -- (3.85, 2.75); % Base
  \draw[thick] (n_sense) -- (3.0, 2.5) -- (3.85, 2.5); % Base connected before Rsense
  \draw[thick, ->, >=latex] (3.95, 2.35) -- (4.15, 2.15); % Emitter
  \draw[thick] (4.15, 2.15) -- (5.2, 2.15) -- (n_out); % Emitter connected after Rsense
  \draw[thick] (3.95, 2.65) -- (4.15, 2.85) -- (4.15, 3.4) -- (1.8, 3.4) -- (1.8, 4.15); % Collector pulls down Q1 base
  \node[left=0.15cm] at (3.85, 2.9) {\small $\mathbf{Q_2}$ (Limit)};

  % Base bias resistor and Zener
  \draw[thick] (0.8, 4.5) -- (0.8, 3.4) -- (1.8, 3.4);
  \draw[thick] (0.8, 3.4) -- (0.8, 2.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.4, 1.7) rectangle (1.2, 2.6) node[midway] {\small $R$};
  \draw[thick] (0.8, 1.7) -- (0.8, 1.2);
  % Zener
  \draw[thick, fill=black] (0.5, 1.2) -- (1.1, 1.2) -- (0.8, 0.6) -- cycle;
  \draw[line width=1.2pt] (0.5, 0.6) -- (1.1, 0.6);
  \draw[line width=1.2pt] (0.5, 0.6) -- (0.5, 0.45);
  \draw[line width=1.2pt] (1.1, 0.6) -- (1.1, 0.75);
  \node[left] at (0.5, 0.9) {\small $V_Z$};
  \draw[thick] (0.8, 0.6) -- (0.8, 0);

  % Load Resistor
  \draw[thick] (7.2, 4.5) -- (7.2, 3.2);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (6.8, 1.8) rectangle (7.6, 3.2) node[midway] {\small $R_L$};
  \draw[thick] (7.2, 1.8) -- (7.2, 0);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Working Principle and Current Limit Derivation:}
\begin{enumerate}[leftmargin=1.5em]
  \item The load current $I_L$ flows directly through $R_{\text{sense}}$, developing a voltage drop $V_{\text{sense}} = I_L R_{\text{sense}} = V_{BE2}$.
  \item \textbf{Under Normal Conditions ($I_L < I_{\text{limit}}$):}
  $V_{BE2} < 0.6\text{ V} \implies$ Protection transistor $Q_2$ remains completely OFF and does not affect the output voltage: $V_o \approx V_Z - V_{BE1}$.
  \item \textbf{Under Overload / Short-Circuit Fault ($I_L \ge I_{\text{limit}}$):}
  When $V_{\text{sense}}$ reaches the cut-in threshold ($V_{BE2} \approx 0.7\text{ V}$), transistor $Q_2$ turns ON and begins shunting excess base drive current away from pass transistor $Q_1$.
  \item Any attempt to draw more current causes $Q_2$ to conduct harder, throttling $Q_1$ and clamping the load current strictly at:
  \[
  \mathbf{I_{\text{limit}} = \frac{V_{BE2(\text{on})}}{R_{\text{sense}}} \approx \frac{0.7\text{ V}}{R_{\text{sense}}}}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{I_{\text{limit}} = \frac{V_{BE2}}{R_{\text{sense}}} \approx \frac{0.7\text{ V}}{R_{\text{sense}}}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: LM317 Adjustable Regulator Design (10V - 25V) [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Bhadra, Q10)}
Design a 10-25 V variable DC voltage regulator using LM317 IC.
\end{questionbox}

\[
V_{\text{out}} = 1.25\text{ V} \left(1 + \frac{R_2}{R_1}\right)
\]
\begin{enumerate}[leftmargin=1.5em]
  \item Select standard program resistor $R_1 = \mathbf{240\ \Omega}$.
  \item For $V_{\text{out}(\min)} = 10.0\text{ V}$:
  \[
  10.0 = 1.25 \left(1 + \frac{R_{2(\min)}}{240}\right) \implies 1 + \frac{R_{2(\min)}}{240} = 8.0 \implies R_{2(\min)} = 7 \times 240 = \mathbf{1680\ \Omega} = \mathbf{1.68\text{ k}\Omega}
  \]
  \item For $V_{\text{out}(\max)} = 25.0\text{ V}$:
  \[
  25.0 = 1.25 \left(1 + \frac{R_{2(\max)}}{240}\right) \implies 1 + \frac{R_{2(\max)}}{240} = 20.0 \implies R_{2(\max)} = 19 \times 240 = \mathbf{4560\ \Omega} = \mathbf{4.56\text{ k}\Omega}
  \]
\end{enumerate}
\textbf{Practical Realization:} Use a fixed precision resistor $R_{2A} = 1.6\text{ k}\Omega$ in series with a $\mathbf{3.0\text{ k}\Omega}$ linear potentiometer ($R_2 = 1.68\text{ k}\Omega \text{ to } 4.56\text{ k}\Omega$). Input DC voltage: $V_{\text{in}} \ge 28\text{ V DC}$.

\begin{answerbox}
$$\mathbf{R_1 = 240\ \Omega, \qquad R_2 = 1.68\text{ k}\Omega \text{ to } 4.56\text{ k}\Omega \quad (\text{Fixed } 1.6\text{ k}\Omega + 3.0\text{ k}\Omega \text{ Potentiometer})}$$
\end{answerbox}
"""
