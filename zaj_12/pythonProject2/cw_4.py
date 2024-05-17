import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as mtick

glue = sns.load_dataset('glue')
data = glue['Score'][glue['Model'] == 'ERNIE']
year = [2017, 2018, 2019]

#create catplot
glue_df = sns.catplot(
    data=glue,
    kind='violin',
    x='Year',
    y='Score',

)
#set labels
glue_df.set_axis_labels('Tasks', 'Scores')
glue_df
plt.show()