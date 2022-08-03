# Operadores Aritmeticos
  # + = soma ou adição
  # - = subtração
  # * = multiplicação
  # / = divisão 
  # ** = potenciação
  # // = divisão inteira
  # % = resto da divisão ou módulo
  # Para fazer a Raiz quadrada, basta eu fazer a potenciação por (1/2) e (1/3) para a raiz cúbica.

# Ordem de Precedência 
  # 1. () parenteses
  # 2. ** potenciação
  # 3. * / // % multiplicação, divisão, divisão inteira e módulo. (resolve quem aparecer primeiro)
  # 4. + - soma e subtração

# Truquinho de Python
  # com o .format() eu posso fazer algumas modificações na forma que eu quero que apareça na tela, por exemplo:
  # print('Prazer em te conhecer {:10}!'.format('João')) irá aparecer assim: "Prazer em te conhecer João      !"
  # se eu quiser posso também formatar com caracteres especiais, por exemplo: {:=^10} vai ficar assim: "Prazer em te conhecer ===João==="
  # Posso também fazer o alinhamento usando o caractere <, > ou ^ (esquerda, direita ou centralizado)
  # print('prazer em te conhecer {:*^10}!'.format('João'))
  # print('prazer em te conhecer {:*>10}!'.format('João'))
  # print('prazer em te conhecer {:*<10}!'.format('João'))

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisaointeira = n1 // n2
resto = n1 % n2

print("A soma de {} e {} vale {}".format(n1, n2, soma))
print("A subtração de {} e {} vale {}".format(n1, n2, subtracao))
print("A multiplicação de {} e {} vale {}".format(n1, n2, multiplicacao))
print("A divisao de {} e {} vale {}".format(n1, n2, divisao))
print("A potencia de {} e {} vale {}".format(n1, n2, potencia))
print("A divisão inteira de {} e {} vale {}".format(n1, n2, divisaointeira))
print("O resto de {} e {} vale {}".format(n1, n2, resto))

