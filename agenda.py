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
	funcoes.delete()
else:
	funcoes.sair()

