numero = int(input('digite um número: '))
def conversão(a):
    n = 0
    while n <= 2:
        if n == 0:
            print('converção para binario')
            per = str(input('sim / não :')).lower()
            if per in ['sim', 's']:
                print('deu certo')
                n = 2
                return 'b'
        if n == 1:
            print('converção para octal')
            per = str(input('sim / não ')).lower()
            if per in ['sim', 's']:
                n = 2
                return 'o'
        if n == 2:
            print('converção para hexadecimal :')
            per = str(input('sim / não' )).lower()
            if per in ['sim', 's']:
                n = 2
                return 'h'  
        n += 1              
            
resultado = conversão(numero)
if resultado == 'b':
    binario = bin(numero)[2:]
    print('Você escolheu binario')
    print('o número {} convertido é {}'.format(numero, binario))
if resultado == 'o':
    octal = oct(numero)[2:]
    print('Você escolheu octal:')
    print('o número {} convertido para octal é {}'.format(numero, octal ))
if resultado == 'h':
    hexadecimal = hex(numero)[2:]
    print('Você escolheu hexadecimal')
    print('O número {} convertido para hexadecimal é {}'.format(numero, hexadecimal))