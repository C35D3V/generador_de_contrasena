# Generador de Contraseñas Seguro

Este proyecto es un **Generador de Contraseñas Seguro** en Python, diseñado para crear contraseñas robustas, evaluar su seguridad y verificar si han sido comprometidas en bases de datos públicas. Este programa es ideal para quienes desean mejorar la seguridad de sus contraseñas personales o profesionales, ofreciendo una solución completa y fácil de usar.

## Características

- **Generación de Contraseñas Aleatorias**: Crea contraseñas de cualquier longitud especificada con una combinación de letras mayúsculas, minúsculas, números y símbolos, asegurando que no haya caracteres repetidos en secuencia.
- **Análisis de Seguridad de Contraseñas**: Calcula la entropía de la contraseña (en bits) y clasifica su seguridad como `Mala`, `Moderada`, `Buena` o `Excelente`.
- **Sugerencias para Mejorar Contraseñas Inseguras**: Proporciona recomendaciones para mejorar las contraseñas calificadas como `Débil`, tales como aumentar la longitud o añadir más tipos de caracteres.
- **Verificación de Contraseñas Comprometidas**: Utiliza la API de [Have I Been Pwned](https://haveibeenpwned.com/) para comprobar si una contraseña ha sido filtrada en bases de datos públicas.

## Requisitos de Instalación

Para utilizar este programa, asegúrate de tener Python 3.x instalado y la biblioteca `requests` disponible. Puedes instalar las dependencias fácilmente con el siguiente comando:

```bash
pip install -r requirements.txt

```

Cómo Usar el Generador de Contraseñas

1. - Clona este repositorio y navega a la carpeta del proyecto:

``` https://github.com/C35D3V/generador_de_contrasena.git 

```

2. - Ejecuta el programa principal:

``` python src/generador_de_contrasena.py

```

3. - Navega por el menú interactivo, donde puedes:

    Generar una o varias contraseñas aleatorias.
    Analizar la seguridad de una contraseña existente.
    Verificar si una contraseña ha sido comprometida en bases de datos públicas.
    
    
- Ejemplo de Uso

Al iniciar el programa, verás un menú como este:

=======================================
=== Menú de Generador de Contraseñas ===
1. Generar una o varias contraseñas
2. Analizar la seguridad y entropía de una contraseña
3. Salir
=======================================


## Generación de Contraseñas Aleatorias

Selecciona la opción 1 para generar contraseñas. Ingresa la longitud y la cantidad deseada, y el programa te proporcionará una lista de contraseñas seguras.

## Análisis de Seguridad

Selecciona la opción 2 para analizar una contraseña. El programa calculará su entropía y te ofrecerá recomendaciones si la contraseña es insegura. Además, verificará si ha sido comprometida usando la API de Have I Been Pwned.

## Consideraciones de Seguridad

Este programa no almacena ninguna contraseña generada ni analizada, y la verificación de contraseñas comprometidas utiliza el método de k-Anonymity para proteger tu privacidad, enviando solo un fragmento encriptado de la contraseña a la API de Have I Been Pwned.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Puedes consultar el archivo LICENSE para más detalles.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, no dudes en hacer un fork y abrir un pull request.
