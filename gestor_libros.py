# gestor_libros.py

class GestorLibros:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, anio, genero):
        libro = {
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "genero": genero
        }
        self.libros.append(libro)

    def modificar_libro(self, indice, titulo, autor, anio, genero):
        if 0 <= indice < len(self.libros):
            self.libros[indice] = {
                "titulo": titulo,
                "autor": autor,
                "anio": anio,
                "genero": genero
            }

    def eliminar_libro(self, indice):
        if 0 <= indice < len(self.libros):
            self.libros.pop(indice)

    def obtener_libros(self):
        return self.libros
