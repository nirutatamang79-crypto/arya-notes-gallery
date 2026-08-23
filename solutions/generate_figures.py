import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('figures', exist_ok=True)
plt.rcParams.update({
    'font.size': 10,
    'font.family': 'sans-serif',
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'grid.alpha': 0.35,
    'grid.linestyle': '--'
})

# ==============================================================================
# 1. Bode Plot: 2083 Baishakh Q5
# H(s) = 50*(1 + s/5) / [s^2 * (1 + s/20)]
# ==============================================================================
w = np.logspace(-1, 3, 1000)
mag_asymp = []
for wi in w:
    if wi < 5:
        mag_asymp.append(33.98 - 40*np.log10(wi))
    elif wi < 20:
        mag_asymp.append(6.02 - 20*np.log10(wi/5))
    else:
        mag_asymp.append(-6.02 - 40*np.log10(wi/20))

s = 1j * w
H_exact = 50 * (1 + s/5) / (s**2 * (1 + s/20))
mag_exact = 20 * np.log10(np.abs(H_exact))
phase_exact = np.angle(H_exact, deg=True)
phase_exact = np.unwrap(phase_exact * np.pi/180) * 180/np.pi

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 5.5), sharex=True)
ax1.semilogx(w, mag_asymp, 'r--', linewidth=2, label='Asymptotic Magnitude')
ax1.semilogx(w, mag_exact, 'b-', linewidth=1.5, label='Exact Magnitude')
ax1.axvline(5, color='green', linestyle=':', label=r'Zero $\omega_{z1} = 5$ rad/s')
ax1.axvline(20, color='purple', linestyle=':', label=r'Pole $\omega_{p1} = 20$ rad/s')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title(r'Bode Diagram: $H(s) = \frac{50(1 + s/5)}{s^2(1 + s/20)}$')
ax1.grid(True, which='both')
ax1.legend(loc='upper right')

ax2.semilogx(w, phase_exact, 'b-', linewidth=1.5, label='Exact Phase')
ax2.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax2.set_ylabel('Phase (deg)')
ax2.grid(True, which='both')
ax2.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figures/bode_2083_baishakh.pdf')
plt.close()

# ==============================================================================
# 2. Bode Plot: 2082 Bhadra Q6
# T(s) = 25*(1 + s/5) / [s^2 * (1 + s) * (1 + s/20)]
# ==============================================================================
w = np.logspace(-1, 3, 1000)
mag_asymp = []
for wi in w:
    if wi < 1:
        mag_asymp.append(27.96 - 40*np.log10(wi))
    elif wi < 5:
        # from w=1 to 5, slope is -60 dB/dec
        mag_asymp.append(27.96 - 60*np.log10(wi/1))
    elif wi < 20:
        # at w=5: 27.96 - 60*log10(5) = -13.97 dB. slope -40 dB/dec
        mag_asymp.append(-13.97 - 40*np.log10(wi/5))
    else:
        # at w=20: -13.97 - 40*log10(4) = -38.05 dB. slope -60 dB/dec
        mag_asymp.append(-38.05 - 60*np.log10(wi/20))

s = 1j * w
T_exact = 25 * (1 + s/5) / (s**2 * (1 + s) * (1 + s/20))
mag_exact = 20 * np.log10(np.abs(T_exact))
phase_exact = np.angle(T_exact, deg=True)
phase_exact = np.unwrap(phase_exact * np.pi/180) * 180/np.pi

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 5.5), sharex=True)
ax1.semilogx(w, mag_asymp, 'r--', linewidth=2, label='Asymptotic Magnitude')
ax1.semilogx(w, mag_exact, 'b-', linewidth=1.5, label='Exact Magnitude')
ax1.axvline(1, color='orange', linestyle=':', label=r'Pole $\omega_{p1} = 1$ rad/s')
ax1.axvline(5, color='green', linestyle=':', label=r'Zero $\omega_{z1} = 5$ rad/s')
ax1.axvline(20, color='purple', linestyle=':', label=r'Pole $\omega_{p2} = 20$ rad/s')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title(r'Bode Diagram: $T(s) = \frac{25(1 + s/5)}{s^2(1 + s)(1 + s/20)}$')
ax1.grid(True, which='both')
ax1.legend(loc='upper right')

