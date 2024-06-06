import pandas as pd

# Wczytanie danych z pliku CSV
df = pd.read_csv('jajka2024.csv', delimiter=';', decimal=',')

# Ustawienie indeksu na nazwy sklepów
df.set_index(df.columns[0], inplace=True)


print(df)
sum(df)