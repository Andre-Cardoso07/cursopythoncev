# tipos primitivos e Saída de Dados
# int() para Numeros ou valores inteiros
# float() para Numeros ou valores reais
# str() para transformar em texto
# bool() para True (Verdadeiro) ou False (Falso) "Importante usar as iniciais maiusculas para True e False"

# print() para imprimir na tela
# input() para receber dados do usuario
# type() para verificar o tipo de dado
# len() para verificar o tamanho de um dado

# Metodo .is alguma coisa para saber se o dado é tal coisa:
  # .isnumeric() para verificar se é um numeros
  # .isalpha() para verificar se é uma letra
  # .isupper() para verificar se é uma letra maiuscula
  # .islower() para verificar se é uma letra minuscula
  # .istitle() para verificar se é uma letra maiuscula e minuscula
  # .isprintable() para verificar se é um caracter imprimivel
  # .isspace() para verificar se é um espaço
  # .isalphanumeric() para verificar se é um caracter alfanumerico
  # .isascii() para verificar se é um caracter ASCII
  # .isdecimal() para verificar se é um caracter decimal
  # .isdigit() para verificar se é um caracter digito
  # .isabs() para verificar se é um caracter absoluto

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
s = n1 + n2
# format() para formatar a saida
print("A soma de {} e {}  {}".format(n1, n2, s))
