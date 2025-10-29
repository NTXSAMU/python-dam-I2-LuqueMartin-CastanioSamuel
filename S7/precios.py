# precios.py
# Programa que utiliza el módulo auxprecios.py con manejo de errores

import auxprecios

print("=== CASO 1: Lista de precios válida ===")
precios = [23.5, 45.9, 12.0, 89.4, 56.7, 34.2, 12.0, 78.5]

datos = auxprecios.obtener_datos_basicos(precios)
if datos:
    print(f"Cantidad: {datos['cantidad']}")
    print(f"Suma total: {datos['suma_total']}")
    print(f"Promedio: {datos['promedio']}")

print(f"Precio máximo: {auxprecios.precio_maximo(precios)}")
print(f"Precio mínimo: {auxprecios.precio_minimo(precios)}")
print(f"Precios mayores que 50: {auxprecios.precios_mayores_que(precios, 50)}")
print(f"Precios menores que 20: {auxprecios.precios_menores_que(precios, 20)}")
print(f"Precios ordenados (descendente): {auxprecios.ordenar_precios(precios, True)}")
print(auxprecios.analisis_avanzado(precios))


# ------------------------------------------------------------
print("\n=== CASO 2: Lista con errores (controlados) ===")

# Caso de error 1: lista vacía
lista_vacia = []
auxprecios.obtener_datos_basicos(lista_vacia)

# Caso de error 2: lista con datos inválidos
lista_invalida = [20, "error", 50, None]
auxprecios.obtener_datos_basicos(lista_invalida)

# Caso de error 3: límite no numérico
auxprecios.precios_mayores_que(precios, "cincuenta")
