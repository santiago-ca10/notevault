# test_repository.py

from app.repositories.note_repository import NoteRepository


def test_insert_and_get():
    repo = NoteRepository()

    repo.create({
        "titulo": "TestRepo",
        "contenido": "Contenido test"
    })

    notas = repo.get_all()

    assert any(n["titulo"] == "TestRepo" for n in notas)


def test_delete():
    repo = NoteRepository()

    repo.create({
        "titulo": "EliminarTest",
        "contenido": "..."
    })

    repo.delete("EliminarTest")

    notas = repo.get_all()

    assert not any(n["titulo"] == "EliminarTest" for n in notas)