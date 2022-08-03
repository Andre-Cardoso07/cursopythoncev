# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# n -> numero
# .is para saber informações sobre o valor digitado.


n = input('Digite algo: ')
print("O tipo primitivo desse valor é: ", type(n))
print("Só tem espaços? ", n.isspace())
print("É um número? ", n.isnumeric())
print("É alfabético? ", n.isalpha())
print("É alfanumérico? ", n.isalnum())
print("Está em maiúsculas? ", n.isupper())
print("Está em minúsculas? ", n.islower())
print("É um titulo ou está capitalizado? ", n.istitle())
print("É um número decimal? ", n.isdecimal())
print("É um digito?", n.isdigit())
print("É um caracter ASCII? ", n.isascii())

# print('é um numero? {}'.format(n.isnumeric())) essa é outra forma de fazer o mesmo que acima
