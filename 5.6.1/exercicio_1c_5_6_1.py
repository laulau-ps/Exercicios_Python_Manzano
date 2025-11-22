"""  Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).  """

resultado = 0

for i in range(1,101):
    resultado += i

print(resultado)