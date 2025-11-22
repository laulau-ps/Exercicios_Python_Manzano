"""   Apresentar os resultados das potências de 3, variando do expoente 0 até o expoente 15. Deve ser 
considerado que qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. Observe que 
neste exercício não pode ser utilizado o operador de exponenciação do portuguol (^).  """

potencia = 1

for i in range(16):
    print(f"3 ^ {i}: {potencia}")
    potencia *= 3
    
        