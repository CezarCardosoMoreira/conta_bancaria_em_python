
#sacar depositar extrato


inicair = """


[d] Depositar
[s] Sacar
[e] Extrato
[f] Fim


"""


saldo = 1000
limite = 500
extrato = ""
numeros_de_saques = 0
LIMITE_DE_SAQUE = 3

while True:

    opcao =input(inicair)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito :R$ {valor:.2f}\n"

        else:
            print("Valor informado é invalido!")    


    elif  opcao == "s":
        valor = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_de_saques >= LIMITE_DE_SAQUE

        if excedeu_saldo :
            print(f"Você não saldo suficiente, seu saldo é : {saldo:.2f}\n")

        elif excedeu_limite :
            print(f"Você não limite suficiente, seu saldo é : {limite:.2f}\n")

        elif excedeu_saques :
            print(f" Você excedeu o limite de saque !")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_de_saques += 1

        else:
            print("O valor informado é inválido, seu limite de saque  é de 500.") 

    elif opcao == "e":
        print("\n *************************   Seu Extrato   *********************************")

        print("Não foram realizadas movimentações." if not extrato else extrato) 

        print(f"\n Saldo: R$ {saldo:.2f}")

        print("******************************   FIM   *****************************************")


    elif opcao == "f":
        break

    else:
        print("Operação inválida! Selecione novamente a operação desejada.") 








    

