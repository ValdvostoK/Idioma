"""
Modulo para gerar certificados em PDF para usuarios que atingiram
um determinado nivel em um idioma.

Uso basico:
    from certificado import gerar_certificado
    caminho = gerar_certificado("Valdrei", "Ingles", nivel=5)
    print(f"Certificado gerado em: {caminho}")
"""

from datetime import date
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


def gerar_certificado(nome, idioma, nivel=None, pasta_saida="certificados"):
    """
    Gera um certificado em PDF para o usuario informado.

    Args:
        nome (str): nome do usuario que recebera o certificado.
        idioma (str): idioma que o usuario praticou (ex: "Ingles").
        nivel (int, opcional): nivel atingido, exibido no certificado.
        pasta_saida (str): pasta onde o PDF sera salvo.

    Returns:
        str: caminho completo do arquivo PDF gerado.
    """
    import os
    os.makedirs(pasta_saida, exist_ok=True)

    nome_arquivo = f"certificado_{nome}_{idioma}.pdf".replace(" ", "_")
    caminho = os.path.join(pasta_saida, nome_arquivo)

    largura, altura = landscape(A4)
    c = canvas.Canvas(caminho, pagesize=landscape(A4))

    # --- Cores ---
    cor_borda = HexColor("#1a3c6e")
    cor_destaque = HexColor("#c9a227")
    cor_texto = HexColor("#1a1a1a")

    # --- Fundo levemente colorido ---
    c.setFillColor(HexColor("#fdfbf5"))
    c.rect(0, 0, largura, altura, fill=1, stroke=0)

    # --- Moldura dupla ---
    margem = 1.2 * cm
    c.setStrokeColor(cor_borda)
    c.setLineWidth(3)
    c.rect(margem, margem, largura - 2 * margem, altura - 2 * margem)

    margem2 = margem + 0.35 * cm
    c.setStrokeColor(cor_destaque)
    c.setLineWidth(1)
    c.rect(margem2, margem2, largura - 2 * margem2, altura - 2 * margem2)

    # --- Titulo ---
    c.setFillColor(cor_borda)
    c.setFont("Helvetica-Bold", 34)
    c.drawCentredString(largura / 2, altura - 4.2 * cm, "CERTIFICADO")

    c.setFont("Helvetica", 14)
    c.setFillColor(cor_texto)
    c.drawCentredString(largura / 2, altura - 5.3 * cm, "DE CONCLUSAO DE NIVEL")

    # --- Texto principal ---
    c.setFont("Helvetica", 14)
    c.drawCentredString(largura / 2, altura - 7.5 * cm, "Certificamos que")

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(cor_borda)
    c.drawCentredString(largura / 2, altura - 9 * cm, nome)

    c.setFont("Helvetica", 14)
    c.setFillColor(cor_texto)
    texto_nivel = f" atingiu o nivel {nivel}" if nivel is not None else ""
    c.drawCentredString(
        largura / 2,
        altura - 10.3 * cm,
        f"concluiu com sucesso o modulo de {idioma}{texto_nivel}",
    )

    # --- Data ---
    data_str = date.today().strftime("%d/%m/%Y")
    c.setFont("Helvetica", 11)
    c.drawCentredString(largura / 2, altura - 12.5 * cm, f"Emitido em {data_str}")

    # --- Linha de assinatura ---
    linha_y = 3.2 * cm
    c.setStrokeColor(cor_texto)
    c.setLineWidth(0.8)
    c.line(largura / 2 - 4 * cm, linha_y, largura / 2 + 4 * cm, linha_y)
    c.setFont("Helvetica", 10)
    c.drawCentredString(largura / 2, linha_y - 0.5 * cm, "Coordenacao do Curso")

    c.showPage()
    c.save()

    return caminho


if __name__ == "__main__":
    # Exemplo de uso / teste rapido
    caminho = gerar_certificado("Valdrei", "Ingles", nivel=5)
    print(f"Certificado gerado em: {caminho}")
