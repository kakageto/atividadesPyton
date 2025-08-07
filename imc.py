import os
os.system("cls || clear")
def classificacao_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"IMC calculado: {imc:.2f}")
    
    if imc <=18.5 and imc<=24.9:
        print("Classificação: Abaixo do peso")
    elif imc <=25 and imc <=29.9:
        print("Classificação: Peso normal")
    elif imc ==30:
        print("Classificação: Sobrepeso")
    elif imc >40:
        print("Classificação: Obesidade")

classificacao_imc(60, 1.60)