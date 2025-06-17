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

#---------arquivos------------------
def salvarCliente(dic):
    arq = open("clientes.txt","w")
    for cpf, dados in dic.items():
        arq.write(f"{cpf}\n")
        arq.write(f"{dados['Nome']}\n")
        arq.write(f"{dados['Endereço']}\n")
        arq.write(f"{dados['Telefone fixo']}\n")
        arq.write(f"{dados['Telefone celular']}\n")
        arq.write(f"{dados['Data de nascimento']}\n")
        arq.write("******************************\n")
    arq.close()

def carregarCliente():
    dic = {}
    if not os.path.exists("clientes.txt"):
        return dic
    arq = open("clientes.txt", "r")
    linhas = [linha.strip() for linha in arq]
    for i in range(0, len(linhas), 7):
        cpf = linhas[i]
        dic[cpf] = {
            "Nome": linhas[i+1],
            "Endereço": linhas[i+2],
            "Telefone fixo": linhas[i+3],
            "Telefone celular": linhas[i+4],
            "Data de nascimento": linhas[i+5]
        }
    arq.close()
    return dic

def salvarVeiculo(dic):
    arq = open("veiculos.txt","w")
    for codigo, dados in dic.items():
        arq.write(f"{codigo}\n")
        arq.write(f"{dados['Descrição']}\n")
        arq.write(f"{dados['Capacidade']}\n")
        arq.write(f"{dados['Combustível']}\n")
        arq.write(f"{dados['Ano']}\n")
        arq.write(f"{dados['Modelo']}\n")
        arq.write("******************************\n")
    arq.close()

def carregarVeiculo():
    dic = {}
    if not os.path.exists("veiculos.txt"):
        return dic
    arq = open("veiculos.txt", "r")
    linhas = [linha.strip() for linha in arq]
    for i in range(0, len(linhas), 7):
        cpf = linhas[i]
        dic[cpf] = {
            "Descrição": linhas[i+1],
            "Capacidade": linhas[i+2],
            "Combustível": linhas[i+3],
            "Ano": linhas[i+4],
            "Modelo": linhas[i+5]
        }
    arq.close()
    return dic

def salvarAluguel(dic):
    arq = open("alugueis.txt","w")



def reservas_cliente(valor, dicio_cliente, dados_cliente, dicio_veiculo, dados_veiculo): #preciso mexer
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

from datetime import date
def opcoes_aluguel(valor, dic):
    dados_aluguel = {}
    if valor ==1:
        print("Dados de todos os alugueis: ")
        if len(dic) != 0:
            for cpf in dic:
                print(f"CPF: {cpf}")
                print(f"Data do aluguel: {dic[cpf]['data']}")
                print(f"Veículo alugado: {dic[cpf]['veiculo']}")
                print("***********************************")
        else:
            print("O banco de dados encontra-se vazio")

    elif valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic:
            print(f"CPF: {cpf}")
            print(f"Data de aluguel: {dic[cpf]['data']}")
            print(f"Veículo alugado: {dic[cpf]['veiculo']}")
        else:
            print("CPF não encontrado no sistema.")

    elif valor == 3:
        print("Realização de aluguel")
        cpf = input("Insira o CPF do cliente: ")
        data = date.today() 
        veiculo = input("Insira o carro a ser alugado: ")
        dados_aluguel["data"] = data
        dados_aluguel["veiculo"] = veiculo
        dic[cpf] = dados_aluguel
    
<<<<<<< HEAD
def opcoes_cliente(valor, dic): #revisar
    if valor == 1:
        if len(dic) != 0:
            print("Dados de todos os clientes:")
            for cpf in dic:
                print(f"CPF: ", cpf)
                print(f"Nome completo: {dic[cpf]['Nome']}")
                print(f"Endereço: {dic[cpf]['Endereço']}")
                print(f"Telefone fixo: {dic[cpf]['Telefone fixo']}")
                print(f"Telefone celular: {dic[cpf]['Telefone celular']}")
                print(f"Data de nascimento: {dic[cpf]['Data de nascimento']}")
                print("************************************************")
        else:
            print("Não há clientes cadastrados.")

    elif valor == 2:
        cpf = input("Insira o CPF do cliente: ")
        if cpf in dic:
            print(dic[cpf])
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
=======
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
>>>>>>> 6c3b995fc2deb77d5228199ca11fcb9b458959e6
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
            main()

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
            main()      

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
    dic_clientes = carregarCliente()  #dados dos clientes
    dic_alugueis = {} #chave será o cpf do cliente e o valor o veículo alugado pelo mesmo além da data de aluguel
    dic_veiculos = carregarVeiculo() #chave é o nome do veículo e 
    option = 1
    while option != 5:
        option = menu()
        if option == 1:
<<<<<<< HEAD
            valor = submenu_cliente()
            opcoes_cliente(valor, dic_clientes)
            salvarCliente(dic_clientes)
        elif option == 2:
            valor = submenu_veiculo()
            opcoes_veiculo(valor, dic_veiculos)
            salvarVeiculo(dic_veiculos)
=======
            opcoes_cliente(dic_clientes)
        elif option == 2:
            opcoes_veiculo(dic_veiculos)
>>>>>>> 6c3b995fc2deb77d5228199ca11fcb9b458959e6
        elif option == 3:
            valor = submenu_aluguel()
            opcoes_aluguel(valor, dic_alugueis)
        elif option == 4:
            valor = submenu_Relatórios()
            reservas_cliente()
        elif option == 5:
            print("Programa encerrado.")
        else:
            print("Opção inválida, tente novamente.")

    
main()
