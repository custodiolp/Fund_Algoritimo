nota_1 = float(input("informe a primeira nota: "))
nota_2 = float(input("informe a segunda nota: "))

media_final = (nota_1 + nota_2) / 2

if media_final == 10:
    print("aprovado com distinção!")
elif media_final >= 5:
    print("aprovado!")
else:
    print("reprovado")