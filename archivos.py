def guardar_inventario(inventario):
    """
    Exporta el inventario a un archivo CSV.

    Pide la ruta del archivo al usuario (por defecto 'inventario.csv') y
    valida que la extensión sea .csv. Escribe una fila de encabezado seguida
    de una línea por cada producto con formato 'nombre,precio,cantidad'.

    Si el inventario está vacío lo informa, pero igualmente permite continuar
    para que el usuario pueda elegir la ruta. Maneja errores de permisos y
    del sistema operativo.

    Args:
        inventario (list): Lista de diccionarios con los productos a exportar.
    """
    if len(inventario) == 0:
        print("\nEl inventario esta vacio. No hay datos para guardar.")

    ruta = input("\nIngrese la ruta del archivo (ej: inventario.csv): ").strip()
    if ruta == '':
        ruta = 'inventario.csv'

    # Validar extensión en bucle
    while ruta != '' and not ruta.lower().endswith(".csv"):
        print("\n¡El archivo tiene que ser '.csv'!")
        ruta = input("\nIngrese la ruta del archivo (ej: inventario.csv): ").strip()

    try:
        with open(ruta, "w") as archivo:
            archivo.write("nombre,precio,cantidad\n")
            for producto in inventario:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print(f"Inventario guardado en: {ruta}")
    except PermissionError:
        print(f"Error: no tienes permisos para escribir en {ruta}")
    except OSError as e:
        print(f"Error del sistema: {e}")
    except:
        print("Error")


def cargar_inventario(inventario):
    """
    Importa productos desde un archivo CSV al inventario.

    El proceso tiene tres etapas:

    1. Lectura y validación del archivo:
       - Verifica que el encabezado sea exactamente 'nombre,precio,cantidad'.
       - Procesa cada fila: omite líneas vacías, valida que tenga 3 columnas,
         convierte tipos y rechaza valores negativos o nombre vacío.
       - Acumula el conteo de filas inválidas sin interrumpir la carga.

    2. Si no hay productos válidos, termina con un aviso.

    3. Modo de carga (elegido por el usuario):
       - Sobrescribir (S): reemplaza todo el inventario con los datos del CSV.
       - Fusionar (N): si el producto ya existe suma la cantidad y actualiza
         el precio si cambió; si no existe lo agrega como nuevo.

    Al finalizar muestra un resumen con productos cargados, filas inválidas
    y la acción realizada.

    Args:
        inventario (list): Lista de diccionarios donde se cargarán los productos.
    """
    ruta = input("Ingrese la ruta del archivo CSV a cargar (oprima 'enter' para cargar inventario.csv): ").strip()
    if ruta == '':
        ruta = 'inventario.csv'

    productos_cargados = []
    errores = 0

    # ── Leer y validar el archivo ────────────────────────────
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()

        if len(lineas) == 0:
            print("El archivo CSV esta vacio.")
            return

        # Valida que la primera línea sea el encabezado esperado
        header = lineas[0].strip()
        if header.lower() != "nombre,precio,cantidad":
            print("Error: el encabezado del CSV no es valido. Se esperaba 'nombre,precio,cantidad'.")
            return

        # Procesa cada fila omitiendo las inválidas y acumulando errores
        for numero_fila, linea in enumerate(lineas[1:], start=2):
            linea = linea.strip()
            if linea == '':
                continue

            columnas = linea.split(",")
            if len(columnas) != 3:
                print(f"  Fila {numero_fila} omitida: no tiene exactamente 3 columnas.")
                errores += 1
                continue

            nombre = columnas[0].strip()
            try:
                precio = float(columnas[1].strip())
                cantidad = int(columnas[2].strip())
                if precio < 0 or cantidad < 0:
                    raise ValueError("Valores negativos no permitidos.")
                if nombre == '':
                    raise ValueError("El nombre no puede estar vacio.")
                productos_cargados.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            except ValueError as e:
                print(f"  Fila {numero_fila} omitida: {e}")
                errores += 1

    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{ruta}'.")
        return
    except UnicodeDecodeError:
        print(f"Error: no se pudo leer '{ruta}' por problemas de codificacion.")
        return
    except Exception as e:
        print(f"Error inesperado al cargar el archivo: {e}")
        return

    if len(productos_cargados) == 0:
        print(f"No se encontraron productos validos en el archivo. Filas invalidas: {errores}")
        return

    # ── Sobrescribir o fusionar ──────────────────────────────
    opcion = input("Sobrescribir inventario actual? (S/N): ").strip().upper()
    while opcion not in ('S', 'N'):
        print("Opcion invalida. Ingresa S para sobrescribir o N para fusionar.")
        opcion = input("Sobrescribir inventario actual? (S/N): ").strip().upper()

    if opcion == 'S':
        inventario.clear()
        inventario.extend(productos_cargados)
        accion = "reemplazo"
        print(f"Inventario reemplazado con {len(productos_cargados)} producto(s).")
    else:
        # Fusión: suma cantidad si el producto existe; agrega si no existe
        nuevos = 0
        actualizados = 0
        for prod_nuevo in productos_cargados:
            encontrado = None
            for prod_existente in inventario:
                if prod_existente['nombre'].lower() == prod_nuevo['nombre'].lower():
                    encontrado = prod_existente
                    break
            if encontrado is not None:
                encontrado['cantidad'] += prod_nuevo['cantidad']
                if encontrado['precio'] != prod_nuevo['precio']:
                    print(f"  Precio de '{prod_nuevo['nombre']}' actualizado: ${encontrado['precio']:.0f} -> ${prod_nuevo['precio']:.0f}")
                    encontrado['precio'] = prod_nuevo['precio']
                actualizados += 1
            else:
                inventario.append(prod_nuevo)
                nuevos += 1
        accion = "fusion"
        print(f"Fusion completada: {nuevos} nuevo(s), {actualizados} actualizado(s).")

    if errores > 0:
        print(f"{errores} fila(s) invalida(s) omitida(s) durante la carga.")
    print(f"Resumen -> Productos cargados: {len(productos_cargados)} | Filas invalidas: {errores} | Accion: {accion}")