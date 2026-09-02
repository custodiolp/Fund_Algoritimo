AnoNasc = int(input("Digite seu ano de nascimento:"))
AnoAtual = int(input("Digite o ano atual:"))

idade = AnoAtual - AnoNasc
voto = ""
Trab = ""

if idade >= 16:
    voto = "Pode votar"
else:
    voto = "Não pode votar"

if idade > 18:
    Trab = "tem permissão para CNH"
else:
    Trab = "não tem permissão para CNH"

print(f"Sua idade é: {idade}. Você {voto} e {Trab}. ")
    