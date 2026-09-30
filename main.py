import Usuarios
import os
from pathlib import Path

json_Lista = Path(__file__).parent / "JSON" / "ListaUsuario.json"
json_Index = Path(__file__).parent / "JSON" / "IndexUsuario.json"

def MenuAdmin():
	print("1 - Inserir")
	print("2 - Remover")
	print("3 - Consultar")
	print("0 - Sair")
	k = input("O que deseja fazer: ")
	if k == 'Sair':
		return 0
	#match k:
		#case "1":
	print("Idiomas")
	print("Palavras")
	print("Licoes")
	print("Exercicios")
	print("Usuarios")

	j = input("Em qual arquivo? ")

	modulo = __import__(j)
	classe = getattr(modulo, j[:-1])
	objeto = classe()
	funcao = getattr(objeto, k)
	funcao()

			#objeto.Inserir()
		#case "0":
			#pass


def MenuUser(nome):
	x = 7
	while x != 0:
		print("1 - Fazer licao?")
		print("2 - Alterar idioma")
		print("3 - Ver ranking")
		print("0 - Sair")
		k = int(input("\nSelecione uma opcao"))

		match k:
			case  1:
				y = 's'
				while y == 's':
					#os("cls")
					print("Usuario: ", nome)
					y = input("Fazer licao? (s/n)")
					if y == 's':
						Usuarios.Usuario().aula(nome)
					else:
						print("Aula encerrada")

			case 2:
				Usuarios.Usuario().alterar(nome)

			case  3:
				Usuarios.Usuario().ranking(nome)

			case  0:
				x = 0


n = 1

lista = Usuarios.Usuario().load_json(json_Index)

while n != 0:
	x = 0
	while x == 0:
		y = input("Usuario: ")

		if Usuarios.Usuario().busca(y) is None:
			print("Usuario não existe")
			x = 0
		else:
			x = 1

	senha = None

	while senha is None:
		senha = input("Senha: ")
		pos = Usuarios.Usuario().busca(y)

		if lista[pos]["senha"] != senha:
			print("Senha incorreta")
			senha = None

	if pos == 0:
		#----MENU ADMIN----
		admin = 1
		while admin != 0:
			admin = MenuAdmin()

	else:
		#----MENU ALUNO----
		user = 1
		while user != 0:
			MenuUser(y)