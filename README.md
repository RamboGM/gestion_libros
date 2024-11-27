
# Gestión de Libros API

## Descripción

Este proyecto es una API desarrollada con FastAPI para gestionar una lista de libros. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre un archivo JSON que actúa como base de datos.

### Características:
- Crear libros mediante un `POST` a `/books`.
- Ver todos los libros disponibles mediante un `GET` a `/books`.
- Ver detalles de un libro específico mediante un `GET` a `/books/{id}`.
- Eliminar un libro mediante un `DELETE` a `/books/{id}`.

## Instalación

Para instalar el proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:

```bash
git clone https://github.com/rambo_GM/gestion_libros.git
```

2. Accede a la carpeta del proyecto:

```bash
cd gestion_libros
```

3. Crea un entorno virtual e instálalo:

```bash
python -m venv env
```

4. Activa el entorno virtual:
   
   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```

   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Uso

1. Inicia el servidor de la API:

```bash
uvicorn app.main:app --reload
```

2. Accede a la documentación interactiva de Swagger en:

```
http://127.0.0.1:8000/docs
```

### Ejemplo de peticiones:

- **Crear un libro**:
  Realiza un `POST` a `/books` con un cuerpo de solicitud como el siguiente:

  ```json
  {
    "id": 1,
    "title": "Cien años de soledad",
    "author": "Gabriel García Márquez",
    "year": 1967
  }
  ```

- **Obtener todos los libros**:
  Realiza un `GET` a `/books`.

- **Obtener un libro por ID**:
  Realiza un `GET` a `/books/{id}`, donde `{id}` es el ID del libro.

- **Eliminar un libro**:
  Realiza un `DELETE` a `/books/{id}`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama nueva con tu funcionalidad o corrección de errores:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza tus cambios y haz commit:
   ```bash
   git commit -am "Descripción de los cambios"
   ```
4. Empuja los cambios a tu repositorio:
   ```bash
   git push origin nueva-funcionalidad
   ```
5. Crea un Pull Request describiendo los cambios que has realizado.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.