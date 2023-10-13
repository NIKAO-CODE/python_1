import random

def jogar():
    imprime_mensagem_de_abertura()

    numero_secreto = define_numero_secreto()
    
    pontos = 1000

    nivel = define_nivel()
    
    total_de_tentativas = define_total_de_tentativas(nivel)


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 10: ")
        print("Você digitou {}".format(chute_str))
        chute = int(chute_str)

        if(chute < 1 or chute > 10):
            print("Você deve digitar um número entre 1 e 10.")
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


def imprime_mensagem_de_abertura():
    print(30 * '*')
    print("Bem vindo ao jogo de Advinhação")
    print(30 * '*')


def define_numero_secreto():
    numero_secreto = random.randint(1, 10)

    return numero_secreto


def define_nivel():
    print("""Qual nível de dificuldade?
        (1) Fácil (2) Médio (3) Difícil""")

    nivel = int(input("Defina o nível: "))

    return nivel


def define_total_de_tentativas(nivel):
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    
    return total_de_tentativas

    

if(__name__ == "__main__"):
    jogar()
