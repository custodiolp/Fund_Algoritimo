maior = 0

for i in range (1,7):
    while True:
        numero = int(input(f"Digite o {i}° numero: "))

        if numero >= 0:
         break

if numero > maior:
     maior = numero

print(f"O maior numero é: {maior}")