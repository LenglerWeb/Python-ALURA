import random

def jogar():

    print("********************************")
    print("Bem-vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,11)
    tentativas = 0
    pontos = 10

    print(numero_secreto)

    print("Qual o nível de dificuldade?")
    print("Fácil (1) | Médio (2) | Difícil (3)")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print("Tentativa", rodada, "de", tentativas)
        #print("Tentativa {} de {}".format(rodada, tentativas))

        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if chute < 1 or chute > 10:
            print("Você deve digitar entre 1 e 10!")
            continue

        if acertou:
            print("Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            if maior:
                print("Você errou! Seu número é MAIOR que o número secreto.")
                if rodada == tentativas:
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif menor:
                print("Você errou! Seu número é MENOR que o número secreto.")
                if rodada == tentativas:
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

    print("Fim do Jogo")

if __name__ == "__main__":
    jogar()
