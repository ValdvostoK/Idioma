import json

lista = {"codigo": 7, "descricao": "grego"}

with open("Listaidioma.json", "r", encoding="utf-8") as f:
    att = json.load(f)

att["idiomas"].append(lista)

with open("ListaIdioma.json", "w", encoding="utf-8") as g:
    json.dump(att, g, indent=4)