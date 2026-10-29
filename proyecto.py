# Sistema de reportes de problemas en la universidad

reportes = []

def mostrar_menu():
    print("\n===== SISTEMA DE REPORTES UNIVERSITARIOS =====")
    print("1. Registrar un reporte")
    print("2. Ver todos los reportes")
    print("3. Actualizar estado de un reporte")
    print("4. Salir")


def registrar_reporte():
    print("\n--- Registrar un problema ---")
    estudiante = input("Nombre del estudiante: ").strip()
    problema = input("Describe el problema: ").strip()
    categoria = input(
        "Categoría (Internet, Equipo, Infraestructura): "
    ).strip()

    if not estudiante or not problema or not categoria:
        print("Error: todos los campos son obligatorios.")
        return

    reporte = {
        "id": len(reportes) + 1,
        "estudiante": estudiante,
        "problema": problema,
        "categoria": categoria,
        "estado": "Pendiente"
    }

    reportes.append(reporte)
    print(f"Reporte #{reporte['id']} registrado correctamente.")


def ver_reportes():
    print("\n--- Lista de reportes ---")

    if not reportes:
        print("Todavía no hay reportes registrados.")
        return

    for reporte in reportes:
        print(f"\nCódigo: {reporte['id']}")
        print(f"Estudiante: {reporte['estudiante']}")
        print(f"Problema: {reporte['problema']}")
        print(f"Categoría: {reporte['categoria']}")
        print(f"Estado: {reporte['estado']}")


def actualizar_estado():
    ver_reportes()

    if not reportes:
        return

    try:
        codigo = int(input("\nCódigo del reporte: "))
    except ValueError:
        print("Error: debes escribir un número.")
        return

    for reporte in reportes:
        if reporte["id"] == codigo:
            print("1. Pendiente")
            print("2. En proceso")
            print("3. Resuelto")

            opcion = input("Selecciona el nuevo estado: ")

            estados = {
                "1": "Pendiente",
                "2": "En proceso",
                "3": "Resuelto"
            }

            if opcion not in estados:
                print("Error: opción no válida.")
                return

            reporte["estado"] = estados[opcion]
            print("Estado actualizado correctamente.")
            return

    print("No se encontró ese reporte.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_reporte()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            actualizar_estado()
        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()