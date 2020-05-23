# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
alugaD = int(input('Quantos dias você alugou o carro? '))
alugaK = float(input('Quantos Quilometros você rodou? '))
alugaV = float((alugaD * 60) + (alugaK * 0.15))
print(f'O total a pagar é R$:{alugaV:.2f}')
