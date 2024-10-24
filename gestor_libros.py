from biblioteca import Biblioteca
from libro import Libro
from tabulate import tabulate

def mostrar_menu():
    print("\n--- Menú de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Listar libros")
    print("3. Editar libro")
    print("4. Eliminar libro")
    print("5. Salir")
    return input("Elige una opción: ")

def gestionar_biblioteca():
    biblioteca = Biblioteca('libros.json')
    
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año: ")
            genero = input("Género: ")
            libro = Libro(titulo, autor, anio, genero)
            biblioteca.agregar_libro(libro)
            print("Libro agregado correctamente.")
        
        elif opcion == '2':
            libros = biblioteca.listar_libros()
            if libros:
                print(tabulate(libros, headers="keys"))
            else:
                print("No hay libros en la biblioteca.")
        
        elif opcion == '3':
            libros = biblioteca.listar_libros()
            print(tabulate(libros, headers="keys"))
            indice = int(input("Elige el índice del libro a editar: "))
            titulo = input("Nuevo título: ")
            autor = input("Nuevo autor: ")
            anio = input("Nuevo año: ")
            genero = input("Nuevo género: ")
            nuevo_libro = Libro(titulo, autor, anio, genero)
            biblioteca.editar_libro(indice, nuevo_libro)
            print("Libro editado correctamente.")
        
        elif opcion == '4':
            libros = biblioteca.listar_libros()
            print(tabulate(libros, headers="keys"))
            indice = int(input("Elige el índice del libro a eliminar: "))
            biblioteca.eliminar_libro(indice)
            print("Libro eliminado correctamente.")
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, elige de nuevo.")

if __name__ == "__main__":
    gestionar_biblioteca()
