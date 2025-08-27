n = input('digite algo: ')
print(type(n))
numero = n.isnumeric()
if numero == True:
    print('{:^5} é um número'.format(n))
else:
    print('{:^5} não é um número'.format(n))
letra = n.isalpha()
if letra == True:
    print('{:^5} é uma letra'.format(n))
else:
    print('{:^5} não é uma letra'.format(n))
maiusculo = n.isupper()
if maiusculo == True:
    print('{:^5} é maiusculo'.format(n))    
else:
    print('{:^5} não é maiusculo'.format(n))