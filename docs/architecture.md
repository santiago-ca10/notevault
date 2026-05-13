#  Arquitectura del Proyecto

El proyecto utiliza una arquitectura modular por capas.

---

#  Capas

##  Config

Contiene la conexión a MongoDB.

---

##  Repository

Contiene las operaciones CRUD hacia MongoDB.

Funciones principales:

- insert_one()
- find()
- update_one()
- delete_one()

---

##  Service

Contiene la lógica de negocio.

Ejemplo:

- validaciones
- manejo de datos

---

##  UI

Interfaz gráfica desarrollada con CustomTkinter.

Características:

- buscador dinámico
- editor de notas
- diseño moderno
- navegación estilo app móvil

---

##  Utils

Funciones auxiliares reutilizables.

Ejemplo:

- fechas relativas