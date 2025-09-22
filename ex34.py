salario = float(input('Qual é o valor do salario'))
if salario >= 1250:
    novo_salario = (salario / 100) * 110
    print('o novo salario é {}'.format(novo_salario))
else:
    novo_salario = (salario / 100) * 115
    print('o novo salario é {}'.format(novo_salario))