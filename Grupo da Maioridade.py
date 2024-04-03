for idd in range(0, 7):
    idd = int(input("qual o seu ao de nascimento: "))
    num = 2024 - idd
    lista = [num] 
    if num >= 18:
        print("vc é de maior {}".format(lista))
    elif num <= 18:
        print("vc é de menor {}".format(lista)) 
