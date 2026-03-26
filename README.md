# Gestor de Inventario

Sistema de gestión de inventario por consola desarrollado en Python. Permite agregar, buscar, actualizar y eliminar productos, calcular estadísticas del inventario, y guardar o cargar datos desde archivos CSV.

---

## Estructura del proyecto

```
gestor-inventario/
├── app.py          # Programa principal y menú de navegación
├── servicios.py    # Lógica de negocio (CRUD y estadísticas)
└── archivos.py     # Persistencia de datos (guardar/cargar CSV)
```

---

## Requisitos

- Python 3.6 o superior
- No requiere librerías externas

---

## Cómo ejecutar

```bash
python app.py
```

---

## Funcionalidades

Al iniciar el programa se muestra el siguiente menú:

```
**************************************************
*              GESTOR DE INVENTARIO              *
**************************************************

ESCOGE UNA OPCIÓN:
    1. Agregar producto
    2. Mostrar inventario
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Calcular estadísticas
    7. Guardar en inventario
    8. Cargar inventario
    9. Salir
```

### 1. Agregar producto

Solicita nombre, precio y cantidad con validación en cada campo:

- El nombre no puede estar vacío.
- El precio debe ser un número decimal mayor a 0.
- La cantidad debe ser un número entero mayor a 0.

Al finalizar muestra un resumen con el costo total de la existencia agregada.

### 2. Mostrar inventario

Imprime todos los productos registrados en formato de tabla con columnas de nombre, precio unitario y cantidad. Si el inventario está vacío, lo informa.

### 3. Buscar producto

Busca un producto por nombre (sin distinguir mayúsculas/minúsculas) y muestra sus datos si existe. Informa si no se encontró.

### 4. Actualizar producto

Localiza un producto por nombre y permite modificar su nombre, precio y cantidad. Los nuevos valores reemplazan completamente a los anteriores.

### 5. Eliminar producto

Busca el producto por nombre, muestra sus datos y pide confirmación (`S/N`) antes de eliminarlo del inventario.

### 6. Calcular estadísticas

Recorre el inventario y calcula:

| Estadística | Descripción |
|---|---|
| Total de productos | Cantidad de referencias distintas registradas |
| Unidades totales | Suma de todas las cantidades |
| Producto más caro | Nombre y precio del producto con mayor precio unitario |
| Mayor stock | Nombre y cantidad del producto con más unidades |
| Valor total del inventario | Suma de (precio × cantidad) de todos los productos |

### 7. Guardar inventario (CSV)

Exporta el inventario a un archivo `.csv`. Pide la ruta del archivo (por defecto `inventario.csv`) y valida que la extensión sea correcta. El archivo generado tiene el siguiente formato:

```
nombre,precio,cantidad
Manzana,1500.0,50
Arroz,3200.0,120
```

Maneja errores de permisos y del sistema operativo.

### 8. Cargar inventario (CSV)

Importa productos desde un archivo `.csv`. El proceso incluye:

1. Validación del encabezado (`nombre,precio,cantidad`).
2. Revisión fila por fila: omite líneas vacías, con columnas incorrectas, valores negativos o nombre vacío, e informa cuántas filas fueron inválidas.
3. Selección del modo de carga:

| Modo | Comportamiento |
|---|---|
| **Sobrescribir (S)** | Reemplaza todo el inventario con los datos del CSV |
| **Fusionar (N)** | Si el producto ya existe, suma la cantidad y actualiza el precio si cambió; si no existe, lo agrega como nuevo |

Al finalizar muestra un resumen con productos cargados, filas inválidas y la acción realizada.

---

## Formato del archivo CSV

El archivo debe seguir esta estructura exacta para ser válido:

```
nombre,precio,cantidad
Producto A,1000.0,10
Producto B,500.5,25
```

- Primera línea: encabezado obligatorio `nombre,precio,cantidad`
- Precio: número decimal (puede usar punto como separador)
- Cantidad: número entero
- No se permiten valores negativos ni nombres vacíos

---

## Descripción de módulos

### `app.py`

Punto de entrada del programa. Inicializa la lista `inventario`, muestra el menú en bucle y delega cada opción a las funciones correspondientes. Valida que la opción ingresada sea un número; si no lo es, muestra un error y repite el menú.

### `servicios.py`

Contiene las funciones de operación sobre el inventario:

| Función | Descripción |
|---|---|
| `agregar_producto(inventario)` | Agrega un nuevo producto con validación de campos |
| `mostrar_inventario(inventario)` | Muestra todos los productos en tabla |
| `buscar_producto(inventario)` | Busca por nombre |
| `actualizar_producto(inventario)` | Modifica un producto existente |
| `eliminar_producto(inventario)` | Elimina un producto con confirmación |
| `calcular_estadisticas(inventario)` | Calcula y muestra métricas del inventario |

### `archivos.py`

Contiene las funciones de persistencia:

| Función | Descripción |
|---|---|
| `guardar_inventario(inventario)` | Exporta el inventario a CSV |
| `cargar_inventario(inventario)` | Importa productos desde un CSV con opción de fusión |

---

## Notas

- El inventario se almacena en memoria durante la sesión. Para conservar los datos entre ejecuciones, usar las opciones 7 (guardar) y 8 (cargar).
- Se recomienda guardar el inventario antes de salir con la opción 9.
- La función `eliminar_producto` tiene un bug conocido: compara el nombre del producto sin convertirlo a minúsculas, por lo que puede no encontrar productos cuyo nombre fue ingresado con mayúsculas. Se recomienda escribir el nombre exactamente como fue registrado.
