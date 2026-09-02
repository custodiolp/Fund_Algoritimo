n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(f"A ordem decrescente é: {n1:.2f}, {n2:.2f}, {n3:.2f}")

elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f"A ordem decrescente é: {n2:.2f}, {n1:.2f}, {n3:.2f}")

elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f"A ordem decrescente é: {n3:.2f}, {n1:.2f}, {n2:.2f}")

elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f"A ordem decrescente é: {n1:.2f}, {n3:.2f}, {n2:.2f}")

elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f"A ordem decrescente é: {n2:.2f}, {n3:.2f}, {n1:.2f}")

elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f"A ordem decrescente é: {n3:.2f}, {n2:.2f}, {n1:.2f}")

else:
    print("erro")


