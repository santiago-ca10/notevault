#  Base de Datos

El proyecto utiliza MongoDB como base de datos documental.

---

#  Docker

MongoDB se ejecuta mediante Docker.

## Ejecutar contenedor

```bash
docker compose up -d
```

---

#  Puerto utilizado

```text
27017
```

---

#  Colección

```text
notes
```

---

#  Estructura Documento

```json
{
  "titulo": "Mi nota",
  "contenido": "Contenido...",
  "fecha": "2026-05-12"
}
```

---

#  Operaciones CRUD

## Crear nota

```python
insert_one()
```

---

## Leer notas

```python
find()
```

---

## Actualizar nota

```python
update_one()
```

---

## Eliminar nota

```python
delete_one()
```