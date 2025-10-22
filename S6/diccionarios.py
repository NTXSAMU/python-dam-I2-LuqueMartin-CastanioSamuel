# ============================================
#   SISTEMA DE GESTIÓN DE CONCESIONARIO
# ============================================

import getpass  # Para obtener el nombre del usuario del sistema

# Diccionario con diccionarios anidados: clave = ID, valor = {modelo, precio}
concesionario = {
    "C001": {"modelo": "Toyota Corolla", "precio": 23000},
    "C002": {"modelo": "Ford Focus", "precio": 25000},
    "C003": {"modelo": "BMW X3", "precio": 48000},
    "C004": {"modelo": "Audi A3", "precio": 32000},
    "C005": {"modelo": "Mercedes-Benz Clase C", "precio": 45000},
    "C006": {"modelo": "Volkswagen Golf", "precio": 27000},
    "C007": {"modelo": "Seat León", "precio": 22000},
    "C008": {"modelo": "Peugeot 208", "precio": 21000},
    "C009": {"modelo": "Renault Clio", "precio": 19000},
    "C010": {"modelo": "Nissan Qashqai", "precio": 28000},
    "C011": {"modelo": "Kia Sportage", "precio": 30000},
    "C012": {"modelo": "Hyundai Tucson", "precio": 31000},
    "C013": {"modelo": "Mazda CX-5", "precio": 34000},
    "C014": {"modelo": "Ford Mustang Dark Horse 2024", "precio": 65000}
}

# Obtener el nombre del usuario del equipo
usuario_equipo = getpass.getuser()

# Bucle principal
while True:
    print("\n🚗============================================🚗")
    print(f"  SISTEMA DE GESTIÓN DE CONCESIONARIO - Usuario: {usuario_equipo}")
    print("🚗============================================🚗")
    print("""
    [1] 📋 Mostrar todos los coches
    [2] ➕ Insertar nuevo coche
    [3] ✏️ Modificar coche existente
    [4] 🗑️ Eliminar coche
    [5] 🔑 Ver IDs y Modelos
    [6] 💰 Mostrar métricas de precios
    [7] 🚪 Salir del programa
    """)

    opcion = input("👉 Elige una opción (1-7): ").strip()

    # Mostrar todos los coches
    if opcion == "1":
        print("\n📋 LISTA DE COCHES DISPONIBLES:")
        print("--------------------------------------------------")
        for clave, valor in concesionario.items():
            print(f"{clave} {valor['modelo']} - {valor['precio']}€")
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
            while True:
                try:
                    nuevo_precio = float(input("👉 Introduce el precio del coche (€): "))
                    break
                except ValueError:
                    print("⚠️ Introduce un valor numérico válido.")
            concesionario[nuevo_id] = {"modelo": nuevo_modelo, "precio": nuevo_precio}
            print(f"✅ Se ha insertado el coche {nuevo_id} {nuevo_modelo} - {nuevo_precio}€")

    # Modificar un coche existente
    elif opcion == "3":
        print("\n✏️ MODIFICAR MODELO O PRECIO")
        modificar_id = input("👉 Introduce el ID del coche a modificar: ").strip()
        if modificar_id in concesionario.keys():
            print(f"Modelo actual: {concesionario[modificar_id]['modelo']} - {concesionario[modificar_id]['precio']}€")
            nuevo_nombre = input("👉 Introduce el nuevo nombre del modelo (ENTER para no cambiar): ").strip()
            nuevo_precio = input("👉 Introduce el nuevo precio (ENTER para no cambiar): ").strip()
            if nuevo_nombre:
                concesionario[modificar_id]['modelo'] = nuevo_nombre
            if nuevo_precio:
                try:
                    concesionario[modificar_id]['precio'] = float(nuevo_precio)
                except ValueError:
                    print("⚠️ Precio no válido, se mantiene el anterior.")
            print(f"✅ Coche actualizado: {modificar_id} {concesionario[modificar_id]['modelo']} - {concesionario[modificar_id]['precio']}€")
        else:
            print("❌ No se encontró el ID especificado.")

    # Eliminar un coche
    elif opcion == "4":
        print("\n🗑️ ELIMINAR COCHE")
        eliminar_id = input("👉 Introduce el ID del coche que deseas eliminar: ").strip()
        if eliminar_id in concesionario.keys():
            eliminado = concesionario[eliminar_id]
            del concesionario[eliminar_id]
            print(f"✅ Coche '{eliminado['modelo']}' eliminado correctamente.")
        else:
            print("❌ No se encontró el ID especificado.")

    # Mostrar IDs y modelos juntos
    elif opcion == "5":
        print("\n🔑 LISTADO DE IDS Y MODELOS")
        print("--------------------------------------------------")
        for clave, valor in concesionario.items():
            print(f"{clave} {valor['modelo']} - {valor['precio']}€")
        print("--------------------------------------------------")
        print(f"Total de coches: {len(concesionario)}")

    # Mostrar métricas de precios
    elif opcion == "6":
        print("\n💰 MÉTRICAS DE PRECIOS")
        print("--------------------------------------------------")
        precios = [v['precio'] for v in concesionario.values()]
        suma = sum(precios)
        media = suma / len(precios)
        max_precio = max(precios)
        coche_mas_caro = [v['modelo'] for v in concesionario.values() if v['precio'] == max_precio][0]
        min_precio = min(precios)
        coche_mas_barato = [v['modelo'] for v in concesionario.values() if v['precio'] == min_precio][0]
        print(f"🔹 Suma total de precios: {suma:.2f}€")
        print(f"🔹 Precio medio: {media:.2f}€")
        print(f"🔹 Coche más caro: {coche_mas_caro} ({max_precio:.2f}€)")
        print(f"🔹 Coche más barato: {coche_mas_barato} ({min_precio:.2f}€)")
        print("--------------------------------------------------")

    # Salir del programa mostrando el nombre del usuario
    elif opcion == "7":
        print("\n🚪 Cerrando el sistema del concesionario...")
        print(f"👋 Hasta pronto, {usuario_equipo}! Gracias por usar el programa. ✅")
        break

    # Opción inválida
    else:
        print("⚠️ Opción no válida. Inténtalo de nuevo.")
