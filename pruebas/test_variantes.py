"""Pruebas sin IA de los controles fijos de las variantes. Uso: python pruebas/test_variantes.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from variantes import a_verificador as A, b_ley_simple as B  # noqa: E402

CORPUS = A.cargar_corpus()
LEYES = B.cargar_corpus()
LEY = LEYES[LEYES["id_ley"] == LEYES["id_ley"].iloc[0]]


def test_a_sin_sitios_inventados():
    r = {"explicacion_simple": "Es falso.", "que_se_sabe": "Revisa salud.gob.mx", "que_no_se_sabe": "",
         "que_puedo_hacer": ["Verifica en salud.gob.mx o la OMS.", "Consulta fuentes oficiales."]}
    out = A.limpiar(r, CORPUS, {"largo_respuesta": ""}, caso=CORPUS.iloc[0])
    assert "salud.gob.mx" not in out["que_se_sabe"]
    assert out["que_puedo_hacer"] == ["Consulta fuentes oficiales."]


def test_a_respeta_maximo_de_frases():
    r = {"explicacion_simple": "Uno. Dos.", "que_se_sabe": "Tres.", "que_no_se_sabe": "",
         "que_puedo_hacer": ["Cuatro.", "Cinco.", "Seis.", "Siete."]}
    out = A.limpiar(r, CORPUS, {"largo_respuesta": "Máximo 5 frases en total."}, caso=CORPUS.iloc[0])
    assert len(out["que_puedo_hacer"]) == 2


def test_a_recorte_cuenta_frases_de_cada_sugerencia():
    r = {"explicacion_simple": "Uno.", "que_se_sabe": "Dos. Tres.", "que_no_se_sabe": "",
         "que_puedo_hacer": ["Cuatro. Cinco.", "Seis."]}
    out = A.limpiar(r, CORPUS, {"largo_respuesta": "Máximo 5 frases en total."}, caso=CORPUS.iloc[0])
    assert out["que_puedo_hacer"] == ["Cuatro. Cinco."]


def test_b_sancion_a_tu_se_descarta():
    r = {"frases": [{"texto": "El juzgado de policía local te multará si un local entrega bolsas.", "articulos": ["5"]},
                    {"texto": "el juzgado de policía local multa al comercio que entrega bolsas.", "articulos": ["5"]}]}
    buenas, desc = B.validar(r, LEY)
    assert desc == 1 and buenas[0]["texto"].startswith("El juzgado")


def test_b_sancion_a_tu_permitida_si_la_ley_sanciona_personas():
    assert not B.sancion_mal_atribuida("Si manejas a más de 30 te pueden multar.", "El conductor que exceda la velocidad será multado.")


def test_b_organismo_ajeno():
    r = {"frases": [{"texto": "La municipalidad puede multar al local.", "articulos": ["5"]}]}
    assert B.validar(r, LEY)[1] == 1


def test_a_sin_caso_no_afirma_hechos():
    r = {"chequeable": True, "explicacion_simple": "El coco no cura.", "que_se_sabe": "Ni un solo estudio lo respalda.",
         "que_no_se_sabe": "", "que_puedo_hacer": ["Revisá fuentes oficiales."]}
    out = A.limpiar(r, CORPUS, {"largo_respuesta": ""}, caso=None)
    assert out["explicacion_simple"] == "" and out["que_se_sabe"] == A.SIN_CASO
    assert out["que_puedo_hacer"] == ["Revisa fuentes oficiales."]


def test_b_cifras_y_municipalidad():
    r = {"frases": [{"texto": "La multa es de hasta 5 UTM (unos $500 mil en 2024) por cada bolsa.", "articulos": ["5"]},
                    {"texto": "La multa es de hasta 5 unidades tributarias mensuales por cada bolsa.", "articulos": ["5"]},
                    {"texto": "El local puede ser multado por la municipalidad.", "articulos": ["4", "5"]},
                    {"texto": "La municipalidad revisa, pero no castiga: eso lo hace el juzgado de policía local.", "articulos": ["4", "5"]},
                    {"texto": "Rige desde febrero de 2019 para el gran comercio.", "articulos": ["transitorio"]},
                    {"texto": "La multa es para el local, no para vos.", "articulos": ["5"]}]}
    buenas, desc = B.validar(r, LEY)
    textos = [b["texto"] for b in buenas]
    assert desc == 2, textos
    assert "La multa es para el local, no para tú." not in textos and any("no para tú" in t or "no para ti" in t for t in textos)


def test_a_sin_estafa_inventada():
    caso = CORPUS[CORPUS["texto_viral"].str.contains("WhatsApp", case=False)].iloc[0]
    r = {"chequeable": True, "explicacion_simple": "Hermano, es una cadena vieja. Es una estafa para que compartas datos.",
         "que_se_sabe": "WhatsApp no cobra.", "que_no_se_sabe": "", "que_puedo_hacer": ["No la reenvíes."]}
    out = A.limpiar(r, CORPUS, {"largo_respuesta": ""}, caso=caso)
    assert "estafa" not in out["explicacion_simple"].lower() and out["explicacion_simple"].startswith("Hermano")


def test_b_muni_lejos_y_citas_en_texto():
    r = {"frases": [{"texto": "Las municipalidades revisan que los comercios cumplan y pueden imponer multas por cada bolsa.", "articulos": ["4"]},
                    {"texto": "La municipalidad revisa, pero no puede multar: eso lo hace el juzgado de policía local.", "articulos": ["4", "5"]},
                    {"texto": "La multa se aplica al comercio que entrega la bolsa [art. 5].", "articulos": ["5"]}]}
    buenas, desc = B.validar(r, LEY)
    assert desc == 1 and buenas[-1]["texto"] == "La multa se aplica al comercio que entrega la bolsa."


if __name__ == "__main__":
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_"):
            f(); print("OK", nombre)
