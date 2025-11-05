#def programa():
#alumnos = []
#n = input("cuantos alumnos?")
#for i in range(0, int(n)):
#nota = int(input("nota:"))
#alumnos.append(nota)
#media = sum(alumnos)/len(alumnos)
#print("media", media)
#print("aprobados:")
#for i in alumnos:
#if i>=5:
#print(i)

# -------------------------------------------

#def programa():
 #   alumnos = []
 #   n = input("cuantos alumnos?")
  #  for i in range(0, int(n)):
   #     nota = int(input("nota:"))
  #      alumnos.append(nota)
   # media = sum(alumnos) / len(alumnos)
    #print("media", media)
   # print("aprobados:")
   # for i in alumnos:
    #    if i >= 5:
     #       print(i)


# programa()

#-------------------------------------------------------
# Solución mejorada en cuanto modularidad y funcionalidad


def pedir_numero_alumnos():
    """Devuelve el número de alumnos introducido por el usuario."""
    while True:
        try:
            n = int(input("¿Cuántos alumnos hay? "))
            if n > 0:
                return n
            print("⚠️ El número debe ser mayor que cero.")
        except ValueError:
            print("⚠️ Debes introducir un número entero.")


def pedir_notas(num_alumnos):
    """
    Recibe el número de alumnos y devuelve una lista con sus notas.
    """
    notas = []
    for i in range(num_alumnos):
        while True:
            try:
                nota = float(input(f"Introduce la nota del alumno {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("⚠️ La nota debe estar entre 0 y 10.")
            except ValueError:
                print("⚠️ Debes introducir un número válido.")
    return notas


def calcular_media(notas):
    """
    Recibe una lista de notas y devuelve la media.
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def filtrar_aprobados(notas):
    """
    Recibe una lista de notas y devuelve una lista con las notas aprobadas.
    """
    return [n for n in notas if n >= 5]


def mostrar_resultados(media, aprobados):
    """
    Muestra los resultados finales.
    Recibe la media y la lista de aprobados como parámetros.
    """
    print("\n=== RESULTADOS ===")
    print(f"Media de la clase: {media:.2f}")
    print("Aprobados:")
    if aprobados:
        for nota in aprobados:
            print(f" - {nota}")
    else:
        print("Ningún alumno ha aprobado.")


def programa():
    """
    Función principal: coordina la ejecución completa del programa.
    """
    print("=== PROGRAMA DE NOTAS ===")

    # Pedimos el número de alumnos y sus notas
    num_alumnos = pedir_numero_alumnos()
    notas = pedir_notas(num_alumnos)

    # Calculamos resultados (sin imprimir dentro de las funciones)
    media = calcular_media(notas)
    aprobados = filtrar_aprobados(notas)

    # Mostramos los resultados pasando parámetros
    mostrar_resultados(media, aprobados)


# ======================================================
#   EJECUCIÓN DEL PROGRAMA
# ======================================================
if __name__ == "__main__":
    programa()
