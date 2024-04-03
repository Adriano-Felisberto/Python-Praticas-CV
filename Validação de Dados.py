sexo = str(input("Informe seu sexo:")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Sexo invalido pfv informe novamente: ")).strip().upper()[0]
print("Sexo registrado com sucesso")