import numpy as np
import matplotlib.pyplot as plt

# Time axis: omega_0 * t from 0 to 2*pi
omega_t = np.linspace(0, 2 * np.pi, 1000)

# Different theta values (angle of initial state from z-axis)
thetas = [np.pi/6, np.pi/4, np.pi/3, np.pi/2, 2*np.pi/3]
labels = [r'$\theta = \pi/6$', r'$\theta = \pi/4$', r'$\theta = \pi/3$',
          r'$\theta = \pi/2$', r'$\theta = 2\pi/3$']

plt.figure(figsize=(8, 5))

for theta, label in zip(thetas, labels):
    # |<psi(t0)|psi(t)>|^2 = cos^2(wt/2) + cos^2(theta)*sin^2(wt/2)
    inner_product_sq = (np.cos(omega_t / 2)**2
                        + np.cos(theta)**2 * np.sin(omega_t / 2)**2)

    # Clamp to [0,1] to avoid numerical errors in arccos
    inner_product_sq = np.clip(inner_product_sq, 0, 1)

    # alpha(t) = arccos(sqrt(...))
    alpha = np.arccos(np.sqrt(inner_product_sq))

    plt.plot(omega_t, alpha, label=label)

# MT bound for theta = pi/2: alpha <= omega_t / 2
plt.plot(omega_t, omega_t / 2, 'k--', linewidth=2, label='MT bound (slope = 1/2)')

plt.xlabel(r'$\omega_0 t$', fontsize=13)
plt.ylabel(r'$\alpha(t)$', fontsize=13)
plt.title('Generalized MT Bound: $\\alpha$ vs $\\omega_0 t$', fontsize=13)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/qsl_plot.png', dpi=150)
plt.show()
