n = int(input("Digite um número: "))


cont = 0
soma = 0

while cont < n:
    x = int(input("Digite um valor: "))
    soma += x # soma os valores digitados
    cont += 1 # contador de repetições do while

print(f"A soma dos valores digitados é: {soma}")