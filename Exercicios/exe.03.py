sexo = int(input("Digite o sexo (1 para masculino e 2 para feminino): "))
altura = float(input("Digite a altura em metros: "))

peso_ideal = (72.7 * altura) - 58

if sexo == 1:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")