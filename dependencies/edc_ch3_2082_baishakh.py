# edc_ch3_2082_baishakh.py
# Chapter 3: 2082 Baishakh Examination Master Solutions (Refined Diagrams)

def get_chapter_2082_baishakh():
    return r"""
\chapter{2082 Baishakh Examination Solutions}

\section*{Examination Overview}
\begin{tabular}{@{}ll@{}}
\textbf{Level:} Bachelor in Engineering (BE) & \textbf{Full Marks:} 60 \\
\textbf{Programme:} BEI, BCT & \textbf{Pass Marks:} 24 \\
\textbf{Year / Part:} I / II & \textbf{Time:} 3 Hours \\
\textbf{Subject:} Electronic Devices \& Circuits (EX 151) & \textbf{Examination Type:} Back (New Course) \\
\end{tabular}

\vspace{0.6cm}
\hrule
\vspace{0.6cm}

% =========================================================================
% QUESTION 1
% =========================================================================
\subsection{Question 1: $\beta$-Independent Voltage Divider Bias Design [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q1)}
Design a $\beta$-independent voltage divider bias circuit using the appropriate guidelines for the given parameters: $V_{CC} = 12\text{V}, I_C = 1\text{mA}$, and $\beta = 100$.
\end{questionbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Emitter Voltage Allocation ($V_E$):}
  Set $V_E = 0.10 \times V_{CC} = 0.10 \times 12\text{V} = \mathbf{1.2\text{ V}}$.
  \[
  R_E = \frac{V_E}{I_E} \approx \frac{1.2\text{V}}{1.0\text{mA}} = \mathbf{1.2\text{ k}\Omega}
  \]
  \item \textbf{Collector Resistor Allocation ($R_C$):}
  Set $V_{CEQ} = \frac{V_{CC} - V_E}{2} = \frac{12 - 1.2}{2} = 5.4\text{V}$:
  \[
  R_C = \frac{V_{CC} - (V_E + V_{CEQ})}{I_C} = \frac{12 - 6.6}{1.0\text{mA}} = 5.4\text{ k}\Omega \quad (\text{Select standard } R_C = \mathbf{5.6\text{ k}\Omega})
  \]
  \item \textbf{Base Voltage Calculation ($V_B$):}
  \[
  V_B = V_E + V_{BE} = 1.2\text{V} + 0.7\text{V} = \mathbf{1.9\text{ V}}
  \]
  \item \textbf{Stiff Biasing Voltage Divider Calculation ($I_{\text{bleed}} \ge 10 I_B$):}
  \[
  I_B = \frac{1\text{mA}}{100} = 10\ \mu\text{A} \implies I_{\text{bleed}} = 100\ \mu\text{A} = 0.10\text{mA}
  \]
  \[
  R_2 = \frac{V_B}{I_{\text{bleed}}} = \frac{1.9\text{V}}{0.10\text{mA}} = \mathbf{19\text{ k}\Omega} \quad (\text{Standard } R_2 = \mathbf{18\text{ k}\Omega}\text{ or } \mathbf{20\text{ k}\Omega})
  \]
  \[
  R_1 = \frac{V_{CC} - V_B}{I_{\text{bleed}} + I_B} = \frac{12\text{V} - 1.9\text{V}}{0.11\text{mA}} = \frac{10.1\text{V}}{0.11\text{mA}} = 91.8\text{ k}\Omega \quad (\text{Standard } R_1 = \mathbf{91\text{ k}\Omega})
  \]
\end{enumerate}

\begin{schematicbox}{Designed Common Emitter Amplifier Schematic ($V_{CC} = 12\text{V}$)}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (7.5, 5.2) node[right] {\large $\mathbf{V_{CC} = +12\text{V}}$};
  \draw[thick] (0, -0.8) -- (7.5, -0.8) node[right] {\textbf{GND}};

  % Divider R1 and R2
  \draw[thick] (1.8, 5.2) -- (1.8, 4.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 3.4) rectangle (2.2, 4.3) node[midway] {\small $R_1=91\text{k}$};
  \draw[thick] (1.8, 3.4) -- (1.8, 2.5) node[circle, fill, inner sep=1.8pt] (vb) {};
  \draw[thick] (1.8, 2.5) -- (1.8, 1.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (1.4, 0.7) rectangle (2.2, 1.6) node[midway] {\small $R_2=18\text{k}$};
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
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 3.4) rectangle (4.65, 4.3) node[midway] {\small $R_C=5.6\text{k}$};
  \draw[thick] (4.25, 4.3) -- (4.25, 5.2);

  % Emitter Resistor RE and Bypass CE
  \draw[thick] (ve) -- (4.25, 1.3);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (3.85, 0.4) rectangle (4.65, 1.3) node[midway] {\small $R_E=1.2\text{k}$};
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
$$\mathbf{R_1 = 91\text{ k}\Omega, \quad R_2 = 18\text{ k}\Omega, \quad R_C = 5.6\text{ k}\Omega, \quad R_E = 1.2\text{ k}\Omega}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 2
% =========================================================================
\subsection{Question 2: CE BJT Amplifier Small Signal Parameter Calculations [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q2)}
Determine input resistance, voltage gain and output resistance of given common emitter BJT Amplifier. $\beta = 120$ and $r_o = 40\text{ k}\Omega$.
Circuit components: $V_{CC} = 20\text{V}, R_1 = 470\text{ k}\Omega, R_2 = 56\text{ k}\Omega, R_C = 2.2\text{ k}\Omega, R_E = 0.56\text{ k}\Omega$ (with bypass capacitor $C_E$).
\end{questionbox}

\paragraph{1. DC Bias Operating Point Analysis:}
\begin{itemize}[leftmargin=1.5em]
  \item Thevenin Base Voltage:
  \[
  V_{\text{th}} = V_{CC} \left(\frac{R_2}{R_1 + R_2}\right) = 20\text{V} \times \left(\frac{56\text{k}\Omega}{470\text{k}\Omega + 56\text{k}\Omega}\right) = 20 \times \frac{56}{526} = \mathbf{2.129\text{ V}}
  \]
  \item Thevenin Resistance:
  \[
  R_{\text{th}} = R_1 \parallel R_2 = \frac{470 \times 56}{526} = \mathbf{50.038\text{ k}\Omega}
  \]
  \item Quiescent Base and Emitter Currents:
  \[
  I_B = \frac{V_{\text{th}} - V_{BE}}{R_{\text{th}} + (1+\beta)R_E} = \frac{2.129\text{V} - 0.7\text{V}}{50.038\text{k}\Omega + (121)(0.56\text{k}\Omega)} = \frac{1.429\text{V}}{50.038\text{k}\Omega + 67.76\text{k}\Omega} = \frac{1.429\text{V}}{117.8\text{k}\Omega} = \mathbf{12.13\ \mu\text{A}}
  \]
  \[
  I_E = (1+\beta)I_B = 121 \times 12.13\ \mu\text{A} = \mathbf{1.468\text{ mA}}
  \]
  \item Dynamic Emitter Resistance:
  \[
  r_e = \frac{V_T}{I_E} = \frac{26\text{ mV}}{1.468\text{ mA}} = \mathbf{17.71\ \Omega}
  \]
\end{itemize}

\paragraph{2. Small-Signal AC Parameters:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Input Resistance ($R_{\text{in}}$):}
  \[
  Z_b = \beta r_e = 120 \times 17.71\ \Omega = \mathbf{2.125\text{ k}\Omega}
  \]
  \[
  R_{\text{in}} = R_1 \parallel R_2 \parallel Z_b = 50.038\text{k}\Omega \parallel 2.125\text{k}\Omega = \frac{50.038 \times 2.125}{52.163} = \mathbf{2.038\text{ k}\Omega}
  \]
  \item \textbf{Output Resistance ($R_{\text{out}}$):}
  \[
  R_{\text{out}} = R_C \parallel r_o = 2.2\text{k}\Omega \parallel 40\text{k}\Omega = \frac{2.2 \times 40}{42.2} = \mathbf{2.085\text{ k}\Omega}
  \]
  \item \textbf{Voltage Gain ($A_v$):}
  \[
  A_v = -\frac{R_C \parallel r_o}{r_e} = -\frac{2085.3\ \Omega}{17.71\ \Omega} = \mathbf{-117.75} \quad (180^\circ \text{ phase inversion})
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{R_{\text{in}} = 2.038\text{ k}\Omega, \qquad R_{\text{out}} = 2.085\text{ k}\Omega, \qquad A_v = -117.75}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 3
% =========================================================================
\subsection{Question 3: BJT Operation as a Switch \& Dynamic Switching Times [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q3)}
Explain the operation principle of a BJT as a switch with the necessary diagrams.
\end{questionbox}

\paragraph{1. Operating States of BJT as a Switch:}
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{OFF State (Cutoff Region):} $V_{\text{in}} \le 0\text{V} \implies I_B = 0 \implies I_C \approx 0$. Transistor behaves as an open contact; $V_{CE} = V_{CC}$.
  \item \textbf{ON State (Saturation Region):} $V_{\text{in}} \gg V_{BE} \implies I_B \ge I_{B(\text{sat})} = \frac{I_{C(\text{sat})}}{\beta_{\min}}$. Transistor behaves as a closed contact; $V_{CE} = V_{CE(\text{sat})} \approx 0.1\text{V} - 0.2\text{V}$.
\end{itemize}

\paragraph{2. Transient Switching Times:}
\begin{schematicbox}{BJT Dynamic Switching Waveforms and Interval Definitions}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Input pulse
  \draw[thick, ->, >=latex] (0, 3.8) -- (10.5, 3.8) node[right] {$t$};
  \draw[thick, ->, >=latex] (0, 3.8) -- (0, 5.5) node[above] {$v_{\text{in}}$};
  \draw[line width=1.2pt, blue] (0, 3.8) -- (1.5, 3.8) -- (1.5, 5.0) -- (5.5, 5.0) -- (5.5, 3.8) -- (10.0, 3.8);
  \node[left] at (0, 5.0) {$V_{in(H)}$};

  % Output Collector Current waveform
  \draw[thick, ->, >=latex] (0, 0) -- (10.5, 0) node[right] {$t$};
  \draw[thick, ->, >=latex] (0, 0) -- (0, 2.8) node[above] {$i_C$};
  \draw[line width=1.3pt, red] (0, 0) -- (1.5, 0) to[out=0, in=180] (2.2, 0.22) to[out=45, in=-120] (3.0, 2.2) -- (5.5, 2.2) to[out=0, in=180] (6.5, 2.2) to[out=-45, in=135] (7.8, 0.22) to[out=0, in=180] (8.5, 0) -- (10.0, 0);

  % 10% and 90% lines
  \draw[dashed, gray] (0, 0.22) node[left] {\scriptsize $10\%$} -- (10.0, 0.22);
  \draw[dashed, gray] (0, 1.98) node[left] {\scriptsize $90\%$} -- (10.0, 1.98);

  % Annotations
  \draw[dashed, gray] (1.5, 3.8) -- (1.5, 0);
  \draw[dashed, gray] (2.2, 2.2) -- (2.2, 0);
  \draw[dashed, gray] (3.0, 2.2) -- (3.0, 0);
  \node[below=0.1cm] at (1.85, 0) {\small $t_d$};
  \node[below=0.1cm] at (2.6, 0) {\small $t_r$};
  \node[above] at (2.25, -0.85) {\small $\mathbf{\longleftarrow t_{\text{on}} \longrightarrow}$};

  \draw[dashed, gray] (5.5, 3.8) -- (5.5, 0);
  \draw[dashed, gray] (6.5, 2.2) -- (6.5, 0);
  \draw[dashed, gray] (7.8, 2.2) -- (7.8, 0);
  \node[below=0.1cm] at (6.0, 0) {\small $t_s$};
  \node[below=0.1cm] at (7.15, 0) {\small $t_f$};
  \node[above] at (6.65, -0.85) {\small $\mathbf{\longleftarrow t_{\text{off}} \longrightarrow}$};
\end{tikzpicture}
\end{schematicbox}

\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Turn-On Time ($t_{\text{on}} = t_d + t_r$):} Delay time $t_d$ (junction capacitance charging) + Rise time $t_r$ ($10\%$ to $90\%$ of $I_C$).
  \item \textbf{Turn-Off Time ($t_{\text{off}} = t_s + t_f$):} Storage time $t_s$ (removal of excess stored base charge) + Fall time $t_f$ ($90\%$ down to $10\%$).
\end{itemize}

\begin{answerbox}
BJT acts as an inverter switch between Cutoff ($V_{CE}=V_{CC}$) and Saturation ($V_{CE}\approx 0.2\text{V}$), with total switching speed governed by $t_{\text{on}} = t_d + t_r$ and $t_{\text{off}} = t_s + t_f$.
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 4
% =========================================================================
\subsection{Question 4: N-Channel Depletion-Type MOSFET [7 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q4)}
Describe the construction and working principle of n-channel depletion type MOSFET with the help of characteristics curve and mathematical expressions.
\end{questionbox}

\paragraph{1. Physical Construction:}
An N-Channel Depletion-Type MOSFET (D-MOSFET) is built on a p-type silicon substrate:
\begin{itemize}[leftmargin=1.5em]
  \item Two heavily doped $n^+$ regions form the \textbf{Source} and \textbf{Drain}.
  \item A physical, chemically doped \textbf{n-type channel} is pre-diffused between source and drain during fabrication.
  \item The \textbf{Gate} terminal is completely insulated from the channel by a dielectric layer of Silicon Dioxide ($\text{SiO}_2$).
\end{itemize}

\paragraph{2. Working Principle:}
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Depletion Mode ($V_{GS} < 0$):} Applying a negative gate voltage repels conduction electrons from the n-channel into the p-substrate, creating a depletion region and reducing drain current $I_D$. At $V_{GS} = V_P$ (Pinch-off voltage), the channel is fully depleted and $I_D = 0$.
  \item \textbf{Enhancement Mode ($V_{GS} > 0$):} Applying a positive gate voltage attracts additional free electrons from the substrate into the channel, enhancing channel conductivity and increasing $I_D$ above $I_{DSS}$.
\end{enumerate}

\begin{schematicbox}{Transfer and Drain Characteristic Curves of N-Channel D-MOSFET}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  % Transfer Characteristics (left)
  \draw[thick, ->, >=latex] (-4.5, 0) -- (2.0, 0) node[right] {$V_{GS}\ (\text{V})$};
  \draw[thick, ->, >=latex] (0, 0) -- (0, 4.2) node[above] {$I_D\ (\text{mA})$};
  \draw[domain=-3.5:1.2, smooth, variable=\x, line width=1.3pt, blue] plot ({\x}, {1.8*(1 + \x/3.5)^2});
  \node[below] at (-3.5, 0) {$V_P$};
  \node[left] at (0, 1.8) {$I_{DSS}$};
  \node[left] at (-1.5, 3.5) {\small\textbf{Depletion Mode}};
  \node[right] at (0.2, 3.5) {\small\textbf{Enhancement Mode}};

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

\paragraph{3. Mathematical Model (Shockley's Equation):}
In the saturation (active) region ($V_{DS} \ge V_{GS} - V_P$):
\[
\mathbf{I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2} \quad \text{valid for both } V_{GS} \le 0 \text{ and } V_{GS} > 0
\]

\begin{answerbox}
$$\mathbf{I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2, \qquad g_m = \frac{2I_{DSS}}{|V_P|}\left(1 - \frac{V_{GS}}{V_P}\right)}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 5
% =========================================================================
\subsection{Question 5: JFET Voltage Divider Bias Q-Point \& Transconductance [6 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q5)}
For the given JFET voltage divider configuration, determine $I_{DQ}, V_{GSQ}, V_{DS}$ and transconductance $g_m$.
Given parameters: $V_{DD} = 20\text{V}, R_1 = 910\text{ k}\Omega, R_2 = 110\text{ k}\Omega, R_D = 2.2\text{ k}\Omega, R_S = 1.1\text{ k}\Omega, I_{DSS} = 10\text{mA}, V_P = -3.5\text{V}$.
\end{questionbox}

\paragraph{1. Gate Voltage Calculation ($V_G$):}
\[
V_G = V_{DD} \left(\frac{R_2}{R_1 + R_2}\right) = 20\text{V} \times \left(\frac{110\text{k}\Omega}{910\text{k}\Omega + 110\text{k}\Omega}\right) = 20 \times \frac{110}{1020} = \mathbf{2.1569\text{ V}}
\]

\paragraph{2. Equation for $V_{GS}$:}
\[
V_{GS} = V_G - I_D R_S = 2.1569 - 1.1 I_D \quad (\text{with } I_D \text{ in mA})
\]

\paragraph{3. Substitution into Shockley's Law:}
\[
I_D = 10 \left(1 - \frac{2.1569 - 1.1 I_D}{-3.5}\right)^2 = 10 \left(\frac{3.5 + 2.1569 - 1.1 I_D}{3.5}\right)^2 = \frac{10}{12.25} (5.6569 - 1.1 I_D)^2
\]
\[
1.225 I_D = 32.0 - 12.445 I_D + 1.21 I_D^2 \implies 1.21 I_D^2 - 13.67 I_D + 32.0 = 0
\]
Solving via quadratic formula:
\[
I_D = \frac{13.67 \pm \sqrt{(13.67)^2 - 4(1.21)(32.0)}}{2(1.21)} = \frac{13.67 \pm \sqrt{186.87 - 154.88}}{2.42} = \frac{13.67 \pm 5.656}{2.42}
\]
Two roots:
\begin{itemize}[leftmargin=1.5em]
  \item $I_{D1} = 7.986\text{ mA} \implies V_{GS1} = 2.1569 - 1.1(7.986) = -6.628\text{V} < V_P$ (\textbf{Invalid}).
  \item $I_{D2} = \mathbf{3.312\text{ mA}} \implies V_{GS2} = 2.1569 - 1.1(3.312) = \mathbf{-1.486\text{ V}}$ (\textbf{Valid}, since $-3.5\text{V} \le V_{GS} \le 0$).
\end{itemize}

\paragraph{4. Calculation of $V_{DS}$ and Transconductance $g_m$:}
\[
V_{DS} = V_{DD} - I_D(R_D + R_S) = 20\text{V} - 3.312\text{mA} \times (2.2\text{k}\Omega + 1.1\text{k}\Omega) = 20 - 3.312(3.3) = \mathbf{9.07\text{ V}}
\]
\[
g_m = \frac{2 I_{DSS}}{|V_P|} \left(1 - \frac{V_{GSQ}}{V_P}\right) = \frac{2 \times 10\text{mA}}{3.5\text{V}} \left(1 - \frac{-1.486\text{V}}{-3.5\text{V}}\right) = 5.714 \times (1 - 0.4246) = \mathbf{3.288\text{ mS}}
\]

\begin{answerbox}
$$\mathbf{I_{DQ} = 3.312\text{ mA}, \qquad V_{GSQ} = -1.486\text{ V}, \qquad V_{DS} = 9.07\text{ V}, \qquad g_m = 3.288\text{ mS}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 6
% =========================================================================
\subsection{Question 6: LC Hartley Oscillator Frequency Derivation [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q6)}
Draw circuit diagram of LC Hartley oscillator. Derive its frequency of oscillation.
\end{questionbox}

A Hartley oscillator employs an inductive voltage divider with two tapped inductors ($L_1, L_2$) having mutual inductance $M$, tuned by capacitor $C$.

\begin{schematicbox}{BJT LC Hartley Oscillator Circuit}
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

  % Tank tuning capacitor C
  \draw[thick] (tank_top) -- (6.8, 3.2) -- (6.8, 2.3);
  \draw[line width=1.4pt, line cap=round] (6.4, 2.3) -- (7.2, 2.3);
  \draw[line width=1.4pt, line cap=round] (6.4, 2.1) -- (7.2, 2.1);
  \node[right] at (7.2, 2.2) {\small $C$};
  \draw[thick] (6.8, 2.1) -- (6.8, 0.8) -- (5.5, 0.8);

  % Tapped Inductors L1 and L2
  \draw[thick] (tank_top) -- (5.5, 2.6);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.1, 2.0) rectangle (5.9, 2.6) node[midway] {\small $L_1$};
  \draw[thick] (5.5, 2.0) -- (5.5, 1.4) node[circle, fill, inner sep=1.8pt] (tap) {};
  \draw[thick] (tap) -- (4.5, 1.4) -- (4.5, 0); % Grounded center tap
  \draw[thick] (tap) -- (5.5, 0.8);
  \draw[thick, fill=blue!5, rounded corners=1.5pt] (5.1, 0.2) rectangle (5.9, 0.8) node[midway] {\small $L_2$};
  \draw[thick] (5.5, 0.2) -- (5.5, -0.3) -- (1.0, -0.3) -- (1.0, 1.8);
  \draw[line width=1.4pt, line cap=round] (0.7, 1.8) -- (1.3, 1.8);
  \draw[line width=1.4pt, line cap=round] (0.7, 2.0) -- (1.3, 2.0);
  \node[left] at (0.7, 1.9) {\small $C_b$};
  \draw[thick] (1.0, 2.0) -- (1.0, 2.5) -- (1.5, 2.5); % Feedback to base
\end{tikzpicture}
\end{schematicbox}

\paragraph{Derivation of Oscillation Frequency:}
The feedback factor is given by $\beta = \frac{X_{L2}}{X_{L1}} = \frac{L_2 + M}{L_1 + M}$.\\
The equivalent tank inductance of the series tapped inductor is:
\[
L_{\text{eq}} = L_1 + L_2 + 2M
\]
The resonant frequency where inductive and capacitive reactances cancel ($X_{L_{\text{eq}}} = X_C$) is:
\[
\omega_0 L_{\text{eq}} = \frac{1}{\omega_0 C} \implies \omega_0^2 = \frac{1}{L_{\text{eq}} C} \implies \mathbf{f_0 = \frac{1}{2\pi \sqrt{(L_1 + L_2 + 2M)C}}}
\]

\begin{answerbox}
$$\mathbf{f_0 = \frac{1}{2\pi \sqrt{(L_1 + L_2 + 2M)C}}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 7
% =========================================================================
\subsection{Question 7: Bandwidth of Class A Tuned Amplifier [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q7)}
Derive the expression of bandwidth of class A tuned amplifier.
\end{questionbox}

A tuned amplifier uses a parallel LC tank circuit as its collector load. At the resonant frequency $f_0 = \frac{1}{2\pi\sqrt{LC}}$, the impedance is purely resistive: $R_p = Q^2 R_s = \frac{L}{C R_s}$.

\begin{schematicbox}{Frequency Response Curve of Tuned Amplifier}
\centering
\begin{tikzpicture}[scale=0.92, transform shape]
  \draw[thick, ->, >=latex] (0, 0) -- (7.0, 0) node[right] {$f$};
  \draw[thick, ->, >=latex] (0, 0) -- (0, 3.8) node[above] {$|A_v|$};
  \draw[line width=1.3pt, blue] (1.0, 0.3) to[out=40, in=180] (3.5, 3.2) to[out=0, in=140] (6.0, 0.3);

  \draw[dashed, red] (0, 3.2) node[left] {$A_{v(\max)}$} -- (3.5, 3.2);
  \draw[dashed, teal] (0, 2.26) node[left] {$\frac{A_{v(\max)}}{\sqrt{2}}$} -- (4.8, 2.26);
  \draw[dashed, gray] (2.2, 2.26) -- (2.2, 0) node[below] {$f_1$};
  \draw[dashed, gray] (3.5, 3.2) -- (3.5, 0) node[below] {$f_0$};
  \draw[dashed, gray] (4.8, 2.26) -- (4.8, 0) node[below] {$f_2$};

  \draw[thick, <->, >=latex] (2.2, 1.2) -- (4.8, 1.2) node[midway, above] {\small $BW = f_2 - f_1$};
\end{tikzpicture}
\end{schematicbox}

\begin{itemize}[leftmargin=1.5em]
  \item The $3\text{dB}$ half-power frequencies ($f_1$ and $f_2$) occur where the tank impedance falls to $\frac{R_p}{\sqrt{2}}$.
  \item The Quality Factor ($Q$) of the resonant circuit is defined as:
  \[
  Q = \frac{\omega_0 L}{R} = \frac{f_0}{BW} \implies \mathbf{BW = f_2 - f_1 = \frac{f_0}{Q} = \frac{1}{2\pi R_p C}}
  \]
\end{itemize}

\begin{answerbox}
$$\mathbf{BW = \frac{f_0}{Q}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 8
% =========================================================================
\subsection{Question 8: Differential Amplifier with Active vs. Passive Load [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q8)}
Show that the voltage gain of the differential amplifier with active load is twice that with passive load.
\end{questionbox}

\begin{schematicbox}{Differential Amplifier with Active Current Mirror Load}
\centering
\begin{tikzpicture}[scale=0.95, transform shape]
  % Rails
  \draw[thick] (0, 5.2) -- (6.8, 5.2) node[right] {$V_{CC}$};
  \draw[thick] (0, -0.8) -- (6.8, -0.8) node[right] {$-V_{EE}$};

  % Active PMOS/PNP Current Mirror Load (Q3, Q4)
  \draw[draw=black!80, fill=white, thick] (1.8, 4.2) circle (0.45cm);
  \draw[line width=1.4pt] (1.95, 3.95) -- (1.95, 4.45); % Base
  \draw[thick, <-, >=latex] (1.75, 4.35) -- (1.55, 4.55); % Emitter in
  \draw[thick] (1.55, 4.55) -- (1.55, 5.2);
  \draw[thick] (1.75, 4.05) -- (1.55, 3.85) -- (1.55, 3.4) node[circle, fill, inner sep=1.8pt] (n_c3) {};
  \node[left=0.15cm] at (1.4, 4.2) {\small $\mathbf{Q_3}$};

  \draw[draw=black!80, fill=white, thick] (4.8, 4.2) circle (0.45cm);
  \draw[line width=1.4pt] (4.65, 3.95) -- (4.65, 4.45); % Base
  \draw[thick, <-, >=latex] (4.85, 4.35) -- (5.05, 4.55); % Emitter in
  \draw[thick] (5.05, 4.55) -- (5.05, 5.2);
  \draw[thick] (4.85, 4.05) -- (5.05, 3.85) -- (5.05, 3.4) node[circle, fill, inner sep=1.8pt] (n_out) {};
  \node[right=0.15cm] at (5.2, 4.2) {\small $\mathbf{Q_4}$};

  % Diode connection for Q3 and mirror bus
  \draw[thick] (1.95, 4.2) -- (2.6, 4.2) -- (2.6, 3.4) -- (n_c3);
  \draw[thick] (2.6, 4.2) -- (4.65, 4.2);

  % Differential Input Pair (Q1, Q2)
  \draw[draw=black!80, fill=white, thick] (1.8, 2.0) circle (0.45cm);
  \draw[line width=1.4pt] (1.65, 1.75) -- (1.65, 2.25); % Base
  \draw[thick] (0.5, 2.0) node[left] {$+v_d/2$} -- (1.65, 2.0);
  \draw[thick] (1.75, 2.15) -- (1.55, 2.35) -- (n_c3);
  \draw[thick, ->, >=latex] (1.75, 1.85) -- (1.55, 1.65); % Emitter
  \draw[thick] (1.55, 1.65) -- (1.55, 1.1) node[circle, fill, inner sep=1.8pt] (n_tail) {};
  \node[left=0.15cm] at (1.4, 2.0) {\small $\mathbf{Q_1}$};

  \draw[draw=black!80, fill=white, thick] (4.8, 2.0) circle (0.45cm);
  \draw[line width=1.4pt] (4.95, 1.75) -- (4.95, 2.25); % Base
  \draw[thick] (6.1, 2.0) node[right] {$-v_d/2$} -- (4.95, 2.0);
  \draw[thick] (4.85, 2.15) -- (5.05, 2.35) -- (n_out);
  \draw[thick, ->, >=latex] (4.85, 1.85) -- (5.05, 1.65); % Emitter
  \draw[thick] (5.05, 1.65) -- (5.05, 1.1) -- (n_tail);
  \node[right=0.15cm] at (5.2, 2.0) {\small $\mathbf{Q_2}$};

  % Tail Current Source
  \draw[thick] (3.3, 1.1) circle (0.4cm);
  \draw[thick, ->, >=latex] (3.3, 1.35) -- (3.3, 0.85);
  \node[right=0.15cm] at (3.7, 1.1) {\small $I_{SS}$};
  \draw[thick] (3.3, 1.5) -- (3.3, 1.1);
  \draw[thick] (3.3, 0.7) -- (3.3, -0.8);

  % Single-ended output
  \draw[thick] (n_out) -- (6.2, 3.4) node[right] {\large $v_o$};
\end{tikzpicture}
\end{schematicbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Differential Amplifier with Passive Resistive Load ($R_C$):}
  For a single-ended output taken from one collector:
  \[
  A_{d(\text{passive})} = \frac{1}{2} g_m R_C
  \]
  \item \textbf{Differential Amplifier with Active Current Mirror Load ($Q_3, Q_4$):}
  \begin{itemize}[leftmargin=1.5em]
    \item When a differential input $v_d = v_1 - v_2$ is applied, transistor $Q_1$ current increases by $i_c = \frac{1}{2} g_m v_d$ and transistor $Q_2$ current decreases by $i_c = -\frac{1}{2} g_m v_d$.
    \item The current mirror replicates the current change of $Q_1$ to the collector of $Q_4$: $i_{c4} = i_{c1} = +\frac{1}{2} g_m v_d$.
    \item At the single-ended output node, the currents add constructively:
    \[
    i_{\text{out}} = i_{c4} - i_{c2} = \left(+\frac{1}{2} g_m v_d\right) - \left(-\frac{1}{2} g_m v_d\right) = \mathbf{g_m v_d}
    \]
    \item The total output resistance is $R_{\text{out}} = r_{o2} \parallel r_{o4}$.
    \[
    v_o = i_{\text{out}} R_{\text{out}} = (g_m v_d)(r_{o2} \parallel r_{o4}) \implies \mathbf{A_{d(\text{active})} = g_m (r_{o2} \parallel r_{o4})}
    \]
  \end{itemize}
\end{enumerate}
Thus, the active current mirror provides differential-to-single-ended conversion that doubles the effective transconductance, making the active load gain \textbf{twice} the single-ended passive load gain ($A_{d(\text{active})} = 2 \times A_{d(\text{passive})}$). $\blacksquare$

\begin{answerbox}
$$\mathbf{A_{d(\text{active})} = g_m R_{\text{out}} = 2 \times \left(\frac{1}{2} g_m R_C\right) = 2 \times A_{d(\text{passive})}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 9
% =========================================================================
\subsection{Question 9: Efficiency of Series-Fed Class A Amplifier [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q9)}
Derive general efficiency of series fed class A amplifier.
\end{questionbox}

In a series-fed direct-coupled Class A amplifier:
\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{DC Input Power:} $P_{i(\text{dc})} = V_{CC} I_{CQ}$.
  \item \textbf{AC Output Power:} $P_{o(\text{ac})} = \frac{V_p I_p}{2} = \frac{V_p^2}{2 R_C}$.
  \item \textbf{Conversion Efficiency:}
  \[
  \eta = \frac{P_{o(\text{ac})}}{P_{i(\text{dc})}} = \frac{\frac{V_p I_p}{2}}{V_{CC} I_{CQ}} = \frac{1}{2} \left(\frac{V_p}{V_{CC}}\right) \left(\frac{I_p}{I_{CQ}}\right) \times 100\%
  \]
  \item \textbf{Maximum Theoretical Efficiency:}
  Since $V_p \le \frac{V_{CC}}{2}$ and $I_p \le I_{CQ}$ in a resistive series-fed collector circuit:
  \[
  \mathbf{\eta_{\max} = \frac{1}{2} \left(\frac{1}{2}\right)(1) \times 100\% = 25\%}
  \]
\end{enumerate}

\begin{answerbox}
$$\mathbf{\eta = \frac{1}{2} \left(\frac{V_p}{V_{CC}}\right) \left(\frac{I_p}{I_{CQ}}\right) \times 100\%, \qquad \eta_{\max} = 25\%}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 10
% =========================================================================
\subsection{Question 10: Class B Maximum Power Capabilities [5 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q10)}
For a class B amplifier using a supply of $V_{CC} = 30\text{V}$ and driving a load of $16\ \Omega$, determine the maximum input power, maximum output power and maximum power dissipation at transistors.
\end{questionbox}

\begin{enumerate}[leftmargin=1.5em]
  \item \textbf{Maximum AC Output Power ($P_{o(\max)}$):}
  Occurs at maximum linear voltage swing $V_p = V_{CC} = 30\text{V}$:
  \[
  P_{o(\max)} = \frac{V_{CC}^2}{2 R_L} = \frac{(30\text{V})^2}{2 \times 16\ \Omega} = \frac{900}{32} = \mathbf{28.125\text{ W}}
  \]
  \item \textbf{Maximum DC Input Power ($P_{i(\max)}$):}
  \[
  I_{dc(\max)} = \frac{2}{\pi} \left(\frac{V_{CC}}{R_L}\right) = \frac{2}{\pi} \times \frac{30\text{V}}{16\ \Omega} = \frac{60}{16\pi} \approx 1.1937\text{ A}
  \]
  \[
  P_{i(\max)} = V_{CC} \times I_{dc(\max)} = \frac{2 V_{CC}^2}{\pi R_L} = \frac{2(900)}{16\pi} = \mathbf{35.81\text{ W}}
  \]
  \item \textbf{Maximum Transistor Power Dissipation ($P_{D(\max)}$):}
  Transistor power dissipation is $P_D = P_i - P_o = \frac{2 V_{CC} V_p}{\pi R_L} - \frac{V_p^2}{2 R_L}$.\\
  Differentiating with respect to $V_p$ and setting to zero gives the worst-case heating condition at $V_p = \frac{2}{\pi} V_{CC} \approx 0.6366 V_{CC}$:
  \[
  \mathbf{P_{D(\max)} = \frac{2 V_{CC}^2}{\pi^2 R_L} = \frac{2 \times (30\text{V})^2}{\pi^2 \times 16\ \Omega} = \frac{1800}{157.91} = \mathbf{11.399\text{ W}}}
  \]
  Per transistor dissipation: $P_{D1(\max)} = \frac{P_{D(\max)}}{2} = \mathbf{5.70\text{ W}}$.
\end{enumerate}

\begin{answerbox}
$$\mathbf{P_{o(\max)} = 28.125\text{ W}, \qquad P_{i(\max)} = 35.81\text{ W}, \qquad P_{D(\max)} = 11.40\text{ W}}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 11
% =========================================================================
\subsection{Question 11: 555 Timer Astable Multivibrator Frequency Derivation [4 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q11)}
Derive frequency of oscillation of 555 timer Astable Multivibrator.
\end{questionbox}

In an Astable 555 multivibrator, capacitor $C$ charges through $(R_A + R_B)$ from $\frac{1}{3}V_{CC}$ to $\frac{2}{3}V_{CC}$ and discharges through $R_B$ from $\frac{2}{3}V_{CC}$ to $\frac{1}{3}V_{CC}$.

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
$$\mathbf{f = \frac{1.44}{(R_A + 2R_B)C}, \qquad \text{Duty Cycle } D = \frac{R_A + R_B}{R_A + 2R_B} \times 100\%}$$
\end{answerbox}

\vspace{0.6cm}

% =========================================================================
% QUESTION 12
% =========================================================================
\subsection{Question 12: Series Voltage Regulator with Current Limiting \& LM317 Design [4 + 4 = 8 Marks]}
\begin{questionbox}{Problem Statement (2082 Baishakh, Q12)}
Draw series voltage regulator with current limiting circuit and explain how this protection circuit works. Design a voltage regulator to give output voltage from $5\text{V}$ to $15\text{V}$ using LM317.
\end{questionbox}

\paragraph{Part (a): Current Limiting Protection Circuit [4 Marks]}
\begin{schematicbox}{Series Transistor Voltage Regulator with Current Limiting Protection}
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

\paragraph{Circuit Operation:}
A current-sense resistor $R_{\text{sense}}$ and protection transistor $Q_2$ are placed in series with pass transistor $Q_1$:
\begin{itemize}[leftmargin=1.5em]
  \item \textbf{Normal Operation ($I_L < I_{\text{limit}}$):} The voltage drop across $R_{\text{sense}}$ is less than the cut-in voltage ($I_L R_{\text{sense}} < 0.6\text{V}$). Transistor $Q_2$ is OFF and does not interfere with regular voltage regulation.
  \item \textbf{Overload / Short-Circuit Condition ($I_L \ge I_{\text{limit}}$):}
  When $I_L R_{\text{sense}} \ge 0.7\text{V}$, transistor $Q_2$ turns ON, diverting excess base drive current away from pass transistor $Q_1$. This limits the maximum output current to a safe threshold:
  \[
  \mathbf{I_{\text{limit}} = \frac{V_{BE2}}{R_{\text{sense}}} \approx \frac{0.7\text{V}}{R_{\text{sense}}}}
  \]
\end{itemize}

\paragraph{Part (b): LM317 Design for $5\text{V} - 15\text{V}$ Output [4 Marks]}
\[
V_{\text{out}} = 1.25\text{V} \left(1 + \frac{R_2}{R_1}\right)
\]
\begin{enumerate}[leftmargin=1.5em]
  \item Select standard $R_1 = \mathbf{240\ \Omega}$.
  \item For $V_{\text{out}(\min)} = 5.0\text{V}$:
  \[
  5.0 = 1.25 \left(1 + \frac{R_{2(\min)}}{240}\right) \implies 1 + \frac{R_{2(\min)}}{240} = 4.0 \implies R_{2(\min)} = 3 \times 240 = \mathbf{720\ \Omega}
  \]
  \item For $V_{\text{out}(\max)} = 15.0\text{V}$:
  \[
  15.0 = 1.25 \left(1 + \frac{R_{2(\max)}}{240}\right) \implies 1 + \frac{R_{2(\max)}}{240} = 12.0 \implies R_{2(\max)} = 11 \times 240 = \mathbf{2640\ \Omega} = \mathbf{2.64\text{ k}\Omega}
  \]
\end{enumerate}
\textbf{Implementation:} Use a fixed resistor $R_{2A} = 680\ \Omega$ in series with a $\mathbf{2.0\text{ k}\Omega}$ linear potentiometer.

\begin{answerbox}
$$\mathbf{R_1 = 240\ \Omega, \qquad R_2 = 720\ \Omega \text{ to } 2.64\text{ k}\Omega \quad (\text{Fixed } 680\ \Omega + 2.0\text{k}\Omega \text{ Potentiometer})}$$
\end{answerbox}
"""
