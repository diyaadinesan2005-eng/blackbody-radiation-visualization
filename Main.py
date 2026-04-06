import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34   # Planck constant (J s)
c = 3e8         # Speed of light (m/s)
k = 1.381e-23   # Boltzmann constant (J/K)
sigma = 5.67037e-8  # Stefan-Boltzmann constant

# Wavelength range (in meters)
lam = np.linspace(100e-9, 4000e-9, 1000)

for T in range(3000, 6001, 1000):
    # Planck’s Radiation Law
    I = (2 * np.pi * h * c**2) / (lam**5) * \
        (1 / (np.exp((h * c) / (lam * k * T)) - 1))

    # Peak wavelength
    print(f"Temperature: {T} K, Lambda max = {lam[np.argmax(I)]:.2e} m")

    # Area under curve (numerical integration)
    x = lam * 1e9  # convert to nm
    area = np.trapz(I, x) * 1e-9

    print(f"Estimated area: {area:.2e}")
    print(f"Sigma T^4: {sigma * T**4:.2e}")
    print()

    # Plot
    plt.plot(x, I, label=f"{T} K")

# Graph settings
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.title("Planck Radiation Curve")
plt.legend()
plt.grid(True)

plt.show()
