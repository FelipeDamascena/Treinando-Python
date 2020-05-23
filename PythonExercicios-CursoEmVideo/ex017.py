# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
cos = float(input('Digite o comprimeto do cateto oposto: '))
sen = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(cos, sen)
print(f'Com os valores do cateto oposto {cos:.2f} e do cateto adjacente {sen:.2f} a hipotenusa é {hi:.2f}')
