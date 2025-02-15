from os import system
system('cls')

def calculoDoisNum():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    entrada = input('Digite o número da operação você deseja efetuar\n1.Soma\n2.Subtração\n3.Divisão\n4.Multiplicação\n')

    if entrada == '1':
        print(f"{num1} + {num2} = {num1 + num2}\n")
    elif entrada == '2':
        print(f"{num1} - {num2} = {num1 - num2}\n")
    elif entrada == '3':
        print(f"{num1} / {num2} = {num1 / num2}\n")
    elif entrada == '4':
        print(f"{num1} X {num2} = {num1 * num2}\n")  

def calculadorIdade(anoNascimento):
    try:
        if type(anoNascimento) == str:
            if anoNascimento.isnumeric():
                anoNascimento = int(anoNascimento)
    except:
        print('Erro ao Executar')

    idade = 2025 - anoNascimento        

    if idade < 1 or idade > 125:
        print('Sua idade é inválida.')
    else:
        print(f"Sua idade é {idade} anos")
    
    return idade

idadeCalculada = calculadorIdade('2007')
idadeCalculada()

while 1 == 3:
    print('1 - Calculadora')
    print('2 - Abrir estoque')
    print('3 - Sair')
    escolha = input('Escolha uma das opções: ')
    
    if escolha == '1':
        calculoDoisNum()
    elif escolha == '2':
        print('Abrindo Estoque.')
    elif escolha == '3':
        print('Saindo do sistema.')
        break