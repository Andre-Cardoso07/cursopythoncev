# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input("Digite um numero: "))
# Variáveis sucessor e antecessor além da variável n
sucessor = n+1
antecessor = n-1
# assim com o .format() eu posso fazer algumas modificações na forma que eu quero que apareça na tela:
print("O sucessor de {} é {} e o antecessor é {}".format(n, n+1, n-1))
# ou assim com variáveis:
print("O sucessor de {} é {} e o antecessor é {}".format(n, sucessor, antecessor))
