```markdown
# Proyecto: Generador de Imágenes con IA

Este proyecto es una aplicación basada en **Streamlit** que permite a los usuarios generar imágenes describiendo sus ideas, utilizando herramientas de IA para crear contenido visual.

## Estructura del Proyecto

### Archivos Principales

- **`app.py`**: Archivo principal que inicializa la aplicación y organiza el flujo entre pantallas. Configura el estado de sesión y redirige a los usuarios entre las pantallas definidas.

- **`pantalla1.py`**: Contiene la primera pantalla de la aplicación, donde se recopilan los parámetros esenciales para la generación de imágenes. Incluye funciones clave como:
  - `generar_dropdown`: Crea selectores desplegables con opciones dinámicas.
  - `filtrar_valores`: Filtra parámetros con valores predeterminados o inválidos.
  - `parametros_obligatorios`: Recopila entradas esenciales del usuario.

- **`pantalla2.py`**: Configura la segunda pantalla, donde se muestra y edita el prompt generado. Funcionalidades principales:
  - Mostrar el prompt generado.
  - Permitir edición.
  - Copiar el prompt al portapapeles y traducirlo a otros idiomas.

- **`prompt_generator.py`**: Implementa la lógica para generar prompts detallados y coherentes basados en los parámetros proporcionados por el usuario. Utiliza estructuras como `TEMPLATE_BASE`, `TIPOS_MAPPING` y `PROPOSITOS_MAPPING` para personalizar los prompts.

### Archivos de Configuración y Estilo

- **`config.toml`**: Contiene configuraciones visuales del tema (colores, fondo, fuentes) y del servidor (puerto, modo headless, etc.).

- **`style_config.py`**: Define estilos personalizados, como colores y tipografías, mediante CSS. Aborda desafíos relacionados con la personalización del diseño.

## Requisitos

- **Python 3.8 o superior**
- Dependencias listadas en `requirements.txt`:
  ```plaintext
  streamlit==1.41.1
  googletrans==4.0.0-rc1
  pandas==2.2.3
  numpy==2.2.1
  requests==2.32.3
  pillow==11.1.0
  ```

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JulietaFantini/beta_final_promp_generator.git
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Características

- **Traducción de Español a Inglés**: Traduce los prompts generados para garantizar flexibilidad en una audiencia más amplia.
- **Validaciones en Tiempo Real**: Asegura que se proporcionen todas las entradas necesarias antes de avanzar a la siguiente pantalla, reduciendo errores del usuario.

## Uso

1. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```
2. Navega por las pantallas para generar y personalizar prompts.

## Personalización

- Para modificar el tema visual, edita el archivo `config.toml`.
- Ajusta los estilos globales en `style_config.py` para personalizar los elementos de la interfaz.

## Contribución

1. Crea una rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
2. Realiza tus cambios y envía un pull request.

## Créditos

Este proyecto fue desarrollado por **Julieta Fantini** como trabajo final integrador de la certificación en IA generativa de **Mundos E**. Para consultas y feedback, podés contactarme a través de **julietafantini@gmail.com**.

Este proyecto explora la integración de la IA con interfaces interactivas, enfocándose en la generación personalizada de imágenes mediante prompts detallados.
```
