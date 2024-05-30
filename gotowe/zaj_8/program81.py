import numpy as np
my_array = np.array([[1, 2, 3, 0], [5, 6, 7, 0]], int)
print(my_array.shape)
my_array = my_array.reshape(1, 8) #zmiana kształtu areja
print(my_array.shape)

my_array = my_array + 3 #dodanie 3 do każdego elementu
print(my_array)
my_array = my_array * 2 #zwielokrotnienie
print(my_array)

for linia in my_array: #zmiana elementów % 6 == 2 na 0
    for index in range(my_array.shape[1]):
        if linia[index] % 6 == 2:
            linia[index] = 0
print(my_array[:])

def change(A, x): #funkcja zmieniające elementy  == 0 na x
    a1 = np.array(A[:])
    for linia in a1:
        for index in range(len(linia)):
            if linia[index] == 0:
                linia[index] = x
    return a1
print(change(my_array, 5))
print(my_array)
