opc = 0
x = 0
L = []
while opc != 5 and x != 10:
    print("")
    print("*=====================================================*")
    print("*=================== Calculadora =====================*")
    print("*=====================================================*")
    print("")
    print("*===================== OPÇÕES ========================*")
    print("*[1]- Soma\n*[2]- Subtração\n*[3]- Multiplicação\n*[4]- Divisão\n*[5]- Sair")
    opc = int(input("Digite uma opção: "))
    print("")
    if opc == 1:
        A = int(input("Digite um numero para A: "))
        B = int(input('Digite um numero para B: '))
        def soma_dados(A,B):
            soma = (A+B)
            return (soma)
        soma_final = soma_dados(A,B)
        print(F'A soma de {A} e {B} é igual a: {soma_final}')
        x = x + 1
        print(x)
        L.append(soma_final)
    if opc == 2:
        A = int(input("Digite um numero para A: "))
        B = int(input('Digite um numero para B: '))
        def subtração_dados(A,B):
            sub = (A-B)
            return (sub)
        subtração_final = subtração_dados(A,B)
        print(f'O resultado da subtração de {A} e {B} é igual a: {subtração_final}')
        x = x + 1
        print(x)
        L.append(subtração_final)
    if opc == 3:
        A = int(input("Digite um numero para A: "))
        B = int(input('Digite um numero para B: '))
        def multiplicação_dados(A,B):
            mult = (A*B)
            return (mult)
        multiplicação_final = multiplicação_dados(A,B)
        print(f'O valor da multiplicação entre {A} e {B} é igual a: {multiplicação_final}')
        x = x + 1
        print(x)
        L.append(multiplicação_final)
    if opc == 4:
        A = int(input("Digite um numero para A: "))
        B = int(input('Digite um numero para B: '))
        def divisão_dados(A,B):
            div = (A/B)
            return (div)
        divisão_final = divisão_dados(A,B)
        print(f'O resultado da divisão entre {A} e {B} é igual a: {divisão_final}')
        x = x + 1
        print(x)
        L.append(divisão_final)
    if opc == 5 or x == 10:
        print(f'Os resultados dos calculos foram: {L}')
        print("FIM DO PROGRAMA")  
    if opc > 5:
        print("Opção invalida\nTente novamente")
        