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

def verificacao_data(data):  
    if data[2] != "/" and data[5] != "/":
        return False
    else:
            dia, mes, ano = data.split("/")
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            if dia < 1:  
                return False
            elif dia > 31:
                return False
            elif mes < 1:
                return False
            elif mes > 12:
                return False
            elif ano < 1900:
                return False
            elif ano > 2025:
                return False
            else:
                return True 

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
        arq.write(f"{dados['Categoria']}\n")
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
    for i in range(0, len(linhas), 8):
        codigo = linhas[i]
        dic[codigo] = {
            "Descrição": linhas[i+1],
            "Categoria": linhas[i+2],
            "Capacidade": linhas[i+3],
            "Combustível": linhas[i+4],
            "Ano": linhas[i+5],
            "Modelo": linhas[i+6]
        }
    arq.close()
    return dic

def salvarAluguel(dic):
    arq = open("alugueis.txt","w")
    for cpf,dados in dic.items():
        arq.write(f"{cpf}\n")
        arq.write(f"{dados['data entrada']}\n")
        arq.write(f"{dados['data saida']}\n")
        arq.write(f"{dados['codigo veiculo']}\n")
        arq.write(f"****************************\n")
    arq.close()

def carregarAluguel():
    dic = {}
    if not os.path.exists("alugueis.txt"):
        return dic
    arq = open("alugueis.txt", "r")
    linhas = [linha.strip() for linha in arq]
    for i in range(0, len(linhas),5):
        cpf = linhas[i]
        dic[cpf] = {
            "data entrada": linhas[i+1],
            "data saida": linhas[i+2],
            "codigo veiculo": linhas[i+3]
        }
    arq.close()
    return dic

