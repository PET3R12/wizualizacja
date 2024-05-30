import numpy as np
panstwa = np.array(['China', 'Japan', 'Germany', 'USA', 'South Korea', 'India', 'Brazil', 'Mexico', 'Spain', 'Russia'])
rok1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94])
rok2014 = np.array([19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69])

#przyrost w produkcji
procenty = ((rok2014/rok1999)*100)
przyrost = [round((element - 100), 2) for element in procenty]
print(przyrost)

#najwięcej i najmniej
print(panstwa[min(rok1999) == rok1999])
print(panstwa[min(rok2014) == rok2014])
print(panstwa[max(rok1999) == rok1999])
print(panstwa[max(rok2014) == rok2014])

#Państwa, które wyprodukowały w 2014 mniej samochodów niż w 1999
print(panstwa[rok1999 > rok2014])


