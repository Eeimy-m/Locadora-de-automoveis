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
            
def conversaoData(data): # é preciso colocar a data de tras pra fernte pra comparar algumas coisas
    dia, mes, ano = data.split("/")
    return (ano+mes+dia)

def verificacao_veiculo(veiculo, dataEntrada, dataSaida, dicio_alugueis):#verifica se esse veiculo ja esta sendo aligado nesse intervalo de datas
    entrada = conversaoData(dataEntrada)
    saida = conversaoData(dataSaida)

    for lista in dicio_alugueis.values():
        for dados in lista:
            if dados['codigo veiculo'] == veiculo:
                entrada_exitente = conversaoData(dados['data entrada'])
                saida_existente = conversaoData(dados['data saida'])

                if (entrada <= saida_existente and saida >= entrada_exitente):
                    return False
    return True

def escolher_opcao_veiculo(lista_codigos, dicio_veiculos):
    cont = 0
    for i in lista_codigos:
        print(f"Opções do veiculo selecionado")
        for codigo, dados_veiculos in dicio_veiculos.items():
            if i == codigo:
                print(f"/--Opção {cont}--/")
                print(f"Descrição: {dados_veiculos['Descrição']}")
                print(f"Capacidade: {dados_veiculos['Capacidade']}")
                print(f"Combustível: {dados_veiculos['Combustível']}")
                print(f"Ano de lançamento: {dados_veiculos['Ano']}")
                print("-" * 20)
                print()
    op = int(input("Selecione uma das opções a cima: "))
    indice = op - 1
    return lista_codigos[indice] #devolve para a função o código do carro escolhido

def escolher_opção_aluguel(lista, dicio_veiculos):
    cont = 0 
    for dicionario in lista:
        cont+=1
        print(f"/--Opção {cont}--/")
        print(f"Data de aluguel: {dicionario['data entrada']}")
        print(f"Data de devolução: {dicionario['data saida']}")
        for codigo_veiculo, dados_veiculo in dicio_veiculos.items():
            if codigo_veiculo == dicionario['codigo veiculo']:
                print(f"Modelo do veículo: {dados_veiculo['Modelo']}")
        print("-" * 20)
        print()
    
    escolha = int(input("Selecione uma das opções fornecidas a cima: "))
    indice = escolha - 1
    return lista[indice]

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
    for cpf,lista in dic.items():
        for dados in lista:
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
        dados = {
            "data entrada": linhas[i+1],
            "data saida": linhas[i+2],
            "codigo veiculo": linhas[i+3]
        }

        if cpf not in dic:
            dic[cpf] = []
        dic[cpf].append(dados)
    arq.close()
    return dic

def salvarRelatorio(tipo, conteudo):
    arq = open("relatorios.txt", "a")#usando a pra add no final do arquivo sem apagar oq tinha antes
    arq.write(f"{tipo}\n") # relatorio por CPF, veiculo ou período
    arq.write(conteudo) #todos os dados dos relatorios
    arq.write("****************************\n")
    arq.close()

def carregarRelatorio():
    if not os.path.exists("relatorios.txt"):
       return
    arq = open("relatorios.txt", "r")
    linhas = [linha.strip() for linha in arq] # le todas as linhas e tira a quebra de linha (\n)
    relatorio = "" # guarda cada bloco do relatorio
    for linha in linhas:
        if linha == "****************************":
            print(relatorio) # exibe todas as infos de relatorio
            print("-"*30)
            relatorio = "" # limpa a variavel pra guardar o prox relatorio
        else:
            relatorio += linha + "\n" # se não, continua guardando as infos
    arq.close()

