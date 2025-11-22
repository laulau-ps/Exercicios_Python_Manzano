"""  Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer. """

numero = int(input("Digite o número a ser multiplicado: "))

for i in range(1,11):
    print(f"{numero} * {i} = ", numero * i)

