from random import *
import numpy as np
import pandas as pd

df1 = pd.DataFrame([[2942,9840,2794,8891,8111,2933,8301,9125],
                    [ 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz','Cezary', 'Zenon', 'Filip', 'Adrian'],
                    [13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name','Age']
weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]
df2 = pd.DataFrame([[2312,2336,2942,9840,2794,8891,8111,2933],
                    ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa','Tomasz', 'Cezary', 'Zenon'],
                    weight,
                    height,
                    glasses]).T
df2.columns = ['ID','Name','W', 'H','Gl']
zloczone_inner = pd.merge(df1, df2, how='inner', on=['ID', 'Name'], indicator=True)
print(zloczone_inner)
zloczone_outer = pd.merge(df1, df2, on=['ID', 'Name'], how='outer',)
print(zloczone_outer)

#sortowanie
print(zloczone_outer.sort_values(by='Name'))

#stwórz tablice przechowującą imiona osób noszących okulary (kolejność w tej
#tablicy musi odpowiednio zachować kolejność z wyjściowej tablicy)
osoby_z_okularami = zloczone_inner[zloczone_inner['Gl'] == True]
print('osoby z okularami:\n', osoby_z_okularami)

#stwórz tablice zawierającą imiona osób w wieku z przedziału [20, 30]

osoby_w_wieku = zloczone_outer['Name'][zloczone_outer['Age'] >= 20][zloczone_outer['Age'] <= 30]
print('osoby [20, 30]:\n', osoby_w_wieku)

#dodaj kolumnę z bmi dla wszystkich osób i wynik zapisz w tablicy (bmi = waga/(wzrost**2)
zloczone_outer['bmi'] = zloczone_outer['W']/(zloczone_outer['H']**2)
print(zloczone_outer)

#policz średni wiek i wyświetl na konsoli

zloczone_outer['Age'] = zloczone_outer['Age'].fillna(0)
sw = sum(zloczone_outer['Age'])/len(zloczone_outer)
print('średni wiek:', sw)

#policz osobno średnie bmi osób noszących i nienoszących okulary i wyświetl na konsoli.

print(zloczone_outer['bmi'])
zloczone_outer.loc[zloczone_outer['bmi'].isnull(), 'bmi'] = 0
sbmi1 = sum(zloczone_outer['bmi'][zloczone_outer['Gl'] == True])/len(zloczone_outer['bmi'][zloczone_outer['Gl'] == True])
print('średnie bmi osób w okularach:', sbmi1)
sbmi2 = sum(zloczone_outer['bmi'][zloczone_outer['Gl'] == False])/len(zloczone_outer['bmi'][zloczone_outer['Gl'] == False])
print('średnie bmi dlas osób bez okularów: ', sbmi2)

#policz osobno średni wiek osób noszących i nienoszących okulary i wyświetl na konsoli.
sw1 = sum(zloczone_outer['Age'][zloczone_outer['Gl'] == True])/len(zloczone_outer['Age'][zloczone_outer['Gl'] == True])
sw2 = sum(zloczone_outer['Age'][zloczone_outer['Gl'] == False])/len(zloczone_outer['Age'][zloczone_outer['Gl'] == False])
print('średni wiek osób noszących okulary:', sw1)
print('średni wiek osób nie noszących okularów:', sw2)
