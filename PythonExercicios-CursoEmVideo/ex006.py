#Faça um programa que leia um numero e mostre seu dobro seu triplo e sua raiz quadrada
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = float(n ** (1/2))
print(f'Analisando o numero {n} seu dobro será {d}, seu triplo será {t} e sua raiz quadrada é {r:.2f}')
