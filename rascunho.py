# arquivo = open ("teste.txt", "w")

# tabela = []
# tabela = [
#             ["João", "(47)99551-4451"],
#             ["Maria", "(47)99223-4346"],
#             ["José", "(47)99003-0020"],
#             ["Ana", "(47)99678-4017"]
#         ]

# tabela = [
#             "João - (47)99551-4451",
#             "Maria - (47)99223-4346",
#             "José - (47)99003-0020",
#             "Ana - (47)99678-4017"
#         ]

# print(tabela)

# for i in range (4):
#     arquivo.write(tabela[i][0] + " - " + tabela[i][1] + '\n')

# for i in range (4):
#     arquivo.write(tabela[i] + '\n')

# arquivo.close

# for i in range (4):
#     for j in range (2):
#         arquivo.write(tabela[i][j] + '\n')

# arquivo.close

# arquivo = open("arquivo.txt", "a", newline="")
# persons = ['Jose antonio de oliveira; jose@fake.com', 
#            'Ana Fake da Silva; ana@fake.net']

# for p in persons:
#     arquivo.write(p+'\n')
# arquivo.close()

# with open ("agenda.txt", "r") as contatos:
#             aux = contatos.readlines()
#             for i in range(6):
#                 aux[i].replace('4', "0")
#             print(aux)
#             for i in range(6):
#                 # aux[i].replace("\n", "")
#                 print(len(aux[i]))
#                 print(aux[i])

tabela = [
            "João - (47)99551-4451",
            "Maria - (47)99223-4346",
            "Gabriel - 47\n",
            "Ana - 21\n"
        ]

tabela1 = []
fone = []
def compara (x):
    if x == 1:
        with open ("agenda.txt", "r") as contatos:
            aux = contatos.readline()
            while aux:
                linha = aux.split()
                tabela1.append(linha)
                fone.append(linha[2])
                aux = contatos.readline()

def le_arquivo (x):
    if x == 1:
        with open ("agenda.txt", "r") as contatos:
            aux = contatos.readlines()
            for i in range(10):
                tabela1.append(aux[i])

compara(1)
#le_arquivo(1)
print(tabela1)
print(fone)

cont = 0
for i in tabela:
    for j in tabela1[2]:
        if(i==j):
            cont += 1
            print(i)
            break
print(cont)

# contatos_temp = [] ### Lista GLOBAL
# def novo_contato (n):
#     while True:
#         if n == 1:
#             print("")
#             nome_contato = input("Insira o nome do contato: ")
#             telefone = input("Insira o telefone do contato: ")

#             contatos_temp.append(nome_contato + " - " + telefone)
#             print("")
#             n = int(input("Deseja adicionar outro contato? (1)Sim ou (2)Não: "))
#         elif n == 2:
#             print(f"{len(contatos_temp)} adicionados.")
#             break
#         else:
#             print("Opção Inválida!")
#             n = int(input("Digite (1) para SIM ou (2) para NÃO!"))
#             continue