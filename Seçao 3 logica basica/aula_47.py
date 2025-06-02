"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

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