# Crie um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


precoproduto = float(input('Qual é o valor do produto? R$ '))
desconto = int(input('Qual é o valor do desconto? '))
precoatual = precoproduto - (precoproduto * desconto / 100)
print(f'O preço do produto com desconto de {desconto}% é R${precoatual:.2f}')


# preco = float(input('Qual é o preço do produto?'))
# desconto = preco * 0.05
# precofinal = preco - desconto
# print(f'O preço final do produto é R${precofinal:.2f}')
