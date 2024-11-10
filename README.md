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

