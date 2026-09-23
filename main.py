import Usuarios


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


def MenuUser():
	print("menu user")


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