ax2.semilogx(w, phase_exact, 'b-', linewidth=1.5, label='Exact Phase')
ax2.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax2.set_ylabel('Phase (deg)')
ax2.grid(True, which='both')
ax2.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figures/bode_2082_bhadra.pdf')
plt.close()

# ==============================================================================
# 3. Bode Plot: 2082 Baishakh Q5
# G(s) = 5s*(1 + s/5) / [(1 + s) * (1 + 0.1s + 0.01s^2)]
# ==============================================================================
w = np.logspace(-1, 3, 1000)
mag_asymp = []
for wi in w:
    if wi < 1:
        # initial +20 dB/dec slope with 20*log10(5*w) = 14 + 20*log10(w)
        mag_asymp.append(13.98 + 20*np.log10(wi))
    elif wi < 5:
        # from w=1 to 5, slope is 0 dB/dec (13.98 dB)
        mag_asymp.append(13.98)
    elif wi < 10:
        # from w=5 to 10, slope is +20 dB/dec: 13.98 + 20*log10(w/5)
        mag_asymp.append(13.98 + 20*np.log10(wi/5))
    else:
        # at w=10: 13.98 + 20*log10(2) = 20.0 dB. Complex pole pair introduces -40 dB/dec slope => net -20 dB/dec
        mag_asymp.append(20.0 - 20*np.log10(wi/10))

s = 1j * w
G_exact = 5 * s * (1 + s/5) / ((1 + s) * (1 + 0.1*s + 0.01*s**2))
mag_exact = 20 * np.log10(np.abs(G_exact))
phase_exact = np.angle(G_exact, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 5.5), sharex=True)
ax1.semilogx(w, mag_asymp, 'r--', linewidth=2, label='Asymptotic Magnitude')
ax1.semilogx(w, mag_exact, 'b-', linewidth=1.5, label='Exact Magnitude')
ax1.axvline(1, color='orange', linestyle=':', label=r'Pole $\omega_{p1} = 1$ rad/s')
ax1.axvline(5, color='green', linestyle=':', label=r'Zero $\omega_{z1} = 5$ rad/s')
ax1.axvline(10, color='purple', linestyle=':', label=r'Complex Poles $\omega_n = 10$ rad/s')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title(r'Bode Diagram: $G(s) = \frac{5s(1 + s/5)}{(1 + s)(1 + 0.1s + 0.01s^2)}$')
ax1.grid(True, which='both')
ax1.legend(loc='lower left')

ax2.semilogx(w, phase_exact, 'b-', linewidth=1.5, label='Exact Phase')
ax2.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax2.set_ylabel('Phase (deg)')
ax2.grid(True, which='both')
ax2.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figures/bode_2082_baishakh.pdf')
plt.close()

# ==============================================================================
# 4. Bode Plot: 2081 Ashwin Q5
# G(s) = 8.264*(1 + s/2) / [s * (1 + (15/121)s + s^2/121)]
# ==============================================================================
w = np.logspace(-1, 3, 1000)
mag_asymp = []
for wi in w:
    if wi < 2:
        # initial -20 dB/dec: 20*log10(8.264) - 20*log10(w) = 18.34 - 20*log10(w)
        mag_asymp.append(18.34 - 20*np.log10(wi))
    elif wi < 11:
        # at w=2: 18.34 - 20*log10(2) = 12.32 dB. Zero at w=2 gives 0 dB/dec slope
        mag_asymp.append(12.32)
    else:
        # at w=11: 12.32 dB. Complex poles at w=11 give -40 dB/dec slope
        mag_asymp.append(12.32 - 40*np.log10(wi/11))

