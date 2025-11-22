""" Elaborar um programa que efetue a leitura de 10 valores numéricos e apresente no final o total do 
somatório e a média aritmética dos valores lidos.     """

i = 1
soma = 0
media = 0

while i < 11:
    valor = int(input("Digite um número: "))
    soma += valor
    media = soma / i
    i += 1
    
print(f"Soma dos valores: {soma} \n Média aritmética: {media}")    
