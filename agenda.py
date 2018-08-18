#Agenda Telefonica
import funcoes

funcoes.bemvindo()
#Opcoes do Usuario
opcao = int(input())

#Estrutura de controle
if opcao == 1:
	funcoes.adicionar()
elif opcao == 2:
	funcoes.listar()
elif opcao == 3:
	funcoes.buscaNome(input("Digite o contato"))
elif opcao == 4:
	funcoes.delete(input("Digite o contato"))
else:
	funcoes.sair()