s = 1j * w
G_exact = 8.264 * (1 + s/2) / (s * (1 + (15/121)*s + (s**2)/121))
mag_exact = 20 * np.log10(np.abs(G_exact))
phase_exact = np.angle(G_exact, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 5.5), sharex=True)
ax1.semilogx(w, mag_asymp, 'r--', linewidth=2, label='Asymptotic Magnitude')
ax1.semilogx(w, mag_exact, 'b-', linewidth=1.5, label='Exact Magnitude')
ax1.axvline(2, color='green', linestyle=':', label=r'Zero $\omega_{z1} = 2$ rad/s')
ax1.axvline(11, color='purple', linestyle=':', label=r'Complex Poles $\omega_n = 11$ rad/s')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title(r'Bode Diagram: $G(s) = \frac{8.264(1 + s/2)}{s(1 + \frac{15}{121}s + \frac{s^2}{121})}$')
ax1.grid(True, which='both')
ax1.legend(loc='upper right')

ax2.semilogx(w, phase_exact, 'b-', linewidth=1.5, label='Exact Phase')
ax2.set_xlabel(r'Frequency $\omega$ (rad/s)')
ax2.set_ylabel('Phase (deg)')
ax2.grid(True, which='both')
ax2.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figures/bode_2081_ashwin.pdf')
plt.close()

# ==============================================================================
# 5. Induction Motor Torque-Speed & Torque-Slip Curve
# ==============================================================================
s_vals = np.linspace(0.001, 1.0, 500)
# T = k * s * E2^2 * R2 / (R2^2 + (s*X2)^2)
# Normalize with X2 = 1, k*E2^2 = 2
def get_torque(s, R2, X2=1.0, kE2sq=2.0):
    return (kE2sq * s * R2) / (R2**2 + (s * X2)**2)

plt.figure(figsize=(7.5, 4.8))
T_norm = get_torque(s_vals, R2=0.2)
T_high_R = get_torque(s_vals, R2=0.5)
T_max_start = get_torque(s_vals, R2=1.0)

# Speed N = Ns * (1 - s)
speed_vals = 1500 * (1 - s_vals)

plt.plot(speed_vals, T_norm, 'b-', linewidth=2, label=r'Normal $R_2$ (Standard Squirrel Cage)')
plt.plot(speed_vals, T_high_R, 'g--', linewidth=1.8, label=r'Higher $R_2$ (Deep Bar / Slip Ring)')
plt.plot(speed_vals, T_max_start, 'r-.', linewidth=1.8, label=r'Maximum Starting Torque ($R_2 = X_2$)')

# Annotations
plt.axvline(1500, color='gray', linestyle=':', label='Synchronous Speed $N_s$ ($s=0$)')
plt.axvline(0, color='black', linestyle='-', linewidth=0.8)

# Mark Tmax
sm_norm = 0.2
N_sm_norm = 1500 * (1 - sm_norm)
Tmax_val = get_torque(sm_norm, R2=0.2)
plt.plot(N_sm_norm, Tmax_val, 'ro')
plt.annotate(r'Breakdown / Pull-out Torque $T_{max}$' + f'\n(at $s_m = R_2/X_2$)',
             xy=(N_sm_norm, Tmax_val), xytext=(N_sm_norm - 400, Tmax_val + 0.15),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6))

# Annotate Stable vs Unstable regions
plt.axvspan(N_sm_norm, 1500, alpha=0.1, color='green', label='Stable Operating Region ($s < s_m$)')
plt.axvspan(0, N_sm_norm, alpha=0.08, color='red', label='Unstable Region ($s > s_m$)')

plt.xlabel('Rotor Speed $N$ (rpm) [$\leftarrow$ Slip $s$ increases from 0 to 1]')
plt.ylabel('Developed Electromagnetic Torque $T$ (Normalized)')
plt.title(r'3-Phase Induction Motor Torque-Speed Characteristic ($T = \frac{k s E_2^2 R_2}{R_2^2 + (s X_2)^2}$)')
plt.grid(True)
plt.legend(loc='upper left', fontsize=8.5)
plt.tight_layout()
plt.savefig('figures/im_torque_speed.pdf')
plt.close()