def reservas_cliente(dicio_cliente, dicio_veiculo, dicio_alugueis): 
    # Evitar o print de dados de um cliente mais de uma vez caso ele tenha alugado o mesmo carro várias vzs
    # 1 - mostrar todos os dados de um aluguel de acordo com um cpf de um cliente (todos os carros que o cliente alugou)
    valor = 1
    while valor != 4:
        valor = submenu_Relatórios()
        if valor == 1:
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_alugueis:
                print(f"CPF: {cpf}")
                for i in dicio_alugueis[cpf]: #ainda vai precisar de ajustes
                    print(f"Data do aluguel: {dicio_alugueis[cpf]['data entrada']}")
                    print(f"Data de devolução: {dicio_alugueis[cpf]['data saida']}")
                    print(f"Veículo alugado: {dicio_alugueis[cpf]['codigo veiculo']}")
                    print("***********************************")
            else:
                print("CPF não encontrado no sistema.")
        
        elif valor == 2:
            veiculo = input("Insira o nome do veículo: ").strip()
            codigo_encontrado = []
            encontrou = False

            for codigo, dados_veiculo in dicio_veiculo.items():
                if dados_veiculo["Modelo"].lower() == veiculo.lower() and encontrou == False:
                    codigo_encontrado.append(codigo)
                    encontrou = True
            
            if not encontrou:
                print(f"O veículo de nome {veiculo} não foi encontrado no sistema.")
            
            cpfs_encontrados = []
            for cpf, dados_alugueis in dicio_alugueis.items():
                if dados_alugueis['codigo veiculo'] == codigo_encontrado[0]:
                    cpfs_encontrados.append(cpf)
            
            if len(cpfs_encontrados) == 0:
                print("O veículo não foi alugado por nenhum cliente.")
            
            elif len(cpfs_encontrados) != 0 and encontrou == True:
                print("/---Dados do veículo---/")
                print(f"Modelo: {dicio_veiculo[codigo_encontrado[0]]['Modelo']}")
                print(f"Código: {codigo_encontrado[0]}")
                print(f"Descrição: {dicio_veiculo[codigo_encontrado[0]]['Descrição']}")
                print(f"Categoria: {dicio_veiculo[codigo_encontrado[0]]['Categoria']}")
                print(f"Capacidade: {dicio_veiculo[codigo_encontrado[0]]['Capacidade']}")
                print(f"Combustível: {dicio_veiculo[codigo_encontrado[0]]['Combustível']}")
                print(f"Ano: {dicio_veiculo[codigo_encontrado[0]]['Ano']}")
                print("-" *10)
                print()
                for cpf in cpfs_encontrados:
                    for i in dicio_cliente:
                        if cpf == i:
                            print("/---Dados do cliente---/")
                            print(f"Nome: {dicio_cliente[i]['Nome']}")
                            print(f"CPF: {i}")
                            print(f"Endereço: {dicio_cliente[i]['Endereço']}")
                            print(f"Telefone fixo: {dicio_cliente[i]['Telefone fixo']}")
                            print(f"Telefone celular: {dicio_cliente[i]['Telefone celular']}")
                            print(f"Data de nascimento: {dicio_cliente[i]['Data de nascimento']}")
                            print("-" * 10)
                            print()
        
        elif valor == 3:
            data_inicio = input("Indique a data de início a ser procurada no formato dd/mm/aa: ")
            data_fim = input("Indique a data de fim a ser procurada no formato dd/mm/aa: ")
            if verificacao_data(data_inicio) and verificacao_data(data_fim):
                lista_veiculos = []
                lista_clientes = []
                for i in dicio_alugueis:
                    if dicio_alugueis[i]['data entrada'] >= data_inicio and dicio_alugueis[i]['data saida'] <= data_fim:
                        lista_veiculos.append(dicio_alugueis[i]['codigo veiculo'])
                        lista_clientes.append(i)
                    
                if lista_veiculos == 0:
                    print("Não houve nenhum aluguel realizado nesse período de tempo.")

                for j in range(len(lista_veiculos)):
                    if lista_veiculos[j] in dicio_veiculo:
                        print("/--Dados do veículo--/")
                        print(f"Código do veículo: {lista_veiculos[j]}")
                        print(f"Modelo: {dicio_veiculo[lista_veiculos[j]]['Modelo']}")
                        print(f"Descrição: {dicio_veiculo[lista_veiculos[j]]['Descrição']}")
                        print(f"Categoria: {dicio_veiculo[lista_veiculos[j]]['Categoria']}")
                        print(f"Capacidade: {dicio_veiculo[lista_veiculos[j]]['Capacidade']}")
                        print(f"Combustível: {dicio_veiculo[lista_veiculos[j]]['Combustível']}")
                        print(f"Ano: {dicio_veiculo[lista_veiculos[j]]['Ano']}")
                        print("-" * 10)
                        print()
                        print("/--Dados do cliente--/")
                        print(f"Nome: {dicio_cliente[lista_clientes[j]]['Nome']}")
                        print(f"CPF: {lista_clientes[j]}")
                        print()
            else:
                print("Data inválida, tente novamente.")
                
        elif valor == 4:
            print("Voltando ao menu principal.")

