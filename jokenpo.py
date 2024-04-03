import random
from time import sleep

#explicação das regras
print('''
COMPUTADOR: Vamos joga Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

#escolha do jogador 
esco = str(input('agora escolha entre pedra, papel e tesoura: ')).upper().strip()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

#listamento das opções do computador
pedra = "PEDRA"
tesoura = "TESOURA"
papel = "PAPEL"
lista = [pedra, papel, tesoura]

#escolha do computador
computador = random.choice(lista)

#resultados das partidas
if esco == computador:
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print("Empate. Vamos jogar novamente.")
    sleep(1.50)
if esco == "PEDRA" and computador == "TESOURA":
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print('JOGADOR ganhou')
    sleep(1.50)
if esco =="TESOURA" and computador == "PEDRA":
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print('COMPUTADOR ganhou')
    sleep(1.50)
if esco == "PAPEL" and computador == "PEDRA":
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print('JOGADOR ganhou')
    sleep(1.50)
if esco == "PEDRA" and computador == "PAPEL":
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print('COMPUTADOR ganhou')
    sleep(1.50)
if esco == "TESOURA" and computador == "PAPEL":
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print('JOGADOR ganhou')
    sleep(1.50)
if esco == "PAPEL" and computador == "TESOURA":
    print('JOGADOR escolheu {} e o computador {} então o resultado sera...'.format(esco, computador))
    sleep(1.50)
    print('computador ganhou')
    sleep(1.50)