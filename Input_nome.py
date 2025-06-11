#Locadora de automóveis

import os
def menu():
    print("Menu")
    print("1 - Cliente")
    print("2 - Veículo")
    print("3 - Aluguéis")  #A opção relatórios está relacionada com aluguéis
    print("4 - Relatórios")
    print("5 - Sair")
    op = int(input("Insira uma opçaõ entre as fornecidas anteriormente:"))
    return op

def submenu_cliente():   #Uma função para cada opção entre veículos, clientes... Para que na hora da opção ser executada haja uma diferenciação
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
    return op

def submenu_aluguel():
    print("Submenu aluguel")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    op = int(input("Selecione uma opção entre as fornecidas:"))
    return op

def submenu_Relatórios():
    print("1 - Todas as reservas de um cliente")
    print("2 - Todas as reservas do veículo")
    print("3 - Reservas por data")
    print("4 - Sair")
    op = int(input("Selecione uma das opções a cima: "))
    return op

#def reservas_cliente():

from datetime import date
def opcoes_aluguel(valor, dic, dados):
    if valor ==1:
        print(dic)
    elif valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic:
            print(dic[cpf])
        else:
            print("CPF não encontrado no sistema.")
    elif valor == 3:
        print("Realização de aluguel")
        cpf = input("Insira o CPF do cliente: ")
        data = date.today() 
        veiculo = input("Insira o carro a ser alugado: ")
        dados["data"] = data
        dados["veiculo"] = veiculo
        dic[cpf] = dados
        
            
def opcoes_cliente(valor, dic, dados):
    if valor == 1:
        if len(dic) == 0:
            print("Não há clientes cadastrados.")
        else:
            print(dic)

    elif valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic:
            print(dic[cpf])
        else:
            print("Usuário não encontrado.")

    elif valor == 3:
        print("Incluir cliente no sistema")
        cpf = input("CPF: ")
        if cpf not in dic:
            nome = input("Nome completo: ")
            endereco = input("Endereço: ")
            telefone_fix = input("Telefone fixo: ")
            cel = input("Telefone celular: ")
            data_nasc = input("Data de nascimento: ")
            dados["Nome"] = nome
            dados["Endereço"] = endereco
            dados["Telefone fixo"] = telefone_fix
            dados["Telefone celular"] = cel
            dados["Data de nascimento"] = data_nasc
            dic[cpf] = dados
            print("Cliente cadastrado com sucesso!")
        else:
            print("CPF já cadastrado. ")

    elif valor == 4:
        op = alterar_cilente()

        cpf = input("CPF do cliente: ")
        if cpf in dic:
            if op == 1:
                novo_nome = input("Novo nome: ")
                dic[cpf]["Nome"] = novo_nome
                print("Nome alterado com sucesso!")
            elif op == 2:
                novo_endereco = input("Novo endereço: ")
                dic[cpf]["Endereço"] = novo_endereco
                print("Endereço alterado com sucesso!")
            elif op == 3:
                novo_tel_fix = input("Novo telefone fixo: ")
                dic[cpf]["Telefone fixo"] = novo_tel_fix
                print("Telefone fixo alterado com sucesso!")
            elif op == 4:
                novo_cel = input("Novo telefone celular: ")
                dic[cpf]["Telefone celular"] = novo_cel
                print("Telefone celular alterado com sucesso!")
            elif op == 5:
                nova_data = input("Nova data de nascimento: ")
                dic[cpf]["Data de nascimento"] = nova_data
                print("Data de nascimento alterada com sucesso!")
            else:
                print("Opção inválida.")
        else:
            print("CPF não encontrado.")
        
    elif valor == 5:
        cpf = input("Informe o CPF do cliente a ser excluído: ")
        if cpf in dic:
            del dic[cpf]
            print("Cliente excluído com sucesso!")
        else:
            print("CPF não cadastrado.")
    elif valor == 6:
        menu()

def alterar_cilente():
    print("Alterar cliente")   
    print("1 - Nome completo")
    print("2 - Endereço")
    print("3 - Telefone fixo")
    print("4 - Telefone celular")
    print("5 - Data de nascimento")
    op = int(input("Selecione uma das opções a cima: "))
    return op

