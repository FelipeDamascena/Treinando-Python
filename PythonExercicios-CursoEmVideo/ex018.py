#faça um programa que leia um valor do angulo qualquer e mostre na tela o valor do seno
#cosseno e tangente
import math
ang = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(ang))
print(f'O seno do angulo de {ang} é: {seno:.2f}')
cosseno = math.cos(math.radians(ang))
print(f'O cosseno do angulo de {ang} é: {cosseno:.2f}')
tangente = math.tan(math.radians(ang))
print(f'A tangente do angulo de {ang} é: {tangente:.2f}')


