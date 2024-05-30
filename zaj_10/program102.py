import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('jajka2024.csv', delimiter=';', decimal=',')
df.set_index(df.columns[0], inplace=True)
df = df.fillna(0)
print(df.columns)
xlabele = list(df.columns)



#Stwórz wykres pudełkowy
df.boxplot()
plt.yticks([0, 6, 8, 10, 12])
plt.show()