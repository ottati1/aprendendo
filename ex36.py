numero = int(input('digite um número: '))
n = 0
while n <= 2:
    if n == 0:
        print('converção para binario')
        per = str(input('sim / não :')).lower()
        if per in 'sim s':
            print('deu certo')
            n = 2
    if n == 1:
        print('converção para octal')
        per = str(input('sim / não')).lower()
    n += 1