# ==============================================================================
# 6. DC Generator Characteristics (OCC, Internal, External)
# ==============================================================================
plt.figure(figsize=(7, 4.5))
If = np.linspace(0, 5, 200)
# OCC curve: E0 vs If (saturation curve)
E0 = 240 * (1 - np.exp(-1.2*If)) + 15
plt.plot(If, E0, 'b-', linewidth=2, label='Open Circuit Characteristic (OCC): $E_0$ vs $I_f$')
plt.axhline(15, color='gray', linestyle=':', label='Residual Voltage at $I_f=0$')
plt.xlabel('Field Current $I_f$ (A)')
plt.ylabel('Generated EMF $E_0$ (V)')
plt.title('DC Generator Open-Circuit Magnetization Curve (OCC)')
plt.grid(True)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('figures/dc_generator_occ.pdf')
plt.close()

# Load characteristics (V vs IL)
IL = np.linspace(0, 100, 200)
E_gen = 220 - 0.05*IL # internal drop due to armature reaction
V_term = E_gen - 0.15*IL # terminal voltage after Ia*Ra drop
plt.figure(figsize=(7, 4.5))
plt.plot(IL, [220]*len(IL), 'k:', label=r'No-load EMF $E_0$')
plt.plot(IL, E_gen, 'b--', linewidth=1.8, label=r'Internal Characteristic: $E$ vs $I_a$ (Armature Reaction drop)')
plt.plot(IL, V_term, 'r-', linewidth=2, label=r'External Characteristic: $V$ vs $I_L$ (Armature $I_a R_a$ drop)')
plt.xlabel('Load Current $I_L$ (A)')
plt.ylabel('Terminal Voltage $V$ (V)')
plt.title('DC Shunt Generator Internal and External Characteristics')
plt.grid(True)
plt.legend(loc='lower left')
plt.tight_layout()
plt.savefig('figures/dc_generator_load_curves.pdf')
plt.close()

# ==============================================================================
# 7. Magnetic Circuit B-H Curve & Hysteresis Loop
# ==============================================================================
plt.figure(figsize=(6.5, 4.5))
H = np.linspace(-1000, 1000, 500)
# S-shaped hysteresis loop
def b_upper(h):
    return 1.4 * np.tanh((h + 200)/300)
def b_lower(h):
    return 1.4 * np.tanh((h - 200)/300)

plt.plot(H, b_upper(H), 'b-', linewidth=1.8)
plt.plot(H, b_lower(H), 'b-', linewidth=1.8, label='Hysteresis Loop')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Mark Remanence Br and Coercivity Hc
Br = b_upper(0)
plt.plot(0, Br, 'ro')
plt.annotate(r'Retentivity / Remanence $B_r$', xy=(0, Br), xytext=(80, Br),
             arrowprops=dict(facecolor='black', shrink=0.05, width=0.8, headwidth=5))

# Coercive force Hc: where b_upper(h) = 0 => h = -200
plt.plot(-200, 0, 'go')
plt.annotate(r'Coercive Force $H_c$', xy=(-200, 0), xytext=(-550, 0.3),
             arrowprops=dict(facecolor='black', shrink=0.05, width=0.8, headwidth=5))

plt.annotate(r'Saturation Region ($B_{sat}$)', xy=(800, 1.35), xytext=(400, 1.1),
             arrowprops=dict(facecolor='black', shrink=0.05, width=0.8, headwidth=5))

plt.xlabel(r'Magnetic Field Intensity $H$ (A$\cdot$t/m)')
plt.ylabel(r'Magnetic Flux Density $B$ (Tesla)')
plt.title(r'Ferromagnetic Material $B$-$H$ Hysteresis Loop')
plt.grid(True)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('figures/bh_hysteresis.pdf')
plt.close()

print('All 7 figures generated successfully!')
