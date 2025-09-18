n = 0
listan = []
while n <= 2:
    numero = input('Digite um número')
    listan.append(numero)
    n += 1
n = 0
listan.sort()
print(listan)
print('o menor númro foi {}'.format(listan[0]))
print('o maior número foi {}'.format(listan[len(listan) -1]))