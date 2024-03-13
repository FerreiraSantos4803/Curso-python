## criação de calculadora quando estou iniciando os estudos
## 10.03.24



while True:
    valor_inicial1 = input('Digite o primeiro valor: ')
    valor_inicial2 = input('Digite o segundo valor: ')

    if valor_inicial1.isdigit() and valor_inicial2.isdigit():
        valor_inicial1 = int(valor_inicial1)
        valor_inicial2 = int(valor_inicial2)
    else:
        print('[ERRO]: Você precisa digitar um número')
        continue

    operador = input('\n + (adição) \n - (subtração) \n * (multiplicação) \n / (divisão)20 \n Esola seu operador: ' )

    def soma():
        somar = valor_inicial1 + valor_inicial2
        print(f'O valor da soma é {somar}')
    def subtracao():
        diminuir = valor_inicial1 - valor_inicial2
        print(f'O valor da soma é {diminuir}')
    def multiplicacao():
        multiplicar = valor_inicial1 * valor_inicial2
        print(f'O valor da multiplicação é {multiplicar}')
    def divisao():
        dividir = valor_inicial1 / valor_inicial2
        print(f'O valor da divisão é {dividir}')

    if operador == "+":
        soma()
    elif operador == "-":
        subtracao()
    elif operador == "*":
        multiplicacao()
    elif operador == "/":
        divisao()
    else:
        print(f'{operador} não é um operador válido. ')
        continue
    fim = input('\n [S]Sim \n [N]Não \n Você deseja continuar?: ')
    if fim == "S" or "s" or "SIM":
        print('Você decidiu encerrar a calculadora, até a próxima.')
        break
    else: 
        continue



## fiz uma pequna alteração