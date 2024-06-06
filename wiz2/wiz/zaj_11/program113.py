import numpy as np
import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

irysy = sns.load_dataset("iris")
# sns.relplot(
#     data=irysy,
#     x='sepal_length',
#     y='sepal_width',
#     hue='species'
# )
# sns.relplot(
#     data=irysy,
#     x='petal_length',
#     y='petal_width',
#     hue='species',
# )
# sns.catplot(
#     data=irysy,
#     x='species',
#     y='petal_length',
#     kind='bar',
#     color='blue'
# )
# sns.catplot(
#     data=irysy,
#     x='species',
#     y='petal_width',
#     kind='bar',
#     color='green'
# )
# sns.catplot(
#     data=irysy,
#     x='species',
#     y='sepal_width',
#     kind='bar',
#     color='red'
# )
sns.pairplot(data=irysy, hue="species")
plt.show()