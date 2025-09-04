a = float(input('Qual é a altura: '))
largura = float(input('Qual é a largura: '))
print('Lembrando e cada 1 l de tinta pinta 2m²')
c = a * largura
print('{} * {} deu um total de {}² sendo nescessario {} para pintar'.format(a, largura, c, c/2))