salario = float(input("Digite o seu salario: "))

if (salario >=0) and (salario <=400):
   diferença = salario * 0.15
   total = diferença + salario
   print("Seu novo salario é: ", total)
   print("Teve um aumento de: ", diferença)
   print("Indice de aumento: 15%")

elif (salario >=400.01) and (salario <=800):
   diferença = salario * 0.12
   total = diferença + salario
   print("Seu novo salario é: ", total)
   print("Teve um aumento de: ", diferença)
   print("Indice de aumento: 12%")

elif (salario >=800.01) and (salario <=1200):
   diferença = salario * 0.10
   total = diferença + salario
   print("Seu novo salario é: ", total)
   print("Teve um aumento de: ", diferença)
   print("Indice de aumento: 10%")

elif (salario >=1200.01) and (salario <=2000):
   diferença = salario * 0.07
   total = diferença+ salario
   print("Seu novo salario é: ", total)
   print("Teve um aumento de: ", diferença)
   print("Indice de aumento: 7%")

elif salario >2000:
   diferença = salario * 0.04
   total = diferença + salario
   print("Seu novo salario é: ", total)
   print("Teve um aumento de: ", diferença)
   print("Indice de aumento: 4%")