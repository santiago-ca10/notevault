from app.config.database import get_collection


class NoteRepository:
    """Repositorio encargado de las operaciones CRUD sobre MongoDB."""

    def __init__(self):
        # Obtiene la colección de notas desde la configuración
        self.col = get_collection()

    def create(self, note):
        """
        Inserta una nueva nota en la base de datos.
        """
        return self.col.insert_one(note)

    def get_all(self):
        """
        Obtiene todas las notas almacenadas.
        """
        return list(self.col.find())

    def get_by_title(self, titulo):
        """
        Busca una nota utilizando su título.
        """
        return self.col.find_one({"titulo": titulo})

    def delete(self, titulo):
        """
        Elimina una nota según el título proporcionado.
        """
        return self.col.delete_one({"titulo": titulo})

    def update(self, titulo, contenido):
        """
        Actualiza el contenido de una nota existente.
        """
        return self.col.update_one(
            {"titulo": titulo},
            {"$set": {"contenido": contenido}}
        )