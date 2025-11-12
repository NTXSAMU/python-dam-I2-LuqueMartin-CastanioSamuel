"""
Generador de personajes de videojuegos - versión sencilla y muy comentada
Requisitos cumplidos:
 - Módulos estándar usados: random, datetime, math
 - Al menos 3 funciones que devuelven valores
 - Control de errores con try/except
 - Comentarios y docstrings explicativos
"""

import random          # Para generar elementos al azar
from datetime import datetime  # Para marcar la fecha/hora de creación
import math            # Para operaciones matemáticas (ej.: cálculo de "poder")

# ---------------------------
# FUNCIONES PRINCIPALES
# ---------------------------

def generar_nombre():
    """
    Genera y devuelve un nombre aleatorio para el personaje.
    Devuelve una cadena (str).
    """
    try:
        # Listas pequeñas de sílabas / prefijos para construir nombres simples
        prefijos = ["Ara", "Bel", "Cor", "Dra", "Eli", "Fen", "Gal", "Hel", "Ira", "Jun"]
        sufijos  = ["dor", "lia", "mar", "nix", "ros", "thas", "vir", "wen", "xor", "ys"]
        # Elegimos uno de cada lista y los concatenamos
        nombre = random.choice(prefijos) + random.choice(sufijos)
        return nombre
    except Exception as e:
        # Nunca falla normalmente, pero en caso de error devolvemos un nombre por defecto
        print("⚠️ Error generando nombre:", e)
        return "NombreDefault"

def generar_clase():
    """
    Genera y devuelve la clase del personaje (ej.: Guerrero, Mago...).
    Devuelve una cadena (str).
    """
    try:
        clases = ["Guerrero", "Mago", "Arquero", "Ladrón", "Clérigo", "Berserker"]
        return random.choice(clases)
    except Exception as e:
        print("⚠️ Error generando clase:", e)
        return "Aventurero"

def generar_stats():
    """
    Genera y devuelve un diccionario con estadísticas básicas:
    fuerza, destreza, inteligencia, vida_base (HP), mana_base.
    Devuelve dict.
    """
    
    try:
        # Estadísticas base generadas aleatoriamente en rangos sencillos
        fuerza = random.randint(5, 18)
        destreza = random.randint(5, 18)
        inteligencia = random.randint(5, 18)

        # Vida y mana base se derivan de otras stats (ejemplo simple)
        vida_base = 50 + fuerza * 3      # más fuerza -> más vida
        mana_base = 30 + inteligencia * 3  # más inteligencia -> más mana

        return {
            "fuerza": fuerza,
            "destreza": destreza,
            "inteligencia": inteligencia,
            "vida_base": vida_base,
            "mana_base": mana_base
        }
    except Exception as e:
        print("⚠️ Error generando estadísticas:", e)
        # En caso de problema devolvemos stats mínimas seguras
        return {"fuerza": 5, "destreza": 5, "inteligencia": 5, "vida_base": 65, "mana_base": 45}

def calcular_poder(stats):
    """
    Calcula y devuelve un valor numérico que representa el 'poder' del personaje.
    Usa math para combinar estadísticas de forma sencilla.
    Devuelve float.
    """
    try:
        # Extraemos stats (con valores por defecto si faltan)
        f = stats.get("fuerza", 5)
        d = stats.get("destreza", 5)
        i = stats.get("inteligencia", 5)

        # Fórmula simple: combinación ponderada + raíz para balancear valores altos
        poder = math.sqrt(f*2 + d*1.5 + i*2.5) * 1.2
        return round(poder, 2)
    except Exception as e:
        print("⚠️ Error calculando poder:", e)
        return 0.0

# ---------------------------
# FUNCIONES AUXILIARES
# ---------------------------

def mostrar_personaje(persona):
    """
    Recibe un diccionario con los datos del personaje y lo muestra bonito por pantalla.
    No devuelve nada.
    """
    # persona es un dict con claves: nombre, clase, stats, fecha, poder
    print("\n------------------------------")
    print(f"Nombre: {persona['nombre']}")
    print(f"Clase: {persona['clase']}")
    print(f"Creado: {persona['fecha']}")
    print("Estadísticas:")
    for k, v in persona["stats"].items():
        print(f"  - {k}: {v}")
    print(f"Poder (valor calculado): {persona['poder']}")
    print("------------------------------\n")

# ---------------------------
# PROGRAMA PRINCIPAL (INTERACTIVO SENCILLO)
# ---------------------------

def main():
    """
    Función principal que gestiona la interacción con el usuario para generar personajes.
    """
    print("=== Generador sencillo de personajes ===")

    # Pedimos al usuario cuántos personajes quiere generar; validamos con try/except
    try:
        cantidad = int(input("¿Cuántos personajes quieres generar? (ej. 1) > ").strip())
        if cantidad <= 0:
            print("Se espera un número positivo. Generando 1 por defecto.")
            cantidad = 1
    except ValueError:
        print("Entrada no válida. Generando 1 personaje por defecto.")
        cantidad = 1
    except Exception as e:
        print("Error inesperado leyendo la cantidad:", e)
        cantidad = 1

    personajes = []  # lista donde guardaremos los personajes generados

    for i in range(cantidad):
        # Timestamp para saber cuándo se creó el personaje
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Generamos cada parte usando las funciones creadas
        nombre = generar_nombre()
        clase = generar_clase()
        stats = generar_stats()
        poder = calcular_poder(stats)

        # Montamos el diccionario del personaje
        personaje = {
            "nombre": nombre,
            "clase": clase,
            "fecha": fecha,
            "stats": stats,
            "poder": poder
        }

        personajes.append(personaje)

    # Mostramos todos los personajes generados
    for p in personajes:
        mostrar_personaje(p)

    print("¡Listo! Si quieres, puedo guardar estos personajes en un archivo o añadir más atributos.")
    # Fin del main

# Ejecuta el programa si el archivo se corre directamente
if __name__ == "__main__":
    main()
