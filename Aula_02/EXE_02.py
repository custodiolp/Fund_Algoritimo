tempo_gasto = int(input("Informe o tempo no gasto no telefone (em minutos): "))

if tempo_gasto >= 400:
    preco = tempo_gasto * 0.15
else:
    if tempo_gasto <= 200:
        preco = tempo_gasto * 0.20
    else:
        preco = tempo_gasto * 0.18

print("total a pagar: ", preco)