def reservas_cliente(dicio_cliente, dicio_veiculo, dicio_alugueis): 
    valor = 1
    while valor != 4:
        valor = submenu_Relatórios()
        if valor == 1:
            cpf = input("Insira o CPF do cliente(apenas os números): ")
            relatorio = "" #variavel pra guardar todas as infos que vai pro arquivo

            if cpf in dicio_alugueis:
                os.system('cls')
                relatorio += f"CPF: {cpf}\n"
                relatorio += f"Nome: {dicio_cliente[cpf]['Nome']}\n\n"

                print("/--Dados do aluguel feito pelo cliente--/")
                print(f"CPF: {cpf}")
                print(f"Nome: {dicio_cliente[cpf]['Nome']}")
                print()
                for i in dicio_alugueis: 
                    if i == cpf:
                        for j in dicio_alugueis[cpf]:
                            relatorio += f"Data do aluguel: {j['data entrada']}\n"
                            relatorio += f"Data de devolucao: {j['data saida']}\n"
                            relatorio += f"Codigo do veiculo: {j['codigo veiculo']}\n\n"

                            print(f"Data do aluguel: {j['data entrada']}")
                            print(f"Data de devolução: {j['data saida']}")
                            print(f"Veículo alugado: {j['codigo veiculo']}") 
                            for codigo, dados_veiculo in dicio_veiculo.items():
                                if codigo == j['codigo veiculo']:
                                    print(f"Modelo: {dicio_veiculo[codigo]['Modelo']}")
                                    print("-" * 20)
                                    print()
                salvarRelatorio("RELATORIO POR CPF", relatorio)            
            else:
                print("CPF não encontrado no sistema.")
        
        elif valor == 2:
            veiculo = input("Insira o nome do veículo: ").strip()
            codigo_encontrado = []
            encontrou = False
            relatorio = "" # variavel pra guardar todas as infos que vai pro arquivo

            for codigo, dados_veiculo in dicio_veiculo.items():
                if dados_veiculo["Modelo"].lower() == veiculo.lower():
                    codigo_encontrado.append(codigo)
                    encontrou = True

            if not encontrou:
                print(f"O veículo de nome {veiculo} não foi encontrado no sistema.")

            elif encontrou:
                cpfs_encontrados = []
                for cpf, lista_alugueis in dicio_alugueis.items():
                    for i in codigo_encontrado:
                        for dados_alugueis in lista_alugueis:
                            if dados_alugueis['codigo veiculo'] == i:
                                cpfs_encontrados.append(cpf)
                if len(cpfs_encontrados) == 0:
                    print("O veículo não foi alugado por nenhum cliente.")

                elif len(cpfs_encontrados) != 0 and encontrou == True:
                            os.system('cls')
                            for codigo in codigo_encontrado:
                                for num_veiculo, dados_veiculo in dicio_veiculo.items():
                                    if codigo == num_veiculo:
                                        dados_veiculo = dicio_veiculo[codigo]
                                        relatorio += f"Modelo: {dados_veiculo['Modelo']}\n"
                                        relatorio += f"Codigo: {codigo}\n"
                                        relatorio += f"Descricao: {dados_veiculo['Descrição']}\n"
                                        relatorio += f"Categoria: {dados_veiculo['Categoria']}\n"
                                        relatorio += f"Capacidade: {dados_veiculo['Capacidade']}\n"
                                        relatorio += f"Combustivel: {dados_veiculo['Combustível']}\n"
                                        relatorio += f"Ano: {dados_veiculo['Ano']}\n\n"

                                        print("/---Dados do veículo---/")
                                        print(f"Modelo: {dicio_veiculo[codigo]['Modelo']}")
                                        print(f"Código: {codigo}")
                                        print(f"Descrição: {dicio_veiculo[codigo]['Descrição']}")
                                        print(f"Categoria: {dicio_veiculo[codigo]['Categoria']}")
                                        print(f"Capacidade: {dicio_veiculo[codigo]['Capacidade']}")
                                        print(f"Combustível: {dicio_veiculo[codigo]['Combustível']}")
                                        print(f"Ano: {dicio_veiculo[codigo]['Ano']}")
                                        print("-" *20)
                                        print()
                                        for cpf in cpfs_encontrados:
                                            for cpf_aluguel, lista_alugueis in dicio_alugueis.items():
                                                for dicionario in lista_alugueis:
                                                    if dicionario['codigo veiculo'] == codigo:
                                                        if cpf_aluguel == cpf:
                                                            cliente = dicio_cliente[cpf]
                                                            relatorio += f"Nome: {cliente['Nome']}\n"
                                                            relatorio += f"CPF: {cpf}\n"
                                                            relatorio += f"Data de aluguel: {dicionario['data entrada']}\n"
                                                            relatorio += f"Data de devolucao: {dicionario['data saida']}\n\n"

                                                            print("/---Dados do aluguel/")
                                                            print(f"Nome: {dicio_cliente[cpf]['Nome']}")
                                                            print(f"CPF: {cpf}")
                                                            print(f"Data de aluguel: {dicionario['data entrada']}")
                                                            print(f"Data de devolução: {dicionario['data saida']}")
                                                            print("-" * 20)
                                                            print()
                            salvarRelatorio("RELATORIO POR VEICULO", relatorio)

        elif valor == 3:
            data_inicio = input("Indique a data de início a ser procurada no formato dd/mm/aa: ")
            data_fim = input("Indique a data de fim a ser procurada no formato dd/mm/aa: ")
            relatorio = "" # variavel pra guardar todas as infos que vai pro arquivo

            if verificacao_data(data_inicio) and verificacao_data(data_fim):
                data_inicio_convertida = conversaoData(data_inicio)
                data_fim_convertida = conversaoData(data_fim)
                relatorio = ""
                lista_veiculos = []
                lista_clientes = []
                for cpf, lista_alugueis in dicio_alugueis.items():
                    for i in lista_alugueis:
                        data_convertida_in = conversaoData(i['data entrada'])
                        data_convertida_out = conversaoData(i['data saida'])
                        if data_convertida_in >= data_inicio_convertida and data_convertida_out <= data_fim_convertida:
                            lista_veiculos.append(i['codigo veiculo'])
                            lista_clientes.append(cpf)
                    
                if len(lista_veiculos) == 0:
                    print("Não houve nenhum aluguel realizado nesse período de tempo.")
        
                for j in range(len(lista_veiculos)):
                    os.system('cls')
                    if lista_veiculos[j] in dicio_veiculo:
                        relatorio += "/--Dados do veiculo--/\n"
                        relatorio += f"Codigo do veiculo: {lista_veiculos[j]}\n"
                        relatorio += f"Modelo: {dicio_veiculo[lista_veiculos[j]]['Modelo']}\n"
                        relatorio += f"Descricao: {dicio_veiculo[lista_veiculos[j]]['Descrição']}\n"
                        relatorio += f"Categoria: {dicio_veiculo[lista_veiculos[j]]['Categoria']}\n"
                        relatorio += f"Capacidade: {dicio_veiculo[lista_veiculos[j]]['Capacidade']}\n"
                        relatorio += f"Combustivel: {dicio_veiculo[lista_veiculos[j]]['Combustível']}\n"
                        relatorio += f"Ano: {dicio_veiculo[lista_veiculos[j]]['Ano']}\n"
                        relatorio += "-------------\n"

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
                        for j in range(len(lista_clientes)):
                            for cpf in dicio_cliente:
                                if cpf == lista_clientes[j]:
                                    relatorio += "/--Dados do Cliente--/\n"
                                    relatorio += f"Nome: {dicio_cliente[cpf]['Nome']}\n"
                                    relatorio += f"CPF: {cpf}\n"
                                    relatorio += f"Endereço: {dicio_cliente[cpf]['Endereço']}\n"
                                    relatorio += f"Telefone fixo: {dicio_cliente[cpf]['Telefone fixo']}\n"
                                    relatorio += f"Telefone celular: {dicio_cliente[cpf]['Telefone celular']}\n"
                                    relatorio += f"Data de nascimento: {dicio_cliente[cpf]['Data de nascimento']}\n"
                                    relatorio += "-------------\n"

                                    print(f"Nome: {dicio_cliente[cpf]['Nome']}")
                                    print(f"CPF: {cpf}")
                                    print(f"Endereço: {dicio_cliente[cpf]['Endereço']}")
                                    print(f"Telefone fixo: {dicio_cliente[cpf]['Telefone fixo']}")
                                    print(f"Telefone celular: {dicio_cliente[cpf]['Telefone celular']}")
                                    print(f"Data de nascimento: {dicio_cliente[cpf]['Data de nascimento']}")
                                    print()
                                    for documento, dados_alugueis in dicio_alugueis.items():
                                        if documento == cpf:
                                            for dado in dados_alugueis:
                                                relatorio += "/--Dados do aluguel--/\n"
                                                relatorio += f"Data de aluguel: {dado['data entrada']}\n"
                                                relatorio += f"Data de devolucao: {dado['data saida']}\n\n"


                                                print("/--Dados do aluguel--/")
                                                print(f"Data de aluguel: {dado['data entrada']}")
                                                print(f"Data de devolução: {dado['data saida']}")
                                                print("-" * 20)
                                                print()
                salvarRelatorio("RELATORIO POR PERIODO", relatorio)
            else:
                print("Data inválida, tente novamente.")
                
        elif valor == 4:
            os.system('cls')
            print("Voltando ao menu principal.")
        
        else:
            print("Opção inválida, tente novamente.")

