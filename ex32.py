ano = str(input('qual ano deseja descobrir :'))
n = 0
n_ano = []
while n <= len(ano) - 1 :
    if n >= 2:
        n_ano.append(ano[n])
    n += 1
a = int(n_ano[0] + n_ano[1])
v = (a / 4)
print (type(v))
