class Libro:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.anio}) - Género: {self.genero}"
