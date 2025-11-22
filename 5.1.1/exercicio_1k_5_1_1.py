"""  Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha, 
banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do 
nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar 
calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor 
total acumulado da área residencial.    """

i = 1
soma_area = 0

while i != 0:
    nome_comodo = input("Digite o nome do cômodo: ")
    largura_comodo = float(input(f"Digite a largura do(a) {nome_comodo}: "))
    comprimento_comodo = float(input(f"Digite a comprimento do(a) {nome_comodo}: "))

    area_comodo = largura_comodo * comprimento_comodo
    soma_area += area_comodo
    
    print(f"A área do(a) {nome_comodo} é: {area_comodo:.2f}m²")
    
    pergunta = input("Deseja adicionar um novo cômodo? (S/N)")
    if pergunta == "s" or pergunta == "S":
        i+= 1
    else:
        i = 0
        print(f"A soma da área de todos os cômodos é de: {soma_area:.2f}m²")
            
    