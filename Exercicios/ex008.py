# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# tamanhom = float(input('Qual é o valor em metros?'))
# centimetros = tamanhom * 100
# milimetros = tamanhom * 1000
# print('O valor {}m em centimetros é {}cm e em milimetros é {}mm'.format(tamanhom, centimetros, milimetros))

medida = float(input('Qual a medida em metros? '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'A medida: {medida}m em\n km é {km}km\n {medida}m em hm é {hm}hm\n {medida}m em dam é {dam}dam\n {medida}m em dm é {dm:.0f}dm\n {medida}m em cm é {cm:.0f}cm\n {medida}m em mm é {mm:.0f}mm')
