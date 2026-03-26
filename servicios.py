def agregar_producto(inventario):
    """
    Solicita nombre, precio y cantidad de un producto y lo agrega al inventario.
 
    Cada campo se valida en un bucle independiente:
    - nombre: no puede estar vacío.
    - precio: decimal mayor a 0.
    - cantidad: entero mayor a 0.
 
    Al finalizar muestra un resumen con el costo total de la existencia agregada.
 
    Args:
        inventario (list): Lista de diccionarios donde se almacenan los productos.
    """
    nombre = input("Ingrese el nombre del producto: ")
    while nombre == "":
        nombre = input("EL NOMBRE NO PUEDE ESTAR VACÍO. Ingrese el nombre: ")
 
    precio = 0
    while precio <= 0:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("Error: El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: El precio debe ser un valor numérico. Inténtelo de nuevo.")
 
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero. Inténtelo de nuevo.")
 
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
 
    costo_total = precio * cantidad
    print(f"\nProducto agregado: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad} | Total existencia: ${costo_total:.2f}")
 
 
def mostrar_inventario(inventario):
    """
    Imprime todos los productos del inventario en formato de tabla.
 
    Muestra columnas de nombre, precio unitario y cantidad. Si el inventario
    está vacío, informa al usuario y retorna sin imprimir la tabla.
 
    Args:
        inventario (list): Lista de diccionarios con los productos registrados.
    """
    if len(inventario) == 0:
        print("\n  El inventario está vacío.")
        return
 
    print("\n" + "*" * 50)
    print(f"{'PRODUCTO':20} {'PRECIO':>10} {'CANTIDAD':>10}")
    print("*" * 50)
 
    for i in inventario:
        print(f"{i['nombre']:<20} ${i['precio']:>9.2f} {i['cantidad']:>9} unidades")
        print("*" * 50)
 
 
def calcular_estadisticas(inventario):
    """
    Calcula y muestra métricas generales del inventario.
 
    Recorre todos los productos y acumula:
    - Total de referencias distintas registradas.
    - Suma de todas las unidades en stock.
    - Producto con el precio unitario más alto.
    - Producto con la mayor cantidad en inventario.
    - Valor total del inventario (suma de precio × cantidad por producto).
 
    Args:
        inventario (list): Lista de diccionarios con los productos registrados.
    """
    if len(inventario) == 0:
        print("\n  No hay productos en el inventario para calcular estadísticas.")
        return
 
    costo_total_inventario = 0
    total_producto = 0
    unidades_totales = 0
    producto_caro = 0
    producto_caro_nombre = ""
    producto_stock = 0
    producto_stock_nombre = ""
 
    for producto in inventario:
        costo_total_inventario += producto["precio"] * producto["cantidad"]
        total_producto += 1
        unidades_totales += producto["cantidad"]
 
        if producto_caro < producto["precio"]:
            producto_caro = producto["precio"]
            producto_caro_nombre = producto["nombre"]
 
        if producto_stock < producto["cantidad"]:
            producto_stock = producto["cantidad"]
            producto_stock_nombre = producto["nombre"]
 
    print("\n" + "*" * 50)
    print("           ESTADÍSTICAS DEL INVENTARIO")
    print("*" * 50)
    print(f"  Cantidad total de productos registrados : {total_producto}")
    print(f"  Unidades totales de productos en inventario : {unidades_totales}")
    print(f"  El producto mas caro de su inventario es: |{producto_caro_nombre} |${producto_caro}")
    print(f"  El producto con mas stock de su inventario es: |{producto_stock_nombre} |${producto_stock}")
    print(f"  Valor total del inventario              : ${costo_total_inventario:.2f}")
    print("*" * 50)
 
 
def buscar_producto(inventario):
    """
    Busca un producto por nombre (sin distinguir mayúsculas/minúsculas).
 
    Recorre el inventario comparando el nombre ingresado contra cada producto.
    Muestra los datos del primero que coincida o informa si no se encontró.
 
    Args:
        inventario (list): Lista de diccionarios con los productos registrados.
    """
    buscar_nombre = input("Escribe el nombre del producto que quieres buscar: ")
    encontrado = False
 
    for producto in inventario:
        if producto["nombre"].lower() == buscar_nombre.lower():
            print("\nProducto encontrado:")
            print(f"|{producto['nombre']:<20} |${producto['precio']:>9.2f} |{producto['cantidad']:>9} unidades")
            encontrado = True
            break
 
    if not encontrado:
        print("Producto no encontrado")
 
 
def actualizar_producto(inventario, nuevo_precio=None, nueva_cantidad=None):
    """
    Localiza un producto por nombre y reemplaza todos sus campos.
 
    Busca el producto ignorando mayúsculas/minúsculas. Si existe, muestra
    los datos actuales y solicita nuevo nombre, precio y cantidad. Los valores
    se sobreescriben directamente en el diccionario.
 
    Args:
        inventario (list): Lista de diccionarios con los productos registrados.
        nuevo_precio (float, optional): Precio de reemplazo (no usado en la versión interactiva).
        nueva_cantidad (int, optional): Cantidad de reemplazo (no usado en la versión interactiva).
    """
 
    try:
        buscar_nombre = input("Escribe el nombre del producto que quieres actualizar: ")
        encontrado = False
    
        for producto in inventario:
            if producto['nombre'].lower() == buscar_nombre.lower():
                print("\nProducto encontrado")
                print(f"|{producto['nombre']:<20} |${producto['precio']:>9.2f} |{producto['cantidad']:>9} unidades")
    
                nuevo_nombre = input("\nIngrese el nuevo nombre: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    
                producto["nombre"] = nuevo_nombre
                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad
    
                print("\nDatos actualizados: ")
                print(f"|{producto['nombre']:<20} |${producto['precio']:>9.2f} |{producto['cantidad']:>9} unidades")
                encontrado = True
                break
    
        if not encontrado:
            print("Producto no encontrado")
    except ValueError:
        print("Error ingrese solo numeros")
        return None
 
 
def eliminar_producto(inventario):
    """
    Elimina un producto del inventario previa confirmación del usuario.
 
    Busca el producto por nombre exacto, muestra sus datos y solicita
    confirmación (S/N) antes de eliminarlo. Si el usuario no confirma
    o el producto no existe, no realiza ningún cambio.
 
    Nota: la comparación de nombre no ignora mayúsculas/minúsculas,
    por lo que el nombre debe ingresarse exactamente como fue registrado.
 
    Args:
        inventario (list): Lista de diccionarios con los productos registrados.
    """
    buscar_nombre = input("Ingrese el nombre del producto a eliminar: ")
    encontrado = False
 
    for producto in inventario:
        if producto["nombre"] == buscar_nombre.lower():  # Bug conocido: no convierte producto["nombre"] a minúsculas
            print("\nProducto encontrado: ")
            print(f"|{producto['nombre']:<20} |${producto['precio']:>9.2f} |{producto['cantidad']:>9} unidades")
            opcion = input("¿Desea eliminarlo? S/N: ").lower()
            if opcion == "s":
                inventario.remove(producto)
                print("\n¡Producto eliminado con exito!")
                encontrado = True
                break
 
    if not encontrado:
        print("\nProducto no encontrado")
