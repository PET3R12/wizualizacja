import numpy as np
import pandas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('penguins.csv')

#średnia waga w każdej płci, średnia waga z podziałem na płeć i gatunek
avg_weight_sex = df.groupby('sex')['body_mass_g'].mean()
avg_weight_species_sex = df.groupby(['species', 'sex'])['body_mass_g'].mean()
print("Średnia waga dla każdej płci:")
print(avg_weight_sex)
print("\nŚrednia waga z podziałem na płeć i gatunek:")
print(avg_weight_species_sex)

#wszystkie wartości dla pingwinów z największą i najmniejszą wagą
najwiekszy = df[df['body_mass_g'] == max(df['body_mass_g'])]
najmniejszy = df[df['body_mass_g'] == min(df['body_mass_g'])]
print(f'Najcięższy pingwin: \n{najwiekszy}')
print(f'\nNajlżejszy pingwin:\n{najmniejszy}')

#ilość pingwinów każdego gatunku na każdej wyspie
print(f'Ilość pingwinów na każdej wyspie:\n{df['island'].value_counts()}')

#ilość pingwinów gatunku 'Adelie' na każdej wyspie
print(f'\nIlość Adalii na każdej wyspie:\n{df[df['species'] == 'Adelie']['island'].value_counts()}')

#narysuj wykres słupkowy ilości pingwinów w zależno±ci od wyspy:
ilosc_wyspa = df['island'].value_counts()

#ilosc_wyspa.plot.bar(color='darkred', title='ilosc', xlabel='wyspa', ylabel='ilosc')
#plt.show()

dzioby_l = df['bill_length_mm']
dzioby_d = df['bill_depth_mm']
print(dzioby_l)
print(dzioby_d)

df['rozmiar'] = (df['body_mass_g']/2000)**5
rozmiar = list(df['rozmiar'])




colors = np.where(df["sex"]=='MALE','b','r')

shapes = np.where(df['species'] == 'Adelie', 'o', np.where(df['species'] == 'Chinstrap', 's', '<'))

# For tworzy dla każdego kształtu ['o', 's', '<'] własną mini bazę (subset), stąd scatter wywoła się 3 razy na podstawie szerokości dzioba itp
for species, marker in zip(df['species'].unique(), ['o', 's', '<']):
    subset = df[df['species'] == species]
    plt.scatter(subset['bill_length_mm'], subset['bill_depth_mm'],
                color=colors[subset.index], s=subset['rozmiar'], label=species, marker=marker)
print(subset)
plt.xlabel('Długość dzioba')
plt.ylabel('Szerokość dzioba')
plt.show()
