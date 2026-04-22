from app.config.database import get_collection

class NoteRepository:
    def __init__(self):
        self.col = get_collection()

    def create(self, note):
        return self.col.insert_one(note)

    def get_all(self):
        return list(self.col.find())

    def get_by_title(self, titulo):
        return self.col.find_one({"titulo": titulo})

    def delete(self, titulo):
        return self.col.delete_one({"titulo": titulo})

    def update(self, titulo, contenido):
        return self.col.update_one(
            {"titulo": titulo},
            {"$set": {"contenido": contenido}}
        )
        