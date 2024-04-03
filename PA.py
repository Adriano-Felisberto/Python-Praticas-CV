primeiro = int(input("informe o numero: "))
razão = int(input("informe a razão: "))
decimal = primeiro + (10 - 1) * razão
for cc in range(primeiro, decimal + razão, razão):
    print(cc)