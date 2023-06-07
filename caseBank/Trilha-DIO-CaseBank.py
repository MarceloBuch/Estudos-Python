menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Cadastrar usuario
[eu] Exibir usuarios
[cc] Cadastrar conta
[ec] Exibir contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
usuarios = []
contas = []
numero_conta = 1
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
            saldo += valor
            deposito = f"Depósito: R$ {valor:.2f}"
            extrato.append(deposito)
            message = "Depósito feito com sucesso!"
            result = [message, saldo, extrato]
            print(f"{result[0]}\n Saldo Atual - R${result[1]}")
            return result

    else:
        message = "Valor incorreto, depósito não realizado!"
        return message

def sacar(*, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        message = "Operação falhou! Você não tem saldo suficiente."
        return message

    elif excedeu_limite:
        message = "Operação falhou! O valor do saque excede o limite."
        return message

    elif excedeu_saques:
        message = "Operação falhou! Número máximo de saques excedido."
        return message

    elif valor > 0:
        saldo -= valor
        saque = f"Saque: R$ {valor:.2f}"
        extrato.append(saque)
        numero_saques += 1
        message = "Saque feito com sucesso!"
        result = [message, saldo, extrato]
        print(f"{result[0]}\n Saldo Atual - R${result[1]}")
        return result

    else:
        message = "Operação falhou! O valor informado é inválido."
        return message

def mostrarExtrato(*, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        for i in extrato:
            print(i)
    else:
        print("Você ainda não fez movimentações na conta")
    print("==========================================")
    print(f"Saldo atual - R${saldo}")

def cadastrarUsuario(usuarios):
    nome = input("Nome do usuario: ")
    dataNas = input("Data de nascimento(modelo: 00-00-00): ")
    cpf = input("CPF/CNPJ: ")
    endereco = input("Endereço do usuario(modelo: logradouro - bairro, cidade - sigla do estado): ")
    if len(usuarios) < 1:
        usuario = {
            "Nome" : nome, 
            "DataNas" : dataNas, 
            "CPF" : cpf,
            "Endereco" : endereco
        }
        print("Usuario Cadastrado!")
        usuarios.append(usuario)
        return usuario
    else:
        for dict in usuarios:
            if cpf in dict.values():
                print("CPF já cadastrado!")
                break
            else:
                usuario = {
                    "Nome" : nome, 
                    "DataNas" : dataNas, 
                    "CPF" : cpf,
                    "Endereco" : endereco
                }
                print("Usuario Cadastrado!")
                usuarios.append(usuario)
                return usuario

    

def exibirUsuarios(usuarios):
    print("\n================ Usuários cadastrados ================")
    for i, usuario in enumerate(usuarios, 1):
            print(f"\nUsuário {i}:")
            for chave, valor in usuario.items():
                print(f"{chave}: {valor}")
    print("\n==================================================")

def cadastrarConta(contas, numero_conta):
    cpf = input("Digite o CPF do usuario que você deseja criar a conta: ")
    if len(contas) > 1:
        conta = {
            "Agencia": "0001",
            "NumeroConta": numero_conta,
            "CPF": cpf
        }
        numero_conta =+ 1
        contas.append(conta)
        return conta
    else:
        for dict in usuarios:
            if cpf in dict.values():
                conta = {
                    "Agencia": "0001",
                    "NumeroConta": numero_conta,
                    "CPFUsuario": cpf
                }
                numero_conta =+ 1
                contas.append(conta)
                print("Conta cadastrada!")
                return conta
            else:
                print(f"Usuario de CPF - {cpf}, não encontrado! Por favor cadastre ele para criar a conta.")
                break



def exibirContas(contas):
    print("\n================ Contas cadastrados ================")
    for i, conta in enumerate(contas, 1):
            print(f"\nConta {i}:")
            for chave, valor in conta.items():
                print(f"{chave}: {valor}")
    print("\n==================================================")


while True:

    opcao = input(menu)

    if opcao == "d":
        depositar(saldo, extrato)

    elif opcao == "s":
        sacar(saldo = saldo, limite = limite, extrato = extrato, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

    elif opcao == "e":
        mostrarExtrato(extrato = extrato)

    elif opcao == "cu":
        cadastrarUsuario(usuarios)
        
    elif opcao == "eu":
        exibirUsuarios(usuarios)
    
    elif opcao == "cc":
        cadastrarConta(contas, numero_conta)
        
    elif opcao == "ec":
        exibirContas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")