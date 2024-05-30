import numpy as np
import pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins")

print(penguins)
sns.relplot(
    data=penguins,
    x='bill_depth_mm',
    y='bill_length_mm',
    hue='sex',
    size='body_mass_g',
    style='species'
)
plt.show()