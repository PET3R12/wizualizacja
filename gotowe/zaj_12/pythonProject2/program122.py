import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def sinplot(flip = 1):
    x = np.linspace(0,2,100)
    x1 = np.linspace(-2, 2, 100)
    for i in range(-8, 8):
        plt.plot(x1, x1*flip, 'blue')
        plt.plot(x1, x1**2, 'red')
        plt.plot(x1, x1**3, 'green')
        plt.plot(x, x**(1/2), 'darkred')
        plt.plot(x, x ** (1/3), 'purple')
sns.set_style("darkgrid")
sns.set_palette("husl")
sinplot()
print(sns.axes_style())
plt.show()

