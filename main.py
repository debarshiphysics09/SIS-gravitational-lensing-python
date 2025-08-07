import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Parameters
theta_E = 20  # Einstein radius in arcseconds

# Grid setup for angular positions (arcseconds)
theta1 = np.linspace(-40, 40, 500)
theta2 = np.linspace(-40, 40, 500)
Theta1, Theta2 = np.meshgrid(theta1, theta2)
theta_mag = np.sqrt(Theta1**2 + Theta2**2)

# Deflection angle for SIS lens model
alpha1 = theta_E * Theta1 / (theta_mag + 1e-6)
alpha2 = theta_E * Theta2 / (theta_mag + 1e-6)

# Source position (background galaxy) in arcseconds
beta0 = np.array([5, 5])  
beta1 = Theta1 - alpha1
beta2 = Theta2 - alpha2

# Gaussian background source intensity profile on source plane
gamma_source = 4.0  # width of Gaussian source in arcseconds
source_intensity = np.exp(-(((beta1 - beta0[0])**2 + (beta2 - beta0[1])**2) / (2 * gamma_source**2)))

# Intensity map on image plane (lensed image)
intensity_image = source_intensity

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Left panel: Lens setup
ax = axs[0]
ax.set_title('Lens Setup')
ax.set_xlabel('Theta_1 (arcseconds)')
ax.set_ylabel('Theta_2 (arcseconds)')
ax.set_xlim([-40, 40])
ax.set_ylim([-40, 40])
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)

# Einstein radius circle
circle = plt.Circle((0, 0), theta_E, color='red', fill=False, lw=2, label='Einstein Radius')
ax.add_patch(circle)

# Source position
ax.plot(beta0[0], beta0[1], 'bo', label='Source position')
ax.legend()
ax.grid(True)

# Right panel: Lensed image intensity with logarithmic color scale
ax = axs[1]
img = ax.imshow(intensity_image, origin='lower', extent=[-40, 40, -40, 40], cmap='viridis', norm=LogNorm(vmin=1e-3, vmax=1))
ax.set_title('Simulated Gravitational Lensing by SIS\nBackground Gaussian source lensed near Einstein radius')
ax.set_xlabel('Theta_1 (arcseconds)')
ax.set_ylabel('Theta_2 (arcseconds)')

# Colorbar for intensity
cbar = fig.colorbar(img, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Intensity (arbitrary units)')

plt.tight_layout()
plt.show()
