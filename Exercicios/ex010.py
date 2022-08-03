# Crie um programa que leia quantos reais a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere que 1 dólar é equivalente a 3,27 reais. US$1 = R$3,27

carteira = float(input('Quantos reais você tem na carteira? R$'))
dolar = carteira/3.27
print('Você pode comprar US${:.2f} dólares'.format(dolar))


# carteira = float(input('Qual o valor em Reais que você possui na carteira? R$'))
# dolaremreal = 3.27
# # dolares = carteira/3.27
# # dolar = (carteira/dolaremreal)
# print (f'Você pode comprar {carteira/dolaremreal:.2f} dolares')
# print (f'Você pode comprar {dolar:.2f} dolares')
# print (f'Você pode comprar {dolares:.2f} dolares')
