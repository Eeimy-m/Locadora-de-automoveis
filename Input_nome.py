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
        print(dic)

    elif valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic:
            print(dic[cpf.values()])
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
        dados["Nome"] = nome
        dados["Endereço"] = endereco
        dados["Telefone fixo"] = telefone_fix
        dados["Teleofne celular"] = cel
        dados["Data de nascimento"] = data_nasc
        dic[cpf] = dados

    elif valor == 4:
        op = alterar_cilente()
        if op == 1:
            cpf = ("CPF do cliente: ")
            novo_nome = input("Novo nome: ")
            dados["Nome"] = novo_nome
        elif op == 2:
            cpf = ("CPF do cliente: ")
            novo_endereco = input("Novo endereço: ")
            dados["Endereço"] = novo_endereco
        elif op == 3:
            cpf = ("CPF do cliente: ")
            novo_tel_fix = input("Novo telefone")
            dados["Telefone fixo"] = novo_tel_fix
        elif op == 4:
            cpf = ("CPF do cliente: ")
            novo_cel = input("Novo telefone celular: ")
            dados["Telefone celular"] = novo_cel
        elif op == 5:
            cpf = ("CPF do cliente: ")
            nova_data = input("Correção da data de nasicmento: ")
            dados["Data de nascimento"] = nova_data
        
    elif valor == 5:
        cpf = input("Digite o CPF do cliente a ser excluído: ")
        if cpf in dic:
            del dic[cpf]
            print("Cliente excluído com sucesso!")
            print(dic)
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
    op = input("Selecione uma das opções a cima: ")
    return op 

def main():
    dic_clientes = {}  
    dados_clientes = {}
    dic_alugueis = {}  #chave será o cpf do cliente e o valor o veículo alugado pelo mesmo além da data de aluguel
    dados_aluguel = {}
    dic_veiculos = {}
    dados_veiculos = {} 
    option = menu()
    cont = 1
    while cont != 5:
        if option == 1:
            valor = submenu_cliente()
            opcoes_cliente(valor, dic_clientes, dados_clientes )
        elif option == 2:
            submenu_veiculo()
        elif option == 3:
            valor = submenu_aluguel()
            opcoes_aluguel(valor, dic_alugueis, dados_aluguel)
        elif option == 4:
            valor = submenu_Relatórios()
            reservas_cliente(valor, )
        else:
            print("Programa encerrado.")

main()
