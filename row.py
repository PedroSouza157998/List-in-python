import os
r=""
values=[]
while True:
    print("="*50)
    print("ESCOLHA OQUE DESEJA FAZER")
    print("="*50)
    print("[1]Se quiser adicionar à lista")
    print("[2]Se quiser remover da lista")
    print("[3]Se quiser mostrar a lista")
    print("[0]Para sair")
    r=input()

    if r=="0":
        exit()

    if r == "1": 
        values = []
        x = True
        while x:
            values.append(input("Digite o valor que você deseja adicionar: "))
            sequenc=input("deseja continuar(S/N)? ")
            if sequenc.upper() == "S": x=True
            else: x=False
            os.system("cls")

        with open('dice.txt', 'a') as file:
            for i in values:
                file.write(str(i) + "\n")

    if r=="2":
        with open('dice.txt', 'r') as file:
            values=[]
            for i in file:
                values.append(i)
            print(values)
            x=input("qual valor deseja apagar: ")
            q = 0
            for i in values:
                if i == x+"\n":
                    del(values[q])
                q +=1
        print(values)
        with open('dice.txt', 'w') as file:
            for i in values:
                file.write(str(i))

    if r=="3":
        os.system("cls")
        with open('dice.txt', 'r') as file:
            x=1
            for i in file:
                print(x ,". ", i)
                x=x+1