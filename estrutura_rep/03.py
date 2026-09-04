n = int((input("Digite um número: ")))

cont = 1
soma = 0

while cont <= n:
    soma += cont
    print(f"Somando {cont} ao total, que agora é {soma}")
    cont += 1 
    print(f"Agora cont é {cont}")

print(f"O resultado da soma é: {soma}")