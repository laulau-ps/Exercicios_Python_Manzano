""" h) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 
10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O 
programa deve apresentar os valores das duas temperaturas. A fórmula de conversão 
é F = 9C + 160 / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.    """

i = 10

while i <= 100:
    fahnrenheit = (9 * i + 160) / 5
    print(f"{i}ºC = {fahnrenheit}ºF")
    i += 10