def opcoes_aluguel(dicio_alugueis, dicio_clientes, dicio_veiculos):
    valor = 1
    while valor != 6:  
        valor = submenu_aluguel()
        if valor ==1:
            print("Dados de todos os alugueis: ")
            if len(dicio_alugueis) != 0:
                for cpf in dicio_alugueis:
                    print(f"CPF: {cpf}")
                    print(f"Data do início: {dicio_alugueis[cpf]['data entrada']}")
                    print(f"Data do fim: {dicio_alugueis[cpf]['data saida']}")
                    print(f"Veículo alugado: {dicio_alugueis[cpf]['codigo veiculo']}")
                    print("***********************************")
            else:
                print("O banco de dados encontra-se vazio")

        elif valor == 2:
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_alugueis:
                print(f"CPF: {cpf}")
                print(f"Data de início: {dicio_alugueis[cpf]['data entrada']}")
                print(f"Data de fim: {dicio_alugueis[cpf]['data saida']}")
                print(f"Veículo alugado: {dicio_alugueis[cpf]['codigo veiculo']}")
            else:
                print("CPF não encontrado no sistema.")

        elif valor == 3:  #melhorei o sistema de input de alugueis
            dados_aluguel = {}
            print("Realização de aluguel")
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_clientes:         
                dataEntrada = input("Insira a data de entrada do aluguel no formato dd/mm/aaaa: ")
                dataSaida = input("Insira a data de saída do aluguel no formato dd/mm/aaaa: ")
                if verificacao_data(dataEntrada) and verificacao_data(dataSaida):
                    veiculo = input("Insira o nome do veículo: ")

                    if veiculo in dicio_veiculos:
                        dados_aluguel["data entrada"] = dataEntrada
                        dados_aluguel["data saida"] = dataSaida
                        dados_aluguel["codigo veiculo"] = veiculo
                        dicio_alugueis[cpf] = dados_aluguel
                        salvarAluguel(dicio_alugueis)
                        print("Aluguel concluído com sucesso!")
                    else:
                        print("Veículo não encontrado no sistema.")
                else:
                    print("O formato da data é inválido, tente novamente.")
            else:
                print("CPF não encontrrado no sistema.")
         
        elif valor == 4: #alterado
            op = alterar_aluguel()
            cpf = input("CPF do cliente: ")
            if cpf in dicio_alugueis:
                if op == 1:
                    nova_data_entrada = input("Informe a nova data de entrada do aluguel no formato dd/mm/aaaa: ") 
                    if verificacao_data(nova_data_entrada):
                        dicio_alugueis[cpf]["data entrada"] = nova_data_entrada
                        salvarAluguel(dicio_alugueis)
                        print("Nova data de entrada adicionada!")
                    else:
                        print("Fromato de data inválido, tente novamente.")
                elif op == 2:
                    nova_data_saida = input("Informe a nova data de entrada do aluguel no formato dd/mm/aaaa: ")
                    if verificacao_data(nova_data_saida):
                        dicio_alugueis[cpf]["data saida"] = nova_data_saida
                        salvarAluguel(dicio_alugueis)
                        print("Nova data de saída adicionada!")
                    else:
                        print("Formato de data inválido, tente novamente.")

                elif op == 3:
                    novo_veiculo = input("Insira o código do novo veículo: ")
                    if novo_veiculo in dicio_veiculos:
                        dicio_alugueis[cpf]["codigo veiculo"] = novo_veiculo
                        salvarAluguel(dicio_alugueis)
                    else:
                        print("Veículo não encontrado no sistema.")
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
    print("1 - Data de entrada do aluguel")
    print("2 - Data de saída do aluguel")
    print("3 - Veículo alugado")
    op = int(input("Insira uma das opções a cima: "))
    return op
    
def opcoes_cliente(dic): 
    valor = 1
    while valor != 6:
        valor = submenu_cliente()
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
                print(f"Nome: {dic[cpf]['Nome']}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {dic[cpf]['Endereço']}")
                print(f"Telefone fixo: {dic[cpf]['Telefone fixo']}")
                print(f"Telefone celular: {dic[cpf]['Telefone celular']}")
                print(f"Data de nascimento: {dic[cpf]['Data de nascimento']}")
            else:
                print("Usuário não encontrado.")

        elif valor == 3:  
            dados_clientes = {}
            print("Incluir cliente no sistema")
            cpf = input("CPF: ")
            if cpf not in dic:
                nome = input("Nome completo: ")
                endereco = input("Endereço: ")
                telefone_fix = input("Telefone fixo: ")
                cel = input("Telefone celular: ")
                data_nasc = input("Data de nascimento: ")
                if verificacao_data(data_nasc):
                    dados_clientes["Nome"] = nome
                    dados_clientes["Endereço"] = endereco
                    dados_clientes["Telefone fixo"] = telefone_fix
                    dados_clientes["Telefone celular"] = cel
                    dados_clientes["Data de nascimento"] = data_nasc
                    dic[cpf] = dados_clientes
                    salvarCliente(dic)
                    print("Cliente cadastrado com sucesso!")
                else:
                    print("Data inválida, tente novamente.")
            else:
                print("CPF já cadastrado. ")

        elif valor == 4:
            op = alterar_cilente()
            cpf = input("CPF do cliente: ")
            if cpf in dic:
                if op == 1:
                    novo_nome = input("Novo nome: ")
                    dic[cpf]["Nome"] = novo_nome
                    salvarCliente(dic)
                    print("Nome alterado com sucesso!")
                elif op == 2:
                    novo_endereco = input("Novo endereço: ")
                    dic[cpf]["Endereço"] = novo_endereco
                    salvarCliente(dic)
                    print("Endereço alterado com sucesso!")
                elif op == 3:
                    novo_tel_fix = input("Novo telefone fixo: ")
                    dic[cpf]["Telefone fixo"] = novo_tel_fix
                    salvarCliente(dic)
                    print("Telefone fixo alterado com sucesso!")
                elif op == 4:
                    novo_cel = input("Novo telefone celular: ")
                    dic[cpf]["Telefone celular"] = novo_cel
                    salvarCliente(dic)
                    print("Telefone celular alterado com sucesso!")
                elif op == 5:
                    nova_data = input("Nova data de nascimento: ")
                    if verificacao_data(nova_data):
                        dic[cpf]["Data de nascimento"] = nova_data
                        salvarCliente(dic)
                        print("Data de nascimento alterada com sucesso!")
                    else:
                        print("Data inválida, tente novamente.")
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

