# Faça um algoritmo que leia o preço de um protudo e mostre seu novo preço com 5% de desconto
preço = float(input('Digite o preço atual: R$:'))
porc = (preço*5)/100
desconto = preço - porc
print(f'Seu preço atual {preço:.2f} com 5% de desconto ficará R$:{desconto:.2f}')
