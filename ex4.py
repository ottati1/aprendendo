n = input('digite algo: ')
print(type(n))
#é um numero?
numero = n.isnumeric()
if numero == True:
    print('{:^5} é um número'.format(n))
else:
    print('{:^5} não é um número'.format(n))
#é uma letra?
letra = n.isalpha()
if letra == True:
    print('{:^5} é uma letra'.format(n))
else:
    print('{:^5} não é uma letra'.format(n))
#esta em maiusculo
maiusculo = n.isupper()
if maiusculo == True:
    print('{:^5} é maiusculo'.format(n))    
else:
    print('{:^5} não é maiusculo'.format(n))
#é minusculos
minusculos = n.islower()
if minusculos == True:
    print('{:^5} é minusculo'.format(n))
else:
    print('{:^5} não é minusculo'.format(n))
#é printavel
printavel = n.isprintable()
if printavel == True:
    print('{:^5} é printavel'.format(n))
else:
    print('{:^5} não é printavel')
#é letra e numero
alsum = n.isalnum()
if alsum == True:
    print('{:^5} Tem letra e nùmero'.format(n))
else:
    print('{:^5} não tem letra e numero'.format(n))