def opcoes_veiculo(valor, dic, dados):
    if valor == 1:
        if len(dic) == 0:
            print("Não há veículos cadastrados.")
        else:
            for codigo in dic:
                print(f"Código: {codigo}")
                print(f"Descrição: {dic[codigo]['Descrição']}")
                print(f"Categoria: {dic[codigo]['Categoria']}")
                print(f"Capacidade: {dic[codigo]['Capacidade']}")
                print(f"Combustível: {dic[codigo]['Combustível']}")
                print(f"Ano: {dic[codigo]['Ano']}")
                print(f"Modelo: {dic[codigo]['Modelo']}")
    
    elif valor == 2:
        codigo = input("Informe o código do veículo: ")
        if codigo in dic:
            print(dic[codigo])
        else:
            print("Veículo não encontrado.")

    elif valor == 3:
        print("Incluir veículo no sistema...")
        codigo = input("Código: ")
        if codigo not in dic:
            desc = input("Descrição: ")
            categ = input("Categoria: ")
            capac = input("Capacidade: ")
            combustivel = input("Combustível: ")
            ano = int(input("Ano: "))
            modelo = input("Modelo: ")
            dados["Descrição"] = desc
            dados["Categoria"] = categ
            dados["Capacidade"] = capac
            dados["Combustível"] = combustivel
            dados["Ano"] = ano
            dados["Modelo"] = modelo
            dic[codigo] = dados.copy() # não sobreescreve os dados conforme vai incluindo novos veiculos, existe outra forma de fazer, consultar Eloize.
            print("Veículo cadastrado com sucesso!")
        else:
            print("Código já cadastrado.")

    elif valor == 4:
        op = alterar_veiculo()

        codigo = input("Código do veículo: ")
        if codigo in dic:
            if op == 1:
                nova_desc =input("Nova descrição: ")
                dic[codigo]["Descrição"] = nova_desc
                print("Descrição alterada com sucesso!")

            elif op == 2:
                nova_categ = input("Nova categoria: ")
                dic[codigo]["Categoria"] = nova_categ
                print("Categoria alterada com sucesso!")

            elif op == 3:
                nova_capac = input("Nova capacidade: ")
                dic[codigo]["Capacidade"] = nova_capac
                print("Capacidade alterada com sucesso!")

            elif op == 4:
                novo_combustivel = input("Novo combustível: ")
                dic[codigo]["Combustível"] = novo_combustivel
                print("Combustível alterado com sucesso!")

            elif op == 5:
                novo_ano = input("Novo ano: ")
                dic[codigo]["Ano"] = novo_ano
                print("Ano alterado com sucesso!")

            elif op == 6:
                novo_modelo = input("Novo modelo: ")
                dic[codigo]["Modelo"] = novo_modelo
                print("Modelo alterado com sucesso!")

            else:
                print("Opção Inválida.")

        else:
            print("Código não encontrado.")

    elif valor == 5:
        codigo = input("Informe o código do veículo a ser excluído: ")
        if codigo in dic:
            del dic[codigo]
            print("Veículo excluído com sucesso!")
        else:
            print("Veículo não cadastrado.")

    elif valor == 6:
        menu()        

def alterar_veiculo():
    print("Alterar Veículo")
    print("1 - Descrição")
    print("2 - Categoria")
    print("3 - Capacidade")
    print("4 - Combustível")
    print("5 - Ano")
    print("6 - Modelo")
    op = int(input("Selecione uma das opções a cima: "))
    return op

def main():
    dic_clientes = {}  
    dados_clientes = {}
    dic_alugueis = {}  #chave será o cpf do cliente e o valor o veículo alugado pelo mesmo além da data de aluguel
    dados_aluguel = {}
    dic_veiculos = {}
    dados_veiculos = {} 
    cont = 1
    while cont != 5:
        option = menu()
        if option == 1:
            valorC = submenu_cliente()
            opcoes_cliente(valorC, dic_clientes, dados_clientes )
        elif option == 2:
            valorV = submenu_veiculo()
            opcoes_veiculo(valorV,dic_veiculos,dados_veiculos)
        elif option == 3:
            valorA = submenu_aluguel()
            opcoes_aluguel(valorA, dic_alugueis, dados_aluguel)
        elif option == 4:
            valor = submenu_Relatórios()
            reservas_cliente(valor, )
        else:
            print("Programa encerrado.")

main()
