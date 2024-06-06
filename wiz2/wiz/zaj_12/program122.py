import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def potegaplot(flip=1):
    x = np.linspace(-2,2,100)
    x2 = np.linspace(0, 2, 100)
    for i in range(1,4):
        plt.plot(x,x**i*flip)
        plt.plot(x2, x2**(1/i)*flip)
sns.set_style("darkgrid")
sns.set_palette("dark")
# potegaplot()
# print(sns.axes_style())
# plt.show()

#ĆW4
glue = sns.load_dataset("glue")

kolory = ['orange', 'green']
palette = {c: "orange" if c != "Transformer" else "green" for c in glue["Encoder"].unique()}

sns.catplot(
    data=glue,
    x='Year',
    y='Score',
    kind='violin',
    col='Model',
    hue='Encoder',
    palette=kolory
)
plt.show()