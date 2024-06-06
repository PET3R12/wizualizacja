from random import *
import numpy as np
import pandas as pd

#stwórz jednowymiarowa serie danych przechowuj¡c¡ liczby całkowite
calkowite = pd.Series([1, 2, 3, 4, 5])
print(calkowite)

#stwórz jednowymiarowa serie danych przechowującą stringi
stringi = pd.Series(['a', 'b', 'c', 'd', 'e'])
print(stringi)

#stwórz liste a następnie przekształć ją na serie
lista = list(range(2, 5))
seria = pd.Series(lista)
print(seria)

#przekształć jedna z serii stworzonych wcze±niej na list¦
l2 = list(stringi)
print(l2)

#stwórz jednowymiarową tablice (z biblioteki Numpy) i przekształć ją na serie
tablica = np.array(lista)
seria = pd.Series(tablica)
print(seria)

#przekształć jedną z serii stworzonych wcześniej na tablice (z biblioteki Numpy)
tablica = np.array(stringi)
print(tablica)

#wykonaj dodawanie, odejmowanie, mnożenie i dzielenie na dwóch dowolnych seriach danych z indeksami (nazwami). Jak to działa?
a = pd.Series(range(5))
b = pd.Series(range(5, 10))
print(a + b)
print(a-b)
print(a*b)
print(a/b)

#stwórz serie danych przechowującą 10 liczb losowych z przedziału [−10, 10]
#z krokiem 0.1 (jak to zrobić?), a następnie stwórz serie zawierającą liczby
#ujemne z wcześniej stworzonej serii w tym podpunkcie.
seria = pd.Series([randrange(-100, 100, 1) / 10 for _ in range(10)])
print(seria)

ujemne = pd.Series([element for element in seria if element < 0])
print(ujemne)

#(b) Przekształć liste, słownik, tablice Numpy oraz serie danych na ramki danych.
print('b)\n')

my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7], 'c': [3, 4, 8], 'd': [4, 10, 12]}
my_array = np.array([[1, 2, 5], [-2, 3, 3], [5, 2, 6]])
my_series = pd.Series([1, 32, -37, 91, 12, 11, -5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

ramka_lista = pd.DataFrame(my_list)
print('ramka z listy: \n', ramka_lista)
ramka_slownik = pd.DataFrame(my_dict)
print('ramka ze slownika: \n', ramka_slownik)
ramka_array = pd.DataFrame(my_array)
print('ramka z arraya: \n', ramka_array)
ramka_seria = pd.DataFrame(my_series, columns=['k1'])
print('ramka z serii: \n', ramka_seria)

#Przekształć odwrotnie (w taką samą listę, słownik, tablicę, oraz serie).
lista = ramka_lista[0].tolist()
print('Lista z ramki: ',lista)
slownik = ramka_slownik.to_dict(orient='list')
print('slownik z ramki: ', slownik)
arr = ramka_array.to_numpy()
print('array z ramki: \n', arr)

print('\nc)')
#(c) Stwórz ramkę danych i poćwicz na niej operacje związane z wyciąganiem
#elementów, sortowaniem w kolumnie, zmianą kształtu.

data = {'a': [1, -3, 2],
        'b': [2, 8, -5],
        'c': [4, 0.5, 7],
        'd': [5, 10, 3]}
df = pd.DataFrame(data, index=['l1', 'l2', 'l3'])
print(df)

#wyciąganie
print(df.at['l3', 'c'])

#sortowanie
print(df.sort_values(by=[element for element in df.keys()]))

#zmiana kształtu/transpozycja
print(df.T)


