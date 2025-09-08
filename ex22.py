nome = str(input('Digite o nome: ')).strip()
print(nome.lower()) #minusculo
print(nome.upper()) #maiusculo
dividido = nome.split()
n = 0
calculo = 0
while n < len(dividido):
    numero = len(dividido[n])
    print(numero)
    n += 1
    calculo += numero
print(calculo)