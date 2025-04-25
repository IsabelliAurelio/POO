i = int(input("Qual a sua idade: "))
b = bool(input("Tem cnh(caso não, deixe vazio): "))
if i >= 18 and b == True:
    print("\033[1;35m Pode continuar \033[m")
else:
    print("\033[1;31m Nao pode continuar \033[m")