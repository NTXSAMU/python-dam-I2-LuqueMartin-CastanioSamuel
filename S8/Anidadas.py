# ======================================================
#   PROGRAMA DE GESTIÓN DE EMPLEADOS DEL TALLER
# ======================================================
# Diccionario de empleados
# Cada clave será un ID (único)
# Cada valor será otro diccionario con información del empleado
# ======================================================

import os

empleados = {}

# Función para limpiar la consola (compatible con Windows/Linux)
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# Función para añadir un empleado
def agregar_empleado():
    limpiar()
    print("=== AÑADIR NUEVO EMPLEADO ===")

    id_emp = input("ID del empleado: ").strip()
    if id_emp in empleados:
        print("⚠️ Ya existe un empleado con ese ID.")
        return

    nombre = input("Nombre: ").strip()
    if not nombre:
        print("⚠️ El nombre no puede estar vacío.")
        return

    rol = input("Rol (mecánico / camarero / encargado): ").strip().lower()
    if rol not in ["mecánico", "camarero", "encargado"]:
        print("⚠️ Rol no válido.")
        return

    try:
        horas = float(input("Horas trabajadas a la semana: "))
        if horas < 0:
            raise ValueError
    except ValueError:
        print("⚠️ Valor de horas no válido.")
        return

    empleados[id_emp] = {
        "nombre": nombre,
        "rol": rol,
        "horas": horas
    }

    print(f"✅ Empleado '{nombre}' agregado correctamente.")

# Función para buscar empleados por campo
def buscar_empleado():
    limpiar()
    print("=== BÚSQUEDA DE EMPLEADO ===")
    campo = input("Buscar por (id/nombre/rol): ").strip().lower()
    valor = input("Valor a buscar: ").strip().lower()

    encontrados = []
    for id_emp, datos in empleados.items():
        if campo == "id" and id_emp.lower() == valor:
            encontrados.append((id_emp, datos))
        elif campo in datos and str(datos[campo]).lower() == valor:
            encontrados.append((id_emp, datos))

    if encontrados:
        print("\n=== RESULTADOS ===")
        for id_emp, datos in encontrados:
            print(f"ID: {id_emp} | Nombre: {datos['nombre']} | Rol: {datos['rol']} | Horas: {datos['horas']}")
    else:
        print("❌ No se encontraron coincidencias.")

# Función para calcular la prima según las horas
def calcular_prima():
    limpiar()
    print("=== CÁLCULO DE PRIMA ===")
    if not empleados:
        print("⚠️ No hay empleados registrados.")
        return

    try:
        id_emp = input("Introduce el ID del empleado: ").strip()
        emp = empleados[id_emp]
        horas = emp["horas"]
        # Prima simple: 1000€ por hora extra por encima de 6h
        prima = max(0, (horas - 6) * 1000)
        print(f"Empleado: {emp['nombre']} ({emp['rol']})")
        print(f"Horas: {horas}h | Prima: {prima:.2f}€")
    except KeyError:
        print("⚠️ ID no encontrado.")
    except Exception as e:
        print("⚠️ Error inesperado:", e)

# Función para mostrar todos los empleados
def mostrar_empleados():
    limpiar()
    print("=== LISTA DE EMPLEADOS ===")
    if not empleados:
        print("⚠️ No hay empleados registrados.")
        return
    for id_emp, datos in empleados.items():
        print(f"{id_emp} -> {datos['nombre']} | {datos['rol']} | {datos['horas']}h")

# Menú principal
def menu():
    while True:
        print("\n" + "="*50)
        print("      GESTIÓN DE EMPLEADOS DEL TALLER")
        print("="*50)
        print("1. Añadir empleado")
        print("2. Buscar empleado")
        print("3. Calcular prima")
        print("4. Mostrar todos")
        print("5. Salir")
        print("="*50)

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            buscar_empleado()
        elif opcion == "3":
            calcular_prima()
        elif opcion == "4":
            mostrar_empleados()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida.")
        input("\nPresiona ENTER para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
