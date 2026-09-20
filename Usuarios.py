import json
from pathlib import Path
import random
import Idiomas

json_Lista = Path(__file__).parent / "JSON" / "ListaUsuario.json"
json_Index = Path(__file__).parent / "JSON" / "IndexUsuario.json"
json_IndexIdioma = Path(__file__).parent / "JSON" / "IndexIdioma.json"

class Node:

    def __init__(self, codigo, posicao = None, esq = None, dir = None):
        self.codigo = codigo
        self.posicao = posicao
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return f"Node({self.codigo})"   

class Usuario:

    def __init__(self):
        self.raiz = None
        self.montagem()

    def montagem(self):
        lista = self.load_json(json_Lista)
        nodes = {}
        for item in lista:
            codigo = item["codigo"]
            posicao = item["posicao"]
            nodes[codigo] = Node(codigo, posicao) 

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

    def busca(self, codigo):
        atual = self.raiz
        while atual is not None and atual.codigo != codigo:
            if codigo < atual.codigo:
                atual = atual.esq
            elif codigo > atual.codigo:
                atual = atual.dir
        if atual is not None:
            return atual.posicao
        else:            
            return None

    def inserir(self):
        #x = self.gerar_codigo()
        nome = input("Qual nome? Usuario")
        x = nome
        senha = input("Senha: ")
        checagem = None
        while checagem is None:
            cod_idioma = input("Qual idioma deseja aprender? ")
            checagem = Idiomas.Idioma().busca(cod_idioma)
            if checagem is None:
                print("Codigo invalido")
        lista = Usuario.load_json(json_Index)
        index = {"usuarios": [{"codigo": item["codigo"], "nome": item["nome"],
                               "senha": item["senha"],
                               "cod_idioma": item["cod_idioma"],
                               "nivel": item["nivel"],
                               "pontos_atual": item["pontos_atual"]} for item in lista]}
        pos = len(index["usuarios"]) 
        y = Node(x, pos)
        atual = self.raiz
        while True:
            if  x < atual.codigo:
                if atual.esq is None:
                    atual.esq = y
                    break
                atual = atual.esq

            elif x > atual.codigo:
                if atual.dir is None:
                    atual.dir = y
                    break
                atual = atual.dir  

        conf = input("Confirmar insercao(S/N)")
        if conf.lower() == "s":
            novo = {"codigo": x, "nome": nome, "senha": senha, "cod_idioma": cod_idioma,
                    "nivel": 1, "pontos_atual": 0}
            index["usuarios"].append(novo)
            with open(json_Index, "w", encoding="utf-8") as g:
                json.dump(index, g, indent=4, ensure_ascii=False)
            self.save_json()
        else:
            print("Op cancelada")      

        return None

    def ranking(self):
        dados = self.load_json(json_Index)
        idiomas = Idiomas.Idioma().load_json(json_IndexIdioma)
        print("Idiomas user", idiomas)
        dados.sort(key=lambda usuario: usuario['pontos_atual'], reverse=True)

        for x, y in enumerate(dados, start = 1):
            nome = y['nome']
            pontos = y["pontos_atual"]
            print(f'{x}° Lugar: {nome} - {pontos} pontos')

    def dicionario(self, node, lista = None):

        if lista is None:
            lista = []

        if node is None:
            return lista
         
        lista.append({
            "codigo": node.codigo,
            "posicao": node.posicao,
            "esq": node.esq.codigo if node.esq else None,
            "dir": node.dir.codigo if node.dir else None
        })

        self.dicionario(node.esq, lista)       
        self.dicionario(node.dir, lista)

        return lista

    def load_json(self, caminho):
        with open(caminho, "r", encoding = "utf-8") as f:
            dados = json.load(f)  
        return dados["usuarios"]  

    def save_json(self):
        dados = {"usuarios": self.dicionario(self.raiz)}
        with open(json_Lista, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent = 4, ensure_ascii = False) 
        print("Arquivo salvo") 


arvore = Usuario()
arvore.ranking()

#arvore.inserir()