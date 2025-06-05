def menu():
    print("Menu")
    print("1 - Cliente")
    print("2 - Veículo")
    print("3 - Aluguéis")
    print("4 - Relatórios")
    print("5 - Sair")
    op = int(input("Insira uma opçaõ entre as fornecidas anteriormente:"))
    return op

def submenu_cliente():
    print("Submenu cliente")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    op = int(input("Selecione uma opção entre as fornecidas:"))
    return op

def submenu_veiculo():
    print("Submenu veículo")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    op = int(input("Selecione uma opção entre as fornecidas:"))

def submenu_aluguel():
    print("Submenu aluguel")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    op = int(input("Selecione uma opção entre as fornecidas:"))

def submenu_Relatórios():
    print("1 - Todas as reservas de um cliente")
    print("2 - Todas as reservas do veículo")
    print("3 - Reservas por data")
    print("6 - Sair")
    op = int(input("Selecione uma opção entre as fornecidas:"))

def opcoes_cliente(valor, dic_clientes, dic_dados):
    if valor == 1:
        print(dic_clientes)
    if valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic_clientes:
            print(dic_clientes[cpf.values()])
        else:
            print("Usuário não encontrado.")
    elif valor == 3:
        print("Incluir cliente no sistema")
        cpf = input("CPF: ")
        nome = input("Nome completo: ")
        endereco = input("Endereço: ")
        telefone_fix = input("Telefone fixo: ")
        cel = input("Telefone celular: ")
        data_nasc = input("Data de nascimento: ")
        dic_dados["Nome"] = nome
        dic_dados["Endereço"] = endereco
        dic_dados["Telefone Fixo"] = telefone_fix
        dic_dados["Celular"] = cel
        dic_dados["Data de nascimento"] = data_nasc
        dic_clientes[cpf] = dic_dados
    elif valor == 4:
        op = alterar_cilente()
        if op == 1:
            cpf = input("Selecione o CPF a ser alterado: ")
            if cpf in dic_clientes:
                novo_cpf = input("Insira o novo CPF: ")
                if novo_cpf in dic_clientes:
                    print("CPF já cadastrado.")
                else:
                    dic_clientes[novo_cpf] = dic_clientes[cpf]
                    del dic_clientes[cpf]
        elif op == 2:
            nome = input("Nome a ser alterado: ")
            if nome in dic_clientes:
                novo_nome = input("Novo nome: ")

    elif valor == 5:
        cpf = input("Digite o CPF do cliente a ser excluído: ")
        if cpf in dic_clientes:
            del dic_clientes[cpf]
            print("Cliente excluído com sucesso!")
            print(dic_clientes)
        else:
            print("CPF não cadastrado")
    elif valor == 6:
        menu()


    def alterar_cilente():
        print("Alterar cliente")
        print("1 - Alterar CPF")   #Dúvida
        print("2 - Nome completo")
        print("3 - Endereço")
        print("4 - Telefone fixo")
        print("5 - Telefone celular")
        print("6 - Data de nascimento")
        op = input("Selecione uma das opções a cima: ")

def main():
    dic_clientes = {}
    dic_dados = {}
    option = menu()
    option = 1
    while option != 5:
        if option == 1:
            valor = submenu_cliente()
            opcoes_cliente(valor,dic_clientes,dic_dados)
        elif option == 2:
            submenu_veiculo()
        elif option == 3:
            submenu_aluguel()
        elif option == 4:
            submenu_Relatórios()
        else:
            print("Programa encerrado.")

main()