n = float(input('Digite o valor do salario do funcionairo?'))
p = int(input('quantos PORCENTO vai aumentar? '))
calc = (n/100) * (100 + p )
print('Com o aumeto de {}PORCENTO o salario sai de {} para {}'.format(p, n, calc))