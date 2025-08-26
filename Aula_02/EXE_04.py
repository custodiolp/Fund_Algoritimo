numero_1 = float(input("informe o primeiro numero: "))
numero_2 = float(input("informe o segundo numero: "))
operacao = (input("informe a operação que deseja usar: "))

if operacao == "+":
    resultado = numero_1 + numero_2 
    print("Total: ", resultado)
elif operacao == "-":
    resultado = numero_1 - numero_2
    print("Total: ", resultado)
elif operacao == "*":
    resultado = numero_1 * numero_2
    print("Total: ", resultado)
elif operacao == "/":
    resultado = numero_1 / numero_2
    print("Total: ", resultado)
else:
    print("Operação não reconhecida")


