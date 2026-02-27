print("------------------------------------------")
print("------------REGISTRO DE VENRAS------------")
print("------------------------------------------")
print("")

# Validar nombre (que no sea vacío ni solo números)
while True:
    nombres = input("Nombre del cliente: ").strip()
    if nombres == "":
        print("El nombre no puede estar vacío.")
    elif nombres.isnumeric():
        print("El nombre no puede ser solo números.")
    else:
        break

# Validar precio (solo números)
while True:
    try:
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
        else:
            break
    except ValueError:
        print("Error: Debes ingresar un número válido para el precio.")

# Validar cantidad (solo enteros)
while True:
    try:
        cantidad_compra = int(input("Ingresa la cantidad comprada: "))
        if cantidad_compra <= 0:
            print("La cantidad debe ser mayor que 0.")
        else:
            break
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

# Validar VIP (solo si o no)
while True:
    vip_input = input("¿Eres VIP? (si/no): ").strip().lower()
    if vip_input == "si":
        vip = True
        break
    elif vip_input == "no":
        vip = False
        break
    else:
        print("Respuesta inválida. Escribe 'si' o 'no'.")

# Cálculos
descuento = 10
subtotal = precio * cantidad_compra

if vip:
    print("Se aplica descuento VIP del 10%")
    total = subtotal - (subtotal * descuento) / 100
else:
    total = subtotal

iva = subtotal * 0.19
total += iva

print("------------------------------------------")
print("Cliente:", nombres)
print("Precio:", precio)
print("Cantidad:", cantidad_compra)
print("Es VIP?:", "Sí" if vip else "No")
print("IVA 19%:", iva)
print("Total a pagar: $", round(total, 2))
print("------------------------------------------")