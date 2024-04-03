num = int(input("qual o numero da tabuada? "))
print("**************RESULTADO******************")
for cc in range(0, 11):
    tabu = num * cc
    print("{} x {}= {}".format(num, cc, tabu))