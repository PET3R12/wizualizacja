import numpy as np
student = np.array(list(range(1, 41)))
wzrost = np.array([153, 154, 154, 155, 158, 159, 160, 161, 163, 164, 165, 165, 165,
                   166, 167, 167, 168, 168, 170, 170, 170, 171, 173, 174, 174, 174,
                   175, 175, 176, 171, 178, 178, 178, 179, 179, 179, 180, 180, 183, 185])

rozmiar_buta = np.array([5, 6, 6, 6, 5, 7, 6, 5, 6, 7, 7, 6, 7, 10, 9.5, 10, 10, 9,
                         10.5, 9.5, 8.5, 9, 10, 8, 10, 9, 12, 11, 9, 10, 11, 11, 12,
                         10.5, 11.5, 11, 13, 12, 12.5, 13])

print(wzrost.shape)
print(student.shape)
print(rozmiar_buta.shape)

#jaki jest ±rednie rozmiar buta?
srednia = sum(rozmiar_buta)/len(rozmiar_buta)
print(srednia)

#jaki jest maksymalnie wymieniony rozmiar buta?
maks = max(rozmiar_buta)
print(maks)

# jaki jest średni wzrost osób z maksymalnym rozmiarem buta?
osoby_z_tym_rozmiarem = np.array(wzrost[rozmiar_buta == maks])
sredni_wzrost = sum(osoby_z_tym_rozmiarem) / len(osoby_z_tym_rozmiarem)
print(sredni_wzrost)

#jaki jest najmniejszy wzrost osób z maksymalnym wymienionym rozmiarem buta?
print(min(osoby_z_tym_rozmiarem))

#jaki jest średni rozmiar buta u osób każdego wzrostu?
slownik = {}

for k in range(0, len(wzrost)):
    wz = wzrost[k]
    rozmiar = rozmiar_buta[k]
    if wz not in slownik:
        slownik[wz] = [rozmiar]
        slownik[wz].append(rozmiar)

for k in slownik:
    rozmiary = slownik[k]
    rozmiary = sum(rozmiary)/len(rozmiary)
    slownik[k] = rozmiary
print(slownik)

#jaki jest średni wzrost tych osób?
print(sum(slownik)/len(slownik))

#jaki jest najmniejszy i największy wzrost u osób z rozmiarem buta 10?
print([max(element) for element in np.array([wzrost[rozmiar_buta == 10]])])
print([min(element) for element in np.array([wzrost[rozmiar_buta == 10]])])

print(max(rozmiar_buta))
print(min(rozmiar_buta))

#stwórz tablice zawieraj¡ca europejski rozmiar butów dla tych osób.
def europejski(amerykanski):
    tabela = {
        5: 36,
        6: 37,
        7: 38.5,
        8: 40.5,
        8.5: 41,
        9: 42,
        9.5: 42.5,
        10: 43,
        10.5: 44,
        11: 44.5,
        11.5: 45,
        12: 46,
        12.5: 46.5,
        13: 47
    }
    eu = tabela[amerykanski]
    return eu
rozmiar_europejski = np.array([europejski(element) for element in rozmiar_buta])
print(rozmiar_europejski)



