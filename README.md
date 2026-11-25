# Calculadora Segura en Python

Aplicación interactiva de consola desarrollada en Python para practicar operaciones aritméticas y manejo de excepciones sin que el programa se cierre ante entradas inválidas o errores matemáticos.

## Funcionalidades

- **Operaciones básicas:** suma, resta, multiplicación y división de dos números.
- **Promedio:** cálculo del promedio a partir de una lista de números.
- **Raíz cuadrada:** cálculo de raíz cuadrada con validación para números negativos.
- **Validación de entradas:** reintenta solicitar valores hasta recibir un número válido.
- **Propagación de excepciones:** demostración paso a paso de cómo viaja una excepción entre funciones hasta ser capturada.
- **Historial de operaciones:** registro de operaciones exitosas, fallidas y de auditoría.

## Manejo de errores

- Captura excepciones específicas (`ZeroDivisionError` y `ValueError`) sin utilizar `except Exception` genérico.
- Utiliza bloques `try/except/else/finally` en el procesamiento de operaciones.
- Muestra mensajes claros y mantiene el menú activo hasta elegir la opción de salir.

## Ejecución

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python calculadora_segura.py
