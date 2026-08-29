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