def opcoes_veiculo(dic): #concertei o erro do while e do valor
    # O valor tem que começar igual a um pra estrutura de repetição funcionar do jeito certo (o exemplo da Elô tá igual a isso)
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
                    print("************************************************")
        
        elif valor == 2:
            codigo = input("Informe o código do veículo: ")
            if codigo in dic:
                print(dic[codigo])
            else:
                print("Veículo não encontrado.")

        elif valor == 3:
            dados_veiculos = {}
            print("Incluir veículo no sistema...")
            codigo = input("Código: ")
            if codigo not in dic:
                desc = input("Descrição: ")
                categ = input("Categoria: ")
                capac = input("Capacidade: ")
                combustivel = input("Combustível: ")
                ano = int(input("Ano: "))
                if ano > 2025:
                    print("Ano inválido, tente novamente.")  
                else:
                    modelo = input("Modelo: ")
                    dados_veiculos["Descrição"] = desc
                    dados_veiculos["Categoria"] = categ
                    dados_veiculos["Capacidade"] = capac
                    dados_veiculos["Combustível"] = combustivel
                    dados_veiculos["Ano"] = ano
                    dados_veiculos["Modelo"] = modelo
                    dic[codigo] = dados_veiculos
                    salvarVeiculo(dic)
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
                    salvarVeiculo(dic)
                    print("Descrição alterada com sucesso!")

                elif op == 2:
                    nova_categ = input("Nova categoria: ")
                    dic[codigo]["Categoria"] = nova_categ
                    salvarVeiculo(dic)
                    print("Categoria alterada com sucesso!")

                elif op == 3:
                    nova_capac = input("Nova capacidade: ")
                    dic[codigo]["Capacidade"] = nova_capac
                    salvarVeiculo(dic)
                    print("Capacidade alterada com sucesso!")

                elif op == 4:
                    novo_combustivel = input("Novo combustível: ")
                    dic[codigo]["Combustível"] = novo_combustivel
                    salvarVeiculo(dic)
                    print("Combustível alterado com sucesso!")

                elif op == 5:
                    novo_ano = input("Novo ano: ")
                    if ano > 2025:
                        print("Ano inválido, tente novamente.")
                    else:
                        dic[codigo]["Ano"] = novo_ano
                        salvarVeiculo(dic)
                        print("Ano alterado com sucesso!")

                elif op == 6:
                    novo_modelo = input("Novo modelo: ")
                    dic[codigo]["Modelo"] = novo_modelo
                    salvarVeiculo(dic)
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
    dic_clientes = carregarCliente()  #dados dos clientes
    dic_alugueis = carregarAluguel() #chave será o cpf do cliente e o valor o veículo alugado pelo mesmo além da data de aluguel
    dic_veiculos = carregarVeiculo() #chave é o nome do veículo e 
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
            reservas_cliente(dic_clientes, dic_veiculos, dic_alugueis)
        elif option == 5:
            print("Programa encerrado.")
        else:
            print("Opção inválida, tente novamente.")
   
main()
