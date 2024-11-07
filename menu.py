from gestor_libros import GestorLibros
from persistencia import cargar_datos, guardar_datos
from tabulate import tabulate

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Añadir libro")
    print("2. Modificar libro")
    print("3. Eliminar libro")
    print("4. Ver libros")
    print("5. Salir")

def ejecutar_opcion(opcion, gestor):
    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        anio = int(input("Ingrese el año de publicación: "))
        genero = input("Ingrese el género: ")
        gestor.agregar_libro(titulo, autor, anio, genero)
        print("Libro añadido correctamente.")
    elif opcion == "2":
        indice = int(input("Ingrese el índice del libro a modificar: "))
        titulo = input("Nuevo título: ")
        autor = input("Nuevo autor: ")
        anio = int(input("Nuevo año de publicación: "))
        genero = input("Nuevo género: ")
        gestor.modificar_libro(indice, titulo, autor, anio, genero)
        print("Libro modificado correctamente.")
    elif opcion == "3":
        indice = int(input("Ingrese el índice del libro a eliminar: "))
        gestor.eliminar_libro(indice)
        print("Libro eliminado correctamente.")
    elif opcion == "4":
        libros = gestor.obtener_libros()
        print(tabulate(libros, headers="keys"))
    elif opcion == "5":
        print("Saliendo...")
    else:
        print("Opción inválida.")
