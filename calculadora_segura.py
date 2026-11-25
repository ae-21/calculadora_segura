import math

# Lista global para almacenar el historial de operaciones
historial_operaciones = []


def obtener_numero(mensaje):
    """Solicita un número flotante por consola hasta recibir una entrada válida."""
    while True:
        try:
            entrada = input(mensaje).strip()
            valor = float(entrada)
            if math.isnan(valor) or math.isinf(valor):
                raise ValueError("El valor no puede ser NaN ni infinito.")
            return valor
        except ValueError:
            print("Entrada inválida: debes ingresar un número válido (ejemplo: 10 o 3.5).")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def promedio(numeros):
    if len(numeros) == 0:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)


def calcular(operacion, *args):
    """Ejecuta la operación solicitada usando try/except/else/finally y registra en el historial."""
    operaciones = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir,
        "promedio": promedio,
        "raiz_cuadrada": raiz_cuadrada,
    }

    args_formateados = args[0] if (operacion == "promedio" and len(args) == 1 and isinstance(args[0], list)) else args
    resultado = None
    mensaje_error = None
    estado = "FALLIDA"

    try:
        funcion = operaciones[operacion]
        resultado = funcion(*args)
    except ZeroDivisionError as error:
        mensaje_error = f"Error de división entre cero: {error}"
        print(mensaje_error)
    except ValueError as error:
        mensaje_error = f"Error de valor: {error}"
        print(mensaje_error)
    else:
        estado = "EXITOSA"
        print(f"Resultado de {operacion}: {resultado}")
        historial_operaciones.append({
            "tipo_registro": "ÉXITO",
            "operacion": operacion,
            "argumentos": args_formateados,
            "detalle": f"Resultado: {resultado}",
        })
    finally:
        detalle_final = (
            f"Operación completada con éxito (resultado={resultado})"
            if estado == "EXITOSA"
            else f"Operación fallida ({mensaje_error})"
        )
        historial_operaciones.append({
            "tipo_registro": f"AUDITORÍA [{estado}]",
            "operacion": operacion,
            "argumentos": args_formateados,
            "detalle": detalle_final,
        })

    return resultado


# --- Demostración de propagación de excepciones ---

def _funcion_origen_error():
    """Función profunda que lanza ValueError intencionalmente."""
    print("  [1] _funcion_origen_error(): detectó un dato inválido y lanza ValueError.")
    raise ValueError("Valor negativo detectado dentro de _funcion_origen_error.")


def _funcion_intermedia():
    """Función intermedia que NO captura la excepción; deja que se propague."""
    print("  [2] _funcion_intermedia(): llama a _funcion_origen_error() sin bloque try/except.")
    _funcion_origen_error()
    print("  [2] _funcion_intermedia(): esta línea NO se ejecuta si ocurre una excepción.")


def propagar_error():
    """Función superior que inicia la cadena y captura la excepción propagada."""
    print("\n--- Iniciando demostración de propagación de excepciones ---")
    print("  [3] propagar_error(): abre bloque try y llama a _funcion_intermedia().")
    try:
        _funcion_intermedia()
    except ValueError as error:
        print(f"  [4] propagar_error(): capturó el ValueError propagado -> '{error}'")
        historial_operaciones.append({
            "tipo_registro": "DEMOSTRACIÓN",
            "operacion": "propagacion_excepciones",
            "argumentos": (),
            "detalle": f"Capturado en propagar_error(): {error}",
        })
    finally:
        print("  [5] propagar_error(): bloque finally ejecutado al cerrar la demostración.\n")


def ver_historial():
    """Muestra todas las operaciones registradas en el historial."""
    print("\n================ HISTORIAL DE OPERACIONES ================")
    if not historial_operaciones:
        print("Aún no hay operaciones registradas.")
    else:
        for idx, registro in enumerate(historial_operaciones, start=1):
            print(
                f"{idx}. [{registro['tipo_registro']}] "
                f"Op: {registro['operacion']} | "
                f"Args: {registro['argumentos']} | "
                f"Info: {registro['detalle']}"
            )
    print("==========================================================\n")


def solicitar_lista_numeros():
    """Solicita cuántos números ingresar (o lista vacía para probar ValueError)."""
    while True:
        try:
            cantidad_texto = input("¿Cuántos números deseas promediar? (ingresa 0 para probar lista vacía): ").strip()
            cantidad = int(cantidad_texto)
            if cantidad < 0:
                raise ValueError("La cantidad de elementos no puede ser negativa.")
            break
        except ValueError as error:
            print(f"Entrada inválida: {error} Ingresa un número entero válido.")

    numeros = []
    for i in range(1, cantidad + 1):
        numeros.append(obtener_numero(f"Ingresa el número {i}: "))
    return numeros


def mostrar_menu():
    print("========================================")
    print("  CALCULADORA SEGURA")
    print("========================================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Calcular promedio")
    print("6. Raíz cuadrada")
    print("7. Probar propagación de excepciones")
    print("8. Ver historial")
    print("9. Salir")
    print("========================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            calcular("sumar", a, b)
        elif opcion == "2":
            a = obtener_numero("Ingresa el minuendo: ")
            b = obtener_numero("Ingresa el sustraendo: ")
            calcular("restar", a, b)
        elif opcion == "3":
            a = obtener_numero("Ingresa el primer factor: ")
            b = obtener_numero("Ingresa el segundo factor: ")
            calcular("multiplicar", a, b)
        elif opcion == "4":
            a = obtener_numero("Ingresa el dividendo: ")
            b = obtener_numero("Ingresa el divisor: ")
            calcular("dividir", a, b)
        elif opcion == "5":
            lista = solicitar_lista_numeros()
            calcular("promedio", lista)
        elif opcion == "6":
            num = obtener_numero("Ingresa un número: ")
            calcular("raiz_cuadrada", num)
        elif opcion == "7":
            propagar_error()
        elif opcion == "8":
            ver_historial()
        elif opcion == "9":
            print("Saliendo de la calculadora segura. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción del 1 al 9.")


if __name__ == "__main__":
    main()
