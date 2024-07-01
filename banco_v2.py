"""
Esse projeto consistiu em criar um banco no qual tem as opções Criar usuário, Criar conta, Listar contas, Depositar, Sacar e Extrato. 
No qual não é possível depositar um número negativo, nem sacar um número negativo ou maior do que já tenha em conta.
Tambem não seja possivel criar dois usuários com o mesmo cpf, mas é possivel criar duas contas com o o mesmo cpf.
é possivel listar todas contas existentes.
E quando eu pedir para ele mostrar o extrato ele irá mostrar todas as minhas transferencias bancárias, assim como
o valor que depositei, saquei, quantidade de saques e mostrar o valor total que tenho em conta.
"""



def menu():
    menu = """

------- MENU -------

[1] Depositar
[2] Saque
[3] Extrato
[4] Nova conta
[5] Novo usuário
[6] Listar contas
[0] Sair

--------------------
=> """
    return input(menu)

def depositar(depositado, saldo, extrato, /):   # A barra indica que tudo que vier antes será positional-only, somente por posição
    print("----- DEPÓSITO -----\n\n")

    if depositado > 0:
        #try:
        saldo += depositado
        print(f"Valor depositado: R$ {depositado:.2f}")
        extrato += f"( + ) Depositou : R$ {depositado:.2f}\n"
        #except ValueError:
            #Se a conversão falhar, o erro é capturado e a mensangem é exibida
        #    print("O valor não é um inteiro.")            

    else:
        print(f"Valor inválido, digite um número positivo maior que 0.")    
            
    return saldo, extrato

def sacar(*, saldo, extrato, quantidade_saques, limite, LIMITE_SAQUE):  # O * indica que todos depois serão keyword-only
    print("----- SACAR -----\n\n")
    sacar = float(input("- Digite o valor para sacar: "))

    if sacar <= 0:
        print(f"Valor inválido, digite um número positivo maior que 0 e menor que {LIMITE_SAQUE}.")

    elif sacar > saldo:
        print("Você não tem saldo suficiente.")

    elif quantidade_saques >= limite:
        print(f"""O limite de saques por dia é {limite}.
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
            sacar = f"( - ) Sacou: R$ {sacar:.2f}\n"  # Formatar o número com 2 casas depois da vírgula
            quantidade_saques += 1
            extrato += sacar
        except ValueError:
            #Se a conversão falhar, o erro é capturado e a mesangem é exibida
            print("O valor não é um inteiro.")
    return saldo, extrato, quantidade_saques

def extrato_transacao(saldo, quantidade_saques, /, *, extrato):  # Antes da barra(/) é positional-only, depois do (*) é keyword-only
    print("\n----- EXTRATO -----\n")
    print(f"Saques realizados: {quantidade_saques}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(extrato) 
    print("--------------------")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario: # esse usuário sem condição é, caso for retornado um valor na variavel usuario chamando a função com filtro, ele executa
        print("### Já existe um usuário com esse CPF! ###")
        return  # Irá retornar para a função Main() pois caso tenha esse usuário cadastrado ele não precisa prosseguir

    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade-sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            Nº Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(linha)
        print("=" * 50)
        
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("### Usuario não encontrado, retorne assim que o usuário esteja criado! ###")

def main():
    usuarios = []
    contas = []
    AGENCIA = "0001"
    saldo = 0
    extrato = ""
    quantidade_saques = 0
    limite = 3
    LIMITE_SAQUE = 500

    while True:

        opcao = menu()     

        if opcao == "1":
            depositado = float(input(" Digite o valor para deposito: "))
            saldo, extrato = depositar(depositado, saldo, extrato)
            print(f"Seu saldo é: R${saldo:.0f},00")

        elif opcao == "2":
            
            saldo, extrato, quantidade_saques = sacar(
                saldo = saldo,
                extrato = extrato,
                quantidade_saques = quantidade_saques,
                limite = limite,
                LIMITE_SAQUE = LIMITE_SAQUE,
            )

        elif opcao == "3":
            extrato_transacao(saldo, quantidade_saques, extrato=extrato)
            
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == "5":
            criar_usuario(usuarios)
            
        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo do Banco.")
            break

        else:
            print("Caracter inválido.")
            break

main()
