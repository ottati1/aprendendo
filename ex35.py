valor_casa = int(input('Qual é o valor da casa ?'))
quantos_anos = int(input('Quantos Anos para pagar ? '))
quanto_ganha = int(input('qual é seu salario ? '))
meses = quantos_anos * 12
valor_para_aprovar = valor_casa / meses
porcentagem_salario = (quanto_ganha / 100) * 30
if porcentagem_salario > valor_para_aprovar:
    print('\033[42mEmprestimo APROVADO\033[m')
else:
    print('\033[41mEmprestimo NEGADO\033[m')
