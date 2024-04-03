fra = str(input("digite uma frase: ")).strip().upper()
pala = fra.split()
jun = "".join(pala)
inv = jun[::-1]
if inv == jun:
    print("temos um palidromo")
else:
    print("não é um palidromo")