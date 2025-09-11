import random
sorteio = random.randint(1, 5)
n = 0
t = 0
while n <= 0:
    t += 1
    chute = int(input('Chute um número:'))
    if chute == sorteio:
        n += 1
        print('você acertou com {} tentativas'.format(t))
    
    else:
        print('você rrou tente outra vez! ')
