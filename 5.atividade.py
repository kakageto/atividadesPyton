import os
os.system("cls || clear")
print("""
_______codigo_________resultado_______
          
          1-          continuar
          2-          mensagem
          3-            sair
    
    
""")
while True:
 
    codigo=int(input("digite um numero: "))
    if codigo==3:
        print()
        print("sair")
        break
    
    elif codigo==2:
        print()
        print("matheus é gay")

    elif codigo==1:
        print()
        print("continuar")

    else:
        print("codigo invalido")


