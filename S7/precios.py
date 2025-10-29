# precios.py
# Programa principal que usa auxprecios.py

import auxprecios as ap

def main():
    precios = [10, 20, 30, 40, 50]

    print("📊 Datos básicos:")
    print(ap.obtener_datos_basicos(precios))

    print("\n💰 Precio máximo y mínimo:")
    print("Máximo:", ap.precio_maximo(precios))
    print("Mínimo:", ap.precio_minimo(precios))

    print("\n🔼 Orden ascendente:", ap.ordenar_precios(precios))
    print("🔽 Orden descendente:", ap.ordenar_precios(precios, True))

    print("\n📈 Precios mayores que 25:", ap.precios_mayores_que(precios, 25))
    print("📉 Precios menores que 25:", ap.precios_menores_que(precios, 25))

    print("\n📊 Análisis avanzado:")
    print(ap.analisis_avanzado(precios))

if __name__ == "__main__":
    main()
