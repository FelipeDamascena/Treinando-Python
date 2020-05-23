# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
n = float(input('Digite um numero: '))
n2 = trunc(n)
print(f'Seu numero {n} na porção inteira é {n2}')
