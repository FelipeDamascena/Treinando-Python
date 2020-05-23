# Faça um programa que leia um valor em metros e o exiba convertido em centimetro e milimetro
medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'Sua medida {medida}\n'
      f'EM KILOMETROS {km}\n'
      f'EM HECTOMETRO {hm}\n'
      f'EM DECAMETRO {dam}\n'
      f'EM DENCIMETRO {dm}\n'
      f'EM CENTIMETRO {cm}\n'
      f'EM MILÍMETRO {mm}')
