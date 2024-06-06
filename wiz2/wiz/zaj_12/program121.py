import math
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,3, 100)
y=x**2
y1 = (math.e)**x
y2 = x**x


plt.subplot(3,1,1)
plt.ylim(0, 20)
plt.plot(x,y,'green',linestyle="--",label="(x^2)")


plt.subplot(3,1,2)
plt.ylim(0, 20)
plt.plot(x,y1,'red',linestyle=":",label="e^x",)


plt.subplot(3,1,3)
plt.ylim(0, 20)
plt.plot(x,y2,'blue',linestyle="-",label="(x^x)")

plt.show()

