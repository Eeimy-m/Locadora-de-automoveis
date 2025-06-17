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


def reservas_cliente(valor, dicio_cliente, dados_cliente, dicio_veiculo, dados_veiculo): 
    #essa função precisa receber como parrâmetro todos os dicionárrios criados até agora
    # 1 - mostrar todos os dados de um aluguel de acordo com um cpf de um cliente
    # 2 - mostrar os dados do cliente de acordo com o código do carro
    if valor == 1:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dicio_cliente:
            for i in dicio_cliente[cpf]:
                print(f"Data do aluguel: {dicio_cliente[cpf][0]}")
                print(f"Veículo: {dicio_cliente[cpf][1]}")
        else:
            print("CPF não encontrado no sistema.")
    
    elif valor == 2:
        veiculo = input("Insira o nome do veículo: ")
        if veiculo in dicio_veiculo:
            print()
        else:
            print("Veículo não encontrado no sistema.")
    
    elif valor == 3:
        data = input("Insira a data a ser analizada: ")
    
    elif valor == 4:
        print()


def opcoes_aluguel(dicio_alugueis, dicio_clientes, dicio_veiculos):
    dados_aluguel = {}
    valor = 1
    while valor != 6:  
        valor = submenu_aluguel()
        if valor ==1:
            print("Dados de todos os alugueis: ")
            if len(dicio_alugueis) != 0:
                for cpf in dicio_alugueis:
                    print(f"CPF: {cpf}")
                    print(f"Data do aluguel: {dicio_alugueis[cpf]["data"]}")
                    print(f"Veículo alugado: {dicio_alugueis[cpf]["codigo veiculo"]}")
                    print("***********************************")
            else:
                print("O banco de dados encontra-se vazio")

        elif valor == 2:
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_alugueis:
                print(f"CPF: {cpf}")
                print(f"Data de aluguel: {dicio_alugueis[cpf]["data"]}")
                print(f"Veículo alugado: {dicio_alugueis[cpf]["codigo veiculo"]}")
            else:
                print("CPF não encontrado no sistema.")

        elif valor == 3:  #melhorei o sistema de input de alugueis
            print("Realização de aluguel")
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_clientes:         
                data = input("Insira a data do aluguel no fromato dd/mm/aa: ")
                if data[2] and data[5] == "/":
                    veiculo = input("Insira o codigo do veiculo a ser alugado: ")
                    if veiculo in dicio_veiculos:
                        dados_aluguel["data"] = data
                        dados_aluguel["codigo veiculo"] = veiculo
                        dicio_alugueis[cpf] = dados_aluguel
                    else:
                        print("Veículo não encontrado no sistema.")
                else:
                    print("O formato da data é inválido, tente novamente.")
            else:
                print("CPF não encontrrado no sistema.")
         
        elif valor == 4: #testar
            op = alterar_aluguel()
            cpf = input("CPF do cliente: ")
            if cpf in dicio_alugueis:
                if op == 1:
                    nova_data = input("Informe a nova data de aluguel: ") #mudar o sistema de datas
                    dicio_alugueis[cpf]["data"] = nova_data
                elif op == 2:
                    novo_veiculo = input("Insira o código do novo veículo: ")
                    dicio_alugueis[cpf]["codigo veiculo"] = novo_veiculo
            else:
                print("CPF não encontrado.")
        
        elif valor == 5:
            cpf = input("Informe o CPF do cliente: ")
            if cpf in dicio_alugueis:
                del dicio_alugueis[cpf]
                print("Aluguel excluído do sistema com sucesso.")
            else:
                print("CPF não encontrado no sistema.")
        
        elif valor == 6:
            print("Voltando ao menu principal.")
            

def alterar_aluguel():
    print("1 - Data de aluguel")
    print("2 - Veículo alugado")
    op = int(input("Insira uma das opções a cima: "))
    return op
    
