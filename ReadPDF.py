import PyPDF2
import pyttsx3

texto_teste = "Esse é um teste para criação de um ebook, oque acha ?"

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with open(caminho_pdf, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)  # Mudança nesta linha
        num_paginas = len(leitor_pdf.pages)
        for pagina_numero in range(num_paginas):
            pagina = leitor_pdf.pages[pagina_numero]  # Mudança nesta linha
            texto += pagina.extract_text()
    return texto
# Exemplo de uso:
caminho_pdf = "ebooks\gte.pdf"
texto_extraido = extrair_texto_pdf(caminho_pdf)

engine = pyttsx3.init()

engine.setProperty("rate", 150)

engine.say(texto_teste)

engine.runAndWait()

engine.stop()


print(texto_extraido)

