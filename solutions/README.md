# IOE Electrical Circuits & Machines (EE 154 / ENEE 154) — Solutions Package

This directory contains the complete, mathematically audited, and typeset master past paper solutions for **Tribhuvan University, Institute of Engineering (IOE)**.

## Contents

- **`Electrical_Circuits_and_Machines_Solutions_Master.pdf`**: The complete 54-page Master Solutions Book (compiled, publication-grade PDF).
- **`Electrical_Circuits_and_Machines_Solutions_Master.tex`**: Complete LaTeX master source code using `circuitikz` for vector circuit schematics and `tcolorbox` for callout boxes.
- **`figures/`**: Directory containing all 7 vector plot figures:
  - `bode_2083_baishakh.pdf`: Bode diagram for $H(s) = \frac{50(1+s/5)}{s^2(1+s/20)}$
  - `bode_2082_bhadra.pdf`: Bode diagram for $T(s) = \frac{25(1+s/5)}{s^2(1+s)(1+s/20)}$
  - `bode_2082_baishakh.pdf`: Bode diagram for $G(s) = \frac{5s(1+s/5)}{(1+s)(1+0.1s+0.01s^2)}$
  - `bode_2081_ashwin.pdf`: Bode diagram for $G(s) = \frac{8.264(1+s/2)}{s(1+\frac{15}{121}s+\frac{s^2}{121})}$
  - `im_torque_speed.pdf`: 3-Phase Induction Motor Torque-Speed Characteristic
  - `dc_generator_occ.pdf` & `dc_generator_load_curves.pdf`: DC Generator Magnetization and Load Curves
  - `bh_hysteresis.pdf`: Ferromagnetic $B$-$H$ Hysteresis Loop
- **`generate_figures.py`**: Python script to regenerate all vector PDF plots in `figures/`.
- **`make_latex_book.py`**: Automated build script to recompile the master LaTeX document.

## How to Recompile

To recompile the PDF at any time, run:
```bash
pdflatex -interaction=nonstopmode Electrical_Circuits_and_Machines_Solutions_Master.tex
pdflatex -interaction=nonstopmode Electrical_Circuits_and_Machines_Solutions_Master.tex
```
*(Running twice resolves all table of contents and internal page references).*
