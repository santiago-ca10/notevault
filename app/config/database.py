import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Carga las variables de entorno desde el archivo .env
load_dotenv()


def get_collection():
    """
    Establece la conexión con MongoDB y retorna
    la colección principal utilizada por la aplicación.
    """

    uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")
    col_name = os.getenv("COLLECTION_NAME")

    client = MongoClient(uri)
    db = client[db_name]

    return db[col_name]