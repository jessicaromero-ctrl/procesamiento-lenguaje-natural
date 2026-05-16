# Procesamiento de Lenguaje Natural - Clase 1
# Python 3.11 + Miniconda + Visual Studio Code
# Objetivo: leer comentarios, limpiar texto, tokenizar, clasificar y guardar resultados.

from pathlib import Path
import csv
import re
import unicodedata
from collections import Counter

ARCHIVO_ENTRADA = Path("comentarios_clase1.txt")
ARCHIVO_SALIDA = Path("resultados_clase1.csv")

STOPWORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "y", "o", "pero", "aunque", "a", "en", "con",
    "por", "para", "me", "mi", "mis", "es", "fue", "muy", "que",
    "se", "al", "lo", "no", "su", "sus", "tuvo", "durante"
}

PALABRAS_POSITIVAS = {
    "excelente", "bien", "buena", "bueno", "interesante", "util", "gusto",
    "claro", "claridad", "paciencia", "relevante", "ayudo", "facil", "organizado"
}

PALABRAS_NEGATIVAS = {
    "demasiadas", "rapido", "faltaron", "fallo", "confusos", "confuso",
    "poca", "lenta", "mal", "problema", "cayo", "demasiado", "no", "permitio"
}

PALABRAS_CATEGORIA = {
    "docente": {"profesor", "docente", "explica", "explicacion", "dudas", "retroalimentacion", "calificar"},
    "contenido": {"clase", "materia", "contenido", "conceptos", "tema", "temas", "teoria", "practica", "practicas", "actividad", "material"},
    "plataforma": {"plataforma", "sistema", "archivo", "entrega", "subir", "cayo"},
}


def cargar_comentarios(ruta: Path) -> list[str]:
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo de entrada: {ruta}")

    comentarios = [linea.strip() for linea in ruta.read_text(encoding="utf-8").splitlines()]
    return [comentario for comentario in comentarios if comentario]


def quitar_acentos(texto: str) -> str:
    normalizado = unicodedata.normalize("NFD", texto)
    return "".join(c for c in normalizado if unicodedata.category(c) != "Mn")


def limpiar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = quitar_acentos(texto)
    texto = re.sub(r"[^a-zñ0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def tokenizar(texto_limpio: str) -> list[str]:
    return texto_limpio.split()


def quitar_stopwords(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in STOPWORDS and len(token) > 2]


def clasificar_sentimiento(tokens: list[str]) -> str:
    positivos = sum(1 for token in tokens if token in PALABRAS_POSITIVAS)
    negativos = sum(1 for token in tokens if token in PALABRAS_NEGATIVAS)

    if positivos > 0 and negativos > 0:
        return "mixto"
    if positivos > negativos:
        return "positivo"
    if negativos > positivos:
        return "negativo"
    return "neutral"


def clasificar_categoria(tokens: list[str]) -> str:
    puntajes = {}
    for categoria, palabras in PALABRAS_CATEGORIA.items():
        puntajes[categoria] = sum(1 for token in tokens if token in palabras)

    mejor_categoria, mejor_puntaje = max(puntajes.items(), key=lambda item: item[1])
    return mejor_categoria if mejor_puntaje > 0 else "sin_categoria"


def analizar_comentarios(comentarios: list[str]) -> list[dict[str, str]]:
    resultados = []

    for i, comentario in enumerate(comentarios, start=1):
        limpio = limpiar_texto(comentario)
        tokens = tokenizar(limpio)
        tokens_utiles = quitar_stopwords(tokens)
        frecuencia = Counter(tokens_utiles)

        resultados.append({
            "id": str(i),
            "comentario_original": comentario,
            "texto_limpio": limpio,
            "tokens_utiles": ", ".join(tokens_utiles),
            "palabras_frecuentes": ", ".join([f"{palabra}:{conteo}" for palabra, conteo in frecuencia.most_common(5)]),
            "categoria": clasificar_categoria(tokens_utiles),
            "sentimiento": clasificar_sentimiento(tokens_utiles),
        })

    return resultados


def guardar_resultados(resultados: list[dict[str, str]], ruta: Path) -> None:
    campos = [
        "id",
        "comentario_original",
        "texto_limpio",
        "tokens_utiles",
        "palabras_frecuentes",
        "categoria",
        "sentimiento",
    ]

    with ruta.open("w", encoding="utf-8-sig", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)


def imprimir_resultados(resultados: list[dict[str, str]]) -> None:
    for fila in resultados:
        print("=" * 90)
        print(f"ID: {fila['id']}")
        print(f"Comentario : {fila['comentario_original']}")
        print(f"Limpio     : {fila['texto_limpio']}")
        print(f"Tokens     : {fila['tokens_utiles']}")
        print(f"Categoría  : {fila['categoria']}")
        print(f"Sentimiento: {fila['sentimiento']}")
    print("=" * 90)


def main() -> None:
    comentarios = cargar_comentarios(ARCHIVO_ENTRADA)
    resultados = analizar_comentarios(comentarios)
    imprimir_resultados(resultados)
    guardar_resultados(resultados, ARCHIVO_SALIDA)
    print(f"\nResultados guardados en: {ARCHIVO_SALIDA.resolve()}")


if __name__ == "__main__":
    main()
