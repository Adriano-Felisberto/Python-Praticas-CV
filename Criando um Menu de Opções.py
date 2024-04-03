sair = False

num = int(input("escolha um numero: "))
num2 = int(input("escolha outro numero: "))

while not sair:

    print("******MENU******")
    print("""
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
    """)
    esco = int(input("Escolha alguma dessas opções: "))
    if esco == 1:
        soma = num + num2
        print("A soma de {} + {} = {}".format(num, num2, soma))
       
    if esco == 2:
        multi = num * num2
        print("A multiplicação de {} + {} = {}".format(num, num2, multi))
    if esco == 3:
        if num < num2:
            print("O numero {} é maior que {}".format(num2, num))
        elif num > num2:
            print("O numero {} é maior que {}".format(num, num2))
    if esco == 4:
        num = int(input("Qual o novo numero que vc deseja? "))
        num2 = int(input("Qual o  proximo novo numero? "))
    if esco == 5:
        sair = True
        print("Desligando o sistema...")
    else:
        print("Resposta invalida")
    