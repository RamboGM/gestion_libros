import json
from libro import Libro

class Biblioteca:
    def __init__(self, archivo_json):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump(self.libros, archivo, indent=4)

    def agregar_libro(self, libro):
        self.libros.append(libro.__dict__)
        self.guardar_libros()

    def listar_libros(self):
        return self.libros

    def editar_libro(self, indice, nuevo_libro):
        self.libros[indice] = nuevo_libro.__dict__
        self.guardar_libros()

    def eliminar_libro(self, indice):
        self.libros.pop(indice)
        self.guardar_libros()
