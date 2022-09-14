# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

# Função para somar dois números
def addNum(firstnum, secondnum):
    return firstnum+secondnum

# Função para subtrair dois números
def difNum(firstnum, secondnum):
    return firstnum - secondnum

# Função para multiplicar dois números
def multNum(firstnum, secondnum):
    return firstnum * secondnum

# Função para dividir dois números
def divNum(firstnum, secondnum):
    if secondnum!= 0: 
        return firstnum / secondnum
    else:
        return print("Erro: não é possível divisão por 0")

# inicia variável para selecionar opção    
opcao = 0

# Repete enquanto usuário não selecionar pra sair
while opcao != 5:
    print("\n******************* Python Calculator *******************")
    print("\nSelecione o número da operaçao desejada")
    print("\n1 - Soma")
    print("\n2 - Subtração")
    print("\n3 - Multiplicação")
    print("\n4 - Divisão")
    print("\n5 - Sair")
    
    # Escolha da opção selecionada
    opcao = int(input("Digite sua opção (1/2/3/4/5): "))

    if (opcao == 5): break

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if opcao == 1: #adição
        print("\n")
        print("Soma: %r + %r = " %(num1, num2), addNum(num1, num2))
        print("\n")
    elif opcao == 2: #subtração
        print("\n")
        print("Subtração: %r - %r =" %(num1, num2), difNum(num1, num2))
        print("\n")
    elif opcao == 3: #multiplicação
        print("\n")
        print("Multiplicação: %r * %r =" %(num1, num2), multNum(num1, num2))      
        print("\n")
    elif opcao == 4: #divisão        
        print("\n")
        print("Divisão: %r / %r =" %(num1, num2), divNum(num1, num2))
        print("\n")


