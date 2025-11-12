import random
from datetime import datetime
import math

# ==========================
# FUNCIONES DE GENERACIÓN
# ==========================

def generar_nombre():
    prefijos = ["Ara", "Bel", "Cor", "Dra", "Eli", "Fen", "Gal", "Hel", "Ira", "Jun"]
    sufijos  = ["dor", "lia", "mar", "nix", "ros", "thas", "vir", "wen", "xor", "ys"]
    return random.choice(prefijos) + random.choice(sufijos)

def generar_clase():
    clases = ["Guerrero", "Mago", "Arquero", "Ladrón", "Clérigo", "Berserker"]
    return random.choice(clases)

def generar_arma(clase):
    """
    Devuelve un arma adecuada según la clase del personaje.
    """
    try:
        if clase == "Guerrero":
            armas = ["Espada", "Hacha", "Lanza"]
        elif clase == "Mago":
            armas = ["Bastón", "Varita mágica", "Orbe"]
        elif clase == "Arquero":
            armas = ["Arco", "Ballesta", "Daga"]
        elif clase == "Ladrón":
            armas = ["Cuchillo", "Daga doble", "Garrote"]
        elif clase == "Clérigo":
            armas = ["Maza", "Báculo sagrado", "Libro de oraciones"]
        elif clase == "Berserker":
            armas = ["Hacha gigante", "Martillo", "Espadón"]
        else:
            armas = ["Puños"]

        return random.choice(armas)
    except Exception as e:
        print("⚠️ Error generando arma:", e)
        return "Arma desconocida"

def generar_stats():
    fuerza = random.randint(5, 18)
    destreza = random.randint(5, 18)
    inteligencia = random.randint(5, 18)
    vida_base = 50 + fuerza * 3
    mana_base = 30 + inteligencia * 3
    return {"fuerza": fuerza, "destreza": destreza, "inteligencia": inteligencia,
            "vida_base": vida_base, "mana_base": mana_base}

def calcular_poder(stats):
    f = stats.get("fuerza", 5)
    d = stats.get("destreza", 5)
    i = stats.get("inteligencia", 5)
    poder = math.sqrt(f*2 + d*1.5 + i*2.5) * 1.2
    return round(poder, 2)

# ==========================
# FUNCIÓN PARA MOSTRAR DATOS
# ==========================

def mostrar_personaje(persona):
    print("\n------------------------------")
    print(f"Nombre: {persona['nombre']}")
    print(f"Clase: {persona['clase']}")
    print(f"Arma: {persona['arma']}")
    print(f"Creado: {persona['fecha']}")
    print("Estadísticas:")
    for k, v in persona["stats"].items():
        print(f"  - {k}: {v}")
    print(f"Poder (valor calculado): {persona['poder']}")
    print("------------------------------\n")

# ==========================
# PROGRAMA PRINCIPAL
# ==========================

def main():
    print("=== Generador de personajes ===")

    try:
        cantidad = int(input("¿Cuántos personajes quieres generar? > ").strip())
        if cantidad <= 0:
            print("Valor no válido. Generando 1 personaje por defecto.")
            cantidad = 1
    except:
        print("Error en la entrada. Generando 1 personaje por defecto.")
        cantidad = 1

    personajes = []

    for i in range(cantidad):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nombre = generar_nombre()
        clase = generar_clase()
        arma = generar_arma(clase)  # 🟢 NUEVA FUNCIÓN AQUÍ
        stats = generar_stats()
        poder = calcular_poder(stats)

        personaje = {
            "nombre": nombre,
            "clase": clase,
            "arma": arma,
            "fecha": fecha,
            "stats": stats,
            "poder": poder
        }

        personajes.append(personaje)

    for p in personajes:
        mostrar_personaje(p)

if __name__ == "__main__":
    main()
