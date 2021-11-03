import forca
import adivinhacao

def escolher_jogo():

    print("**************************")
    print("Escolha o seu jogo")
    print("**************************")

    print("(1) Adivinhação | (2) Forca")

    jogo = int(input("Qual o jogo? "))

    if jogo == 1:
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif jogo == 2:
        print("Jogando Forca")
        forca.jogar()

if __name__ == "__main__":
    escolher_jogo()