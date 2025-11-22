"""  
Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo 
seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo 
usuário.     """

i = 1
maior_numero = 0
menor_numero = 0
referencia_inicio = 1
            
print("Esse programa só para ao informar um número negativo")
            
while i != 0:
    numero = float(input("Digite um número: "))
    if numero >=0:
        if referencia_inicio == 1:
            maior_numero = numero
            menor_numero = numero
            referencia_inicio = 0
        
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero   
    else:
        i = 0
        print(f"Menor número positivo digitado: {menor_numero} \n Maior número positivo digitado: {maior_numero}")
    
    
          
        
                