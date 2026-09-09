import json

class Node:

    def __init__(self, codigo, descricao = None, esq = None, dir = None):
        self.codigo = codigo
        self.descricao = descricao
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return f"Node({self.codigo})"  

class Idioma:

    def montagem(self):
        rota = "IndexIdioma.json"
        lista = Idioma.load_json(rota)
        nodes = {}
        for item in lista:
            codigo = item["codigo"]
            descricao = item["descricao"]
            nodes[codigo] = Node(codigo, descricao) 

        for item in lista:
            atual = nodes[item["codigo"]]
            atual_esq = item.get("esq")  
            atual_dir = item.get("dir")  
            if atual_esq is not None:
                atual.esq = nodes.get(atual_esq)
            if atual_dir is not None:
                atual.dir = nodes.get(atual_dir)  

        raiz_codigo = lista[0]["codigo"]
        self.raiz = nodes[raiz_codigo]  

        return nodes 

    def load_json(self, caminho):
        with open(caminho, "r", encoding = "utf-8") as f:
            dados = json.load(f)  
        return dados["idiomas"] 

arvore = Idioma()

#lista = arvore.montagem()

load = arvore.load_json("IndexIdioma.json")

index = [[item["codigo"], item["descricao"]] for item in load]
ultimo = [len(index) - 1]
#print(ultimo)

print("index  ", index)

#print(lista)