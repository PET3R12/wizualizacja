f = open('txt.txt', 'r+', encoding='UTF-8')
s = f.read()
print(s)
print(type(s))
f.close()