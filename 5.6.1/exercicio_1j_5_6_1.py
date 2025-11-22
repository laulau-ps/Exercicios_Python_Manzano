"""  Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 
10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O 
programa deve apresentar os valores das duas temperaturas. A fórmula de conversão 
é celsius * 9 / 5 + 32 sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. """

conversao = 0

for i in range(10, 101, 10):
    conversao = i * 9 / 5 + 32
    print(f"{i}ºC = {conversao}ºF")