import os
os.system("cls || clear")

senha_cadastrada="1234"

while True:
    senha=str(input("digite a sua senha: "))

    if senha == senha_cadastrada:
        print("bem vindo")
        break

    else:
        print("senha invalida")