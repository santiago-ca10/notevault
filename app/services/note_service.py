from datetime import datetime

from app.repositories.note_repository import NoteRepository


class NoteService:
    """Servicio encargado de gestionar la lógica de negocio de las notas."""

    def __init__(self):
        # Instancia del repositorio para acceder a MongoDB
        self.repo = NoteRepository()

    def crear_nota(self, titulo, contenido):
        """
        Crea una nueva nota validando que el título exista.
        """

        if not titulo:
            raise ValueError("El título es obligatorio")

        return self.repo.create({
            "titulo": titulo,
            "contenido": contenido,
            "fecha": datetime.now()
        })

    def obtener_notas(self):
        """
        Obtiene todas las notas almacenadas.
        """
        return self.repo.get_all()

    def buscar_nota(self, titulo):
        """
        Busca una nota por su título.
        """
        return self.repo.get_by_title(titulo)

    def eliminar_nota(self, titulo):
        """
        Elimina una nota según el título proporcionado.
        """
        return self.repo.delete(titulo)

    def actualizar_nota(self, titulo, contenido):
        """
        Actualiza el contenido de una nota existente.
        """
        return self.repo.update(titulo, contenido)