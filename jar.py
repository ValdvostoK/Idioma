import json
import random

class aula:

    def __innit__(self, x):
        print("iniit")

    def escrever(self, x, y):
        print(self)
        z = x +y
        return z

print("ola")


with open("ListaIdioma.json", "r") as lista:
            inserir = json.load(lista)

print(inserir[codigo])

def gerar_codigo():
    novo = random.randint(1, 1000000)
    return novo

          
var = gerar_codigo()
print(var)