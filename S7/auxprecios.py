# auxprecios.py
# Módulo para analizar una lista de precios con manejo de errores

def obtener_datos_basicos(lista_precios):
    try:
        if not isinstance(lista_precios, list):
            raise TypeError("El parámetro debe ser una lista.")
        if not all(isinstance(p, (int, float)) for p in lista_precios):
            raise ValueError("Todos los elementos deben ser números.")
        if len(lista_precios) == 0:
            raise ValueError("La lista está vacía.")

        cantidad = len(lista_precios)
        suma_total = sum(lista_precios)
        promedio = suma_total / cantidad

    except (TypeError, ValueError) as e:
        print(f"Error en obtener_datos_basicos: {e}")
        return None
    else:
        return {
            "cantidad": cantidad,
            "suma_total": suma_total,
            "promedio": promedio
        }


def precio_maximo(lista_precios):
    try:
        return max(lista_precios)
    except ValueError:
        print("Error: lista vacía en precio_maximo.")
        return None


def precio_minimo(lista_precios):
    try:
        return min(lista_precios)
    except ValueError:
        print("Error: lista vacía en precio_minimo.")
        return None


def precios_mayores_que(lista_precios, limite):
    return [p for p in lista_precios if p > limite]


def precios_menores_que(lista_precios, limite):
    return [p for p in lista_precios if p < limite]


def ordenar_precios(lista_precios, descendente=False):
    return sorted(lista_precios, reverse=descendente)


def analisis_avanzado(lista_precios):
    """Devuelve rango y mediana de la lista."""
    if not lista_precios:
        raise ValueError("La lista está vacía.")
    lista_ordenada = sorted(lista_precios)
    rango = max(lista_ordenada) - min(lista_ordenada)
    mitad = len(lista_ordenada) // 2

    if len(lista_ordenada) % 2 == 0:
        mediana = (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        mediana = lista_ordenada[mitad]

    return {"rango": rango, "mediana": mediana}
