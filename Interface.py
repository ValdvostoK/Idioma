import json
import random
import unicodedata
from pathlib import Path
from nicegui import ui, app

BASE = Path(__file__).parent / "JSON"
JSON_USUARIO_INDEX  = BASE / "IndexUsuario.json"
JSON_IDIOMA_INDEX   = BASE / "IndexIdioma.json"
JSON_PALAVRA_INDEX  = BASE / "IndexPalavra.json"
JSON_EXERCICIO_INDEX = BASE / "IndexExercicio.json"

#CSS
CARD = "w-full max-w-1g shadow-lg rounded-xl p-6 bg-white"
TITULO = "text-3xl font-bold text-blue mb-2"

sessao = {
    "user": None,
    "admin": False,
}

@ui.page("/")
def login():
    sessao["user"] = None
    sessao["admin"] = False

    ui.query('body').style('background-color: #87cefa')
    with ui.column().classes("w-full flex items-center justify-center background-color: #fee2e2"):
        with ui.card().classes(CARD):
            ui.label("Max Idiomas").classes(TITULO)
            ui.label("Login").classes("text-grey mb-5")

ui.run(title="Max Idiomas", native=True)
