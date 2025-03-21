import os
os.system("cls || clear")

while True:
    idade=int(input("digite a idade: "))
    if idade >=18 and idade <=60:
        print("Conteudo liberado")
        break

    else:
        print("idade invalida")