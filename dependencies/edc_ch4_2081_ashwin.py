# edc_ch4_2081_ashwin.py
# Chapter 4: 2081 Ashwin Examination Master Solutions (Refined Diagrams)

def get_chapter_2081_ashwin():
    return r"""
\chapter{2081 Ashwin Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BEI, BCT & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Electronic Devices \& Circuits (EX 151) & \textbf{Examination Type:} Regular (New Course - 2080 Batch) \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: Stiff $\beta$-Independent CE Amplifier Design [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q1)}
Design $\beta$-independent type DC biased common emitter amplifier. Given parameters: $V_{CC} = 20\text{V}, I_C = 1.5\text{mA}$ and $\beta = 110$. Use stiff biasing method.
\end{questionbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Emitter Voltage Allocation ($V_E$):}
  Set $V_E = 0.10 \times V_{CC} = 0.10 \times 20\text{V} = \mathbf{2.0\text{V}}$.
  \[
  R_E = \frac{V_E}{I_E} \approx \frac{2.0\text{V}}{1.5\text{mA}} = 1.33\text{ k}\Omega \quad (\text{Select standard } R_E = \mathbf{1.3\text{ k}\Omega}\text{ or } \mathbf{1.5\text{ k}\Omega})
  \]
  \item \textbf{Collector Resistor Allocation ($R_C$):}
  Set $V_{CEQ} = \frac{V_{CC} - V_E}{2} = \frac{20 - 2.0}{2} = 9.0\text{V}$:
  \[
  R_C = \frac{V_{CC} - (V_E + V_{CEQ})}{I_C} = \frac{20 - 11.0}{1.5\text{mA}} = \frac{9.0\text{V}}{1.5\text{mA}} = \mathbf{6.0\text{ k}\Omega} \quad (\text{Select standard } R_C = \mathbf{6.2\text{ k}\Omega})
  \]
  \item \textbf{Base Voltage Calculation ($V_B$):}
  \[
  V_B = V_E + V_{BE} = 2.0\text{V} + 0.7\text{V} = \mathbf{2.7\text{ V}}
  \]
  \item \textbf{Stiff Biasing Bleeder Current Rule ($I_{\text{bleed}} \ge 10 I_B$):}
  \[
  I_B = \frac{1.5\text{mA}}{110} = 13.64\ \mu\text{A} \implies I_{\text{bleed}} = 10 \times 13.64\ \mu\text{A} = 136.4\ \mu\text{A} = 0.1364\text{mA}
  \]
  \[
  R_2 = \frac{V_B}{I_{\text{bleed}}} = \frac{2.7\text{V}}{0.1364\text{mA}} = 19.79\text{ k}\Omega \quad (\text{Select standard } R_2 = \mathbf{20\text{ k}\Omega}\text{ or } \mathbf{18\text{ k}\Omega})
  \]
  \[
  R_1 = \frac{V_{CC} - V_B}{I_{\text{bleed}} + I_B} = \frac{20\text{V} - 2.7\text{V}}{0.15\text{mA}} = \frac{17.3\text{V}}{0.15\text{mA}} = 115.33\text{ k}\Omega \quad (\text{Select standard } R_1 = \mathbf{120\text{ k}\Omega})
  \]
\end{enumerate}

\begin{schematicbox}{Designed Stiff CE Amplifier Circuit ($V_{CC} = 20\text{V}$)}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.5, 5.2) node[right] {\large $\mathbf{V_{CC} = +20\text{V}}$};
  \draw[thick] (0, -0.8) -- (7.5, -0.8) node[right] {\textbf{GND}};

  % Divider R1 and R2
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 3.4) rectangle (2.2, 4.3) node[midway] {\small $R_1=120\text{k}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (vb) {};
  \draw[thick] (1.8, 2.5) -- (1.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 0.7) rectangle (2.2, 1.6) node[midway] {\small $R_2=20\text{k}$};
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
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 3.4) rectangle (4.65, 4.3) node[midway] {\small $R_C=6.2\text{k}$};
  \draw[thick] (4.25, 4.3) -- (4.25, 5.2);

  % Emitter Resistor RE and Bypass CE
  \draw[thick] (ve) -- (4.25, 1.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 0.4) rectangle (4.65, 1.3) node[midway] {\small $R_E=1.3\text{k}$};
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
$$\mathbf{R_1 = 120\text{ k}\Omega, \quad R_2 = 20\text{ k}\Omega, \quad R_C = 6.2\text{ k}\Omega, \quad R_E = 1.3\text{ k}\Omega}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: Common Collector (Emitter Follower) Small Signal Analysis [1 + 4 = 5 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q2)}
Why is a common collector BJT amplifier also known as an emitter follower? Draw the small signal model of common collector amplifier circuit and derive expressions for input resistance, voltage gain, and current gain.
\end{questionbox}

\paragraph{Part (a): Why Termed "Emitter Follower" [1 Mark]}
In a Common Collector configuration, the output voltage is extracted at the emitter terminal. Since $v_o = v_e = v_{\text{in}} - v_{be} \approx v_{\text{in}}$ and the voltage gain is nearly unity ($A_v \approx 0.99 \approx 1$) with zero phase shift ($0^\circ$), the emitter AC output potential \textbf{closely tracks and follows the input signal}, hence the name \textbf{Emitter Follower}.

\paragraph{Part (b): Parameter Derivations [4 Marks]}
\begin{schematicbox}{Small-Signal Model of Common Collector (Emitter Follower)}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Input
  \draw[thick] (0, 2.0) node[left] {$v_{\text{in}}$} -- (1.5, 2.0);
  % RB
  \draw[thick] (1.0, 2.0) -- (1.0, 1.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.6, 0.5) rectangle (1.4, 1.4) node[midway] {\small $R_B$};
  \draw[thick] (1.0, 0.5) -- (1.0, 0);

  % Base to Emitter branch: beta*re and (1+beta)*(RE || RL)
  \draw[thick] (1.5, 2.0) -- (3.0, 2.0);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.0, 1.7) rectangle (4.2, 2.3) node[midway] {\small $\beta r_e$};
  \draw[thick] (4.2, 2.0) -- (5.2, 2.0) node[circle, fill, inner sep=1.8pt] (ve) {};

  % RE || RL
  \draw[thick] (ve) -- (5.2, 1.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (4.7, 0.5) rectangle (5.7, 1.4) node[midway] {\small $R_E \parallel R_L$};
  \draw[thick] (5.2, 0.5) -- (5.2, 0);

  % Ground Rail
  \draw[thick] (0, 0) -- (6.5, 0) node[right] {\textbf{Collector (GND)}};

  % Output node
  \draw[thick] (ve) -- (6.5, 2.0) node[right] {\large $v_o$};
\end{tikzpicture}
\end{schematicbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Input Resistance ($R_{\text{in}}$):}
  Looking into the base terminal:
  \[
  Z_b = \beta r_e + (1+\beta)(R_E \parallel R_L) \approx \mathbf{\beta (r_e + R_E \parallel R_L)} \quad (\text{very high, } > 100\text{ k}\Omega)
  \]
  Total amplifier input resistance: $R_{\text{in}} = R_1 \parallel R_2 \parallel Z_b$.
  \item \textbf{Voltage Gain ($A_v$):}
  \[
  v_o = i_e (R_E \parallel R_L), \qquad v_{\text{in}} = i_e [r_e + (R_E \parallel R_L)]
  \]
  \[
  \mathbf{A_v = \frac{v_o}{v_{\text{in}}} = \frac{R_E \parallel R_L}{r_e + R_E \parallel R_L} \approx 1 \quad (\text{Non-inverting, } 0^\circ \text{ phase shift})}
  \]
  \item \textbf{Current Gain ($A_i$):}
  \[
  \mathbf{A_i = \frac{i_o}{i_{\text{in}}} = (1+\beta) \left(\frac{R_B}{R_B + Z_b}\right) \left(\frac{R_E}{R_E + R_L}\right) \approx \beta} \quad (\text{very high})
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{R_{\text{in}} \approx R_B \parallel \beta R_E, \qquad A_v = \frac{R_E \parallel R_L}{r_e + R_E \parallel R_L} \approx 1, \qquad A_i \approx \beta}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: Derivation of BJT Transconductance $g_m$ [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q3)}
Derive trans-conductance of BJT.
\end{questionbox}

The transconductance $g_m$ quantifies the small-signal sensitivity of the collector output current with respect to changes in the base-emitter input voltage:
\[
g_m = \left. \frac{\partial i_C}{\partial v_{BE}} \right|_{Q-\text{point}}
\]
\paragraph{Derivation from Shockley Diode Conduction Equation:}
The collector current of a BJT operating in the active region is given by:
\[
i_C = I_S e^{v_{BE} / V_T}
\]
where $I_S$ is the reverse saturation current and $V_T = \frac{kT}{q} \approx 26\text{ mV}$ is the thermal voltage at room temperature ($300\text{ K}$).\\
Differentiating with respect to $v_{BE}$:
\[
\frac{d i_C}{d v_{BE}} = I_S \cdot \frac{d}{d v_{BE}}\left(e^{v_{BE}/V_T}\right) = I_S \cdot \left(\frac{1}{V_T} e^{v_{BE}/V_T}\right) = \frac{I_S e^{v_{BE}/V_T}}{V_T}
\]
Recognizing that $I_S e^{V_{BEQ}/V_T} = I_C$ (quiescent collector current):
\[
\mathbf{g_m = \frac{I_C}{V_T} = \frac{1}{r_e}} \quad \blacksquare
\]

\begin{answerbox}
$$\mathbf{g_m = \frac{I_C}{V_T} \approx \frac{I_C}{26\text{ mV}}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: N-Channel Enhancement-Type MOSFET [7 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q4)}
Describe the construction and working principle of n channel enhancement-type MOSFET with the help of necessary diagrams and its drain characteristic curve.
\end{questionbox}

\paragraph{1. Physical Construction:}
An N-Channel Enhancement MOSFET (E-MOSFET) is fabricated on a p-type substrate without any pre-existing channel:
\begin{itemize}[leftmargin=1.5em]
  \item Two heavily doped $n^+$ regions form the Source and Drain.
  \item A thin dielectric insulating layer of $\text{SiO}_2$ separates the metal/polysilicon Gate electrode from the substrate.
  \item With $V_{GS} = 0\text{V}$, two back-to-back $p$-$n$ junctions block all current flow between drain and source ($I_D = 0$).
\end{itemize}

\paragraph{2. Working Principle and Inversion Layer Formation:}
\begin{itemize}[leftmargin=1.5em]
  \item When a positive gate voltage is applied ($V_{GS} > 0$), the electric field repels holes away from the surface and attracts minority electrons.
  \item When $V_{GS} \ge V_T$ (\textbf{Threshold Voltage}, typically $+1\text{V}$ to $+3\text{V}$), an \textbf{inversion layer of electrons} forms beneath the gate oxide, creating an induced n-channel bridging source and drain.
\end{itemize}

\begin{schematicbox}{Drain Characteristic Curves of N-Channel E-MOSFET}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  \draw[thick, ->, >=latex] (0, 0) -- (7.0, 0) node[right] {$V_{DS}\ (\text{V})$};
  \draw[thick, ->, >=latex] (0, 0) -- (0, 4.0) node[above] {$I_D\ (\text{mA})$};

  \draw[line width=1.2pt, teal] (0, 0) to[out=60, in=180] (2.5, 3.4) -- (6.5, 3.4) node[right] {\small $V_{GS} = 4\text{V}$};
  \draw[line width=1.2pt, teal] (0, 0) to[out=55, in=180] (2.0, 2.3) -- (6.5, 2.3) node[right] {\small $V_{GS} = 3\text{V}$};
  \draw[line width=1.2pt, teal] (0, 0) to[out=50, in=180] (1.5, 1.2) -- (6.5, 1.2) node[right] {\small $V_{GS} = 2\text{V}$};
  \draw[thick, red, dashed] (0, 0.05) -- (6.5, 0.05) node[right] {\small $V_{GS} \le V_T\ (I_D=0)$};
  \draw[thick, dashed, purple] (0, 0) to[out=45, in=-135] (2.5, 3.4) node[above=0.1cm] {\small\textbf{Pinch-off Locus}};
\end{tikzpicture}
\end{schematicbox}

\paragraph{3. Drain Current Conduction Equations:}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Ohmic / Triode Region ($V_{DS} < V_{GS} - V_T$):}
  \[
  I_D = K \left[2(V_{GS} - V_T)V_{DS} - V_{DS}^2\right]
  \]
  \item \textbf{Saturation Region ($V_{DS} \ge V_{GS} - V_T$):}
  \[
  \mathbf{I_D = K (V_{GS} - V_T)^2 = \frac{1}{2}\mu_n C_{ox} \left(\frac{W}{L}\right)(V_{GS} - V_T)^2}
  \]
\end{itemize}

\begin{answerbox}
$$\mathbf{I_D = K(V_{GS} - V_T)^2 \quad \text{for } V_{GS} \ge V_T \text{ and } V_{DS} \ge V_{GS} - V_T}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: JFET Q-Point and Pinch-Off Region Verification [6 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q5)}
Find $I_D$ and $V_{DS}$ for the following circuit. Given data are $V_P = -5.5\text{V}, I_{DSS} = 10\text{mA}$. Assume all capacitors are ideal and check whether the transistor is operating in the pinch-off region or not.
Circuit parameters: $V_{DD} = 20\text{V}, R_1 = 1.5\text{ M}\Omega, R_2 = 330\text{ k}\Omega, R_D = 2.0\text{ k}\Omega, R_S = 1.0\text{ k}\Omega$.
\end{questionbox}

\begin{schematicbox}{Given JFET Circuit Schematic}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (6.5, 5.2) node[right] {\large $\mathbf{V_{DD} = +20\text{V}}$};
  \draw[thick] (0, -0.8) -- (6.5, -0.8) node[right] {\textbf{GND}};

  % R1 and R2
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 3.4) rectangle (2.2, 4.3) node[midway] {\small $R_1=1.5\text{M}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (vg) {};
  \draw[thick] (1.8, 2.5) -- (1.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 0.7) rectangle (2.2, 1.6) node[midway] {\small $R_2=330\text{k}$};
  \draw[thick] (1.8, 0.7) -- (1.8, -0.8);

  % JFET
  \draw[thick] (vg) -- (3.35, 2.5);
  \draw[draw=black!80, fill=white, thick] (3.8, 2.5) circle (0.55cm);
  \draw[line width=1.6pt] (3.75, 2.15) -- (3.75, 2.85); % Channel
  \draw[thick, ->, >=latex] (3.35, 2.5) -- (3.75, 2.5); % Gate
  \draw[thick] (3.75, 2.75) -- (4.25, 2.75) -- (4.25, 3.4); % Drain
  \draw[thick] (3.75, 2.25) -- (4.25, 2.25) -- (4.25, 1.6) node[circle, fill, inner sep=1.8pt] (vs) {}; % Source
  \node[right=0.2cm] at (4.4, 2.5) {\large\textbf{N-JFET}};

  % RD
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 3.4) rectangle (4.65, 4.3) node[midway] {\small $R_D=2\text{k}$};
  \draw[thick] (4.25, 4.3) -- (4.25, 5.2);

  % RS
  \draw[thick] (vs) -- (4.25, 1.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 0.4) rectangle (4.65, 1.3) node[midway] {\small $R_S=1\text{k}$};
  \draw[thick] (4.25, 0.4) -- (4.25, -0.8);
\end{tikzpicture}
\end{schematicbox}

\paragraph{1. Gate Voltage Calculation ($V_G$):}
\[
V_G = V_{DD} \left(\frac{R_2}{R_1 + R_2}\right) = 20\text{V} \times \left(\frac{330\text{k}\Omega}{1500\text{k}\Omega + 330\text{k}\Omega}\right) = 20 \times \frac{0.33}{1.83} = \mathbf{3.6066\text{ V}}
\]

\paragraph{2. Equation for $V_{GS}$:}
\[
V_{GS} = V_G - I_D R_S = 3.6066 - 1.0 I_D \quad (\text{with } I_D \text{ in mA})
\]

\paragraph{3. Substitution into Shockley's Equation:}
\[
I_D = 10 \left(1 - \frac{3.6066 - 1.0 I_D}{-5.5}\right)^2 = 10 \left(\frac{5.5 + 3.6066 - I_D}{5.5}\right)^2 = \frac{10}{30.25} (9.1066 - I_D)^2
\]
\[
3.025 I_D = 82.93 - 18.213 I_D + I_D^2 \implies I_D^2 - 21.238 I_D + 82.93 = 0
\]
Solving via quadratic formula:
\[
I_D = \frac{21.238 \pm \sqrt{(21.238)^2 - 4(1)(82.93)}}{2} = \frac{21.238 \pm \sqrt{451.05 - 331.72}}{2} = \frac{21.238 \pm 10.924}{2}
\]
Two mathematical roots:
\begin{itemize}[leftmargin=1.5em]
  \item $I_{D1} = 16.081\text{ mA} \implies V_{GS1} = 3.6066 - 16.081 = -12.47\text{V} < V_P$ (\textbf{Invalid}).
  \item $I_{D2} = \mathbf{5.157\text{ mA}} \implies V_{GS2} = 3.6066 - 5.157 = \mathbf{-1.550\text{ V}}$ (\textbf{Valid}!).
\end{itemize}

\paragraph{4. Calculation of Drain-to-Source Voltage ($V_{DS}$):}
\[
V_{DS} = V_{DD} - I_D(R_D + R_S) = 20\text{V} - 5.157\text{mA} \times (2.0\text{k}\Omega + 1.0\text{k}\Omega) = 20 - 5.157(3.0) = \mathbf{4.529\text{ V}}
\]

\paragraph{5. Verification of Pinch-Off Region:}
The minimum drain-to-source voltage required for pinch-off (saturation) is:
\[
V_{DS(\text{sat})} = V_{GS} - V_P = -1.550\text{V} - (-5.5\text{V}) = \mathbf{3.950\text{ V}}
\]
Since $V_{DS} = 4.529\text{V} \ge V_{DS(\text{sat})} = 3.950\text{V}$, \textbf{the JFET is definitively operating in the pinch-off (saturation) region}.

\begin{answerbox}
$$\mathbf{I_D = 5.157\text{ mA}, \quad V_{GS} = -1.550\text{ V}, \quad V_{DS} = 4.529\text{ V}, \quad V_{DS} > (V_{GS} - V_P) \implies \text{Confirmed in Pinch-off Region!}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: Colpitts Oscillator Schematic \& Frequency Derivation [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q6)}
State Barkhausen criterion for sinusoidal oscillation. Draw the circuit diagram of Colpitts oscillator and write its frequency of oscillation.
\end{questionbox}

A \textbf{Colpitts Oscillator} utilizes a capacitive voltage divider composed of two capacitors ($C_1, C_2$) in parallel with an inductor $L$ in its feedback tank.

\begin{schematicbox}{BJT Colpitts Oscillator Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.5, 5.2) node[right] {$V_{CC}$};
  \draw[thick] (0, 0) -- (7.5, 0) node[right] {GND};

  % BJT Transistor Q1 (NPN)
  \draw[draw=black!80, fill=white, thick] (2.5, 2.5) circle (0.55cm);
  \draw[line width=1.6pt] (2.15, 2.15) -- (2.15, 2.85); % Base
  \draw[thick] (2.15, 2.5) -- (1.5, 2.5); % Base lead
  \draw[thick] (2.3, 2.7) -- (2.75, 3.05) -- (2.75, 3.6); % Collector
  \draw[thick, ->, >=latex] (2.3, 2.3) -- (2.6, 2.05); % Emitter
  \draw[thick] (2.6, 2.05) -- (2.75, 1.95) -- (2.75, 0); % Emitter to GND
  \node[left=0.15cm] at (2.0, 2.5) {\small $\mathbf{Q_1}$};

  % Radio Frequency Choke (RFC)
  \draw[thick] (2.75, 3.6) -- (2.75, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (2.35, 3.6) rectangle (3.15, 4.3) node[midway] {\small RFC};
  \draw[thick] (2.75, 4.3) -- (2.75, 5.2);

  % Output to Tank coupling capacitor
  \draw[thick] (2.75, 3.2) -- (4.2, 3.2);
  \draw[line width=1.4pt, line cap=round] (4.2, 2.8) -- (4.2, 3.6);
  \draw[line width=1.4pt, line cap=round] (4.4, 2.8) -- (4.4, 3.6);
  \node[above] at (4.3, 3.6) {\small $C_c$};
  \draw[thick] (4.4, 3.2) -- (5.5, 3.2) node[circle, fill, inner sep=1.8pt] (tank_top) {};

  % Tank Inductor L
  \draw[thick] (tank_top) -- (6.8, 3.2) -- (6.8, 2.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (6.4, 1.4) rectangle (7.2, 2.6) node[midway] {\small $L$};
  \draw[thick] (6.8, 1.4) -- (6.8, 0.8) -- (5.5, 0.8);

  % Split Capacitors C1 and C2
  \draw[thick] (tank_top) -- (5.5, 2.4);
  \draw[line width=1.4pt, line cap=round] (5.1, 2.4) -- (5.9, 2.4);
  \draw[line width=1.4pt, line cap=round] (5.1, 2.2) -- (5.9, 2.2);
  \node[right] at (5.9, 2.3) {\small $C_1$};
  \draw[thick] (5.5, 2.2) -- (5.5, 1.5) node[circle, fill, inner sep=1.8pt] (tap) {};
  \draw[thick] (tap) -- (4.5, 1.5) -- (4.5, 0); % Grounded center tap

  \draw[thick] (tap) -- (5.5, 1.0);
  \draw[line width=1.4pt, line cap=round] (5.1, 1.0) -- (5.9, 1.0);
  \draw[line width=1.4pt, line cap=round] (5.1, 0.8) -- (5.9, 0.8);
  \node[right] at (5.9, 0.9) {\small $C_2$};
  \draw[thick] (5.5, 0.8) -- (5.5, -0.3) -- (1.0, -0.3) -- (1.0, 1.8);
  \draw[line width=1.4pt, line cap=round] (0.7, 1.8) -- (1.3, 1.8);
  \draw[line width=1.4pt, line cap=round] (0.7, 2.0) -- (1.3, 2.0);
  \node[left] at (0.7, 1.9) {\small $C_b$};
  \draw[thick] (1.0, 2.0) -- (1.0, 2.5) -- (1.5, 2.5); % Feedback to base
\end{tikzpicture}
\end{schematicbox}

\paragraph{Frequency of Oscillation:}
The series combination of $C_1$ and $C_2$ gives the equivalent tank capacitance:
\[
C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2} \implies \mathbf{f_0 = \frac{1}{2\pi \sqrt{L C_{\text{eq}}}} = \frac{1}{2\pi \sqrt{L \left(\frac{C_1 C_2}{C_1 + C_2}\right)}}}
\]

\begin{answerbox}
$$\mathbf{f_0 = \frac{1}{2\pi \sqrt{L C_{\text{eq}}}}, \qquad C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: 555 Timer Astable Multivibrator Frequency Derivation [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q7)}
Derive frequency of oscillation of 555 timer Astable Multivibrator.
\end{questionbox}

\begin{schematicbox}{555 Timer Astable Multivibrator Circuit}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (6.8, 5.2) node[right] {$V_{CC}$};
  \draw[thick] (0, -0.8) -- (6.8, -0.8) node[right] {GND};

  % Resistors RA and RB
  \draw[thick] (1.2, 5.2) -- (1.2, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.8, 3.4) rectangle (1.6, 4.3) node[midway] {\small $R_A$};
  \draw[thick] (1.2, 3.4) -- (1.2, 2.7) node[circle, fill, inner sep=1.8pt] (dis) {};
  \draw[thick] (dis) -- (1.2, 2.0);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (0.8, 1.1) rectangle (1.6, 2.0) node[midway] {\small $R_B$};
  \draw[thick] (1.2, 1.1) -- (1.2, 0.4) node[circle, fill, inner sep=1.8pt] (trig) {};

  % Timing Capacitor C
  \draw[thick] (trig) -- (1.2, 0.0);
  \draw[line width=1.4pt, line cap=round] (0.8, 0.0) -- (1.6, 0.0);
  \draw[line width=1.4pt, line cap=round] (0.8, -0.2) -- (1.6, -0.2);
  \node[left] at (0.8, -0.1) {\small $C$};
  \draw[thick] (1.2, -0.2) -- (1.2, -0.8);

  % 555 IC Box
  \draw[thick, fill=blue!5, rounded corners=2pt] (2.8, 0.4) rectangle (5.4, 4.6);
  \node at (4.1, 2.5) {\large\textbf{555 Timer}};
  \node at (4.1, 4.2) {\small $V_{CC}$ (8,4)};
  \draw[thick] (4.1, 4.6) -- (4.1, 5.2);
  \node at (4.1, 0.8) {\small GND (1)};
  \draw[thick] (4.1, 0.4) -- (4.1, -0.8);

  % Discharge pin 7
  \draw[thick] (dis) -- (2.8, 2.7);
  \node[right] at (2.8, 2.7) {\small 7 (Disch)};

  % Trigger & Threshold pins 2, 6
  \draw[thick] (trig) -- (2.8, 0.4);
  \node[above right] at (2.8, 0.4) {\small 2,6 (Trig/Thresh)};

  % Output Pin 3
  \draw[thick] (5.4, 2.5) -- (6.5, 2.5) node[right] {\large $v_o$};
  \node[left] at (5.4, 2.5) {\small 3 (OUT)};
\end{tikzpicture}
\end{schematicbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Charging Time ($T_{\text{HIGH}}$):}
  \[
  v_C(t) = V_{CC} - \frac{2}{3}V_{CC} e^{-t / (R_A+R_B)C} = \frac{2}{3}V_{CC} \implies T_{\text{HIGH}} = (R_A + R_B) C \ln(2) \approx \mathbf{0.693(R_A + R_B)C}
  \]
  \item \textbf{Discharging Time ($T_{\text{LOW}}$):}
  \[
  v_C(t) = \frac{2}{3}V_{CC} e^{-t / R_B C} = \frac{1}{3}V_{CC} \implies T_{\text{LOW}} = R_B C \ln(2) \approx \mathbf{0.693 R_B C}
  \]
  \item \textbf{Total Period and Frequency:}
  \[
  T = T_{\text{HIGH}} + T_{\text{LOW}} = 0.693(R_A + 2R_B)C \implies \mathbf{f = \frac{1}{T} = \frac{1.44}{(R_A + 2R_B)C}}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{f = \frac{1.44}{(R_A + 2R_B)C}, \qquad T_{\text{HIGH}} = 0.693(R_A+R_B)C, \qquad T_{\text{LOW}} = 0.693 R_B C}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: Widlar Current Source Output Resistance Derivation [5 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q8)}
Draw a Widlar Current Source. Derive an expression for an output resistance of Widlar Current Source.
\end{questionbox}

\begin{schematicbox}{Widlar Current Source Circuit Diagram}
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

Applying small-signal analysis to the output transistor $Q_2$ with emitter resistance $R_E$:
\begin{enumerate}[leftmargin=1.5em]
  \item Looking into the collector of $Q_2$, the effective emitter-to-ground impedance is $R_E' = R_E \parallel r_{\pi 2}$.
  \item Taking the early-effect output resistance $r_{o2} = \frac{V_A}{I_O}$ into account, the small-signal KVL at the collector gives:
  \[
  i_o = \frac{v_o - v_e}{r_{o2}} + g_{m2} v_{be2}
  \]
  where $v_e = i_o (R_E \parallel r_{\pi 2})$ and $v_{be2} = -v_e = -i_o (R_E \parallel r_{\pi 2})$.
  \[
  i_o = \frac{v_o - i_o(R_E \parallel r_{\pi 2})}{r_{o2}} - g_{m2} i_o (R_E \parallel r_{\pi 2})
  \]
  \[
  v_o = i_o \left[ r_{o2} + (R_E \parallel r_{\pi 2}) + g_{m2} r_{o2} (R_E \parallel r_{\pi 2}) \right]
  \]
  \[
  \mathbf{R_{\text{out}} = \frac{v_o}{i_o} = r_{o2} \left[ 1 + g_{m2} (R_E \parallel r_{\pi 2}) \right] + (R_E \parallel r_{\pi 2}) \approx r_{o2} \left( 1 + g_{m2} R_E \right)}
  \]
\end{enumerate}
\textbf{Significance:} The emitter resistor $R_E$ provides negative current feedback that multiplies the intrinsic output resistance $r_{o2}$ by a factor of $(1 + g_{m2} R_E)$, providing an exceptionally stable, high-impedance current source.

\begin{answerbox}
$$\mathbf{R_{\text{out}} \approx r_{o2} \left[ 1 + g_{m2} (R_E \parallel r_{\pi 2}) \right] \approx r_{o2}(1 + g_{m2} R_E)}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: Efficiency Calculation of Transformer-Coupled Class A Amplifier [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q9)}
Calculate the efficiency of a transformer coupled Class A amplifier for a supply of $12\text{V DC}$ and output of $V_p = 12\text{V}$ and $6\text{V}$.
\end{questionbox}

For an ideal transformer-coupled Class A amplifier:
\[
\eta = \frac{1}{2} \left(\frac{V_p}{V_{CC}}\right)^2 \times 100\%
\]
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Case 1: For $V_p = 12.0\text{V}$ (Maximum Linear Swing):}
  \[
  \eta = \frac{1}{2} \left(\frac{12\text{V}}{12\text{V}}\right)^2 \times 100\% = \frac{1}{2} (1.0)^2 \times 100\% = \mathbf{50.0\%}
  \]
  \item \textbf{Case 2: For $V_p = 6.0\text{V}$ (Half Voltage Swing):}
  \[
  \eta = \frac{1}{2} \left(\frac{6\text{V}}{12\text{V}}\right)^2 \times 100\% = \frac{1}{2} (0.5)^2 \times 100\% = \frac{1}{2} (0.25) \times 100\% = \mathbf{12.5\%}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{\text{At } V_p = 12\text{V}: \quad \eta = 50.0\%, \qquad \text{At } V_p = 6\text{V}: \quad \eta = 12.5\%}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: Transformer-Coupled Class B Push-Pull Amplifier Efficiency [5 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q10)}
Draw the circuit diagram and the characteristic curve of a transformer coupled class B push-pull amplifier and derive its general efficiency.
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
  \draw[thick] (2.3, 2.0) -- (2.3, -1.2);

  % Transistors Q1 and Q2 (NPN)
  \draw[thick] (1.7, 3.5) -- (3.2, 3.5);
  \draw[draw=black!80, fill=white, thick] (3.6, 3.5) circle (0.45cm);
  \draw[line width=1.4pt] (3.45, 3.25) -- (3.45, 3.75);
  \draw[thick] (3.2, 3.5) -- (3.45, 3.5);
  \draw[thick, ->, >=latex] (3.55, 3.35) -- (3.75, 3.15); % Emitter
  \draw[thick] (3.75, 3.15) -- (3.75, 2.0);
  \draw[thick] (3.75, 3.85) -- (3.75, 4.5) -- (5.6, 4.5); % Collector
  \node[left=0.15cm] at (3.2, 3.8) {\small $\mathbf{Q_1}$};

  \draw[thick] (1.7, 0.5) -- (3.2, 0.5);
  \draw[draw=black!80, fill=white, thick] (3.6, 0.5) circle (0.45cm);
  \draw[line width=1.4pt] (3.45, 0.25) -- (3.45, 0.75);
  \draw[thick] (3.2, 0.5) -- (3.45, 0.5);
  \draw[thick, ->, >=latex] (3.55, 0.35) -- (3.75, 0.15); % Emitter
  \draw[thick] (3.75, 0.15) -- (3.75, -1.2);
  \draw[thick] (3.75, 0.85) -- (3.75, 1.5) -- (5.6, 1.5); % Collector
  \node[left=0.15cm] at (3.2, 0.8) {\small $\mathbf{Q_2}$};

  % Output Transformer T2 Primary
  \draw[thick] (5.6, 4.5) to[out=-30, in=30] (5.6, 3.0) to[out=-30, in=30] (5.6, 1.5);
  \draw[thick] (5.6, 3.0) -- (6.2, 3.0) -- (6.2, 5.2);

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

\paragraph{Analytical Derivation of General Efficiency:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{AC Output Power ($P_o$):}
  \[
  P_{o(\text{ac})} = \frac{V_p^2}{2 R_L'}
  \]
  \item \textbf{DC Input Power ($P_i$):} The average current drawn from supply $V_{CC}$ across both half cycles is:
  \[
  I_{\text{dc}} = \frac{2}{\pi} I_p = \frac{2}{\pi} \left(\frac{V_p}{R_L'}\right) \implies P_{i(\text{dc})} = V_{CC} I_{\text{dc}} = \frac{2}{\pi} \frac{V_{CC} V_p}{R_L'}
  \]
  \item \textbf{Conversion Efficiency ($\eta$):}
  \[
  \mathbf{\eta = \frac{P_{o(\text{ac})}}{P_{i(\text{dc})}} = \frac{\frac{V_p^2}{2 R_L'}}{\frac{2 V_{CC} V_p}{\pi R_L'}} = \frac{\pi}{4} \left(\frac{V_p}{V_{CC}}\right) \times 100\%}
  \]
  At maximum linear swing ($V_p = V_{CC}$): $\mathbf{\eta_{\max} = \frac{\pi}{4} \approx 78.54\%}$.
\end{enumerate}

\begin{answerbox}
$$\mathbf{\eta = \frac{\pi}{4} \left(\frac{V_p}{V_{CC}}\right) \times 100\%, \qquad \eta_{\max} = 78.54\%}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 11
% =========================================================================
\subsection{Question 11: Class A Tuned Amplifier 3dB Bandwidth [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q11)}
Draw the circuit diagram of class A tuned amplifier with its frequency response. Derive its 3dB bandwidth.
\end{questionbox}

\begin{schematicbox}{Class A Tuned Amplifier Circuit and Resonant Response}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Circuit (Left)
  \draw[thick] (0, 4.8) -- (4.2, 4.8) node[right] {$V_{CC}$};
  \draw[thick] (0, 0) -- (4.2, 0) node[right] {GND};

  % BJT Transistor Q1 (NPN)
  \draw[draw=black!80, fill=white, thick] (2.2, 1.8) circle (0.45cm);
  \draw[line width=1.4pt] (2.05, 1.55) -- (2.05, 2.05); % Base
  \draw[thick] (0.8, 1.8) node[left] {$v_{\text{in}}$} -- (2.05, 1.8);
  \draw[thick] (2.2, 2.25) -- (2.35, 2.05);
  \draw[thick, ->, >=latex] (2.15, 1.65) -- (2.35, 1.45); % Emitter
  \draw[thick] (2.35, 1.45) -- (2.35, 0);

  % Parallel Tuned LC Tank
  \draw[thick] (2.35, 2.05) -- (2.35, 2.8) node[circle, fill, inner sep=1.8pt] (tank_bot) {};
  \draw[thick] (tank_bot) -- (1.5, 2.8) -- (1.5, 3.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.1, 3.4) rectangle (1.9, 4.2) node[midway] {\small $L$};
  \draw[thick] (1.5, 4.2) -- (1.5, 4.8);

  \draw[thick] (tank_bot) -- (3.2, 2.8) -- (3.2, 3.4);
  \draw[line width=1.4pt, line cap=round] (2.8, 3.4) -- (3.6, 3.4);
  \draw[line width=1.4pt, line cap=round] (2.8, 3.6) -- (3.6, 3.6);
  \node[right] at (3.6, 3.5) {\small $C$};
  \draw[thick] (3.2, 3.6) -- (3.2, 4.8);

  % Output node
  \draw[thick] (tank_bot) -- (4.2, 2.8) node[right] {\large $v_o$};

  % Resonant Response Curve (Right)
  \draw[thick, ->, >=latex] (5.5, 0) -- (11.5, 0) node[right] {$f$};
  \draw[thick, ->, >=latex] (5.5, 0) -- (5.5, 4.2) node[above] {$|A_v|$};
  \draw[line width=1.3pt, blue] (6.5, 0.3) to[out=40, in=180] (8.5, 3.6) to[out=0, in=140] (10.5, 0.3);

  \draw[dashed, red] (5.5, 3.6) node[left] {$A_{v(\max)}$} -- (8.5, 3.6);
  \draw[dashed, teal] (5.5, 2.54) node[left] {$\frac{A_{v(\max)}}{\sqrt{2}}$} -- (9.7, 2.54);
  \draw[dashed, gray] (7.3, 2.54) -- (7.3, 0) node[below] {$f_1$};
  \draw[dashed, gray] (8.5, 3.6) -- (8.5, 0) node[below] {$f_0$};
  \draw[dashed, gray] (9.7, 2.54) -- (9.7, 0) node[below] {$f_2$};

  \draw[thick, <->, >=latex] (7.3, 1.2) -- (9.7, 1.2) node[midway, above] {\small $BW = f_2 - f_1$};
\end{tikzpicture}
\end{schematicbox}

\paragraph{Derivation of 3dB Bandwidth:}
The resonant frequency of the parallel LC tank is $f_0 = \frac{1}{2\pi\sqrt{LC}}$. The loaded quality factor $Q$ is defined as $Q = \frac{R_p}{\omega_0 L} = \omega_0 C R_p$.\\
The $3\text{dB}$ bandwidth between lower ($f_1$) and upper ($f_2$) half-power cutoff frequencies is:
\[
\mathbf{BW = f_2 - f_1 = \frac{f_0}{Q} = \frac{1}{2\pi R_p C}}
\]

\begin{answerbox}
$$\mathbf{BW = \frac{f_0}{Q} = \frac{1}{2\pi R_p C}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 12
% =========================================================================
\subsection{Question 12: LM317 Variable DC Regulator Design (10V - 20V) [4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q12)}
Design variable DC voltage regulator using LM 317 to get $(10-20)\text{ volts}$ output.
\end{questionbox}

\[
V_{\text{out}} = 1.25\text{V} \left(1 + \frac{R_2}{R_1}\right)
\]
\begin{enumerate}[leftmargin=1.5em]
  \item Select standard $R_1 = \mathbf{240\ \Omega}$.
  \item For $V_{\text{out}(\min)} = 10.0\text{V}$:
  \[
  10.0 = 1.25 \left(1 + \frac{R_{2(\min)}}{240}\right) \implies R_{2(\min)} = 7.0 \times 240 = \mathbf{1680\ \Omega} = \mathbf{1.68\text{ k}\Omega}
  \]
  \item For $V_{\text{out}(\max)} = 20.0\text{V}$:
  \[
  20.0 = 1.25 \left(1 + \frac{R_{2(\max)}}{240}\right) \implies R_{2(\max)} = 15.0 \times 240 = \mathbf{3600\ \Omega} = \mathbf{3.60\text{ k}\Omega}
  \]
\end{enumerate}
\textbf{Implementation:} Use a fixed resistor $R_{2A} = 1.6\text{ k}\Omega$ in series with a $\mathbf{2.0\text{ k}\Omega}$ linear potentiometer ($R_2 = 1.68\text{ k}\Omega \text{ to } 3.60\text{ k}\Omega$). Input voltage: $V_{\text{in}} \ge 23\text{V DC}$.

\begin{answerbox}
$$\mathbf{R_1 = 240\ \Omega, \qquad R_2 = 1.68\text{ k}\Omega \text{ to } 3.60\text{ k}\Omega \quad (\text{Fixed } 1.6\text{k}\Omega + 2.0\text{k}\Omega \text{ Potentiometer})}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 13
% =========================================================================
\subsection{Question 13: Series Transistor Regulator with Error Amplifier \& Stability Factor [2 + 2 = 4 Marks]}
\begin{questionbox}{Problem Statement (2081 Ashwin, Q13)}
Explain the working principle of a series transistor voltage regulator with improved performance and derive an expression for the voltage stability.
\end{questionbox}

\begin{schematicbox}{Series Voltage Regulator with Op-Amp / BJT Error Amplifier}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 4.5) node[left] {$V_{\text{in}}$} -- (1.5, 4.5);
  \draw[thick] (0, 0) -- (7.8, 0) node[right] {GND};

  % Pass Transistor Q1 (NPN)
  \draw[draw=black!80, fill=white, thick] (2.2, 4.5) circle (0.55cm);
  \draw[line width=1.6pt] (2.2, 4.15) -- (2.2, 4.85); % Base
  \draw[thick] (1.5, 4.5) -- (1.85, 4.7); % Collector
  \draw[thick, ->, >=latex] (2.2, 4.3) -- (2.55, 4.5); % Emitter
  \draw[thick] (2.55, 4.5) -- (7.2, 4.5) node[right] {\large $V_o$};
  \node[above=0.2cm] at (2.2, 5.05) {\small $\mathbf{Q_1}$ (Pass)};

  % Voltage Divider Sampling Network (R1, R2)
  \draw[thick] (6.2, 4.5) -- (6.2, 3.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.8, 2.7) rectangle (6.6, 3.6) node[midway] {\small $R_1$};
  \draw[thick] (6.2, 2.7) -- (6.2, 2.0) node[circle, fill, inner sep=1.8pt] (vsample) {};
  \draw[thick] (vsample) -- (6.2, 1.4);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.8, 0.5) rectangle (6.6, 1.4) node[midway] {\small $R_2$};
  \draw[thick] (6.2, 0.5) -- (6.2, 0);

  % Error Amplifier (Op-Amp)
  \draw[thick, fill=white] (3.5, 1.5) -- (3.5, 3.1) -- (4.8, 2.3) -- cycle;
  \node at (3.8, 2.7) {\large $-$};
  \node at (3.8, 1.9) {\large $+$};

  % Inverting input samples Vo
  \draw[thick] (vsample) -- (4.8, 2.0) -- (4.8, 3.4) -- (3.0, 3.4) -- (3.0, 2.7) -- (3.5, 2.7);
  % Non-inverting input receives VZ
  \draw[thick] (2.0, 1.9) node[left] {$V_Z$} -- (3.5, 1.9);
  % Output controls Pass Transistor Base
  \draw[thick] (4.8, 2.3) -- (5.2, 2.3) -- (5.2, 3.8) -- (2.2, 3.8) -- (2.2, 4.15);
\end{tikzpicture}
\end{schematicbox}

An improved series regulator incorporates an active error amplifier (Op-Amp or BJT $Q_2$) comparing a sampled fraction of the output $\beta_s V_o = \frac{R_2}{R_1+R_2}V_o$ against reference voltage $V_Z$.
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Operation:} If $V_o$ increases due to input or load variations, $V_{\text{sample}}$ increases above $V_Z$, causing the error amplifier output to pull down the base potential of pass transistor $Q_1$, decreasing $V_o$ back to the set level.
  \item \textbf{Voltage Stability Factor ($S_V$):}
  \[
  \mathbf{S_V = \frac{\Delta V_o}{\Delta V_{\text{in}}} = \frac{r_z}{R + r_z} \cdot \frac{1}{1 + A_{\text{error}} \beta_s} \approx \frac{r_z}{R \cdot A_{\text{error}} \beta_s}}
  \]
  The high open-loop gain $A_{\text{error}}$ of the error amplifier suppresses input line fluctuations by several orders of magnitude.
\end{itemize}

\begin{answerbox}
$$\mathbf{S_V = \frac{\Delta V_o}{\Delta V_{\text{in}}} \approx \frac{r_z}{R \cdot A_{\text{error}} \beta_s}}$$
\end{answerbox}
"""
