from app.repositories.note_repository import NoteRepository
from datetime import datetime

class NoteService:

    def __init__(self):
        self.repo = NoteRepository()

    def crear_nota(self, titulo, contenido):
        if not titulo:
            raise ValueError("El título es obligatorio")
        return self.repo.create({
            "titulo": titulo,
            "contenido": contenido,
            "fecha" : datetime.now()
        })

    def obtener_notas(self):
        return self.repo.get_all()

    def buscar_nota(self, titulo):
        return self.repo.get_by_title(titulo)

    def eliminar_nota(self, titulo):
        return self.repo.delete(titulo)

    def actualizar_nota(self, titulo, contenido):
        return self.repo.update(titulo, contenido)