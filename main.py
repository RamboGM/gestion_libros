# main.py
from gestor_libros import GestorLibros
from persistencia import cargar_datos, guardar_datos
from menu import mostrar_menu, ejecutar_opcion

ARCHIVO_DATOS = "data/libros.json"

def main():
    gestor = GestorLibros()
    gestor.libros = cargar_datos(ARCHIVO_DATOS)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "5":  # Opción para salir
            break
        ejecutar_opcion(opcion, gestor)

    # Guardar los datos antes de salir
    guardar_datos(ARCHIVO_DATOS, gestor.obtener_libros())
    print("Datos guardados correctamente.")

if __name__ == "__main__":
    main()
