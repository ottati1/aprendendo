numero = str(input('Digite um númeor: '))
n = 0
n_lista = []
while n < len(numero):#criar uma nova lista separando os numeros
    a = numero[n]
    n_lista.append(a)
    n += 1
n_lista.sort()
print(n_lista)
n = 0 
while n < len(n_lista):
    if n == 0:
        print('A Unidade é {}'.format(n_lista[n]))
    if n == 1:
        print('A Dezena é {}'.format(n_lista[n]))
    if n == 2:
        print('a Centena é {}'.format(n_lista[n]))
    if n == 3:
        print('O milhar é {}'.format(n_lista[n]))
           
    n += 1
    
    