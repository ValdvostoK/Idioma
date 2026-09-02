import json
import random


class Node:

    def __init__(self, codigo, descricao = None, esq = None, dir = None):
        self.codigo = codigo
        self.descricao = descricao
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return f"Node({self.codigo})"    

class Idioma:

    def __init__(self):
        self.raiz = None

    def montagem(self):
        lista = Idioma.load_json("ListaIdioma.json")
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

    def busca(self, codigo):
        atual = self.raiz
        while atual is not None and atual.codigo != codigo:
            if codigo < atual.codigo:
                atual = atual.esq
            elif codigo > atual.codigo:
                atual = atual.dir
        if atual is not None:
            return atual
        else:            
            return None

    def gerar_codigo(self):
        while True:
            novo = random.randint(1, 1000000)
            if self.busca(novo) is None:
                return novo     

    def inserir(self, descricao):
        x = self.gerar_codigo()
        y = Node(x, descricao)
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
            self.save_json()
        else:
            print("Op cancelada")      

        return None

    def minimo(self, cod):
        print("Min cod  ", cod)
        print("Min cod esq ", cod.esq)
        while cod.esq:
            cod = cod.esq
        return cod

    def excluir(self, codigo, atual = None):

        if atual is None:
            atual = self.raiz
        print("prieiro atu", atual.descricao)    

        if codigo < atual.codigo:
                atual.esq = self.excluir(codigo, atual.esq)

        elif codigo > atual.codigo:
                atual.dir = self.excluir(codigo, atual.dir)
        else:
            if atual.esq is None:
                print("atual.esq is none  ", atual)
                return atual.dir
                    
            elif atual.dir is None:
                print("dir  ", atual.dir)
                return atual.esq

            print("atual dir  ", atual)
            sucessor = atual.dir
            sucessor = self.minimo(sucessor)
            print("sucess>  ", sucessor)
            atual.codigo = sucessor.codigo  
            atual.descricao = sucessor.descricao  
            print("atual sucess  ", atual)
            atual.dir = self.excluir(atual.codigo, atual.dir)     

        print("atual  final", atual.descricao)
        return atual

    def remover(self, codigo):
        y = self.excluir(codigo)  #usar variavel
        print("y   ", y)
        self.save_json()

    def dicionario(self, node, lista = None):

        print("Node dic  ", node)
        if lista is None:
            lista = []

        if node is None:
            return lista
         
        lista.append({
            "codigo": node.codigo,
            "descricao": node.descricao,
            "esq": node.esq.codigo if node.esq else None,
            "dir": node.dir.codigo if node.dir else None
        })

        self.dicionario(node.esq, lista)       
        self.dicionario(node.dir, lista)

        return lista

    def load_json(caminho):
        with open(caminho, "r", encoding = "utf-8") as f:
            dados = json.load(f)  
        return dados["idiomas"]  

    def save_json(self):
        dados = {"idiomas": self.dicionario(self.raiz)}
        with open("ListaIdioma.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent = 4, ensure_ascii = False) 
        print("Arquivo salvo") 

arvore = Idioma()

arvore.montagem() 
#print("Resultado do print", lista)

#x = int(input("Qual numero"))
#mouse = arvore.busca(x)
#print("mouse: ", mouse)

desc = input("descricao  ")
print(arvore.inserir(desc))

#arvore.remover(x)
