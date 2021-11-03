import random





def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto não enforcou E não acertou(False)
    while not enforcou and not acertou:

        chute = pede_chute(letras_acertadas)

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            #print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta) - erros))
            desenha_forca(erros)

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)



    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("       GAME-OVER")


# Funções
def imprime_mensagem_abertura():
    print("**************************")
    print("Bem-vindo ao jogo da Forca")
    print("**************************")

def carrega_palavra_secreta():
    arquivo = open("palavra_secreta.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute(letras_acertadas):
    chute = input("Qual letra? {} : ".format(letras_acertadas)).lower().strip()
    # print("Ainda faltam acertar {} letras".format(letras_faltando))
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra.lower():
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print(" ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("  Parabéns, você ganhou!")
    print(" ")

def imprime_mensagem_perdedor(palavra_secreta):
    print(" ")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \    ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXXX     XXXX   |      ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print(" ")




if __name__ == "__main__":
    jogar()