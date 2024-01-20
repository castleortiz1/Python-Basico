def convertir_moneda(cantidad, tasa_cambio):
    return cantidad * tasa_cambio

# Tasas de cambio ficticias
tasa_usd_a_eur = 0.85
tasa_usd_a_gbp = 0.75

# Solicitar entrada al usuario
cantidad = float(input("Ingrese la cantidad en USD: "))

# Mostrar opciones de monedas
print("Opciones de conversión:")
print("1. USD a EUR")
print("2. USD a GBP")

opcion = input("Seleccione la opción de conversión (1 o 2): ")

if opcion == '1':
    resultado = convertir_moneda(cantidad, tasa_usd_a_eur)
    print(f"{cantidad} USD son {resultado} EUR")
elif opcion == '2':
    resultado = convertir_moneda(cantidad, tasa_usd_a_gbp)
    print(f"{cantidad} USD son {resultado} GBP")
else:
    print("Opción no válida")
