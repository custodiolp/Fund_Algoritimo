# Exercicio para achar o valor no plano cartesiano

x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))

if x>0 and y>0:
    print("Valor no Q1")
elif x<0 and y>0:
    print("Valor no Q2")
elif x<0 and y<0:
    print("Valor no Q3")
elif x>0 and y<0:
    print("Valor no Q4")
elif x==0 and y==0:
    print("Valor no ponto de origem")
elif x==0 and not y==0:
    print("Valor no eixo X")
elif y==0 and not x==0:
    print("Valor no eixo Y")