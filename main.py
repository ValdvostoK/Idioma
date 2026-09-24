import Usuarios
import os


def MenuAdmin():
	print("1 - Inserir")
	print("2 - Remover")
	print("3 - Consultar")
	print("0 - Sair")
	k = input("O que deseja fazer: ")
	match k:
		case "1":
			print("Idiomas")
			print("Palavras")
			print("Licoes")
			print("Exercicios")
			print("Usuarios")

			j = input("Em qual arquivo? ")

			modulo = __import__(j)
			classe = getattr(modulo, j[:-1])
			objeto = classe()

			objeto.Inserir()
		case "0":
			pass


def MenuUser(nome):
	x = 0
	while x != 0:
		print("1 - Fazer licao?")
		print("2 - Alterar idioma")
		print("3 - Ver ranking")
		print("0 - Sair")
		k = int(input("\nSelecione uma opcao"))

		match k:
			case "1":
				y = 's'
				while y == 's':
					os("cls")
					print("Usuario: ", nome)
					y = input("Fazer licao? (s/n)")
					if y == 's':
						Usuarios.Usuario().exercicio(nome)
					else:
						print("Aula encerrada")

			case "2":
				Usuarios.Usuario().alterar(nome)

			case "3":
				Usuarios.Usuario().ranking(nome)

			case "0":
				x = 0


n = 1

lista = Usuarios.Usuario().load_json("ListaUsuario.json")

while n != 0:
	x = 0
	while x == 0:
		x = input("Usuario: ")

		if Usuarios.Usuario().busca(x) is None:
			print("Usuario não existe")
			x = 0
		else:
			x = 1

	senha = None

	while senha is None:
		senha = input("Senha: ")
		pos = Usuarios.Usuario().busca(x)

		if lista[pos]["senha"] is None:
			print("Senha incorreta")
			senha = None

	if pos == 0:
		#----MENU ADMIN----
		admin = 1
		while admin != 0:
			MenuAdmin()

	else:
		#----MENU ALUNO----
		user = 1
		while user != 0:
			MenuUser()