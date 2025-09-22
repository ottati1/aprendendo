n1 = int(input('Digite um número :'))
n2 = int(input('Digite mais um :'))
if n1 > n2:
    print('o primeiro número {} é maior que o segundo número {}'.format(n1, n2))
elif n1 < n2:
    print('o primeiro número {} é menor que o segundo número {}'. format(n1, n2))
else:
    print('ambos os números são iguais {}'.format(n1))