"""Pruebas sin IA del paso de estilo (nucleo/tono.py). Uso, desde la raíz del repo:
    python -m pytest pruebas/test_tono.py      o      python pruebas/test_tono.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nucleo import tono as T  # noqa: E402

O = "Si un comercio no cumple, el juzgado de policía local le aplica una multa por cada bolsa."

TRATO = [("Trata de 'hermano' en la respuesta.", "hermano"), ("Juvenil, corto, preciso y agresivo", None),
         ("Trátalos como 'compadre'", "compadre"), ("Llámale amigo", "amigo"), ("Dile parcero siempre", "parcero"),
         ("Amable y pausado, como un nieto que explica con paciencia.", None), ("Trata de ser breve y claro", None),
         ("Trata de no usar jerga", None), ("Trata de usted a la persona", None), ("Trata a la persona como 'hermano'", "hermano")]

SENTIDO = [(O, "El juzgado de policía local te lanza la multa.", True),
           (O, "Hermano, si un comercio no cumple, el juzgado de policía local le pone multa.", False),
           (O, "Si el local se pasa, le cae multa del juzgado de policía local. Denúncialo YA.", True),
           (O, "¿Viste un comercio así? El juzgado lo multa.", True),
           ("Si manejas a más de 30 km/h te pueden multar.", "Ojo: si vas a más de 30 te pueden multar.", False),
           ("Esa cadena es falsa.", "Hermano, esa cadena es falsa, no la compartas.", False),
           (O, "El comercio paga la multa, no tú.", True),  # perdió "juzgado"
           (O, "Si recibes bolsas, pagas la multa.", True),
           ("Los comercios no pueden entregar bolsas plásticas.", "Hermano, deja de usar bolsas plásticas: los comercios no pueden entregarlas.", True)]

CONSERVA = [("La multa la impone el juzgado de policía local correspondiente.", "Hermano, la multa la dicta el juzgado de policía local.", True),
            ("La multa la impone el juzgado de policía local correspondiente.", "Antes de compartir, verifica si el comercio ya lo aplica.", False),
            ("Multa de hasta 5 unidades tributarias mensuales por cada bolsa.", "Multa de hasta cinco UTM por bolsa.", False),
            ("Rige desde febrero 2019 para gran comercio y agosto 2020 para pymes.", "Hermano, rige desde febrero 2019 para el gran comercio y agosto 2020 para pymes.", True),
            ("Los comercios no pueden entregar bolsas plásticas.", "Hermano, los locales no pueden dar bolsas plásticas.", True),
            ("Es una cadena que circula hace años; WhatsApp no cobra.", "Hermano, esa cadena es vieja y la app no cobra.", False)]


def test_trato_pedido():
    for texto, esperado in TRATO:
        assert T.trato_pedido({"tono": texto}) == esperado, texto


def test_cambia_sentido():
    for original, nuevo, esperado in SENTIDO:
        assert T.cambia_sentido(original, nuevo) == esperado, nuevo


def test_conserva():
    for original, nuevo, esperado in CONSERVA:
        assert T.conserva(original, nuevo) == esperado, nuevo


def test_asegurar_trato():
    r = T._asegurar_trato({"explicacion_simple": "Esa cadena es vieja.", "que_puedo_hacer": ["No la reenvíes."]},
                          ["explicacion_simple", "que_puedo_hacer"], "hermano")
    assert r["explicacion_simple"] == "Hermano, esa cadena es vieja."
    assert T._asegurar_trato({"frases": ["Hermano, ya está."]}, ["frases"], "hermano")["frases"] == ["Hermano, ya está."]


def test_tutear():
    assert T.tutear("Revisá fuentes oficiales, la multa no es para vos.") == "Revisa fuentes oficiales, la multa no es para ti."
    assert T.tutear("Vos tenés que verificar.") == "Tú tienes que verificar."


def test_personalizado():
    base = {"usuario": "u", "tono": "t", "instrucciones_extra": "i", "largo_respuesta": "l"}
    assert not T.personalizado(dict(base), base)
    assert T.personalizado(dict(base, tono="otro"), base)


if __name__ == "__main__":
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_"):
            f(); print("OK", nombre)
