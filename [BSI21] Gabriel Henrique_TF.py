### -------------------------- ALGORITMOS E PROGRAMAÇÃO II -------------------------- ###
### --------------------- [BSI 21] GABRIEL HENRIQUE DE OLIVEIRA --------------------- ###
###-----------------------------------------------------------------------------------###
### ---------------------- TRABALHO FINAL - AGENDA DE CONTATOS ---------------------- ###

# Função MENU - exibe opções do Menu
def menu (op):
    if op == '0':
        print("""
    MENU
    ----------------------------------------
    0 - SAIR
    1 - Adicionar Novo Contato
    2 - Total de Contatos Gravados na Agenda
    3 - Listar Contatos à Gravar na Agenda
    4 - Gravar Contatos na Agenda
    5 - Listar Todos os Contatos Gravados
    ----------------------------------------
    """)

# Função NOVO CONTATO - adiciona contantos em loop em uma lista auxiliar
contatos_temp = [] ### Lista GLOBAL
def novo_contato (n):
    while True:
        if n == '1':
            print("")
            nome_contato = input("Insira o nome do contato: ")
            telefone = input("Insira o telefone do contato: (somente números) ")
            contatos_temp.append(nome_contato + " - " + telefone)
            print("")
            n = input("Deseja adicionar outro contato? (1)Sim ou (2)Não: ")
        elif n == '2':
            print(f"{len(contatos_temp)} contato(s) adicionado(s).")
            break
        else:
            print("Opção Inválida!")
            n = input("Digite (1) para SIM ou (2) para NÃO! ")
            continue

# Função TOTAL CONTATOS - exibe número total de contatos gravados no arquivo 'agenda.txt'
A = 0 ## GLOBAL
def total_contatos (x):
    cont = 0
    with open ("agenda.txt","r") as contatos:
        for linha in contatos:
            cont += 1
        global A
        A = cont
        print(cont,"contato(s).")

# Função LISTA CONTATOS - exibe os contatos à serem gravados no arquivo 'agenda.txt'
def lista_contatos (x):
    if x == '3':
        if len(contatos_temp) > 0:
            for i in range (len(contatos_temp)):
                print(contatos_temp[i])
            print("-----------------------------")
            print(f"{len(contatos_temp)} contato(s).")
        else:
            print("Nenhum contato à ser gravado!")

# Função GRAVA ARQUIVO - grava os contatos temporários no arquivo 'agenda.txt'
def grava_arquivo (x):
    while True:
        if x == '1':
            arquivo = open ("agenda.txt", "a")
            for i in range (len(contatos_temp)):
                arquivo.write(contatos_temp[i] + '\n')
            arquivo.close
            print(f"{len(contatos_temp)} contato(s) gravado(s).")
            # Limpando Lista Global auxiliar de contatos à serem gravados
            contatos_temp.clear()
            break
        elif x == '2':
            print("Contatos NÃO FORAM GRAVADOS!")
            break
        else:
            print("Opção Inválida!")
            x = input("GRAVAR CONTATOS: (1) SIM ou (2) NÃO --> ")
            continue

# Função LÊ ARQUIVO - lista os contatos gravados no arquivo 'agenda.txt'
# def le_arquivo (x):
#     if x == '5':
#         total_contatos(2)
#         print("")
#         with open ("agenda.txt", "r") as contatos:
#             aux = contatos.readlines()
#             for i in range(A):
#                 print(aux[i])

def le_arquivo (x):
    if x == '5':
        print("")
        with open ("agenda.txt", "r") as contatos:
            aux = contatos.readline()
            while aux:
                linha = aux.split()
                print(f"{linha[0]} {linha[1]} {linha[2]}")
                aux = contatos.readline()
        print("")
        print("---------------------")

op_menu = '0'
while True:
    menu(op_menu)
    arquivo = open ("agenda.txt", "a")
    opcao = input("Insira a opção desejada: ")
    
    # Opção SAIR
    if opcao == '0':
        print("")
        print("-#-#-#-#-#-#-#- Até a Próxima! -#-#-#-#-#-#-#-")
        break

    # Opção NOVO CONTATO
    elif opcao == '1':
        print("")
        print("Cadastro de NOVO CONTATO:")
        print("-------------------------------")
        novo_contato(opcao)
    
    # Opção TOTAL CONTATOS GRAVADOS
    elif opcao == '2':
        print("")
        print("Nº Contatos GRAVADOS na agenda:")
        print("-------------------------------")
        total_contatos(opcao)
    
    # Opção EXIBIR CONTATOS À SEREM GRAVADOS
    elif opcao == '3':
        print("")
        print("Contatos aguardando GRAVAÇÃO:")
        print("-----------------------------")
        lista_contatos(opcao)
    
    # Opção GRAVAR CONTATOS NO ARQUIVO
    elif opcao == '4':
        print("")
        op_grava = input("GRAVAR CONTATOS: (1) SIM ou (2) NÃO --> ")
        print("-----------------------------")
        grava_arquivo(op_grava)
    
    # Opção EXIBIR CONTATOS JÁ GRAVADOS
    elif opcao == '5':
        print("")
        print("Contatos já GRAVADOS:")
        print("---------------------")
        le_arquivo(opcao)
    
    # TRATAMENTO DE ERROS DO MENU
    else:
        print("")
        print("-#-#-#-#-#-#-#- Opção Inválida! -#-#-#-#-#-#-#-")
        continue