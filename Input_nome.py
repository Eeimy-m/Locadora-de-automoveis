import os
def menu():
    os.system('cls')
    print("Menu")
    print("1 - Cliente")
    print("2 - Veículo")
    print("3 - Aluguéis")
    print("4 - Relatórios")
    print("5 - Sair")
    op = int(input("Insira uma opçaõ entre as fornecidas anteriormente:"))
    return op

def submenu_cliente():
    os.system('cls')
    print("Submenu cliente")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    op = int(input("Selecione uma opção entre as fornecidas:"))
    return op

def submenu_veiculo():
    os.system('cls')
    print("Submenu veículo")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    op = int(input("Selecione uma opção entre as fornecidas:"))

def submenu_aluguel():
    os.system('cls')
    print("Submenu aluguel")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    op = int(input("Selecione uma opção entre as fornecidas:"))

def submenu_Relatórios():
    os.system('cls')
    print("1 - Todas as reservas de um cliente")
    print("2 - Todas as reservas do veículo")
    print("3 - Reservas por data")


def opcoes_cliente(valor, dic, dados):
    os.system('cls')
    if valor == 3:
        print("Incluir cliente no sistema")
        cpf = input("CPF: ")
        nome = input("Nome completo: ")
        endereco = input("Endereço: ")
        telefone_fix = input("Telefone fixo: ")
        cel = input("Telefone celular: ")
        data_nasc = input("Data de nascimento: ")
        dados["Nome"] = nome
        dados["Endereço"] = endereco
        dados["Telefone fixo"] = telefone_fix
        dados["Teleofne celular"] = cel
        dados["Data de nascimento"] = data_nasc
        dic[cpf] = dados
    elif valor == 1:
        print(dic)
    elif valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic:
            print(dic[cpf.values()])
        else:
            print("Usuário não encontrado.")
    elif valor == 4:
        op = alterar_cilente()
        if op == 1:
            cpf = input("Selecione o CPF a ser alterado: ")
            if cpf in dic:
                novo_cpf = input("Insira o novo CPF: ")
                if novo_cpf in dic:
                    print("CPF já cadastrado.")
                else:
                    dic[novo_cpf] = dic[cpf]
                    del dic[cpf]
        elif op == 2:
            cpf = ("CPF do cliente: ")
            novo_nome = input("Novo nome: ")
            dados["Nome"] = novo_nome
        elif op == 3:
            cpf = ("CPF do cliente: ")
            novo_endereco = input("Novo endereço: ")
            dados["Endereço"] = novo_endereco
        elif op == 4:
            cpf = ("CPF do cliente: ")
            novo_tel_fix = input("Novo telefone")
            dados["Telefone fixo"] = novo_tel_fix
        elif op == 5:
            cpf = ("CPF do cliente: ")
            novo_cel = input("Novo telefone celular: ")
            dados["Telefone celular"] = novo_cel
        elif op == 6:
            cpf = ("CPF do cliente: ")
            nova_data = input("Correção da data de nasicmento: ")
            dados["Data de nascimento"] = nova_data
    


    def alterar_cilente():
        os.system('cls')
        print("Alterar cliente")
        print("1 - Alterar CPF")   #Dúvida
        print("2 - Nome completo")
        print("3 - Endereço")
        print("4 - Telefone fixo")
        print("5 - Telefone celular")
        print("6 - Data de nascimento")
        op = input("Selecione uma das opções a cima: ")
        return op 

def main():
    dic_clientes = {}
    dados_clientes = {}
    option = menu()
    option = 1
    while option != 5:
        if option == 1:
            valor = submenu_cliente()
            opcoes_cliente(valor, dic_clientes, dados_clientes )
        elif option == 2:
            submenu_veiculo()
        elif option == 3:
            submenu_aluguel()
        elif option == 4:
            submenu_Relatórios()
        else:
            print("Programa encerrado.")

main()