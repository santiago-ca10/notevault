#test_service.py

import pytest
from app.services.note_service import NoteService


def test_crear_nota_valida():
    service = NoteService()
    result = service.crear_nota("Test", "Contenido")

    assert result is not None


def test_crear_nota_sin_titulo():
    service = NoteService()

    with pytest.raises(ValueError):
        service.crear_nota("", "Contenido")


def test_obtener_notas():
    service = NoteService()
    notas = service.obtener_notas()

    assert isinstance(notas, list)