def opcoes_cliente(dic): #revisar
    valor = 1
    while valor != 6:
        valor = submenu_cliente()
        if valor == 1:
            if len(dic) != 0:
                print("Dados de todos os clientes:")
                for cpf in dic:
                    print(f"CPF: ", cpf)
                    print(f"Nome completo: {dic[cpf]["Nome"]}")
                    print(f"Endereço: {dic[cpf]["Endereço"]}")
                    print(f"Telefone fixo: {dic[cpf]["Telefone fixo"]}")
                    print(f"Telefone celular: {dic[cpf]["Telefone celular"]}")
                    print(f"Data de nascimento: {dic[cpf]["Data de nascimento"]}")
                    print("************************************************")
            else:
                print("Não há clientes cadastrados.")

        elif valor == 2:
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dic:
                print(f"Nome: {dic[cpf]["Nome"]}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {dic[cpf]["Endereço"]}")
                print(f"Telefone fixo: {dic[cpf]["Telefone fixo"]}")
                print(f"Telefone celular: {dic[cpf]["Telefone celular"]}")
                print(f"Data de nascimento: {dic[cpf]["Data de nascimento"]}")
            else:
                print("Usuário não encontrado.")

        elif valor == 3:  #sistema de input está dando errado
            dados_clientes = {}
            print("Incluir cliente no sistema")
            cpf = input("CPF: ")
            if cpf not in dic:
                nome = input("Nome completo: ")
                endereco = input("Endereço: ")
                telefone_fix = input("Telefone fixo: ")
                cel = input("Telefone celular: ")
                data_nasc = input("Data de nascimento: ")
                dados_clientes["Nome"] = nome
                dados_clientes["Endereço"] = endereco
                dados_clientes["Telefone fixo"] = telefone_fix
                dados_clientes["Telefone celular"] = cel
                dados_clientes["Data de nascimento"] = data_nasc
                dic[cpf] = dados_clientes
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
            cpf = input("Digite o CPF do cliente a ser excluído: ")
            if cpf in dic:
                del dic[cpf]
                print("Cliente excluído com sucesso!")
            else:
                print("CPF não cadastrado.")
        elif valor == 6:
            print("Saindo do submenu.")

def alterar_cilente():
    print("Alterar cliente")   
    print("1 - Nome completo")
    print("2 - Endereço")
    print("3 - Telefone fixo")
    print("4 - Telefone celular")
    print("5 - Data de nascimento")
    op = int(input("Selecione uma das opções a cima: "))
    return op


def opcoes_veiculo(dic):
    dados_veiculos = {} 
    valor = 1
    while valor != 6:
        valor = submenu_veiculo()
        if valor == 1:
            if len(dic) == 0:
                print("Não há veículos cadastrados.")
            else:
                for codigo in dic:
                    print(f"Código: {codigo}")
                    print(f"Modelo: {dic[codigo]['Modelo']}")
                    print(f"Descrição: {dic[codigo]['Descrição']}")
                    print(f"Categoria: {dic[codigo]['Categoria']}")
                    print(f"Capacidade: {dic[codigo]['Capacidade']}")
                    print(f"Combustível: {dic[codigo]['Combustível']}")
                    print(f"Ano: {dic[codigo]['Ano']}")
        
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
                dados_veiculos["Descrição"] = desc
                dados_veiculos["Categoria"] = categ
                dados_veiculos["Capacidade"] = capac
                dados_veiculos["Combustível"] = combustivel
                dados_veiculos["Ano"] = ano
                dados_veiculos["Modelo"] = modelo
                dic[codigo] = dados_veiculos
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
            print("Saindo do submenu.")

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
    dic_clientes = {}  #dados dos clientes
    dic_alugueis = {}  #chave será o cpf do cliente e o valor o veículo alugado pelo mesmo além da data de aluguel
    dic_veiculos = {}  #chave é o nome do veículo e 
    option = 1
    while option != 5:
        option = menu()
        if option == 1:
            opcoes_cliente(dic_clientes)
        elif option == 2:
            opcoes_veiculo(dic_veiculos)
        elif option == 3:
            opcoes_aluguel(dic_alugueis, dic_clientes, dic_veiculos)
        elif option == 4:
            valor = submenu_Relatórios()
            reservas_cliente()
        elif option == 5:
            print("Programa encerrado.")
        else:
            print("Opção inválida, tente novamente.")

main()
