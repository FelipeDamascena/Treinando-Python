# Faça um programa que mostre quanto alguem ganha e acrescente 15% ao seu salário
salario = float(input('Digite seu salario atual: R$:'))
porc = salario*15/100
nvsalario = salario + porc
print(f'seu salario R$:{salario:.2f} com 15% de aumento, seu novo salario sera: R$:{nvsalario:.2f}')
