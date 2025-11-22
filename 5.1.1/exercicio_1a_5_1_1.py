""" Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer. """

i = 1

numero = int(input("Digite um número: "))

while i <= 10:
    multiplicacao = numero * i
    print(f"{numero} * {i} = {multiplicacao}")
    i += 1