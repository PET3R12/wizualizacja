import math
import numpy as np
import matplotlib.pyplot as plt

#wykres funkcji y =1/(1 + x^2) na przedziale [−10, 10].
x = np.linspace(-10, 10)
y = np.divide(1, 1+x**2)
plt.plot(x, y, 'green', linestyle="-", label="sin(2x)")
plt.legend(title='1/(1+x**2)')
plt.show()


x1 = np.linspace(0, 3)
y1 = x1**2
y2 = math.e**x1
y3 = x1**x1
plt.plot(x1, y1, 'green', linestyle="-", label="x^2")
plt.plot(x1, y2, 'red', linestyle=":", label="e^x")
plt.plot(x1, y3, 'blue', linestyle='-', label="x^x")
plt.legend(title="Wykres")
plt.show()

x1 = np.linspace(0, 4)
y1 = x1**2
y2 = math.e**x1
y3 = x1**x1
plt.plot(x1, y1, 'green', linestyle="-", label="x^2")
plt.plot(x1, y2, 'red', linestyle=":", label="e^x")
plt.plot(x1, y3, 'blue', linestyle='-', label="x^x")
plt.legend(title="Wykres")
plt.show()

x3 = np.linspace(0, 4)
plt.subplot(3, 1, 1)
plt.plot(x3, y1, linestyle='--', color='green', label='x^2')
plt.subplot(3, 1, 2)
plt.plot(x3, y2, linestyle=':', color='red', label='e^x')
plt.subplot(3, 1, 3)
plt.plot(x3, y3, 'blue', linestyle='-', label='x^x')
plt.show()
