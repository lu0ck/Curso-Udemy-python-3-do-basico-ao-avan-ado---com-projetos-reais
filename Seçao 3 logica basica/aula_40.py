while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite o operador (+, -, *, /): ')
    numero_2 = input('Digite outro número: ')
    if operador == '+':
        resultado = float(numero_1) + float(numero_2)
        print(f'{numero_1} + {numero_2} = {resultado}')
    elif operador == '-':
        resultado = float(numero_1) - float(numero_2)
        print(f'{numero_1} - {numero_2} = {resultado}')
    elif operador == '*':
        resultado = float(numero_1) * float(numero_2)
        print(f'{numero_1} * {numero_2} = {resultado}')
    elif operador == '/':
        if float(numero_2) == 0:
            print('Não é possível dividir por zero.')
        else:
            resultado = float(numero_1) / float(numero_2)
            print(f'{numero_1} / {numero_2} = {resultado}')
