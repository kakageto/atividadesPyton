import os
os.system("cls || clear")
soma=0
while True:
   
    num=int(input("digite um numero: "))
    if num ==0:
        print(f"zero inserido, soma total: {soma}")
        break

    else:
        soma+=num