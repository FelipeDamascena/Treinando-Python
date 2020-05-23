## Faça um programa que leia o que foi escrito no teclado e mostre na tela seu tipo primitivo e todas as informações
a = input('Digite algo: ')
print('Seu tipo primitivo é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em letra maiuscula?', a.isupper())
print('Está em letra minuscula?', a.islower())
print('Está capitalizada? ', a.istitle())


