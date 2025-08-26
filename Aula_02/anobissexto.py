# faz a leitura de um usuario e armazena na variavel ano
ano = int(input("digite o ano: "))

# verifica se o ano é divisivel por 400 ou 4 e não divisivel por 100
if (ano % 400 == 0 ) or (ano % 4 == 0 and not (ano % 100 == 0 )):
    print("Bissexto")
else:
    print("Não é bissexto")