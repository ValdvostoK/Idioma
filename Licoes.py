import json
from pathlib import Path
import random


class Node:

    def __init__(self, codigo, posicao = None, esq = None, dir = None):
        self.codigo = codigo
        self.posicao = posicao
        self.esq = esq
        self.dir = dir

    def __repr__(self):
        return f"Node({self.codigo})"  

class Licao:

    def __innit__(self):
        self.raiz = None