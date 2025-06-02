palavra_secreta = "python"
tentativas = 3

while True:
    if tentativas <= 0:
        print("Você perdeu todas as tentativas!")
        break

    chute = input(f"Digite a palavra secreta ({tentativas} tentativas restantes): ")

    if chute == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta.")
        break
    else:
        print("Palavra incorreta. Tente novamente.")
        tentativas -= 1