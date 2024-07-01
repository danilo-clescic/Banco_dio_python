"""
Banco no qual tem as opções Depositar, Sacar e Extrato. No qual não é possível depositar um número negativo, 
nem sacar um número negativo ou maior do que já tenha em conta.
E quando eu pedir para ele mostrar o extrato ele irá mostrar todas as minhas transferencias bancárias, assim como
o valor que depositei, saquei e mostrar o valor total que tenho em conta.
"""

menu = """

------- MENU -------

[1] Depositar
[2] Saque
[3] Extrato
[0] Sair

--------------------
=> """

saldo = 0
extrato = ""
quantidade_saques = 1
LIMITE_QUANT_SAQUE = 3
LIMITE_SAQUE = 500

while True:

    opcao = input(menu)     

    if opcao == "1":       
        print("----- DEPÓSITO -----\n\n")
        depositar = float((input(" Digite o valor para deposito: ")))

        if depositar <= 0:
            print(f"Valor inválido, digite um número positivo maior que 0 e menor que {LIMITE_SAQUE}.")                

        else:
            try:
                #Tenta converter o valor para inteiro
                depositar = float(depositar)
                saldo = float(saldo)
                saldo += depositar
                print(f"Valor depositado: R$ {depositar:.2f}")
                depositar = f"( + ) Depositou : R$ {depositar:.2f}\n"
                extrato += depositar
            except ValueError:
                #Se a conversão falhar, o erro é capturado e a mesangem é exibida
                print("O valor não é um inteiro.")

    elif opcao == "2":
            print("----- SACAR -----\n\n")
            sacar = float(input(" Digite o valor para sacar: "))

            if sacar <= 0:
                print(f"Valor inválido, digite um número positivo maior que 0 e menor que {LIMITE_SAQUE}.")

            elif sacar > saldo:
                print("Você não tem saldo suficiente.")

            elif quantidade_saques > LIMITE_QUANT_SAQUE:
                print(f"""O limite de saques por dia é {LIMITE_QUANT_SAQUE}.
                    Você excedeu seu limite, volte amanhã.""")

            elif sacar > LIMITE_SAQUE:
                print(f"""O limite diário por saque é de: R$ {LIMITE_SAQUE:.2f} .
                    Tente um valor menor.""")
            else:
                try:
                    #Tenta converter o valor para inteiro
                    sacar = float(sacar)
                    saldo = float(saldo)
                    saldo -= sacar
                    print(f"Valor sacado: R$ {sacar:.2f}")
                    sacar = f"( - ) Sacou: R$ {sacar:.2f}\n"  # Formatar o núemro com 2 casas depois da vírgula
                    quantidade_saques += 1
                    extrato += sacar
                except ValueError:
                    #Se a conversão falhar, o erro é capturado e a mesangem é exibida
                    print("O valor não é um inteiro.")

    elif opcao == "3":
        print("\n----- EXTRATO -----\n")
        print(f"Saques realizados: {quantidade_saques}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(extrato) 
        print("--------------------")

    elif opcao == "0":
        print("Saindo do Banco.")
        break

    else:
        print("Caracter inválido.")
        break