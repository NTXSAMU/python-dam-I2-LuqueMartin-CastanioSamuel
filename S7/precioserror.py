# precioserror.py
# Programa principal que usa auxprecioserror.py

import auxprecioserror as ape

def main():
    # Caso 1: lista vacía
    precios_vacios = []
    print("Caso 1: Lista vacía")
    ape.obtener_datos_basicos(precios_vacios)
    ape.precio_maximo(precios_vacios)
    ape.precio_minimo(precios_vacios)
    print()

    # Caso 2: lista con valores no numéricos
    precios_invalidos = [10, "veinte", 30]
    print("Caso 2: Lista con valores no numéricos")
    ape.obtener_datos_basicos(precios_invalidos)
    print()

    # Caso 3: correcto
    precios = [15, 25, 35, 45, 55]
    print("Caso 3: Lista correcta")
    print(ape.obtener_datos_basicos(precios))
    print(ape.analisis_avanzado(precios))

if __name__ == "__main__":
    main()
