algo = str(input('Digite algo: ')).lower()
ond_a = algo.find('a')
quantos_a = algo.count('a')
if ond_a >= 0: #função para descobrir onde esta o primeiro a e quantos tem
    print('O a foi encontrado primeiro na posição {}'.format(ond_a))
    print('exite {} a nesta frase!'.format(quantos_a))
n = 0
while n < len(algo):#função para descobrir a ultima letra
    função = algo[n]
    posição = 0
    if função == 'a':
        posição = n
    n += 1
print('o ultimo a esta na posição {}'.format(posição))