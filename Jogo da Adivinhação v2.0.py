import random

print("Ola eu sou o seu computador")
print("Vamos jogar o jogo da adivinhação")
print("As regras são o seguinte:")
print("Só será permitido a escolha de 1 ate 10")
print("Se você acertar o meu número você ganhar ")
print("caso você erre perdeu")
print("Eu já escolhi o meu número")
computador = random.randint(1, 10)


acertou = False
cont = 0
while not acertou:
    esco = int(input("Escolha um número de 1 a 10:"))
    cont = cont + 1

    if esco != computador:
        print("O seu palpite foi de {}".format(esco))
        print("O número do computador é:")
        if esco < computador:
            print("O número é maior")
        if esco > computador:
            print("O número é menor")
       
    
    if esco == computador:
        print("você ganhou")
        print("computador escolheu {} e o jogador {}".format(esco, computador))
        print("para vencer forão necessarios {} jogadas".format(cont))
        acertou = True
print("Desligando o sistema....")
