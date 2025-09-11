nome = str(input('Digite o nome: '))#.strip()
print(nome.lower()) #minusculo
print(nome.upper()) #maiusculo
dividido = nome.split()
n = 0
calculo = 0
print(dividido)
while n < len(dividido):
    numero = len(dividido[n])
    n += 1
    calculo += numero
print(calculo) # quantas letras tem ao todo
primeiro_nome = len(dividido[0])
print('o peimeiro nome tem {} letras'.format(primeiro_nome))