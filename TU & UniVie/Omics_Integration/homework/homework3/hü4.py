import numpy as np
import matplotlib.pyplot as plt

# Range of r4 values
r4 = np.linspace(0, 10, 200)

# FVA bounds for r2 as function of r4
r2_min = np.zeros_like(r4)
r2_max = (10 - r4) / 2

# Plot
plt.figure(figsize=(8, 5))
plt.plot(r4, r2_min, label="Lower bound of r2")
plt.plot(r4, r2_max, label="Upper bound of r2")
plt.fill_between(r4, r2_min, r2_max, alpha=0.2)

plt.xlim(0, 10)
plt.ylim(0, 5)
plt.xlabel("r4")
plt.ylabel("r2")
plt.title("FVA: r2 as a function of r4")
plt.grid(True)
plt.legend()
plt.show()