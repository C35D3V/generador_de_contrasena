import random
import math
import hashlib

# Intentamos importar requests y mostramos un mensaje si no está instalado
try:
    import requests
except ImportError:
    print("La biblioteca 'requests' no está instalada. Ejecuta 'pip install requests' o 'pip install -r requirements.txt' para instalarla.")
    exit(1)  # Finalizamos el script si requests no está disponible

#lista con caracteres a usar (minusculas, mayusculas, digitos, simbolos)
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digitos = '0123456789'
simbolos = '@#$%*'

#todos los caracteres posibles en una lista
todos_los_caracteres = letras_minusculas + letras_mayusculas + digitos + simbolos

#definir una funcion para generar una contraseña


def generar_contrasena(longitud):

    """
    Esta función genera una contraseña aleatoria de la longitud especificada, asegurando
    que no haya caracteres repetidos en secuencia.
    """
    contrasena = []

    primer_caracter = random.choice (todos_los_caracteres)
    contrasena.append(primer_caracter)

    for _ in range(1, longitud):
        while True:
            caracter = random.choice(todos_los_caracteres)

            if caracter != contrasena[-1]:
                contrasena.append(caracter)
                break
    
    return ''.join(contrasena)


def analizar_seguridad(contrasena):
    """
    Calcula la entropía de la contraseña en bits y proporciona una calificación de seguridad.
    Incluye también una calificación general de seguridad en función de la variedad y longitud.
    """
    # Determinamos el espacio de búsqueda según los tipos de caracteres que tiene la contraseña
    espacio_busqueda = 0
    if any(c in letras_minusculas for c in contrasena):
        espacio_busqueda += 26
    if any(c in letras_mayusculas for c in contrasena):
        espacio_busqueda += 26
    if any(c in digitos for c in contrasena):
        espacio_busqueda += 10
    if any(c in simbolos for c in contrasena):
        espacio_busqueda += len(simbolos)

    # Calculamos la entropía
    entropia = len(contrasena) * math.log2(espacio_busqueda)

    # Calificación de entropía basada en bits
    if entropia < 40:
        calificacion_entropia = "Mala"
    elif 40 <= entropia < 60:
        calificacion_entropia = "Moderada"
    elif 60 <= entropia < 80:
        calificacion_entropia = "Buena"
    else:
        calificacion_entropia = "Excelente"
    
    # Calificación general de seguridad basada en longitud y variedad de caracteres
    tiene_minuscula = any(c in letras_minusculas for c in contrasena)
    tiene_mayuscula = any(c in letras_mayusculas for c in contrasena)
    tiene_digito = any(c in digitos for c in contrasena)
    tiene_simbolo = any(c in simbolos for c in contrasena)
    tipos_presentes = sum([tiene_minuscula, tiene_mayuscula, tiene_digito, tiene_simbolo])
    
    if len(contrasena) > 14 and tipos_presentes == 4:
        calificacion_general = "Fuerte"
    elif len(contrasena) >= 11 and tipos_presentes >= 3:
        calificacion_general = "Moderada"
    else:
        calificacion_general = "Débil"
    
    # Generar recomendaciones si la contraseña es débil
    sugerencias = []
    if calificacion_general == "Débil":

        if len(contrasena) < 11:
            sugerencias.append("Considera usar una contraseña de al menos 11 caracteres.")
        if tipos_presentes < 3:
            sugerencias.append("Incorpora letras mayúsculas, minúsculas, números y símbolos.")
        if any(contrasena[i] == contrasena[i+1] for i in range(len(contrasena) - 1)):
            sugerencias.append("Evita caracteres consecutivos idénticos.")
    
    return entropia, calificacion_entropia, calificacion_general, sugerencias


