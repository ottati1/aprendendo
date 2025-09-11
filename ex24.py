cidade = str(input('digite o nome da cidade: ')).lower()
dividir = cidade.split()
encontrar = dividir[0].find('santo')
e = encontrar
if e == 0:
    print('o nome da cidade comeca com o nom santo')
else:
    print('A cidade não começa com o nome santos')