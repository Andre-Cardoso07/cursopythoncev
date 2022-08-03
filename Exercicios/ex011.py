# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Qual é a altura da parede em metros?'))
largura = float(input('Qual é a largura da parede em metros?'))
areaparede = altura * largura
print(
    f' A area da parede é {areaparede}m² e será necessária {areaparede/2}L de tinta para pintar essa parede.')
