""" Elaborar um programa que apresente os resultados da soma e da média aritmética dos valores 
pares situados na faixa numérica de 50 a 70.    """

i = 50
soma = 0
media = 0
contadora = 1

while i < 71:
    if i % 2 == 0:
        soma += i
        media = soma / contadora
        contadora += 1
    i += 1
    
print(f"Soma dos valores: {soma} \n Média aritmética: {media}")    
