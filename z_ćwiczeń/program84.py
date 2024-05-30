import numpy as np
imiona = np.array(['anna', 'zofia',
                   'sylwia', 'katarzyna', 'teresa',
                   'tomasz', 'cezary', 'zenon', 'filip',
                   'adrian'])
wiek = np.array([21, 40, 13, 31, 34, 14, 13, 28, 20, 15])
plec = np.array(['k', 'k', 'k', 'k', 'k', 'm', 'm', 'm', 'm', 'm'])
waga = np.array([65, 80, 64, 69, 74, 61, 66, 61, 69, 77])
wzrost = np.array([179, 179, 151, 177, 170, 157, 151, 153, 160, 160])
okulary = np.array(['nie', 'tak', 'nie', 'tak', 'nie', 'tak', 'nie', 'tak', 'nie', 'tak'])

#wypisz na konsoli imiona posortowane alfabetycznie
print(sorted(imiona))

#stwórz tablice przechowującą imiona osób noszących okulary (kolejności w tej
# tablicy muszą odpowiednio zachować kolejnoość z wyjściowej tablicy)
osoby_w_okularach = np.array([imiona[okulary == 'tak']])
print(osoby_w_okularach)

#stwórz tablice zawieraj¡ca imiona kobiet w wieku z przedziału lat [20, 30]
osoby_z_przedziału = np.array([imiona[(wiek >= 20) & (wiek <= 30)]])
print(osoby_z_przedziału)

#stwórz tablice zawierająca imiona osób o wadze z przedziału [60, 80], wzroście [160, 180] nienoszących okularów.
tablica = np.array([imiona[(waga >= 60) & (waga < 81) & (wzrost >= 160) & (wzrost < 181) & (okulary == 'nie')]])
print(tablica)

#policz bmi dla wszystkich osób i wynik zapisz w tablicy
bmi = np.array([waga/wzrost**2])
print(bmi)

#policz ±redni wiek i wy±wietl na konsoli imi¦ osoby najbli»ej ±redniej.
print(sum(wiek)/len(wiek))
srednia = sum(wiek)/len(wiek)
print(np.array(imiona[abs(wiek - srednia) == min(abs(wiek - srednia))]))
