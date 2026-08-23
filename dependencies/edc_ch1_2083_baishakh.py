# edc_ch1_2083_baishakh.py
# Chapter 1: 2083 Baishakh Examination Master Solutions (Refined & Fully Verified)

def get_chapter_2083_baishakh():
    return r"""
\chapter{2083 Baishakh Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BEI, BCT & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Electronic Devices \& Circuits (ENEX 151) & \textbf{Examination Type:} Back (New Course) \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: BJT vs. FET Conduction \& Common Collector Amplifier Design [1 + 5 = 6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q1)}
Why BJT is bipolar and FET is unipolar? Design $\beta$-independent type DC biased common collector amplifier. Given parameters are: $V_{CC} = 20\text{ V}, I_C = 2\text{ mA}$, and $\beta = 100$. Use firm biasing method.
\end{questionbox}

\paragraph{Part (a): Bipolar vs. Unipolar Operating Mechanism [1 Mark]}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{BJT is Bipolar:} Its current conduction relies simultaneously on \textbf{both majority and minority charge carriers} (free electrons and holes) flowing across two $p$-$n$ junctions (emitter-base and collector-base).
  \item \textbf{FET is Unipolar:} Electric conduction takes place exclusively through a continuous channel containing \textbf{only one type of charge carrier} (electrons in n-channel, holes in p-channel) modulated by an electric field with zero minority carrier participation.
\end{itemize}

\paragraph{Part (b): $\beta$-Independent Common Collector (Emitter Follower) Design [5 Marks]}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Emitter Bias Voltage Selection ($V_{EQ}$):}
  To allow maximum symmetrical undistorted AC output voltage swing without premature clipping:
  \[
  V_{EQ} = \frac{V_{CC}}{2} = \frac{20\text{ V}}{2} = \mathbf{10.0\text{ V}}
  \]
  \item \textbf{Emitter Resistor ($R_E$):}
  Since $I_E \approx I_C = 2.0\text{ mA}$:
  \[
  R_E = \frac{V_{EQ}}{I_E} = \frac{10.0\text{ V}}{2.0\text{ mA}} = 5.0\text{ k}\Omega \quad (\text{Select standard } R_E = \mathbf{5.1\text{ k}\Omega})
  \]
  \item \textbf{Base DC Voltage ($V_B$):}
  \[
  V_B = V_{EQ} + V_{BE} = 10.0\text{ V} + 0.7\text{ V} = \mathbf{10.7\text{ V}}
  \]
  \item \textbf{Firm Biasing Method ($I_{\text{bleed}} = 10 I_B$):}
  \[
  I_B = \frac{I_C}{\beta} = \frac{2.0\text{ mA}}{100} = 0.02\text{ mA} = 20\ \mu\text{A}
  \]
  \[
  I_{\text{bleed}} = 10 \times I_B = 10 \times 0.02\text{ mA} = \mathbf{0.20\text{ mA}}
  \]
  \item \textbf{Voltage Divider Resistors ($R_1, R_2$):}
  \[
  R_2 = \frac{V_B}{I_{\text{bleed}}} = \frac{10.7\text{ V}}{0.20\text{ mA}} = 53.5\text{ k}\Omega \quad (\text{Select standard } R_2 = \mathbf{56\text{ k}\Omega})
  \]
  \[
  R_1 = \frac{V_{CC} - V_B}{I_{\text{bleed}} + I_B} = \frac{20\text{ V} - 10.7\text{ V}}{0.20\text{ mA} + 0.02\text{ mA}} = \frac{9.3\text{ V}}{0.22\text{ mA}} = 42.27\text{ k}\Omega \quad (\text{Select standard } R_1 = \mathbf{43\text{ k}\Omega})
  \]
  \item \textbf{$\beta$-Independency Verification:}
  \[
  R_{\text{th}} = R_1 \parallel R_2 = 43\text{ k}\Omega \parallel 56\text{ k}\Omega = \frac{43 \times 56}{43 + 56} = \mathbf{24.32\text{ k}\Omega}
  \]
  Firm bias stability criterion: $R_{\text{th}} \le 0.1(1+\beta)R_E = 0.1(101)(5.1\text{ k}\Omega) = 51.5\text{ k}\Omega \implies 24.32\text{ k}\Omega < 51.5\text{ k}\Omega \quad \checkmark$
\end{enumerate}

\begin{schematicbox}{Designed $\beta$-Independent Common Collector (Emitter Follower) Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.2, 5.2) node[right] {\large $\mathbf{V_{CC} = +20\text{V}}$};
  \draw[thick] (0, -0.8) -- (7.2, -0.8) node[right] {\textbf{GND}};

  % Divider R1 and R2
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.15, 3.4) rectangle (2.45, 4.3) node[midway] {\small $R_1=43\text{k}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (vb) {};
  \draw[thick] (1.8, 2.5) -- (1.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.15, 0.7) rectangle (2.45, 1.6) node[midway] {\small $R_2=56\text{k}$};
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
  \draw[thick] (3.8, 2.7) -- (4.25, 3.05) -- (4.25, 5.2); % Collector directly to VCC
  \draw[thick, ->, >=latex] (3.8, 2.3) -- (4.1, 2.05); % Emitter
  \draw[thick] (4.1, 2.05) -- (4.25, 1.95) -- (4.25, 1.6) node[circle, fill, inner sep=1.8pt] (ve) {};
  \node[right=0.2cm] at (4.4, 2.7) {\large $\mathbf{Q_1}$};

  % Emitter Resistor RE
  \draw[thick] (ve) -- (4.25, 1.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.6, 0.4) rectangle (4.9, 1.3) node[midway] {\small $R_E=5.1\text{k}$};
  \draw[thick] (4.25, 0.4) -- (4.25, -0.8);

  % Output coupling capacitor C2
  \draw[thick] (ve) -- (5.4, 1.6);
  \draw[line width=1.4pt, line cap=round] (5.4, 1.2) -- (5.4, 2.0);
  \draw[line width=1.4pt, line cap=round] (5.6, 1.2) -- (5.6, 2.0);
  \node[above] at (5.5, 2.0) {$C_2$};
  \draw[thick] (5.6, 1.6) -- (6.8, 1.6) node[right] {\large $V_o$};
\end{tikzpicture}
\end{schematicbox}

\begin{answerbox}
$$\mathbf{R_1 = 43\text{ k}\Omega, \quad R_2 = 56\text{ k}\Omega, \quad R_E = 5.1\text{ k}\Omega, \quad V_{EQ} = 10\text{ V}, \quad I_{CQ} = 2.0\text{ mA}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: Role of Bypass Capacitor \& Common Base AC Parameters [2 + 5 = 7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q2)}
Explain the role of bypass capacitor in amplifier circuits. Draw the small signal equivalent circuit of a common base amplifier circuit and find its input impedance, output impedance and voltage gain.
\end{questionbox}

\paragraph{Part (a): Role of Bypass Capacitor [2 Marks]}
\begin{itemize}[leftmargin=1.5em]
  \item In a BJT amplifier, the emitter resistor $R_E$ provides crucial DC operating point stability against temperature variations and $\beta$ changes.
  \item However, for AC signals, an unbypassed $R_E$ introduces negative series current feedback which drastically reduces the AC voltage gain ($A_v \approx -R_C/R_E$).
  \item Connecting a **bypass capacitor ($C_E$)** in parallel with $R_E$ provides a near zero-impedance AC short-circuit path ($X_{C_E} = \frac{1}{2\pi f C_E} \approx 0$) to ground at signal frequencies, eliminating AC negative feedback and maximizing voltage gain ($A_v \approx -R_C/r_e$).
\end{itemize}

\paragraph{Part (b): Common Base Small-Signal Equivalent Model [5 Marks]}
\begin{schematicbox}{Small-Signal $r_e$ Model of Common Base (CB) Amplifier}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Common Base Ground Rail
  \draw[thick] (0, 0) -- (8.5, 0) node[right] {\textbf{Base (GND)}};

  % Input Terminal at Emitter (Left)
  \draw[thick] (0.2, 2.5) node[left] {$v_{\text{in}}$} -- (1.5, 2.5) node[circle, fill, inner sep=1.8pt] (e_node) {};
  \draw[thick, ->, >=latex] (0.5, 2.75) -- (1.2, 2.75) node[midway, above] {$i_e$};

  % Emitter Biasing Resistor RE
  \draw[thick] (1.5, 2.5) -- (1.5, 1.8);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.05, 0.8) rectangle (1.95, 1.8) node[midway] {\small $R_E$};
  \draw[thick] (1.5, 0.8) -- (1.5, 0);

  % Dynamic Emitter Resistance re
  \draw[thick] (e_node) -- (3.0, 2.5) -- (3.0, 1.8);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (2.55, 0.8) rectangle (3.45, 1.8) node[midway] {\small $r_e$};
  \draw[thick] (3.0, 0.8) -- (3.0, 0);
  \node[above] at (2.25, 2.5) {\textbf{Emitter}};

  % Dependent Collector Current Source alpha * ie (Right branch, pointing UP to collector)
  \draw[thick] (5.5, 0) -- (5.5, 0.8);
  \draw[thick] (5.5, 1.25) circle (0.45cm);
  \draw[thick, ->, >=latex] (5.5, 0.9) -- (5.5, 1.6);
  \node[left=0.15cm] at (5.05, 1.25) {\small $\mathbf{\alpha i_e}$};
  \draw[thick] (5.5, 1.7) -- (5.5, 2.5) -- (7.0, 2.5) node[circle, fill, inner sep=1.8pt] (c_node) {};
  \node[above] at (6.25, 2.5) {\textbf{Collector}};

  % Collector Resistor RC
  \draw[thick] (7.0, 2.5) -- (7.0, 1.8);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (6.55, 0.8) rectangle (7.45, 1.8) node[midway] {\small $R_C$};
  \draw[thick] (7.0, 0.8) -- (7.0, 0);

  % Output Node
  \draw[thick] (c_node) -- (8.2, 2.5) node[right] {\large $v_o$};
\end{tikzpicture}
\end{schematicbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Input Impedance ($Z_{\text{in}}$):}
  Looking into the emitter terminal with base grounded:
  \[
  Z_{\text{in}} = R_E \parallel r_e \approx \mathbf{r_e = \frac{V_T}{I_E}} \quad (\text{very low, typically } 10\ \Omega - 50\ \Omega)
  \]
  \item \textbf{Output Impedance ($Z_{\text{out}}$):}
  Looking back from the collector with $v_{\text{in}} = 0 \implies i_e = 0$:
  \[
  Z_{\text{out}} = R_C \parallel r_o \approx \mathbf{R_C} \quad (\text{high})
  \]
  \item \textbf{Voltage Gain ($A_v$):}
  \[
  v_o = -(-\alpha i_e)(R_C \parallel R_L) = \alpha i_e (R_C \parallel R_L), \qquad v_{\text{in}} = i_e r_e
  \]
  \[
  \mathbf{A_v = \frac{v_o}{v_{\text{in}}} = \frac{\alpha (R_C \parallel R_L)}{r_e} \approx +\frac{R_C \parallel R_L}{r_e}} \quad (\text{Non-inverting, } 0^\circ \text{ phase shift})
  \]
  \item \textbf{Current Gain ($A_i$):}
  \[
  \mathbf{A_i = \frac{i_o}{i_e} = -\alpha \approx -1}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{Z_{\text{in}} \approx r_e = \frac{V_T}{I_E}, \qquad Z_{\text{out}} \approx R_C, \qquad A_v = +\frac{\alpha(R_C \parallel R_L)}{r_e}, \qquad A_i = -\alpha \approx -1}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: N-Channel Depletion-Type MOSFET [6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q3)}
Describe the construction and working principle of N Channel D-MOSFET with the help of characteristic curves and mathematical expressions.
\end{questionbox}

\paragraph{1. Physical Construction:}
Fabricated on a p-type silicon substrate with two heavily doped $n^+$ Source and Drain regions, physically connected by an initial pre-diffused n-channel. The Gate electrode is completely insulated from the channel by an ultrathin silicon dioxide ($\text{SiO}_2$) dielectric layer ($R_{\text{in}} > 10^{12}\ \Omega$).

\begin{schematicbox}{Transfer and Drain Characteristics of N-Channel D-MOSFET}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Transfer Characteristics (left)
  \draw[thick, ->, >=latex] (-4.5, 0) -- (2.0, 0) node[right] {$V_{GS}\ (\text{V})$};
  \draw[thick, ->, >=latex] (0, 0) -- (0, 4.2) node[above] {$I_D\ (\text{mA})$};
  \draw[domain=-3.5:1.2, smooth, variable=\x, line width=1.3pt, blue] plot ({\x}, {1.8*(1 + \x/3.5)^2});
  \node[below] at (-3.5, 0) {$V_P$};
  \draw[dashed, gray] (0, 1.8) -- (-3.5, 1.8);
  \node[left] at (0, 1.8) {$I_{DSS}$};
  \node[left] at (-1.5, 3.5) {\small\textbf{Depletion Mode ($V_{GS}<0$)}};
  \node[right] at (0.2, 3.5) {\small\textbf{Enhancement Mode ($V_{GS}>0$)}};

  % Drain Characteristics (right)
  \draw[thick, ->, >=latex] (4.0, 0) -- (11.0, 0) node[right] {$V_{DS}\ (\text{V})$};
  \draw[thick, ->, >=latex] (4.0, 0) -- (4.0, 4.2) node[above] {$I_D\ (\text{mA})$};
  \draw[line width=1.2pt, teal] (4.0, 0) to[out=60, in=180] (5.5, 3.4) -- (9.8, 3.4) node[right] {\small $V_{GS} = +1\text{V}$};
  \draw[line width=1.2pt, teal] (4.0, 0) to[out=55, in=180] (5.2, 2.4) -- (9.8, 2.4) node[right] {\small $V_{GS} = 0\text{V}\ (I_{DSS})$};
  \draw[line width=1.2pt, teal] (4.0, 0) to[out=50, in=180] (4.8, 1.4) -- (9.8, 1.4) node[right] {\small $V_{GS} = -1\text{V}$};
  \draw[line width=1.2pt, teal] (4.0, 0) to[out=45, in=180] (4.4, 0.6) -- (9.8, 0.6) node[right] {\small $V_{GS} = -2\text{V}$};
  \draw[thick, red, dashed] (4.0, 0.05) -- (9.8, 0.05) node[right] {\small $V_{GS} \le V_P\ (I_D=0)$};
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. Working Principle \& Modes of Operation:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Depletion Mode ($V_{GS} < 0$):} Negative gate voltage repels electrons out of the n-channel, creating a depletion region and reducing drain current below $I_{DSS}$. At $V_{GS} = V_P$ (pinch-off), the channel is completely closed ($I_D = 0$).
  \item \textbf{Enhancement Mode ($V_{GS} > 0$):} Positive gate voltage attracts additional free electrons into the channel, widening it and increasing drain current above $I_{DSS}$.
\end{enumerate}

\paragraph{3. Governing Shockley Equation:}
\[
\mathbf{I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2 \quad \text{for } V_{DS} \ge V_{GS} - V_P}
\]
\[
\mathbf{g_m = \left.\frac{\partial I_D}{\partial V_{GS}}\right|_{V_{DS}} = \frac{2I_{DSS}}{|V_P|}\left(1 - \frac{V_{GS}}{V_P}\right) = g_{m0}\left(1 - \frac{V_{GS}}{V_P}\right)}
\]

\begin{answerbox}
$$\mathbf{I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2 \quad \text{valid in both Depletion } (V_{GS}<0) \text{ and Enhancement } (V_{GS}>0) \text{ modes}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: JFET Voltage Divider Bias Analysis [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q4)}
Find $I_D$ and $V_{DS}$ for the given circuit. Given parameters: $V_P = -4\text{ V}$ and $I_{DSS} = 8\text{ mA}$.
Circuit values: $V_{DD} = +16\text{ V}, R_1 = 2.1\text{ M}\Omega, R_2 = 270\text{ k}\Omega, R_D = 2.4\text{ k}\Omega, R_S = 1.5\text{ k}\Omega$.
\end{questionbox}

\begin{schematicbox}{JFET Voltage-Divider Bias Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.0) -- (6.5, 5.0) node[right] {\large $\mathbf{V_{DD} = +16\text{V}}$};
  \draw[thick] (0, 0) -- (6.5, 0) node[right] {\textbf{GND}};

  % Gate Voltage Divider (R1 and R2)
  \draw[thick] (1.5, 5.0) -- (1.5, 4.2);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.85, 3.2) rectangle (2.15, 4.2) node[midway] {\small $R_1=2.1\text{M}$};
  \draw[thick] (1.5, 3.2) -- (1.5, 2.5) node[circle, fill, inner sep=1.8pt] (vg_node) {};
  \draw[thick] (1.5, 2.5) -- (1.5, 1.8);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.85, 0.8) rectangle (2.15, 1.8) node[midway] {\small $R_2=270\text{k}$};
  \draw[thick] (1.5, 0.8) -- (1.5, 0);

  % N-JFET Transistor
  \draw[thick] (vg_node) -- (3.5, 2.5);
  \draw[thick] (3.5, 2.5) -- (3.9, 2.5);
  \draw[line width=1.5pt] (3.9, 1.8) -- (3.9, 3.2); % Channel bar
  \draw[thick, ->, >=latex] (3.5, 2.5) -- (3.9, 2.5); % Inward arrow for N-JFET
  \node[left=0.2cm] at (3.5, 2.8) {\large $\mathbf{V_G}$};

  % Drain Branch (RD)
  \draw[thick] (3.9, 3.0) -- (4.8, 3.0) -- (4.8, 3.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (4.15, 3.4) rectangle (5.45, 4.3) node[midway] {\small $R_D=2.4\text{k}$};
  \draw[thick] (4.8, 4.3) -- (4.8, 5.0);

  % Source Branch (RS)
  \draw[thick] (3.9, 2.0) -- (4.8, 2.0) -- (4.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (4.15, 0.7) rectangle (5.45, 1.6) node[midway] {\small $R_S=1.5\text{k}$};
  \draw[thick] (4.8, 0.7) -- (4.8, 0);
  \node[right=0.15cm] at (4.0, 2.5) {\large $\mathbf{Q_1}$ (N-JFET)};
\end{tikzpicture}
\end{schematicbox}

\paragraph{1. Thevenin Gate DC Voltage ($V_G$):}
Since the gate of a JFET draws negligible current ($I_G \approx 0$):
\[
V_G = V_{DD} \left(\frac{R_2}{R_1 + R_2}\right) = 16\text{ V} \times \left(\frac{270\text{ k}\Omega}{2100\text{ k}\Omega + 270\text{ k}\Omega}\right) = 16 \times \frac{270}{2370} = \mathbf{1.823\text{ V}}
\]

\paragraph{2. Gate-to-Source Voltage Equation ($V_{GS}$):}
Applying KVL around the gate-source loop:
\[
V_{GS} = V_G - I_D R_S = 1.823 - 1.5 I_D \quad (\text{with } I_D \text{ in mA and } R_S = 1.5\text{ k}\Omega)
\]

\paragraph{3. Solving via Shockley's Equation:}
\[
I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2 = 8 \left(1 - \frac{1.823 - 1.5 I_D}{-4}\right)^2 = 8 \left(\frac{4 + 1.823 - 1.5 I_D}{4}\right)^2
\]
\[
I_D = \frac{8}{16} (5.823 - 1.5 I_D)^2 = 0.5 \left(33.907 - 17.469 I_D + 2.25 I_D^2\right)
\]
\[
2 I_D = 33.907 - 17.469 I_D + 2.25 I_D^2 \implies \mathbf{2.25 I_D^2 - 19.469 I_D + 33.907 = 0}
\]
Solving using the quadratic formula:
\[
I_D = \frac{19.469 \pm \sqrt{(-19.469)^2 - 4(2.25)(33.907)}}{2(2.25)} = \frac{19.469 \pm \sqrt{379.04 - 305.16}}{4.5} = \frac{19.469 \pm 8.595}{4.5}
\]
Two mathematical roots:
\begin{itemize}[leftmargin=1.5em]
  \item $I_{D1} = \frac{28.064}{4.5} = 6.236\text{ mA} \implies V_{GS1} = 1.823 - 1.5(6.236) = -7.53\text{ V} < V_P = -4\text{ V}$ (\textbf{Physically Invalid, beyond pinch-off}).
  \item $I_{D2} = \frac{10.874}{4.5} = \mathbf{2.416\text{ mA}} \implies V_{GS2} = 1.823 - 1.5(2.416) = \mathbf{-1.802\text{ V}}$ (\textbf{Physically Valid, in active channel region}).
\end{itemize}

\paragraph{4. Calculation of Drain-to-Source Voltage ($V_{DS}$):}
\[
V_{DS} = V_{DD} - I_D(R_D + R_S) = 16\text{ V} - 2.416\text{ mA} \times (2.4\text{ k}\Omega + 1.5\text{ k}\Omega) = 16 - 2.416(3.9) = \mathbf{6.576\text{ V}}
\]
\textbf{Pinch-Off Verification:}
\[
V_{DS} = 6.576\text{ V} \ge V_{GS} - V_P = -1.802\text{ V} - (-4.0\text{ V}) = 2.198\text{ V} \implies \text{Confirmed in Saturation Region!} \quad \checkmark
\]

\begin{answerbox}
$$\mathbf{I_D = 2.416\text{ mA}, \qquad V_{GS} = -1.802\text{ V}, \qquad V_{DS} = 6.576\text{ V}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: RC vs. LC Oscillators \& Wien Bridge Oscillator [1 + 5 = 6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q5)}
What is the main difference between RC and LC oscillator circuits in terms of application? Explain the operation of Wien Bridge Oscillator circuit with the help of circuit diagram and necessary mathematical expressions.
\end{questionbox}

\paragraph{Part (a): Application Differences Between RC and LC Oscillators [1 Mark]}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{RC Oscillators (e.g., Wien Bridge, Phase-Shift):} Used primarily for **Audio Frequencies (AF)** ($10\text{ Hz} - 1\text{ MHz}$) where resistor-capacitor networks provide compact size, high low-frequency stability, and smooth sinusoidal waveforms.
  \item \textbf{LC Oscillators (e.g., Hartley, Colpitts):} Used primarily for **Radio Frequencies (RF)** ($100\text{ kHz} - 500\text{ MHz}$) where compact inductors and capacitors form high-$Q$ resonant tank circuits. At audio frequencies, LC inductors become excessively bulky and lossy.
\end{itemize}

\paragraph{Part (b): Wien Bridge Oscillator Operation \& Derivations [5 Marks]}
\begin{schematicbox}{Op-Amp Wien Bridge Oscillator Circuit with RC Lead-Lag Network}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Op-Amp
  \draw[thick, fill=white] (4.5, 2.0) -- (4.5, 3.6) -- (6.0, 2.8) -- cycle;
  \node at (4.8, 3.2) {\large $-$};
  \node at (4.8, 2.4) {\large $+$};
  \draw[thick] (6.0, 2.8) -- (7.5, 2.8) node[right] {\large $v_o$};

  % Inverting Feedback Branch (Rf and R1)
  \draw[thick] (4.5, 3.2) -- (3.5, 3.2) -- (3.5, 4.4) -- (4.4, 4.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (4.4, 4.1) rectangle (5.6, 4.7) node[midway] {\small $R_f$};
  \draw[thick] (5.6, 4.4) -- (6.8, 4.4) -- (6.8, 2.8);

  \draw[thick] (3.5, 3.2) -- (2.5, 3.2) -- (2.5, 2.2);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (2.2, 1.3) rectangle (2.8, 2.2) node[midway] {\small $R_1$};
  \draw[thick] (2.5, 1.3) -- (2.5, 1.1);
  \draw[line width=1.2pt] (2.25, 1.1) -- (2.75, 1.1);
  \draw[line width=1.0pt] (2.34, 1.02) -- (2.66, 1.02);
  \draw[line width=0.8pt] (2.42, 0.94) -- (2.58, 0.94);

  % Non-Inverting Feedback Lead-Lag Network
  \draw[thick] (6.8, 2.8) -- (6.8, 0.2) -- (5.6, 0.2);
  \draw[line width=1.4pt, line cap=round] (5.6, -0.2) -- (5.6, 0.6);
  \draw[line width=1.4pt, line cap=round] (5.4, -0.2) -- (5.4, 0.6);
  \node[above] at (5.5, 0.6) {\small $C$};
  \draw[thick] (5.4, 0.2) -- (4.6, 0.2);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.6, -0.1) rectangle (4.6, 0.5) node[midway] {\small $R$};
  \draw[thick] (3.6, 0.2) -- (1.5, 0.2) node[circle, fill, inner sep=1.8pt] (vfb) {};

  % Connection to Non-Inverting Input
  \draw[thick] (vfb) -- (1.5, 2.4) -- (4.5, 2.4);

  % Parallel R and C branch to ground
  \draw[thick] (vfb) -- (1.0, 0.2) -- (1.0, -0.5);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.7, -1.4) rectangle (1.3, -0.5) node[midway] {\small $R$};
  \draw[thick] (1.0, -1.4) -- (1.0, -1.8);

  \draw[thick] (vfb) -- (2.0, 0.2) -- (2.0, -0.7);
  \draw[line width=1.4pt, line cap=round] (1.7, -0.7) -- (2.3, -0.7);
  \draw[line width=1.4pt, line cap=round] (1.7, -0.9) -- (2.3, -0.9);
  \node[right] at (2.3, -0.8) {\small $C$};
  \draw[thick] (2.0, -0.9) -- (2.0, -1.8);

  \draw[thick] (1.0, -1.8) -- (2.0, -1.8) -- (1.5, -1.8) -- (1.5, -2.0);
  \draw[line width=1.2pt] (1.25, -2.0) -- (1.75, -2.0);
  \draw[line width=1.0pt] (1.34, -2.08) -- (1.66, -2.08);
  \draw[line width=0.8pt] (1.42, -2.16) -- (1.58, -2.16);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Derivation of Resonant Frequency and Gain Requirement:}
The transfer function of the lead-lag feedback network $\beta(s) = \frac{v_f(s)}{v_o(s)}$ is:
\[
\beta(s) = \frac{Z_p}{Z_s + Z_p} = \frac{\frac{R}{1+sRC}}{\left(R + \frac{1}{sRC}\right) + \frac{R}{1+sRC}} = \frac{sRC}{(sRC)^2 + 3sRC + 1}
\]
Substituting $s = j\omega$:
\[
\beta(j\omega) = \frac{j\omega RC}{(1 - \omega^2 R^2 C^2) + 3j\omega RC}
\]
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Oscillation Frequency ($f_0$):} For zero phase shift ($\angle \beta = 0^\circ$), the imaginary term in the bracket must vanish:
  \[
  1 - \omega_0^2 R^2 C^2 = 0 \implies \omega_0 = \frac{1}{RC} \implies \mathbf{f_0 = \frac{1}{2\pi RC}}
  \]
  \item \textbf{Attenuation at Resonance:}
  \[
  \beta(j\omega_0) = \frac{j}{3j} = \frac{1}{3}
  \]
  \item \textbf{Barkhausen Gain Requirement ($|A_v \beta| \ge 1$):}
  \[
  A_v = 1 + \frac{R_f}{R_1} \ge \frac{1}{\beta} = 3 \implies \mathbf{R_f \ge 2 R_1}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{f_0 = \frac{1}{2\pi RC}, \qquad R_f \ge 2 R_1 \quad (|A_v| \ge 3)}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: Base-Current-Compensated Current Mirror [5 + 2 = 7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q6)}
Explain how a base current compensation circuit reduces the difference between $I_O$ and $I_{\text{REF}}$ in a simple current mirror circuit.
\end{questionbox}

\paragraph{1. Circuit Description \& Role of Compensating Transistor $Q_3$:}
In a standard two-transistor current mirror, the reference branch must supply the base currents of both $Q_1$ and $Q_2$, introducing a relative error of $\approx 2/\beta$. A 3-transistor compensated current mirror inserts an emitter-follower transistor $Q_3$ to buffer the base currents.

\begin{schematicbox}{Base-Current-Compensated BJT Current Mirror Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.0, 5.2) node[right] {$V_{CC}$};
  \draw[thick] (0, 0) -- (7.0, 0) node[right] {GND};

  % R_REF
  \draw[thick] (1.5, 5.2) -- (1.5, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.1, 3.4) rectangle (1.9, 4.3) node[midway] {\small $R_{\text{REF}}$};
  \draw[thick] (1.5, 3.4) -- (1.5, 2.5) node[circle, fill, inner sep=1.8pt] (n1) {};
  \node[left=0.1cm] at (1.5, 4.7) {$I_{\text{REF}} \downarrow$};

  % Transistor Q1 (NPN)
  \draw[thick] (n1) -- (1.5, 2.0);
  \draw[draw=black!80, fill=white, thick] (1.5, 1.5) circle (0.45cm);
  \draw[line width=1.4pt] (1.35, 1.25) -- (1.35, 1.75);
  \draw[thick] (1.5, 2.0) -- (1.65, 1.75); % Collector
  \draw[thick, ->, >=latex] (1.45, 1.35) -- (1.65, 1.15); % Emitter
  \draw[thick] (1.65, 1.15) -- (1.65, 0); % To GND
  \node[left=0.15cm] at (1.1, 1.5) {\small $\mathbf{Q_1}$};

  % Helper Transistor Q3 (NPN)
  \draw[thick] (n1) -- (3.0, 2.5); % Collector of Q1 to Base of Q3
  \draw[draw=black!80, fill=white, thick] (3.5, 2.5) circle (0.45cm);
  \draw[line width=1.4pt] (3.35, 2.25) -- (3.35, 2.75); % Base
  \draw[thick] (3.0, 2.5) -- (3.35, 2.5);
  \draw[thick] (3.5, 2.95) -- (3.65, 3.1) -- (3.65, 5.2); % Q3 Collector to VCC
  \draw[thick, ->, >=latex] (3.45, 2.35) -- (3.65, 2.15); % Q3 Emitter
  \draw[thick] (3.65, 2.15) -- (3.65, 1.5) node[circle, fill, inner sep=1.8pt] (n_bases) {};
  \node[right=0.15cm] at (3.9, 2.8) {\small $\mathbf{Q_3}$};

  % Connect Q3 emitter to bases of Q1 and Q2
  \draw[thick] (n_bases) -- (1.35, 1.5);
  \draw[thick] (n_bases) -- (5.35, 1.5);

  % Transistor Q2 (NPN)
  \draw[draw=black!80, fill=white, thick] (5.5, 1.5) circle (0.45cm);
  \draw[line width=1.4pt] (5.35, 1.25) -- (5.35, 1.75);
  \draw[thick, ->, >=latex] (5.45, 1.35) -- (5.65, 1.15); % Emitter
  \draw[thick] (5.65, 1.15) -- (5.65, 0); % To GND
  \draw[thick] (5.65, 1.75) -- (5.65, 4.2) node[circle, fill, inner sep=1.8pt] {};
  \node[right=0.1cm] at (5.65, 3.8) {$I_O \uparrow$ (To Load)};
  \node[right=0.15cm] at (5.9, 1.5) {\small $\mathbf{Q_2}$};
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. Mathematical Derivation of Output Current $I_O$:}
\begin{enumerate}[leftmargin=1.5em]
  \item Assuming matched transistors ($I_{C1} = I_{C2} = I_O$ and $I_{B1} = I_{B2} = I_B = \frac{I_O}{\beta}$):
  \[
  I_{E3} = I_{B1} + I_{B2} = 2 I_B = \frac{2 I_O}{\beta}
  \]
  \item Transistor $Q_3$ base current is reduced by a factor of $(1+\beta)$:
  \[
  I_{B3} = \frac{I_{E3}}{1+\beta} = \frac{2 I_O}{\beta(1+\beta)} \approx \frac{2 I_O}{\beta^2}
  \]
  \item Applying KCL at the reference collector node:
  \[
  I_{\text{REF}} = I_{C1} + I_{B3} = I_O + \frac{2 I_O}{\beta(\beta + 1)} = I_O \left[1 + \frac{2}{\beta^2 + \beta}\right]
  \]
  \[
  \mathbf{I_O = \frac{I_{\text{REF}}}{1 + \frac{2}{\beta^2 + \beta}} \approx I_{\text{REF}} \left(1 - \frac{2}{\beta^2}\right)}
  \]
\end{enumerate}

\paragraph{3. Error Comparison:}
\begin{itemize}[leftmargin=1.5em]
  \item Simple 2-BJT Mirror Error: $\frac{|I_{\text{REF}} - I_O|}{I_{\text{REF}}} \approx \frac{2}{\beta} = 2.0\%$ (for $\beta = 100$).
  \item Base-Compensated Mirror Error: $\frac{|I_{\text{REF}} - I_O|}{I_{\text{REF}}} \approx \frac{2}{\beta^2} = 0.02\%$ (a **100-fold accuracy improvement**).
\end{itemize}

\begin{answerbox}
$$\mathbf{I_O = \frac{I_{\text{REF}}}{1 + \frac{2}{\beta^2 + \beta}} \approx I_{\text{REF}} \left(1 - \frac{2}{\beta^2}\right) \implies \text{Error reduced from } O(1/\beta) \text{ to } O(1/\beta^2)}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: Class B Power Amplifier Calculations [6 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q7)}
For a class B amplifier providing a $20\text{ V peak}$ signal to a $16\ \Omega$ load (speaker) and a power supply of $V_{CC} = 30\text{ V}$, determine the input power, output power, and circuit efficiency.
\end{questionbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Peak Output Voltage ($V_p$):}
  \[
  V_p = \mathbf{20.0\text{ V}}
  \]
  \item \textbf{AC Output Signal Power ($P_{o(\text{ac})}$):}
  \[
  P_{o(\text{ac})} = \frac{V_p^2}{2 R_L} = \frac{(20\text{ V})^2}{2 \times 16\ \Omega} = \frac{400}{32} = \mathbf{12.5\text{ W}}
  \]
  \item \textbf{Average DC Supply Current ($I_{\text{dc}}$):}
  For a complementary Class B push-pull amplifier, each transistor conducts over half a cycle:
  \[
  I_{\text{dc}} = \frac{2}{\pi} I_p = \frac{2}{\pi} \left(\frac{V_p}{R_L}\right) = \frac{2}{\pi} \left(\frac{20\text{ V}}{16\ \Omega}\right) = \frac{40}{16\pi} = \frac{2.5}{\pi} \approx \mathbf{0.7958\text{ A}}
  \]
  \item \textbf{DC Input Power ($P_{i(\text{dc})}$):}
  \[
  P_{i(\text{dc})} = V_{CC} I_{\text{dc}} = 30\text{ V} \times 0.7958\text{ A} = \frac{75}{\pi} \approx \mathbf{23.873\text{ W}}
  \]
  \item \textbf{Circuit Conversion Efficiency ($\eta$):}
  \[
  \mathbf{\eta = \frac{P_{o(\text{ac})}}{P_{i(\text{dc})}} \times 100\% = \frac{12.5\text{ W}}{23.873\text{ W}} \times 100\% = \frac{\pi}{4} \left(\frac{V_p}{V_{CC}}\right) \times 100\% = \frac{\pi}{4} \left(\frac{20\text{ V}}{30\text{ V}}\right) \times 100\% = \mathbf{52.36\%}}
  \]
  \item \textbf{Total Transistor Power Dissipation ($P_{d(\text{total})}$):}
  \[
  P_{d(\text{total})} = P_{i(\text{dc})} - P_{o(\text{ac})} = 23.873\text{ W} - 12.5\text{ W} = \mathbf{11.373\text{ W}} \quad (5.687\text{ W per transistor})
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{P_{o(\text{ac})} = 12.50\text{ W}, \qquad P_{i(\text{dc})} = 23.87\text{ W}, \qquad \eta = 52.36\%}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: Transformer-Coupled Class A Power Amplifier [7 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q8)}
Draw the circuit diagram and the characteristic curve of a transformer-coupled class A amplifier and derive its general and maximum efficiency.
\end{questionbox}

\paragraph{1. Circuit Operation:}
A step-down output transformer matches the high collector output impedance to a low-impedance loudspeaker ($R_L$). The reflected AC load resistance seen by the primary is $R_L' = \left(\frac{N_1}{N_2}\right)^2 R_L$.

\begin{schematicbox}{Transformer-Coupled Class A Amplifier Circuit \& Dynamic AC/DC Load Line Curves}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Circuit (Left)
  \draw[thick] (0, 4.8) -- (3.6, 4.8);
  \node[above] at (1.5, 4.8) {\large $\mathbf{V_{CC}}$};
  \draw[thick] (0, 0) -- (3.6, 0) node[below left] {\textbf{GND}};

  % Transformer Primary
  \draw[thick] (2.5, 4.8) -- (2.5, 4.2);
  \draw[thick] (2.5, 4.2) to[out=-30, in=30] (2.5, 3.5) to[out=-30, in=30] (2.5, 2.8) to[out=-30, in=30] (2.5, 2.1);
  \draw[thick] (2.5, 2.1) -- (2.5, 1.8);

  % Core
  \draw[thick] (2.7, 4.2) -- (2.7, 2.1);
  \draw[thick] (2.8, 4.2) -- (2.8, 2.1);

  % Secondary
  \draw[thick] (3.0, 4.2) to[out=150, in=-150] (3.0, 3.5) to[out=150, in=-150] (3.0, 2.8) to[out=150, in=-150] (3.0, 2.1);
  \draw[thick] (3.0, 4.2) -- (3.8, 4.2) -- (3.8, 3.5);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.4, 2.8) rectangle (4.2, 3.5) node[midway] {\small $R_L$};
  \draw[thick] (3.8, 2.8) -- (3.8, 2.1) -- (3.0, 2.1);

  % Transistor Q1 (NPN)
  \draw[draw=black!80, fill=white, thick] (2.5, 1.3) circle (0.45cm);
  \draw[line width=1.4pt] (2.35, 1.05) -- (2.35, 1.55);
  \draw[thick] (1.0, 1.3) node[left] {$v_{\text{in}}$} -- (2.35, 1.3);
  \draw[thick] (2.5, 1.8) -- (2.65, 1.55);
  \draw[thick, ->, >=latex] (2.45, 1.15) -- (2.65, 0.95);
  \draw[thick] (2.65, 0.95) -- (2.65, 0);
  \node[above right=0.05cm] at (2.85, 1.3) {\small $\mathbf{Q_1}$};

  % Characteristic AC/DC Load Line (Right)
  \draw[thick, ->, >=latex] (6.0, 0) -- (11.8, 0) node[right] {$V_{CE}\ (\text{V})$};
  \draw[thick, ->, >=latex] (6.0, 0) -- (6.0, 4.5) node[above] {$I_C\ (\text{mA})$};

  % DC Load line (Vertical line at VCC because R_dc approx 0)
  \draw[line width=1.2pt, blue] (8.5, 0) -- (8.5, 4.0) node[above] {\small\textbf{DC Load Line}};

  % AC Load line (Slope = -1/RL')
  \draw[line width=1.3pt, red] (6.2, 3.6) -- (11.0, 0) node[below] {$2V_{CC}$};
  \node[above=0.1cm, red] at (7.2, 3.2) {\small\textbf{AC Load Line}};

  % Q point
  \draw[fill=black] (8.5, 1.8) circle (2pt) node[right=0.1cm] {\small $\mathbf{Q\ (V_{CC}, I_{CQ})}$};
  \draw[dashed, gray] (8.5, 1.8) -- (6.0, 1.8) node[left] {$I_{CQ}$};
  \draw[dashed, gray] (6.2, 3.6) -- (6.0, 3.6) node[left] {$2I_{CQ}$};
  \draw[dashed, gray] (8.5, 1.8) -- (8.5, 0) node[below] {$V_{CC}$};
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. Efficiency Derivation:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{DC Input Power:} At quiescent bias $V_{CEQ} = V_{CC}$ (since primary DC winding resistance is $\approx 0\ \Omega$):
  \[
  P_{i(\text{dc})} = V_{CC} I_{CQ}
  \]
  \item \textbf{AC Output Power:}
  \[
  P_{o(\text{ac})} = \frac{V_p I_p}{2} = \frac{(V_{\max} - V_{\min})(I_{\max} - I_{\min})}{8}
  \]
  \item \textbf{General Efficiency ($\eta$):}
  \[
  \mathbf{\eta = \frac{P_{o(\text{ac})}}{P_{i(\text{dc})}} = \frac{\frac{V_p I_p}{2}}{V_{CC} I_{CQ}} = \frac{1}{2} \left(\frac{V_p}{V_{CC}}\right) \left(\frac{I_p}{I_{CQ}}\right) \times 100\%}
  \]
  \item \textbf{Maximum Efficiency ($\eta_{\max}$):} For maximum symmetrical undistorted output swing, $V_p = V_{CC}$ (voltage swings between $0\text{ V}$ and $2V_{CC}$) and $I_p = I_{CQ}$:
  \[
  \mathbf{\eta_{\max} = \frac{1}{2} (1)(1) \times 100\% = 50.0\%}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{\eta = \frac{1}{2} \left(\frac{V_p}{V_{CC}}\right) \left(\frac{I_p}{I_{CQ}}\right) \times 100\%, \qquad \eta_{\max} = 50.0\%}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: Stability Factor of Discrete Series Voltage Regulator [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q9)}
Derive the expression for stability factor of a discrete-transistor series regulator.
\end{questionbox}

\paragraph{1. Circuit Model \& Voltage Stability Factor Definition:}
The Voltage Stability Factor ($S_V$) defines the line regulation capability of the series voltage regulator:
\[
S_V = \left.\frac{\Delta V_o}{\Delta V_{\text{in}}}\right|_{R_L = \text{constant}}
\]

\begin{schematicbox}{Discrete Transistor Series Voltage Regulator Small-Signal Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 4.2) node[left] {$V_{\text{in}}$} -- (1.5, 4.2);
  \draw[thick] (0, 0) -- (7.5, 0) node[right] {GND};

  % Pass Transistor Q1 (NPN)
  \draw[draw=black!80, fill=white, thick] (2.2, 4.2) circle (0.55cm);
  \draw[line width=1.6pt] (2.2, 3.85) -- (2.2, 4.55); % Base
  \draw[thick] (1.5, 4.2) -- (1.85, 4.4); % Collector
  \draw[thick, ->, >=latex] (2.2, 4.0) -- (2.55, 4.2); % Emitter
  \draw[thick] (2.55, 4.2) -- (7.0, 4.2) node[right] {\large $V_o = V_Z - V_{BE}$};
  \node[above=0.2cm] at (2.2, 4.75) {\small $\mathbf{Q_1}$ (Pass Transistor)};

  % Base bias branch
  \draw[thick] (1.2, 4.2) -- (1.2, 3.2);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.8, 2.2) rectangle (1.6, 3.2) node[midway] {\small $R$};
  \draw[thick] (1.2, 2.2) -- (1.2, 1.5) node[circle, fill, inner sep=1.8pt] (nb) {};
  \draw[thick] (nb) -- (2.2, 1.5) -- (2.2, 3.85); % Base connection

  % Zener Diode
  \draw[thick] (nb) -- (1.2, 1.1);
  \draw[thick, fill=black] (0.9, 1.1) -- (1.5, 1.1) -- (1.2, 0.5) -- cycle;
  \draw[line width=1.2pt] (0.9, 0.5) -- (1.5, 0.5);
  \draw[line width=1.2pt] (0.9, 0.5) -- (0.9, 0.35);
  \draw[line width=1.2pt] (1.5, 0.5) -- (1.5, 0.65);
  \node[left=0.1cm] at (0.9, 0.8) {\small $V_Z, r_z$};
  \draw[thick] (1.2, 0.5) -- (1.2, 0);

  % Load Resistor
  \draw[thick] (6.0, 4.2) -- (6.0, 2.8);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.6, 1.4) rectangle (6.4, 2.8) node[midway] {\small $R_L$};
  \draw[thick] (6.0, 1.4) -- (6.0, 0);
\end{tikzpicture}
\end{schematicbox}

\paragraph{2. Derivation of Stability Factor $S_V$:}
\begin{enumerate}[leftmargin=1.5em]
  \item The Zener diode has dynamic internal resistance $r_z$. A change in input voltage $\Delta V_{\text{in}}$ produces a change in Zener voltage $\Delta V_Z$ through the voltage divider formed by $R$ and $r_z$:
  \[
  \Delta V_Z = \Delta V_{\text{in}} \left(\frac{r_z}{R + r_z}\right)
  \]
  \item The output voltage follows the base voltage via the emitter-follower pass transistor $Q_1$:
  \[
  V_o = V_Z - V_{BE} \implies \Delta V_o = \Delta V_Z - \Delta V_{BE}
  \]
  \item Since the base-emitter voltage drop $V_{BE} \approx 0.7\text{ V}$ remains virtually constant ($\Delta V_{BE} \approx 0$):
  \[
  \Delta V_o \approx \Delta V_Z = \Delta V_{\text{in}} \left(\frac{r_z}{R + r_z}\right)
  \]
  \item Therefore, the voltage stability factor is:
  \[
  \mathbf{S_V = \frac{\Delta V_o}{\Delta V_{\text{in}}} = \frac{r_z}{R + r_z}}
  \]
\end{enumerate}
For good line regulation, $r_z \ll R$, which ensures $S_V \ll 1$ (typically $S_V \approx 0.01 - 0.05$).

\begin{answerbox}
$$\mathbf{S_V = \frac{\Delta V_o}{\Delta V_{\text{in}}} = \frac{r_z}{R + r_z} \approx \frac{r_z}{R} \ll 1}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: LM317 Variable DC Voltage Regulator Design (3V - 15V) [4 Marks]}
\begin{questionbox}{Problem Statement (2083 Baishakh, Q10)}
Design a variable DC voltage regulator using the LM317 to output (3-15) volts.
\end{questionbox}

The LM317 maintains a precision internal reference voltage of $V_{\text{ref}} = 1.25\text{ V}$ between its Output and Adjust terminals:
\[
V_{\text{out}} = V_{\text{ref}} \left(1 + \frac{R_2}{R_1}\right) + I_{\text{adj}} R_2 \approx 1.25\text{ V} \left(1 + \frac{R_2}{R_1}\right) \quad (\text{since } I_{\text{adj}} \approx 50\ \mu\text{A} \text{ is negligible})
\]

\begin{schematicbox}{LM317 Adjustable Linear Voltage Regulator Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Input
  \draw[thick] (0, 2.5) node[left] {$V_{\text{in}} \ge 18\text{V}$} -- (1.5, 2.5);
  % Cin
  \draw[thick] (0.8, 2.5) -- (0.8, 1.8);
  \draw[line width=1.4pt, line cap=round] (0.5, 1.8) -- (1.1, 1.8);
  \draw[line width=1.4pt, line cap=round] (0.5, 1.6) -- (1.1, 1.6);
  \node[left] at (0.5, 1.7) {\small $0.1\mu\text{F}$};
  \draw[thick] (0.8, 1.6) -- (0.8, 0);

  % LM317 IC Box
  \draw[thick, fill=blue!5, rounded corners=2pt] (1.5, 1.5) rectangle (4.5, 3.5);
  \node at (3.0, 2.85) {\large\textbf{LM317}};
  \node[right] at (1.55, 2.5) {\footnotesize \textbf{IN}};
  \node[left] at (4.45, 2.5) {\footnotesize \textbf{OUT}};
  \node[above] at (3.0, 1.55) {\footnotesize \textbf{ADJ}};

  % Output rail
  \draw[thick] (4.5, 2.5) -- (7.5, 2.5) node[right] {\large $V_o = 3\text{V}-15\text{V}$};

  % R1 Resistor
  \draw[thick] (5.5, 2.5) -- (5.5, 1.8);
  \draw[thick, fill=white, rounded corners=1.5pt] (5.1, 0.9) rectangle (5.9, 1.8) node[midway] {\small $R_1=240\Omega$};
  \draw[thick] (5.5, 0.9) -- (5.5, 0.2) node[circle, fill, inner sep=1.8pt] (n_adj) {};
  \draw[thick] (n_adj) -- (3.0, 0.2) -- (3.0, 1.5);

  % R2 Potentiometer
  \draw[thick] (n_adj) -- (5.5, -0.4);
  \draw[thick, fill=white, rounded corners=1.5pt] (5.1, -1.3) rectangle (5.9, -0.4) node[midway] {\small $R_2$};
  \draw[thick, ->, >=latex] (4.6, -1.1) -- (5.4, -0.6); % Arrow for pot
  \draw[thick] (5.5, -1.3) -- (5.5, -1.8);

  % Cout
  \draw[thick] (6.8, 2.5) -- (6.8, 1.8);
  \draw[line width=1.4pt, line cap=round] (6.5, 1.8) -- (7.1, 1.8);
  \draw[line width=1.4pt, line cap=round] (6.5, 1.6) -- (7.1, 1.6);
  \node[right] at (7.1, 1.7) {\small $1\mu\text{F}$};
  \draw[thick] (6.8, 1.6) -- (6.8, -1.8);

  % Ground rail
  \draw[thick] (0, -1.8) -- (7.5, -1.8) node[right] {GND};
  \draw[thick] (0.8, 0) -- (0.8, -1.8);
\end{tikzpicture}
\end{schematicbox}

\paragraph{Component Value Calculations:}
\begin{enumerate}[leftmargin=1.5em]
  \item Standard program resistor selection: $R_1 = \mathbf{240\ \Omega}$ (satisfies $I_L \ge 5\text{ mA}$ minimum load requirement).
  \item For minimum output $V_{\text{out}(\min)} = 3.0\text{ V}$:
  \[
  3.0 = 1.25 \left(1 + \frac{R_{2(\min)}}{240}\right) \implies 1 + \frac{R_{2(\min)}}{240} = 2.4 \implies R_{2(\min)} = 1.4 \times 240 = \mathbf{336\ \Omega}
  \]
  \item For maximum output $V_{\text{out}(\max)} = 15.0\text{ V}$:
  \[
  15.0 = 1.25 \left(1 + \frac{R_{2(\max)}}{240}\right) \implies 1 + \frac{R_{2(\max)}}{240} = 12.0 \implies R_{2(\max)} = 11 \times 240 = \mathbf{2640\ \Omega} = \mathbf{2.64\text{ k}\Omega}
  \]
\end{enumerate}
\textbf{Practical Realization:} Use a fixed resistor $R_{2A} = 330\ \Omega$ in series with a $\mathbf{2.5\text{ k}\Omega}$ linear potentiometer ($R_2 = 330\ \Omega \text{ to } 2.83\text{ k}\Omega$). Input DC voltage requirement: $V_{\text{in}} \ge V_{\text{out}(\max)} + 3\text{ V} = 18\text{ V DC}$.

\begin{answerbox}
$$\mathbf{R_1 = 240\ \Omega, \qquad R_2 = 336\ \Omega \text{ to } 2.64\text{ k}\Omega \quad (\text{Fixed } 330\ \Omega + 2.5\text{ k}\Omega \text{ Potentiometer}), \qquad V_{\text{in}} \ge 18\text{ V}}$$
\end{answerbox}
"""
