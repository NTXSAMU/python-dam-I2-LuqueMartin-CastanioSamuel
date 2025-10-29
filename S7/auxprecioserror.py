# auxprecioserror.py
# Módulo con manejo de errores explícito en todas las funciones

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
        return {"cantidad": cantidad, "suma_total": suma_total, "promedio": promedio}
    finally:
        print("Ejecución finalizada en obtener_datos_basicos.")


def precio_maximo(lista_precios):
    try:
        if not lista_precios:
            raise ValueError("La lista está vacía.")
        return max(lista_precios)
    except ValueError as e:
        print(f"Error en precio_maximo: {e}")
        return None
    finally:
        print("Finalizó precio_maximo.")


def precio_minimo(lista_precios):
    try:
        if not lista_precios:
            raise ValueError("La lista está vacía.")
        return min(lista_precios)
    except ValueError as e:
        print(f"Error en precio_minimo: {e}")
        return None
    finally:
        print("Finalizó precio_minimo.")


def precios_mayores_que(lista_precios, limite):
    try:
        if not isinstance(limite, (int, float)):
            raise TypeError("El límite debe ser numérico.")
        return [p for p in lista_precios if p > limite]
    except Exception as e:
        print(f"Error en precios_mayores_que: {e}")
        return []
    finally:
        print("Finalizó precios_mayores_que.")


def precios_menores_que(lista_precios, limite):
    try:
        if not isinstance(limite, (int, float)):
            raise TypeError("El límite debe ser numérico.")
        return [p for p in lista_precios if p < limite]
    except Exception as e:
        print(f"Error en precios_menores_que: {e}")
        return []
    finally:
        print("Finalizó precios_menores_que.")


def ordenar_precios(lista_precios, descendente=False):
    try:
        return sorted(lista_precios, reverse=descendente)
    except Exception as e:
        print(f"Error en ordenar_precios: {e}")
        return []
    finally:
        print("Finalizó ordenar_precios.")


def analisis_avanzado(lista_precios):
    try:
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

    except Exception as e:
        print(f"Error en analisis_avanzado: {e}")
        return None
    finally:
        print("Finalizó analisis_avanzado.")
