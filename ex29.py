velocidade = int(input('Qual velucidade foi atingida: '))
if velocidade > 80:
    print('Você foi multado em R${}'.format((velocidade - 80) * 7))
else:
    print('você não atingiu a velocidade maxima parabéns')