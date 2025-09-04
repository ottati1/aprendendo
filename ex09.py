n = int(input('Digite um número para ter sua taboada'))
taboada = 0
print('='*20)
while taboada <= 10:
    
    print('{:>6} x {} = {}'.format(n, taboada, n*taboada))
    taboada += 1
print('='*20)