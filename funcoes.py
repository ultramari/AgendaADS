def bemvindo():
	print("\n--------------Agenda v0.1----------------\n")
	print("Selecione uma Opcao")
	print("1 - Adicionar um novo contato")
	print("2 - Listar os contatos da agenda")
	print("3 - buscar um contato")
	print("4 - Deletar um contato")
	print("qualquer outra tecla para sair")

def falha():
	print("Opcao Incorreta")

def sair():
	print(opcao)
	exit()

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

def falha():
    print("Opcao Incorreta")


def sair():
    print("saindo...")
    exit()


def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:")
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome + ", " + telefone+"\n")
	agenda.close()

def listar():
	array = readCSV()
	for index, item in enumerate(array):
		print(index, " - ", array[index])


def buscar(valor):
	array = readCSV()

	numIndex = ""
	for index, item in enumerate(array):
		if valor in array[index]:
			numIndex = index

	return numIndex

def buscaNome(value):
	var = buscar(value)
	if var == "":
		print("o contato não foi encontrado")
	else:
		print("O valor existe ")

def delete(value):
	array = readCSV()
	index = buscar(value)

	if index == "" :
		print("o registro não existe")
	else:
		array.pop(index)
		print("o registro foi deletado com sucesso!")

	writeCSV(array)


def readCSV():
	with open("agendatelefonica.csv") as agenda:
		return agenda.readlines()

def writeCSV(array):
	with open("agendatelefonica.csv", 'w') as agenda:
		for item in array:
			agenda.write(item)
			
