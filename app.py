from servicios import *
from archivos import *

# PROGRAMA PRINCIPAL

print("*" * 50)
print("*" + " " * 14 + "GESTOR DE INVENTARIO" + " " * 14 + "*")
print("*" * 50)

inventario = [] 
opcion = 0       

# Bucle principal: se repite hasta que el usuario elija salir (opción 4) 
while opcion !=9:

    print("""\nESCOGE UNA OPCIÓN:
    1. Agregar producto
    2. Mostrar inventario
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Calcular estadísticas
    7. Guardar en inventario
    8. Cargar inventario
    9. Salir""")

    # Validar que la opción ingresada sea numero
    try:
        opcion = int(input("\nEscoge el número de la opción (1/2/3/4): "))
    except ValueError:
        print("Error: Ingrese un valor numérico.")
        continue  # Volver al inicio del bucle sin procesar nada más



    #Menú principal (Agregar / Mostrar / Buscar / Actualizar / Eliminar / Estadísticas 
    # / Guardar CSV / Cargar CSV / Salir)
    # Procesar la opción con condicionales
    if opcion == 1:
        agregar_producto(inventario)

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        buscar_producto(inventario)
        
    elif opcion == 4:
        actualizar_producto(inventario)
        
    elif opcion ==5:
        eliminar_producto(inventario)
        
    elif opcion ==6:
        calcular_estadisticas(inventario)

    elif opcion ==7:
        guardar_inventario(inventario)
        
    elif opcion ==8:
        cargar_inventario(inventario)
        
    elif opcion == 9:
        print("\n¡Hasta luego! Cerrando el gestor de inventario.")

    else:
        # Manejar opciones fuera del rango válido sin cerrar el programa
        print("Opción inválida. Por favor elige entre 1 y 9.")