def verificar_contrasena_comprometida(contrasena):
    """
    Verifica si una contraseña ha sido filtrada usando la API de Have I Been Pwned.
    """
    # Calculamos el hash SHA-1 de la contraseña
    sha1_hash = hashlib.sha1(contrasena.encode('utf-8')).hexdigest().upper()
    prefijo, sufijo = sha1_hash[:5], sha1_hash[5:]

    # Enviamos los primeros cinco caracteres del hash a la API
    url = f"https://api.pwnedpasswords.com/range/{prefijo}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta es incorrecta
    except requests.RequestException as e:
        print("Error al conectarse a la API de Have I Been Pwned:", e)
        return None

    # Comprobamos si la respuesta fue exitosa
    if response.status_code != 200:
        print("Error al conectarse a la API de Have I Been Pwned.")
        return None
    
    # Buscamos el sufijo en la respuesta
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == sufijo:
            return int(count)  # Devolvemos la cantidad de veces que la contraseña fue comprometida
    
    return 0  # La contraseña no fue comprometida


def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("=========================================")
    print("\n=== Menú de Generador de Contraseñas ===")
    print("1. Generar una o varias contraseñas")
    print("2. Analizar la seguridad y entropia de una contraseña")
    print("3. Salir")
    print("=========================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        # Opción 1: Generar una o varias contraseñas
        if opcion == "1":
            while True:
                longitud = input("Ingrese la longitud de la contraseña (mínimo 8 caracteres) o escriba 'volver' para regresar al menú: ")
                if longitud.lower() == "volver":
                    break  # Regresamos al menú principal
                try:
                    longitud = int(longitud)
                    if longitud >= 8:
                        break
                    else:
                        print("Error: La longitud mínima es de 8 caracteres. Inténtelo de nuevo.")
                except ValueError:
                    print("Error: Ingrese un número válido o 'volver' para regresar al menú.")

            # Si el usuario eligió volver, salimos antes de continuar
            if isinstance(longitud, str) and longitud.lower() == "volver":
                continue

            while True:
                cantidad = input("¿Cuántas contraseñas deseas generar? Escribe 'volver' para regresar al menú: ")
                if cantidad.lower() == "volver":
                    break  # Regresamos al menú principal
                try:
                    cantidad = int(cantidad)
                    if cantidad > 0:
                        break
                    else:
                        print("Error: La cantidad debe ser un número positivo. Inténtelo de nuevo.")
                except ValueError:
                    print("Error: Ingrese un número válido o 'volver' para regresar al menú.")

            # Si el usuario eligió volver, salimos antes de mostrar las contraseñas generadas
            if isinstance(cantidad, str) and cantidad.lower() == "volver":
                continue

            # Generamos la cantidad solicitada de contraseñas y las guardamos en una lista
            contrasenas_generadas = [generar_contrasena(longitud) for _ in range(cantidad)]

            # Mostramos las contraseñas generadas
            print("\nContraseñas generadas:")
            for i, contrasena in enumerate(contrasenas_generadas, 1):
                print(f"{i}. {contrasena}")

        # Opción 2: Calificar la seguridad y entropía de una contraseña existente
        elif opcion == "2":
            contrasena_a_analizar = input("Ingrese la contraseña a analizar o escriba 'volver' para regresar al menú: ")
            if contrasena_a_analizar.lower() == "volver":
                continue  # Regresamos al menú principal

            entropia, calificacion_entropia, calificacion_general, sugerencias = analizar_seguridad(contrasena_a_analizar)
            print(f"\nResultado del análisis de seguridad:")
            print(f"Entropía: {entropia:.2f} bits - {calificacion_entropia}")
            print(f"Calificación general de seguridad: {calificacion_general}")

            if calificacion_general == "Débil":
                print("Sugerencias para mejorar la contraseña:")
                for sugerencia in sugerencias:
                    print("- " + sugerencia)

            # Verificamos si la contraseña ha sido comprometida
            compromisos = verificar_contrasena_comprometida(contrasena_a_analizar)
            if compromisos is None:
                print("No se pudo verificar si la contraseña ha sido comprometida.")
            elif compromisos > 0:
                print(f"¡Advertencia! Esta contraseña ha sido comprometida {compromisos} veces.")
            else:
                print("La contraseña no aparece en bases de datos de contraseñas comprometidas.")

        # Opción 3: Salir del programa
        elif opcion == "3":
            print("Gracias por usar el generador de contraseñas. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

# Ejecutamos el programa
main()
