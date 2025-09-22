numero = int(input('digite um número: '))
def conversão(a):
    n = 0
    while n <= 2:
        if n == 0:
            print('converção para binario')
            per = str(input('sim / não :')).lower()
            if per in 'sim s':
                print('deu certo')
                n = 2
                return 'b'
        if n == 1:
            print('converção para octal')
            per = str(input('sim / não ')).lower()
            if per in 'sim s':
                n = 2
                return 'o'
        if n == 2:
            print('converção para hexadecimal :')
            per = str(input('sim / não' )).lower
            if per in 'sim s':
                print('deu certo 3')
                
                
            
resultado = conversão(numero)
print(resultado)