km = int(input('quantos km vai viajar: '))
cal1 = km * 0.50
cal2 = km * 0.45
if km <= 200:
    print('Voce gastara R$0,50 por km sendo o total de R${}'.format(cal1))
else:
    print('Voce gastara R$0,45 por km sendo o total de R${}'.format(cal2))