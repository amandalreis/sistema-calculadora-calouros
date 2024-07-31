import os # Aqui, estou importando uma biblioteca do python. Ela é necessária pra rodar o comando os.system('clear'), que serve para limpar o terminal.

def mostrar_menu():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.
    print("Bem-vindo(a) à calculadora!")
    print("1. Realizar soma")
    print("2. Realizar subtração")
    print("3. Realizar multiplicação")
    print("4. Realizar divisão")
    print("5. Obter resto de divisão")
    print("6. Calcular porcentagem")
    print("7. Sair do sistema")
    opcao = input("Selecione uma das opções acima: ")#Para solicitar e receber um valor do usuário através do terminal

    if (opcao == "1"):
        realizar_soma()
    elif (opcao == "2"):
        realizar_subtracao()
    elif (opcao == "3"):
        realizar_multiplicacao()
    elif (opcao == "4"):
        realizar_divisao()
    elif (opcao == "5"):
        obter_resto_de_divisao()
    elif (opcao == "6"):
        calcular_porcentagem()
    elif (opcao == "7"):
        sair()
    else:
        os.system('clear')
        print("Valor inválido.")
        voltar_ao_menu()

def voltar_ao_menu():
    input("Insira qualquer valor para voltar ao menu: ")
    mostrar_menu()

def realizar_soma():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.
    quantidade_numeros_a_somar = int(input("Quantos números você deseja somar? "))

    if (quantidade_numeros_a_somar < 2):
        print("É impossível somar menos de dois números!")
        voltar_ao_menu()

    soma = 0

    for i in range(0, quantidade_numeros_a_somar):
        numero = float(input(f"Digite o {i + 1}º número: "))
        soma += numero
    
    print(f"O resultado da soma entre os números fornecidos é: {soma}")

    voltar_ao_menu()

def realizar_subtracao():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.

    primeiro_numero = float(input("Qual o número do qual você deseja subtrair? "))
    segundo_numero = float(input("Qual o valor a ser subtraído do primeiro número informado? "))

    subtracao = primeiro_numero - segundo_numero

    print(f"O resultado da subtração entre os números fornecidos é: {subtracao}")

    voltar_ao_menu()

def realizar_multiplicacao():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.

    quantidade_numeros_a_multiplicar = int(input("Quantos números você deseja multiplicar? "))

    if (quantidade_numeros_a_multiplicar < 2):
        print("É impossível multiplicar menos de dois números!")
        voltar_ao_menu()

    multiplicacao = 1

    for i in range(0, quantidade_numeros_a_multiplicar):
        numero = float(input(f"Digite o {i + 1}º número: "))
        multiplicacao *= numero
    
    print(f"O resultado da multiplicação entre os números fornecidos é: {multiplicacao}")

    voltar_ao_menu()

def realizar_divisao():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.

    primeiro_numero = float(input("Qual o número a ser dividido? "))
    segundo_numero = float(input("Qual o número que deve dividir o primeiro número informado? "))

    if (segundo_numero == 0.0):
        print("É impossível dividir um número por zero!")
        voltar_ao_menu()
    else:
        divisao = primeiro_numero / segundo_numero

        print(f"O resultado da divisão entre os números fornecidos é: {divisao}")

        voltar_ao_menu()

def obter_resto_de_divisao():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.

    primeiro_numero = float(input("Qual o número a ser dividido? "))
    segundo_numero = float(input("Qual o número que deve dividir o primeiro número informado? "))

    if (segundo_numero == 0.0):
        print("É impossível dividir um número por zero!")
        voltar_ao_menu()
    else:
        resto = primeiro_numero % segundo_numero

        print(f"O resto da divisão entre os números é: {resto}")

        voltar_ao_menu()


def calcular_porcentagem():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.

    primeiro_numero = float(input("Qual o número que representa a porcentagem a ser descoberta? "))
    segundo_numero = float(input("Qual o número que representa a porcentagem total? "))

    porcentagem = (primeiro_numero / segundo_numero) * 100

    print(f"{primeiro_numero} é {porcentagem}% de {segundo_numero}")

    voltar_ao_menu()

def sair():
    os.system('clear')
    print("Até mais! Encerrando execução... :)")
    exit()

mostrar_menu()
