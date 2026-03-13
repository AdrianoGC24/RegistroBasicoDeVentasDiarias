# 📦 Gestión de Inventario / Inventory Management

## Descripción 

Programa de consola desarrollado en Python que permite registrar un producto en el inventario. Solicita al usuario el nombre, precio y cantidad del producto, valida que los datos numéricos sean correctos, calcula el costo total de la existencia y muestra un resumen detallado.

---

## Funcionalidades

- Solicita el nombre del producto al usuario.
- Valida que el precio ingresado sea un número decimal válido (`float`).
- Valida que la cantidad ingresada sea un número entero válido (`int`).
- Muestra un mensaje de error y vuelve a solicitar el dato si el usuario ingresa un valor inválido.
- Calcula el costo total de la existencia (`precio × cantidad`).
- Muestra un resumen con toda la información del producto.

---

## Tecnologías

- **Python 3**
- Terminal / Consola (Linux Ubuntu)

---

## Cómo ejecutar

Asegúrate de tener Python 3 instalado. Luego, en la terminal ejecuta:

```bash
python3 main.py
```

---

## Ejemplo de uso 

```
Ingrese el nombre del producto: Arroz
Ingrese el precio del producto: 3500
Ingrese la cantidad del producto: 12
Producto: Arroz | Precio: 3500.0 | Cantidad: 12 | Total: 42000.0
```

---

## Conceptos aplicados
| Concepto (ES)        |
|----------------------|
| Variables            |
| Entrada del usuario  |
| Manejo de errores    |
| Ciclos `while`       |
| Bloques `try/except` |
| F-strings            |
| Operaciones básicas  |

---

## Autor

Adriano Gonzalez Cera
