"""Pruebas sin IA del perfil juvenil (variantes/b_perfil.py).

Uso, desde la raíz del repo:
    python pruebas/test_perfil.py
    python -m pytest pruebas/test_perfil.py      (si tienen pytest instalado)
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from variantes import b_perfil as P  # noqa: E402


def test_normalizar_perfil():
    casos = [
        ("Escolar", "Escolar"),
        ("escolar", "Escolar"),
        ("Estudiante de enseñanza media", "Escolar"),
        ("Universitario", "Universitario"),
        ("universidad", "Universitario"),
        ("Educación superior", "Universitario"),
        ("Laboral/Cesante", "Laboral/Cesante"),
        ("laboral-cesante", "Laboral/Cesante"),
        ("cesante", "Laboral/Cesante"),
        ("joven trabajador", "Laboral/Cesante"),
        ("", "Escolar"),
        ("perfil que no existe", "Escolar"),
    ]
    for entrada, esperado in casos:
        assert P.normalizar_perfil(entrada) == esperado, entrada


def test_instrucciones_incluyen_perfil_y_reglas():
    for perfil in P.PERFILES:
        texto = P.instrucciones_perfil(perfil)
        assert f"PERFIL ACTIVO: {perfil}" in texto
        assert "REGLAS DE TONO" in texto
        assert "nunca QUÉ dice la ley" in texto
    assert "analogías del colegio" in P.instrucciones_perfil("Escolar")
    assert "lenguaje formal" in P.instrucciones_perfil("Universitario").lower()
    assert "bolsillo" in P.instrucciones_perfil("Laboral/Cesante").lower()


def test_perfil_desconocido_cae_en_escolar():
    texto = P.instrucciones_perfil("No existe")
    assert "PERFIL ACTIVO: Escolar" in texto
    assert "analogías del colegio" in texto


def test_bloque_dignidad_cita_articulos():
    texto = P.bloque_dignidad("Ley 21.202", ["1", "2"], "ecologia")
    assert "Impacto en la Dignidad Humana" in texto
    assert "arts. 1, 2" in texto
    assert "humedal" in texto.lower() or "ecosistema" in texto.lower()
    assert "21.202" in texto


def test_bloque_dignidad_sin_articulos_no_inventa_cita():
    texto = P.bloque_dignidad("Ley X", [])
    assert "arts." not in texto
    assert "Dignidad Humana" in texto


def test_bloque_dignidad_no_agrega_cifras_ni_organismos():
    nombre = "Ley 21.202"
    arts = ["1", "2"]
    texto = P.bloque_dignidad(nombre, arts, "ecologia")
    permitidos = set(re.findall(r"\d+", nombre + " " + " ".join(arts)))
    assert set(re.findall(r"\d+", texto)) <= permitidos
    for organismo in ("municipalidad", "juzgado", "ministerio", "sernac",
                      "carabineros", "tribunal", "fiscalía"):
        assert organismo not in texto.lower()


def test_articulos_citados_orden_y_sin_duplicados():
    frases = [{"articulos": ["3", "1"]}, {"articulos": ["1", "5 bis"]}, {"articulos": []}]
    assert P.articulos_citados(frases) == ["3", "1", "5 bis"]


def test_bloque_dignidad_categoria_trabajo():
    texto = P.bloque_dignidad("Ley 21.165", ["3"], "trabajo")
    assert "trabajo" in texto.lower()
    assert "arts. 3" in texto


def test_inferir_categoria():
    assert P.inferir_categoria("Ley 21.202 · Protección de Humedales Urbanos") == "ecologia"
    assert P.inferir_categoria("Ley 21.100 · Prohíbe la entrega de bolsas plásticas") == "ecologia"
    assert P.inferir_categoria("Ley 21.165 · Jornada parcial para estudiantes trabajadores") == "trabajo"
    assert P.inferir_categoria("Código del Trabajo · Artículo 8 sobre práctica profesional") == "educacion"
    assert P.inferir_categoria("Ley X") == "generico"


def test_bloque_dignidad_desde_frases():
    frases = [{"articulos": ["1"]}, {"articulos": ["1", "2"]}]
    texto = P.bloque_dignidad_desde_frases("Ley de Humedales Urbanos", frases, "ecologia")
    assert "arts. 1, 2" in texto
    assert "Humedales" in texto


if __name__ == "__main__":
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_"):
            f()
            print("OK", nombre)
