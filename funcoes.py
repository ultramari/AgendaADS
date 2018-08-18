def bemvindo():
	print("\n--------------Agenda v0.1----------------\n")
	print("Selecione uma Opcao")
	print("1 - Adicionar um novo contato")
	print("2 - Listar os contatos da agenda")
	print("3 - Deletar um contato")
	print("qualquer outra tecla para sair")

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

def delete(value):
	array = readCSV()
	index = buscar(value)

	if index == "" :
		print("o registro não existe")
	else:
		array.pop(index)

	writeCSV(array)


def readCSV():
	with open("agendatelefonica.csv") as agenda:
		return agenda.readlines()

def writeCSV(array):
	with open("agendatelefonica.csv", 'w') as agenda:
		for item in array:
			agenda.write(item)