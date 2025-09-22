def reta(a, b):
    if a > b:
        v.append('1')
    
n = 0
lista_retas = []
while n <= 2:
    numero = int(input('Digite o valor da {} reta: '.format(n + 1)))
    lista_retas.append(numero)
    n += 1
v = []
n1 = lista_retas[0] + lista_retas[1]
reta(n1, lista_retas[2])
n2 = lista_retas[1] + lista_retas[2]
reta(n2, lista_retas[0])
n3 = lista_retas[2] + lista_retas[0]
reta(n3, lista_retas[1])
conta = len(v)
if conta >= 3:
    print('é possivel fazer um tirangulo com os números apresntados ')
else:
    print('com os npumeros apresntados não é possivel fazer um triangulo')
    