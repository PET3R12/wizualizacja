import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 100)
y1 = np.cos(x)
y2 = np.sin(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
