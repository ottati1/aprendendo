ano = int(input('qual ano deseja descobrir :'))
b = ano % 4
a = ano % 400
if b == 0:
    print('é um ano bixesto')
elif a == 0:
    print('é um ano bixesto')


else:
    print('não é um ano bixesto')