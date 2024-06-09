from colorama import Fore, init
init()
color = {
    "yellow": Fore.LIGHTYELLOW_EX,
    "magenta": Fore.LIGHTMAGENTA_EX,
    "green": Fore.LIGHTGREEN_EX,
    "cyan": Fore.LIGHTCYAN_EX,
    "white": Fore.LIGHTWHITE_EX,
    "black": Fore.LIGHTBLACK_EX,
    "blue": Fore.LIGHTBLUE_EX,
    "red": Fore.LIGHTRED_EX,
    "reset": Fore.RESET
}
menu = f"""{color["cyan"]}=====  <<< Menu  >>>  =====             
{color["cyan"].strip() + "|"}{color["reset"]}{color["green"]}[d] Depositar{color["reset"]} {color["cyan"] + "            |"}{color["reset"]}              
{color["cyan"].strip() + "|"}{color["reset"]}{color["green"]}[s] Sacar{color["reset"]}   {color["cyan"] + "              |"}{color["reset"]}                         
{color["cyan"].strip() + "|"}{color["reset"]}{color["green"]}[e] Extrato{color["reset"]}   {color["cyan"] + "            |"}{color["reset"]}           
{color["cyan"].strip() + "|"}{color["reset"]}{color["green"]}[q] Sair{color["reset"]}   {color["cyan"] + "               |"}{color["reset"]}                     
{color["cyan"]}============================{color["reset"]} 
{color["white"]} Insira a Opção :{color["reset"]} """

saldo = 0
limite = 500
extrato = ""
deposito = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        while True:
            try:
                valor = float(input(f"{color['white']}Informe o valor do depósito: {color['reset']}"))
                if valor > 0:
                    saldo += valor
                    extrato += f"{color['blue']}Depósito: R$ {valor:.2f}{color['reset']}\n"
                    print(f"{color['yellow']}Depósito efetuado com sucesso!!{color['reset']}")
                    break
                else:
                    print(f"{color['red']}Operação falhou! O valor informado é inválido.{color['reset']}")
            except ValueError:
                print(f"{color['red']}Valor inválido! Digite um número válido para o depósito.{color['reset']}")
    elif opcao == "s":
        while True:
            try:
                valor = float(input(f"{color['white']}Informe o valor do saque: {color['reset']}"))

                excedeu_saldo = valor > saldo

                excedeu_limite = valor > limite

                excedeu_saques = numero_saques >= LIMITE_SAQUES

                if excedeu_saldo:
                    print(f"{color['red']}Operação falhou! Você não tem saldo suficiente.{color['reset']}")

                elif excedeu_limite:
                    print(f"{color['red']}Operação falhou! O valor do saque excede o limite.{color['reset']}")

                elif excedeu_saques:
                    print(f"{color['red']}Operação falhou! Número máximo de saques excedido.{color['reset']}")

                elif valor > 0:
                    saldo -= valor
                    extrato += f"{color['red']}Saque: R$ {valor:.2f}{color['reset']}\n"
                    print(f"{color['white']}Saque efetuado com sucesso!!!{color['reset']}")
                    numero_saques += 1
                    break
                else:
                    print(f"{color['red']}Operação falhou! O valor informado é inválido.{color['reset']}")
            except ValueError:
                print(f"{color['red']}Valor inválido! Digite um número válido para o saque.{color['reset']}")
    elif opcao == "e":
        print(f"{color['red']}\n================ EXTRATO ================{color['reset']}")
        print(f"{color['yellow']}Não foram realizadas movimentações.{color['reset']}" if not extrato else extrato)
        print(f"{color['white']}Quantidade Saques: {numero_saques}{color['reset']}")
        print(f"\n{color['white']}Saldo: R$ {saldo:.2f}{color['reset']}")
        print(f"{color['red']}=========================================={color['reset']}")

    elif opcao == "q":
        print(f"{color['magenta']}Obrigado por no escolher. Tenha um otimo dia.{color['reset']}")
        break

    else:
        print(f"{color['red']}Operação inválida, por favor selecione novamente a operação desejada!!!!!!!{color['reset']}")