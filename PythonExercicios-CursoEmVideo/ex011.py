# Faça um programa que leia a altura e a largura de uma parede em metros
# Calcule a area e a qunatidade de tinta necessária para pintala
# Sabendo que para cada litro de tinta pinta uma area 2m²
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area}m²')
tinta = area / 2
print(f"A quantidade de tinta que você vai precisar para pintar a parede é de {tinta}l")
