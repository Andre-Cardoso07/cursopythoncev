# Crie um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioatual = float(input('Qual o seu salário atual? R$'))
aumento = int(input('Qual a porcentagem de aumento do salário? '))
novosalario = salarioatual + (salarioatual * aumento/100)
print(
    f'O seu salário atual é R${salarioatual:.2f} e terá um aumento de {aumento}%, portanto será agora R${novosalario:.2f} Parabéns!')
