"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

input_numero = input('Digite um número inteiro: ')
try:
    numero = int(input_numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
except ValueError:
    print(f'O valor {input_numero} não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_digitada = input('Digite a hora (0-23): ')
try:
    hora = int(hora_digitada)
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
    else:
        print('Hora inválida. Digite um número entre 0 e 23.')
except:
    print(f'O valor {hora_digitada} não é um número inteiro.')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""


nome_usuario = input('digite seu primeiro nome:')
if len(nome_usuario) <= 4:
    print('seu nome é curto')
elif len(nome_usuario) <= 6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')