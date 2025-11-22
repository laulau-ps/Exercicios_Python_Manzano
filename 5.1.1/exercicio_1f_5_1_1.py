""" Elaborar um programa que apresente como resultado o valor de uma potência de uma base qualquer elevada a um expoente qualquer, ou seja, de BE, em que B é o valor da base e E o valor do expoente. Observe que neste exercício não pode ser utilizado o operador de exponenciação do portuguol (^).  """

i = 0
potencia = 1

base = int(input("Informe a base da potência: "))
expoente = int(input("Informe a base da potência: "))

while i < expoente:
    potencia *= base
    i += 1
    
print(f"{base} ^ {expoente} = {potencia}")