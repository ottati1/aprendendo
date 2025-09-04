import random
nome = ['victor', 'nicole', 'nath', 'guto']
numero = len(nome)
sorte = random.randint(0, numero)
print('quem ira apresenta o trabalho é o {}'.format(nome[sorte-1]))