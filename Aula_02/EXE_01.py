distancia = float(input("informe a qtde de KM: "))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print("Total a pagar: ", preco)