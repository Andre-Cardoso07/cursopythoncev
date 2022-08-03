# Crie um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


diasalugados = int(input('Quantos dias você alugou o carro? '))
kmrodados = float(input('Quantos km rodados? '))
valorkm = 0.15
valorcarro = 60

print(
    f'O total a pagar é de R${(diasalugados * valorcarro) + (kmrodados * valorkm):.2f}')
