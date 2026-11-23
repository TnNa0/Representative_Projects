import numpy as np
import matplotlib.pyplot as plt

# Example parameters
v = 1.0
kcat = 100.0
Kin = 0.8
R = 0.008314   # kJ/(mol*K)
T = 298.15     # K

# Include both negative and positive drG, but avoid zero
drG_neg = np.linspace(-40, -0.01, 500)
drG_pos = np.linspace(0.01, 10, 300)

thermo_neg = 1 - np.exp(drG_neg / (R * T))
thermo_pos = 1 - np.exp(drG_pos / (R * T))

Etot_neg = v / (kcat * Kin * thermo_neg)
Etot_pos = v / (kcat * Kin * thermo_pos)

plt.figure(figsize=(8,5))
plt.plot(drG_neg, Etot_neg, label='drG < 0 (physical for forward flux)')
plt.plot(drG_pos, Etot_pos, '--', label='drG > 0 (gives negative Etot)')
plt.axvline(0, color='black', linewidth=1)
plt.xlabel('drG [kJ/mol]')
plt.ylabel('[Etot]')
plt.title('Etot vs drG')
plt.grid(True)
plt.legend()
plt.show()