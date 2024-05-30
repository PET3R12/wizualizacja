import numpy as np
import pandas as pd
f = open('penguins.csv', 'r+')
s = f.readlines()
usecols = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']

data = pd.read_csv("penguins.csv", delimiter=None, engine='python')
df = pd.DataFrame(data, columns=usecols, )
suma = 0
#średnia waga w każdej płci, średnia waga z podziałem na płeć i gatunek

df['body_mass_g'] = df['body_mass_g'].fillna(0).astype(int)
for element in df['body_mass_g']:
    element = int(element)
suma = sum(df['body_mass_g'][df['sex'] == 'MALE'][df['species'] == 'Adelie'])
ilosc = len(df['body_mass_g'][df['sex'] == 'MALE'][df['species'] == 'Adelie'])
print(f'MALE, Adelie: {suma/ilosc}')
suma = sum(df['body_mass_g'][df['sex'] == 'FEMALE'][df['species'] == 'Adelie'])
ilosc = len(df['body_mass_g'][df['sex'] == 'FEMALE'][df['species'] == 'Adelie'])
print(f'FEMALE, Adelie: {suma/ilosc}')
