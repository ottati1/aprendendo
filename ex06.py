# crie um programa que leia um numero mostre o seu dobro seu tiplo e raiz quadrada
from math import sqrt
n = float(input('Digite um número: '))
raiz = sqrt(n)
print('O número digitado foi {:^5}\n Seu dobro é {:^5} \n Seu triplo é{:^5} \n E sua raiz é {:^5}'.format(n, n*2, n*3, raiz))