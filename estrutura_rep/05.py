n = int(input("Digite o ultimo digito da contagem: "))

x = 0

while x <= n:
    if x % 2 == 0:
        print(x)
    x += 1