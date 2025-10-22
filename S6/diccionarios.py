# ============================================
#   SISTEMA DE GESTIÓN DE CONCESIONARIO
# ============================================

import getpass  # Para obtener el nombre del usuario del sistema

# Diccionario plano: clave = ID, valor = [modelo, precio]
concesionario = {
    "C001": ["Toyota Corolla", 23000],
    "C002": ["Ford Focus", 25000],
    "C003": ["BMW X3", 48000],
    "C004": ["Audi A3", 32000],
    "C005": ["Mercedes-Benz Clase C", 45000],
    "C006": ["Volkswagen Golf", 27000],
    "C007": ["Seat León", 22000],
    "C008": ["Peugeot 208", 21000],
    "C009": ["Renault Clio", 19000],
    "C010": ["Nissan Qashqai", 28000],
    "C011": ["Kia Sportage", 30000],
    "C012": ["Hyundai Tucson", 31000],
    "C013": ["Mazda CX-5", 34000],
    "C014": ["Ford Mustang Dark Horse 2024", 65000]
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
            print(f"{clave} {valor[0]} - {valor[1]}€")
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
            concesionario[nuevo_id] = [nuevo_modelo, nuevo_precio]
            print(f"✅ Se ha insertado el coche {nuevo_id} {nuevo_modelo} - {nuevo_precio}€")

    # Modificar un coche existente
    elif opcion == "3":
        print("\n✏️ MODIFICAR MODELO O PRECIO")
        modificar_id = input("👉 Introduce el ID del coche a modificar: ").strip()
        if modificar_id in concesionario.keys():
            print(f"Modelo actual: {concesionario[modificar_id][0]} - {concesionario[modificar_id][1]}€")
            nuevo_nombre = input("👉 Introduce el nuevo nombre del modelo (ENTER para no cambiar): ").strip()
            nuevo_precio = input("👉 Introduce el nuevo precio (ENTER para no cambiar): ").strip()
            if nuevo_nombre:
                concesionario[modificar_id][0] = nuevo_nombre
            if nuevo_precio:
                try:
                    concesionario[modificar_id][1] = float(nuevo_precio)
                except ValueError:
                    print("⚠️ Precio no válido, se mantiene el anterior.")
            print(f"✅ Coche actualizado: {modificar_id} {concesionario[modificar_id][0]} - {concesionario[modificar_id][1]}€")
        else:
            print("❌ No se encontró el ID especificado.")

    # Eliminar un coche
    elif opcion == "4":
        print("\n🗑️ ELIMINAR COCHE")
        eliminar_id = input("👉 Introduce el ID del coche que deseas eliminar: ").strip()
        if eliminar_id in concesionario.keys():
            eliminado = concesionario[eliminar_id]
            del concesionario[eliminar_id]
            print(f"✅ Coche '{eliminado[0]}' eliminado correctamente.")
        else:
            print("❌ No se encontró el ID especificado.")

    # Mostrar IDs y modelos juntos
    elif opcion == "5":
        print("\n🔑 LISTADO DE IDS Y MODELOS")
        print("--------------------------------------------------")
        for clave, valor in concesionario.items():
            print(f"{clave} {valor[0]} - {valor[1]}€")
        print("--------------------------------------------------")
        print(f"Total de coches: {len(concesionario)}")

    # Mostrar métricas de precios
    elif opcion == "6":
        print("\n💰 MÉTRICAS DE PRECIOS")
        print("--------------------------------------------------")
        precios = [v[1] for v in concesionario.values()]
        suma = sum(precios)
        media = suma / len(precios)
        max_precio = max(precios)
        coche_mas_caro = [v[0] for v in concesionario.values() if v[1] == max_precio][0]
        print(f"🔹 Suma total de precios: {suma:.2f}€")
        print(f"🔹 Precio medio: {media:.2f}€")
        print(f"🔹 Coche más caro: {coche_mas_caro} ({max_precio:.2f}€)")
        print("--------------------------------------------------")

    # Salir del programa mostrando el nombre del usuario
    elif opcion == "7":
        print("\n🚪 Cerrando el sistema del concesionario...")
        print(f"👋 Hasta pronto, {usuario_equipo}! Gracias por usar el programa. ✅")
        break

    # Opción inválida
    else:
        print("⚠️ Opción no válida. Inténtalo de nuevo.")
