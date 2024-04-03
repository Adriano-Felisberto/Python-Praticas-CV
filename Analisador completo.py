somaidd = 0
mediaidd = 0
maioriddhomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1, 5):
    print("----------PESSOA {}-----------".format(p))
    nome = str(input("Qual o nome dessa pessoa? "))
    idade = int(input("Quantos anos essa pessoa tem? "))
    sexo = str(input("Qual o sexo dessa pessoa?"))
    somaidd += idade
    if p == 1 and sexo in "mM":
        maioriddhomem = idade
        nomevelho = nome
    if sexo in "Mn" and idade > maioriddhomem:
        maioriddhomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
mediaidd = somaidd / 4
print("A media de idade é de {}".format(mediaidd))
print("O homem mas velho tem {} anos e se chama {}".format(maioriddhomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))