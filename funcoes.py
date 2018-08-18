#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
    print("\n--------------Agenda v0.1----------------\n")
    print("Selecione uma Opcao")
    print("1 - Adicionar um novo contato")
    print("2 - Listar os contatos da agenda")
    print("qualquer outra tecla para sair")

#Funcoes do processo
def adicionar():
    print("Adicionar um registro")
    agenda = open("agendatelefonica.csv",'a')
    nome = input("Nome do Contato:")
    telefone = input("Digite o telefone:")
    print("Contato salvo com nome:",nome," e numero",telefone)
    agenda.write(nome + ", " + telefone+"\n")
    agenda.close()

def listar():
    #print("Lista de Contatos")

    #agenda = open("agendatelefonica.csv")
    #linhas = agenda.readlines()

    #for item in linhas:
    #	print("------------------------")
    #	print(item)

    #print("Listado corretamente")
    #agenda.close()
    return null

def buscar(nome):
    array = readCSV()
    for item in array:
        if nome in item:
            print(item)
            deletar(item)
        else:
            print("Nao apareceu")
    return item

def readCSV():
    agenda = open("agendatelefonica.csv")
    array = agenda.readlines()
    agenda.close()
    return array

def deletar(item):
    array = readCSV()
    if item in array:
        print(" Deletar: " +item)

def falha():
    print("Opcao Incorreta")


def sair():
    print("saindo...")
    exit()


buscar("Renato")