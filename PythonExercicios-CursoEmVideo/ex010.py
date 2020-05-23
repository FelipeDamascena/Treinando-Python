# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
din = float(input('Quanto dinheiro você tem na carteira: R$:'))
dolar = din / 5.54
euro = din / 5.97
print(f'Com o valor de R$:{din:.2f} você pode comprar em dolar US$:{dolar:.2f} e em euro E$:{euro:.2f}')
