import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn


# definition of the spherical bessel function
def bessel_j0(p):
    return np.sin(p)/p


# definition of 
x = np.linspace(0, 10, 100)
y = np.sin(x)/x
y1 = spherical_jn(0, x)

plt.plot(x, y, 'r--', label='Analytical')
plt.plot(x, y1, 'b:', label='Numerical')
plt.xlim(0, 10)
plt.xlabel('$x$')
plt.ylabel('$j_0(x)$')
plt.legend()
plt.savefig('plot_bessel.png', dpi=128)