def opcoes_aluguel(dicio_alugueis, dicio_clientes, dicio_veiculos):
    valor = 1
    while valor != 6:  
        valor = submenu_aluguel()
        if valor ==1:
            os.system('cls')
            print("/--Dados de todos os alugueis--/")
            if len(dicio_alugueis) != 0:
                for cpf, lista_dados in dicio_alugueis.items():
                        for aluguel in lista_dados:
                            print(f"CPF: {cpf}")
                            print(f"Data do início: {aluguel['data entrada']}")
                            print(f"Data do fim: {aluguel['data saida']}")
                            print(f"Veículo alugado: {aluguel['codigo veiculo']}")
                            for j in dicio_veiculos:
                                if j == aluguel['codigo veiculo']:
                                    print(f"Modelo: {dicio_veiculos[j]['Modelo']}")
                            print("-" * 10)
            else:
                print("O banco de dados encontra-se vazio")

        elif valor == 2:
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_alugueis:
                os.system('cls')
                print(f"/--Dados do aluguel do cliente de CPF {cpf}--/")
                print(f"Nome: {dicio_clientes[cpf]['Nome']}")
                print()
                for documento, lista_dados in dicio_alugueis.items():
                    if documento == cpf:
                        for aluguel in lista_dados:
                            print(f"Data de início: {aluguel['data entrada']}")
                            print(f"Data de fim: {aluguel['data saida']}")
                            print(f"Veículo alugado: {aluguel['codigo veiculo']}")
                            for i in dicio_veiculos:
                                if i == aluguel['codigo veiculo']:
                                    print(f"Modelo: {dicio_veiculos[i]['Modelo']}")
                                    print("-" * 10)
                                    print()
            else:
                print("CPF não encontrado no sistema.")

        elif valor == 3:  
            dados_aluguel = {}
            os.system('cls')
            print("/--Realização de aluguel--/")
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dicio_clientes:         
                dataEntrada = input("Insira a data de entrada do aluguel no formato dd/mm/aaaa: ")
                dataSaida = input("Insira a data de saída do aluguel no formato dd/mm/aaaa: ")
                if conversaoData(dataSaida) > conversaoData(dataEntrada): # a data de saida tem que ser maior que a data de entrada
                    if verificacao_data(dataEntrada) and verificacao_data(dataSaida):
                        veiculo = input("Insira o modelo do veiculo a ser alugado: ")
                        lista_veiculos = []
                        encontrou = False
                        for codigo, dados_veiculo in dicio_veiculos.items():
                            if dados_veiculo["Modelo"].lower() == veiculo.lower():
                                lista_veiculos.append(codigo)
                                encontrou = True
                        if len(lista_veiculos) > 1:
                            escolha = escolher_opcao_veiculo(lista_veiculos, dicio_veiculos) 
                        else:
                            escolha = lista_veiculos[0]

                        if escolha in dicio_veiculos:
                            if verificacao_veiculo(veiculo,dataEntrada,dataSaida,dicio_alugueis):
                                dados_aluguel["data entrada"] = dataEntrada
                                dados_aluguel["data saida"] = dataSaida
                                dados_aluguel["codigo veiculo"] = escolha
                                if cpf not in dicio_alugueis:
                                    dicio_alugueis[cpf] = [] #para ter varios alugueis no mesmo cpf
                                dicio_alugueis[cpf].append(dados_aluguel)
                                salvarAluguel(dicio_alugueis)
                                os.system('cls')
                                print("Aluguel concluído com sucesso!")
                            else:
                                print("Veículo ja alugado para esta data.")
                        else:
                            print("Veículo não encontrado no sistema.")
                    else:
                        print("O formato da data é inválido, tente novamente.")
                else:
                    print("O formato da data é inválido, tente novamente.")
            else:
                print("CPF não encontrrado no sistema.")
         
        elif valor == 4: 
            op = alterar_aluguel()
            cpf = input("CPF do cliente: ")
            alugueis_encontrados = []
            for cpf_aluguel, lista_alugueis in dicio_alugueis.items():
                for aluguel in lista_alugueis:
                    if cpf_aluguel == cpf:
                        alugueis_encontrados.append(aluguel) #A vatiável aluguel é um dicionário
            if cpf in dicio_clientes:
                if len(alugueis_encontrados) > 1:                
                    opcao_aluguel = escolher_opção_aluguel(alugueis_encontrados, dicio_veiculos) #a função retorna um dicionário
                    for cpf_aluguel, lista_alugueis in dicio_alugueis.items():
                        if cpf == cpf_aluguel:  
                            for aluguel in lista_alugueis:
                                if opcao_aluguel == aluguel:
                                    if op == 1:
                                        nova_data_entrada = input("Informe a nova data de entrada do aluguel no formato dd/mm/aaaa: ") 
                                        if verificacao_data(nova_data_entrada):
                                            aluguel["data entrada"] = nova_data_entrada
                                            salvarAluguel(dicio_alugueis)
                                            os.system('cls')
                                            print("Nova data de entrada adicionada!")
                                        else:
                                            print("Fromato de data inválido, tente novamente.")
                                    elif op == 2:
                                        nova_data_saida = input("Informe a nova data de saída do aluguel no formato dd/mm/aaaa: ")
                                        if verificacao_data(nova_data_saida):
                                            aluguel["data saida"] = nova_data_saida
                                            salvarAluguel(dicio_alugueis)
                                            os.system('cls')
                                            print("Nova data de saída adicionada!")
                                        else:
                                            print("Formato de data inválido, tente novamente.")

                                    elif op == 3: #preciso alterar
                                        novo_veiculo = input("Insira o nome do novo veículo: ")
                                        lista_veiculos = []
                                        encontrou = False
                                        for codigo, dados_veiculo in dicio_veiculos.items():
                                            if dados_veiculo["Modelo"].lower() == novo_veiculo.lower():
                                                lista_veiculos.append(codigo)
                                                encontrou = True

                                        if len(lista_veiculos) > 1:
                                            escolha = escolher_opcao_veiculo(lista_veiculos, dicio_veiculos)
                                            for codigo in dicio_veiculos: 
                                                if codigo == escolha:
                                                    aluguel['codigo veiculo'] = escolha
                                                    salvarAluguel(dicio_alugueis)
                                                    print("Veículo atualizado com sucesso!")

                                        elif len(lista_veiculos) == 1:
                                            for codigo, dados_veiculo in dicio_veiculos.items():
                                                if lista_veiculos[0] == codigo:
                                                    aluguel["codigo veiculo"] = codigo
                                                    salvarAluguel(dicio_alugueis)
                                                    print("Veículo atualizado com sucesso!")
                                        
                                        else:
                                            print("Não foi possível concluir a atualização do veículo.")

                elif len(alugueis_encontrados) == 1:
                    if op == 1:
                        nova_data_entrada = input("Informe a nova data de entrada do aluguel no formato dd/mm/aaaa: ") 
                        if verificacao_data(nova_data_entrada):
                            aluguel["data entrada"] = nova_data_entrada
                            salvarAluguel(dicio_alugueis)
                            os.system('cls')
                            print("Nova data de entrada adicionada!")
                        else:
                            print("Fromato de data inválido, tente novamente.")
                    elif op == 2:
                        nova_data_saida = input("Informe a nova data de entrada do aluguel no formato dd/mm/aaaa: ")
                        if verificacao_data(nova_data_saida):
                            aluguel["data saida"] = nova_data_saida
                            salvarAluguel(dicio_alugueis)
                            os.system('cls')
                            print("Nova data de saída adicionada!")
                        else:
                            print("Formato de data inválido, tente novamente.")

                    elif op == 3: 
                        novo_veiculo = input("Insira o nome do novo veículo: ")
                        lista_veiculos = []
                        encontrou = False
                        for codigo, dados_veiculo in dicio_veiculos.items():
                            if dados_veiculo["Modelo"].lower() == novo_veiculo.lower():
                                lista_veiculos.append(codigo)
                                encontrou = True

                        if len(lista_veiculos) > 1:
                            escolha = escolher_opcao_veiculo(lista_veiculos, dicio_veiculos) 
                            for cpf_aluguel, lista_alugueis in dicio_alugueis.items():
                                if cpf == cpf_aluguel:  
                                    for aluguel in lista_alugueis:
                                        if opcao_aluguel == aluguel:
                                            if aluguel['Modelo'] == novo_veiculo.lower():
                                                aluguel['codigo veiculo'] = escolha
                                                salvarAluguel(dicio_alugueis)
                                                print("Veículo atualizado com sucesso!")

                        elif len(lista_veiculos) == 1:
                            for codigo, dados_veiculo in dicio_veiculos.items():
                                for cpf_aluguel, lista_alugueis in dicio_alugueis.items():
                                    if cpf == cpf_aluguel:  
                                        for aluguel in lista_alugueis:
                                            if opcao_aluguel == aluguel:
                                                if lista_veiculos[0] == dados_veiculo['Modelo'].lower():
                                                    if aluguel['Nome'] == novo_veiculo.lower():
                                                        aluguel["codigo veiculo"] = codigo
                                                        salvarAluguel(dicio_alugueis)
                                                        print("Veículo atualizado com sucesso!")
                            
                        else:
                            print("Não foi possível concluir a atualização do veículo.")                    

            else:
                print("CPF não encontrado.")
        
        elif valor == 5:
            cpf = input("Informe o CPF do cliente: ")
            if cpf in dicio_alugueis:
                del dicio_alugueis[cpf]
                salvarAluguel(dicio_alugueis)
                print("Aluguel excluído do sistema com sucesso.")
            else:
                print("CPF não encontrado no sistema.")
        
        elif valor == 6:
            os.system('cls')
            print("Voltando ao menu principal.")
        
        else:
            os.system('cls')
            print("Opção inválida, tente novamente.")
            
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
                os.system('cls')
                print("Dados de todos os clientes:")
                for cpf in dic:
                    print(f"CPF: ", cpf)
                    print(f"Nome completo: {dic[cpf]['Nome']}")
                    print(f"Endereço: {dic[cpf]['Endereço']}")
                    print(f"Telefone fixo: {dic[cpf]['Telefone fixo']}")
                    print(f"Telefone celular: {dic[cpf]['Telefone celular']}")
                    print(f"Data de nascimento: {dic[cpf]['Data de nascimento']}")
                    print("-" * 20)
            else:
                print("Não há clientes cadastrados.")

        elif valor == 2:
            cpf = input("Insira o CPF do cliente: ")
            if cpf in dic:
                os.system('cls')
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
                    os.system('cls')
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
                    os.system('cls')
                    print("Nome alterado com sucesso!")
                elif op == 2:
                    novo_endereco = input("Novo endereço: ")
                    dic[cpf]["Endereço"] = novo_endereco
                    salvarCliente(dic)
                    os.system('cls')
                    print("Endereço alterado com sucesso!")
                elif op == 3:
                    novo_tel_fix = input("Novo telefone fixo: ")
                    dic[cpf]["Telefone fixo"] = novo_tel_fix
                    salvarCliente(dic)
                    os.system('cls')
                    print("Telefone fixo alterado com sucesso!")
                elif op == 4:
                    novo_cel = input("Novo telefone celular: ")
                    dic[cpf]["Telefone celular"] = novo_cel
                    salvarCliente(dic)
                    os.system('cls')
                    print("Telefone celular alterado com sucesso!")
                elif op == 5:
                    nova_data = input("Nova data de nascimento: ")
                    if verificacao_data(nova_data):
                        dic[cpf]["Data de nascimento"] = nova_data
                        salvarCliente(dic)
                        os.system('cls')
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
                salvarCliente(dic)
                os.system('cls')
                print("Cliente excluído com sucesso!")
            else:
                print("CPF não cadastrado.")

        elif valor == 6:
            os.system('cls')
            print("Saindo do submenu.")
        
        else:
            print("Opção inválida, tente novamente.")
            
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
                os.system('cls')
                for codigo in dic:
                    print(f"Código: {codigo}")
                    print(f"Descrição: {dic[codigo]['Descrição']}")
                    print(f"Categoria: {dic[codigo]['Categoria']}")
                    print(f"Capacidade: {dic[codigo]['Capacidade']}")
                    print(f"Combustível: {dic[codigo]['Combustível']}")
                    print(f"Ano: {dic[codigo]['Ano']}")
                    print(f"Modelo: {dic[codigo]['Modelo']}")
                    print("-" * 20)
        
        elif valor == 2:
            veiculo = input("Informe o nome do veículo: ").strip()
            codigo_encontrado = []
            encontrou = False
            for codigo, dados_veiculo in dic.items():
                if dados_veiculo["Modelo"].lower() == veiculo.lower():
                    codigo_encontrado.append(codigo)
                    encontrou = True

            if not encontrou:
                print(f"O veículo de nome {veiculo} não foi encontrado no sistema.")
            
            elif encontrou: 
                if len(codigo_encontrado) > 1:
                    codigo_escolhido = escolher_opcao_veiculo(codigo_encontrado, dic)
                    print("/--Dados do veículo--/")
                    print(f"Código: {codigo_escolhido}")
                    print(f"Modelo: {dic[codigo_escolhido]['Modelo']}")
                    print(f"Descrição: {dic[codigo_escolhido]['Descrição']}")
                    print(f"Categoria: {dic[codigo_escolhido]['Categoria']}")
                    print(f"Capacidade: {dic[codigo_escolhido]['Capacidade']}")
                    print(f"Combustível: {dic[codigo_escolhido]['Combustível']}")
                    print(f"Ano: {dic[codigo_escolhido]['Ano']}")
                    print("-" * 20)
                    print()
                else:
                    print("/--Dados do veículo--/")
                    print(f"Código: {codigo}")
                    print(f"Modelo: {dic[codigo]['Modelo']}")
                    print(f"Descrição: {dic[codigo]['Descrição']}")
                    print(f"Categoria: {dic[codigo]['Categoria']}")
                    print(f"Capacidade: {dic[codigo]['Capacidade']}")
                    print(f"Combustível: {dic[codigo]['Combustível']}")
                    print(f"Ano: {dic[codigo]['Ano']}")
                    print("-" * 20)
                    print()


        elif valor == 3:
            dados_veiculos = {}
            print("/--Incluir veículo no sistema--/")
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
                    os.system('cls')
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
                    os.system('cls')
                    print("Descrição alterada com sucesso!")

                elif op == 2:
                    nova_categ = input("Nova categoria: ")
                    dic[codigo]["Categoria"] = nova_categ
                    salvarVeiculo(dic)
                    os.system('cls')
                    print("Categoria alterada com sucesso!")

                elif op == 3:
                    nova_capac = input("Nova capacidade: ")
                    dic[codigo]["Capacidade"] = nova_capac
                    salvarVeiculo(dic)
                    os.system('cls')
                    print("Capacidade alterada com sucesso!")

                elif op == 4:
                    novo_combustivel = input("Novo combustível: ")
                    dic[codigo]["Combustível"] = novo_combustivel
                    salvarVeiculo(dic)
                    os.system('cls')
                    print("Combustível alterado com sucesso!")

                elif op == 5:
                    novo_ano = input("Novo ano: ")
                    if ano > 2025:
                        print("Ano inválido, tente novamente.")
                    else:
                        dic[codigo]["Ano"] = novo_ano
                        salvarVeiculo(dic)
                        os.system('cls')
                        print("Ano alterado com sucesso!")

                elif op == 6:
                    novo_modelo = input("Novo modelo: ")
                    dic[codigo]["Modelo"] = novo_modelo
                    salvarVeiculo(dic)
                    os.system('cls')
                    print("Modelo alterado com sucesso!")

                else:
                    os.system('cls')
                    print("Opção Inválida.")

            else:
                os.system('cls')
                print("Código não encontrado.")

        elif valor == 5:
            codigo = input("Informe o código do veículo a ser excluído: ")
            if codigo in dic:
                del dic[codigo]
                salvarVeiculo(dic)
                os.system('cls')
                print("Veículo excluído com sucesso!")
            else:
                os.system('cls')
                print("Veículo não cadastrado.")

        elif valor == 6:
            os.system('cls')
            print("Saindo do submenu.")
        
        else:
            os.system('cls')
            print("Opção inválida, tente novamente.")

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
    dic_relatorios = carregarRelatorio()
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