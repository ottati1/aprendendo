some = 0
for c in range(0, 500, 3):
    if c % 2 != 0:
        some += c
print('A soma de todos os valores é {}'.format(some))