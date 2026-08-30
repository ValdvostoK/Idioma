import json
import random
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "ListaIdioma.json")

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

update_path = os.path.join(base_dir, "ListaIdioma.json")
with open(update_path, "w") as file:
    json.dump(lista, file, indent = 4)

print("Sucesso")    

class ListaIdioma:

    def __innit__(self, codigo, descricao):
        self.codigo = codigo
        self.descricao = descricao
        self.esq = None
        self.dir = None 

    def busca(self, codigo):
        atual = self.codigo
        while atual is not None:
            if atual.codigo == codigo:
                return codigo
            elif codigo < atual.codigo:
                atual = atual.esq
            else:
                atual = atual.dir  
        return None

    def gerar_codigo(self):
        while True:
            novo = random.randint(1, 1000000)
            if self.busca(novo) is None:
                return novo  
            
    def adicionar(self, descricao):
        codigo = self.gerar_codigo()
        novo = ListaIdioma(codigo, descricao)
        if codigo == None:
            return ListaIdioma
        atual = self.root
        with open("ListaIdioma.json", "r") as lista:
            inserir = json.load(lista)
        while True:
            if codigo < atual.esq: 
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

    def excluir(root, codigo):
        if (codigo == None):
            print("Nao existe")
        elif(codigo < root):
            ListaIdioma.excluir(root.esq, codigo)
        elif(codigo > root):
            ListaIdioma.excluir(root.dir, codigo)
        return None
            