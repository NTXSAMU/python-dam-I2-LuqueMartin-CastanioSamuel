# ============================================
#   SISTEMA DE GESTIÓN DE CONCESIONARIO
# ============================================

import getpass  # Para obtener el nombre del usuario del sistema

# Diccionario inicial con los coches disponibles
concesionario = {
    "C001": "Toyota Corolla",
    "C002": "Ford Focus",
    "C003": "BMW X3",
    "C004": "Audi A3",
    "C005": "Mercedes-Benz Clase C",
    "C006": "Volkswagen Golf",
    "C007": "Seat León",
    "C008": "Peugeot 208",
    "C009": "Renault Clio",
    "C010": "Nissan Qashqai",
    "C011": "Kia Sportage",
    "C012": "Hyundai Tucson",
    "C013": "Mazda CX-5",
    "C014": "Ford Mustang Dark Horse 2024"
}

# Obtener el nombre del usuario del equipo
usuario_equipo = getpass.getuser()

# Bucle principal
while True:
    print("\n🚗============================================🚗")
    print("         SISTEMA DE GESTIÓN DE CONCESIONARIO")
    print("🚗============================================🚗")
    print("""
    [1] 📋 Mostrar todos los coches
    [2] ➕ Insertar nuevo coche
    [3] ✏️ Modificar coche existente
    [4] 🗑️ Eliminar coche
    [5] 🔑 Ver IDs y Modelos juntos
    [6] 🚪 Salir del programa
    """)
    
    opcion = input("👉 Elige una opción (1-6): ").strip()

    # Mostrar todos los coches
    if opcion == "1":
        print("\n📋 LISTA DE COCHES DISPONIBLES:")
        print("--------------------------------------------------")
        for clave, valor in concesionario.items():
            print(f"{clave}  {valor}")
        print("--------------------------------------------------")
        print(f"Total de coches: {len(concesionario)}")

    # Insertar un nuevo coche
    elif opcion == "2":
        print("\n➕ INSERTAR NUEVO COCHE")
        nuevo_id = input("👉 Introduce un nuevo ID (por ejemplo C015): ").strip()
        if nuevo_id in concesionario.keys():
            print(f"⚠️ El ID {nuevo_id} ya existe. No se puede insertar.")
        else:
            nuevo_modelo = input("👉 Introduce el nombre del nuevo modelo: ").strip()
            concesionario[nuevo_id] = nuevo_modelo
            print(f"✅ Se ha insertado el coche {nuevo_id} {nuevo_modelo}")

    # Modificar un coche
    elif opcion == "3":
        print("\n✏️ MODIFICAR MODELO DE COCHE")
        modificar_id = input("👉 Introduce el ID del coche a modificar: ").strip()
        if modificar_id in concesionario.keys():
            nuevo_nombre = input(f"👉 Introduce el nuevo nombre para {concesionario[modificar_id]}: ").strip()
            concesionario[modificar_id] = nuevo_nombre
            print(f"✅ El coche {modificar_id} ha sido actualizado a: {nuevo_nombre}")
        else:
            print("❌ No se encontró el ID especificado.")

    # Eliminar un coche
    elif opcion == "4":
        print("\n🗑️ ELIMINAR COCHE")
        eliminar_id = input("👉 Introduce el ID del coche que deseas eliminar: ").strip()
        if eliminar_id in concesionario.keys():
            eliminado = concesionario[eliminar_id]
            del concesionario[eliminar_id]
            print(f"✅ El coche '{eliminado}' (ID {eliminar_id}) ha sido eliminado correctamente.")
        else:
            print("❌ No se encontró el ID especificado.")

    # Mostrar IDs y modelos juntos
    elif opcion == "5":
        print("\n🔑 LISTADO DE IDS Y MODELOS")
        print("--------------------------------------------------")
        for clave, valor in concesionario.items():
            print(f"{clave} {valor}")
        print("--------------------------------------------------")
        print(f"Total de coches: {len(concesionario)}")

    # Salir del programa mostrando el nombre del usuario del sistema
    elif opcion == "6":
        print("\n🚪 Cerrando el sistema del concesionario...")
        print(f"👋 Hasta pronto, {usuario_equipo}! Gracias por usar el programa. ✅")
        break

    # Opción inválida
    else:
        print("⚠️ Opción no válida. Inténtalo de nuevo.")
