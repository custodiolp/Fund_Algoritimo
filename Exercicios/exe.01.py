origem = int(input("Digite o código de origem: "))
preco = float(input("Digite o preço do produto: "))

procedencia = ""

if origem == 1:
    procedencia = "Sul"

elif origem == 2:
    procedencia = "Norte"

elif origem == 3:
    procedencia = "Leste"

elif origem == 4:
    procedencia = "Oeste"

elif origem == 5 or origem == 6:
    procedencia = "Nordeste"

elif (origem >= 7) and (origem <= 9):
    procedencia = "Sudeste"

elif (origem >= 10) and (origem <= 20):
    procedencia = "Centro-Oeste"

elif (origem >= 25) and (origem <= 30):
    procedencia = "Nordeste"

else:
    procedencia = "Importado"

print(f"procedência: {procedencia} e o preço é: R${preco:.2f}")