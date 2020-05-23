# Faça um programa que leia uma temperatura em graus celsius e retorne em fahrenheit
# celsius = float(input('Digite aqui a temperatura em °C: '))
# faren = (celsius*(9 / 5)) + 32
# print(f'Sua temperatura {celsius:.1f}°C em fahrenheint é {faren:.1f}°F!')

# Lendo uma temperatura em fahrenheit e convertendo em Celsius
faren = float(input('Informe a temperatura em °F: '))
celsius = (faren - 32) * 5/9
print(f'Sua temperatura {faren:.1f}°F em Celsius é {celsius:.1f}°C!')
