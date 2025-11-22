""" Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.  """

i = 1
somatoria = 0

while i <= 500:
    if i % 2 == 0:
       somatoria += i
    i += 1    
    
print(somatoria)    