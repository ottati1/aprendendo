import random
nomes = ['victor', 'nath', 'guto', 'nicole', 'julio']
quantidade_nomes = len(nomes)
nova_lista = [ ]
n = 0
while n < quantidade_nomes:
    sorteio = random.randint(0, quantidade_nomes - 1) #sorteia o nome
    nome_de_sorteio = nomes[sorteio] #puxa o nome da lista
   
    if nome_de_sorteio not in nova_lista:
        nova_lista.append(nome_de_sorteio) #adiciona o nome na lista 
        n += 1
    #print('{}'.format(nomes[sorteio]))
   
print(nova_lista)