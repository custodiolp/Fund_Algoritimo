cod = float(input("Digite o código: "))

classi = ""

if cod == 1:
    classi = "Alimento não perecivel"

elif cod == 2 or 3 or 4:
    classi = "Alimento perecivel"

elif cod == 5 or 6:
    classi = "Vestuario"

elif cod == 7:
    classi = "Higiene pessoal"

elif cod >= 8 and cod <= 15:
    classi = "Limpeza e utensilios domesticos"

else:
    classi = "invalido"

print({classi})