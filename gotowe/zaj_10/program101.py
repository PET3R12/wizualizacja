import numpy as np
import pandas as pd
df = pd.read_csv('jajka2024.csv', delimiter=';', decimal=',')
df.set_index(df.columns[0], inplace=True)
print(df)

#obliczyć średnią cenę wszystkich jaj.
print('średnia cena jaj:', df.sum().sum()/len(df))


#wyznaczyć w którym mieście i w jakiej sieci s¡ najtańsze a w jakich najdroższe
#jajka. Wynik zapisz w postaci dwuwymiarowej tablicy przechowującej pary
#(Miasto, nazwa sieci).

najnizsze_indeksy = df.idxmin()
najwyzsze_indeksy = df.idxmax()

najtansze = [[miasto, sklep] for miasto, sklep in zip(najnizsze_indeksy, df.loc[najnizsze_indeksy])]
najdroższe = [[miasto, sklep] for miasto, sklep in zip(najwyzsze_indeksy, df.loc[najwyzsze_indeksy])]

najtansze = pd.DataFrame(najtansze, columns=['Nazwa sieci:', 'Miasto:'])
najdroższe = pd.DataFrame(najdroższe)
print('\nNajtańsze:\n', najtansze)
print('\nNajdroższe:\n', najdroższe)


#CW3
print('\nCW3')
import pandas as pd
data = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='UTF-8')
data2 = data.stack()
data3 = data2.str.replace(',', '.').astype('float')
srednia = data3.mean()
minCena = data3.min()
maxCena = data3.max()
print('Najtańsze:\n', data3[data3 == minCena])
print('Najdroższe:\n', data3[data3 == maxCena])
print(data3)



