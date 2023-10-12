import random

def jogar():

    print(30 * '*')
    print("Bem vindo ao jogo de Advinhação")
    print(30 * '*')

    numero_secreto = random.randint(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("""Qual nível de dificuldade?
        (1) Fácil (2) Médio (3) Difícil""")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou {}".format(chute_str))
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número maior que 0.")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O número secreto é menor.")
            elif(menor):
                print("Você errou! O número secreto é maior.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
