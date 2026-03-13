#Se solicita al usuario que ingrese el nombre del producto.
nombre = input("Ingrese el nombre del producto: ")

# Se valida y se solicita el precio (float) del producto, asegurando que el usuario ingrese un valor numérico válido.
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: El precio debe ser un valor numérico. Inténtelo de nuevo.")

# Se valida y se solicita la cantidad (int) del producto, asegurando que el usuario ingrese un número entero válido.
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: La cantidad debe ser un número entero. Inténtelo de nuevo.")

# Calcular el costo total
costo_total = precio * cantidad

# La consola nos va mostar un resumen del producto ingresado, su precio, cantidad y el costo total de la existencia.
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# Este programa permite gestionar el ingreso de un producto al inventario, 
# validando que los datos numéricos sean correctos, calculando el costo 
# total de la existencia y mostrando un resumen detallado al usuario.
