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

"""
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print('*')