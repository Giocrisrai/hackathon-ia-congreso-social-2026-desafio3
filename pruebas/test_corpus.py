"""Pruebas sin IA del corpus de la Variante B (datos/b_leyes.csv).

Uso, desde la raíz del repo:
    python pruebas/test_corpus.py
""" 
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "datos" / "b_leyes.csv"

PRIMERA_LEY = "L21100"                                  # test_variantes.py depende de esta ley
LEYES_DEMO = {"L21165", "L21202", "CDT8"}               # normas de la demo (ver docs/fuentes_3_normas.md)
OBLIGATORIAS = ["id_ley", "nombre_ley", "articulo", "texto", "url_oficial", "cobertura"]


def _corpus() -> pd.DataFrame:
    return pd.read_csv(RUTA, dtype=str).fillna("")


def test_primera_ley_sigue_siendo_21100():
    df = _corpus()
    assert df.iloc[0]["id_ley"] == PRIMERA_LEY, "La primera fila debe seguir siendo L21100"


def test_leyes_demo_cargadas():
    faltan = LEYES_DEMO - set(_corpus()["id_ley"])
    assert not faltan, f"Faltan cargar estas leyes de la demo: {sorted(faltan)}"


def test_sin_pares_id_articulo_duplicados():
    df = _corpus()
    dup = df[df.duplicated(["id_ley", "articulo"], keep=False)]
    assert dup.empty, f"Artículos repetidos: {dup[['id_ley', 'articulo']].values.tolist()}"


def test_campos_obligatorios_no_vacios():
    df = _corpus()
    for col in OBLIGATORIAS:
        vacios = df[df[col].str.strip() == ""]
        assert vacios.empty, f"Campo '{col}' vacío en filas {vacios.index.tolist()}"


def test_urls_empiezan_con_http():
    df = _corpus()
    malas = df[~df["url_oficial"].str.startswith(("http://", "https://"))]
    assert malas.empty, f"URL que no empieza con http en filas {malas.index.tolist()}"


def test_nombre_consistente_por_ley():
    df = _corpus()
    for id_ley, grupo in df.groupby("id_ley"):
        assert grupo["nombre_ley"].nunique() == 1, f"nombre_ley distinto dentro de {id_ley}"
        assert grupo["url_oficial"].nunique() == 1, f"url_oficial distinta dentro de {id_ley}"
        assert grupo["historia"].nunique() == 1, f"historia distinta dentro de {id_ley}"


def test_cobertura_valida():
    df = _corpus()
    validas = {"completa", "artículos seleccionados"}
    malas = df[~df["cobertura"].str.startswith(tuple(validas))]
    assert malas.empty, f"cobertura no reconocida en filas {malas.index.tolist()}"


if __name__ == "__main__":
    fallos = 0
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_"):
            try:
                f()
                print("OK", nombre)
            except AssertionError as e:
                fallos += 1
                print("FALLA", nombre, "-", e)
    sys.exit(1 if fallos else 0)
