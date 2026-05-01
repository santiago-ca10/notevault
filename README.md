# 📝 NoteVault

Aplicación de escritorio para la gestión de notas desarrollada en Python, utilizando MongoDB como base de datos documental y una interfaz moderna con CustomTkinter.

---

##  Características

- Crear notas con título y contenido
- Visualizar todas las notas almacenadas
- Buscar notas por título
- Actualizar contenido de notas existentes
- Eliminar notas
- Interfaz gráfica moderna con CustomTkinter
- Persistencia de datos mediante MongoDB y Docker
- Arquitectura organizada por capas

---

##  Arquitectura / Estructura

El proyecto sigue una arquitectura por capas:

```text
app/
├── config/ # Configuración de base de datos
├── models/ # Modelos de datos
├── repositories/ # Acceso a MongoDB (CRUD)
├── services/ # Lógica de negocio
├── ui/ # Interfaz gráfica
└── main.py # Punto de entrada
```

---

## 🐳 Base de Datos (MongoDB con Docker)

Para levantar MongoDB:

```bash
docker-compose up -d
```

## ⚙️ Configuración

Crear un archivo `.env` en la raíz del proyecto:
```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=notevault_db
COLLECTION_NAME=notas
```

## Instalación

Crear entorno virtual:
```
python -m venv venv
```
Activar entorno:
```
venv\Scripts\activate
```
Instalar dependencias:
```
pip install -r requirements.txt
```

## Ejecución

Ejecutar la aplicación:

```
python -m app.main
```

## 🧪 Tecnologías utilizadas

Python

pymongo

MongoDB

Docker

CustomTkinter

## 📌 Notas
- MongoDB se utiliza como base de datos NoSQL documental.
- La conexión se gestiona mediante variables de entorno.
- Se implementan operaciones CRUD completas.
- La aplicación sigue una arquitectura desacoplada basada en capas.
