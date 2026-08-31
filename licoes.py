import json
import random
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "ListaLicoes.json")

try:
    with open(json_path, "r") as file:
        data = json.load(file)
except json.JSONDecodeError as e:
    print("Erro ao carregar JSON", e)
    exit()
except FileNotFoundError as e:
    print("Arquivo nao encontrado", e)
    exit()  

lista = [item for item in data if item["codigo"]>0]

update_path = os.path.join(base_dir, "ListaLicoes.json")
with open(update_path, "w") as file:
    json.dump(lista, file, indent = 4)

print("Sucesso")

class ListaLicoes:

    def __init__(self, codigo, niveis, codigo_idioma):
        self.codigo = codigo
        self.niveis = niveis
        self.codigo_idioma = codigo_idioma
        self.esq = None
        self.dir = None

    def busca(self, codigo):
        atual = self.codigo
        while atual is not None:
            if atual.cogigo == codigo:
                return codigo
            elif atual.codigo < codigo:
                atual = atual.esq
            else:
                atual = atual.dir
        return None

    def gerar_codigo(self):
        while True:
            novo = random.randint(1, 1000000)
            if self.busca(novo) is None:
                return novo

    def adicionar(self, descricao)
        codigo = self.gerar_codigo()
        novo = ListaLicoes(codigo, descricao)
        if codigo == None:
            return None
        if self.root is None:
            self.root = novo
            return None
        atual = self.root
        with open("Listalicoes.json", "r") as lista:
            inserir = json.load(lista)
        while True:
            if codigo < atual.codigo:
                if atual.esq is None:
                    atual.esq = novo
                    break 
                atual = atual.esq
            else:
                if atual.dir is None:
                    atual.dir = novo
                    break
                atual = atual.dir
        inserir = [item for item in data if item["codigo"]>0]    
        return None

    def excluir(root, codigo)
        if (codigo == None):
            print("Nao existe")
        elif(codigo < root):
            ListaIdioma.excluir(root.esq, codigo)
        elif(codigo > root):
            ListaIdioma.excluir(root.dir, codigo)
        return None