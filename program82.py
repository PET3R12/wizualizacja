#cw2
import numpy as np

a = np.array([[1, 1, 2], [2, 1, 0], [4, 1, 2]])
b = np.array([[2, 5, 7], [2, 8, 0], [4, 3, 1]])
print(a + b,'\n')
print(a * b,'\n')

#mnożenie macierzy a * b:
result = np.zeros((a.shape[0], b.shape[1]))
for i in range(a.shape[0]):
    for j in range(b.shape[1]):
        for k in range(a.shape[1]):
            result[i, j] += a[i, k] * b[k, j]
print("Wynik mnożenia macierzy a i b:")
print(result)
#za pomocą funkcji wbudowanych
print(np.dot(a, b))
#a do -1
print(np.linalg.matrix_power(a, -1), '\n')

#a do 5
print(np.linalg.matrix_power(a, 5), '\n')

#detB
print(np.linalg.det(b))

#b do -3
print(np.linalg.matrix_power(b, -3), '\n')

#zaokrąglenie
wynik = np.linalg.matrix_power(b, -3)
for linie in range(len(wynik)):
    for index in range(len(wynik[linie])):
        wynik[linie][index] = round(wynik[linie][index], 2)

print(wynik, '\n')

#zaokrąglenie funkcją
print(np.round(np.linalg.matrix_power(b, -3), 2),'\n')

c = np.array([[1], [2], [3]])
d = np.array([[1, 2, 3]])
#c*d
print(np.dot(c, d), '\n')

#d*c
print(np.dot(d, c), '\n')

e = np.array([[1, 5], [2, 1]])
f = np.array([[2, 1], [2, 8]])

#e/f
print(np.dot(e, np.linalg.matrix_power(f, -1)), '\n')
print(e/f, '\n')
print(e % f)



