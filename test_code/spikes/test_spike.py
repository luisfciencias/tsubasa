# script to test the tools pipeline
import numpy as np
import matplotlib.pyplot as plt
from tools_spike import sin

x = np.linspace(0, 10, 100)
y = sin(x)
plt.plot(x, y, 'r--')
plt.show()

