# Crie um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# n = int(input('Digite um número qualquer e veja a sua tabuada'))
# print('a tabuada de {} é:\n {} x 1 = {}\n {} x 2 = {}\n {} x 3 = {}\n {} x 4 = {}\n {} x 5 = {}\n {} x 6 = {}\n {} x 7 = {}\n {} x 8 = {}\n {} x 9 = {}\n {} x 10 = {}\n'.format(n, n, n*1, n, n*2, n, n*3, n, n*4, n, n*5, n, n*6, n, n*7, n, n*8, n, n*9, n, n*10))
# # Esse é o modo arcaico de fazer e bem manual

x = int(input('Digite um número inteiro para calculo da tabuada:'))
print('Sua tabuada é:')
print('-' * 12)
for e in range(1, 11):
    print(f'{x} x {e:2} = {x*e}')  # novo método para fazer a tabuada
print('-' * 12)
