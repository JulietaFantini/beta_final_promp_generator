# Project: AI Image Generator

This project is a **Streamlit**-based application that allows users to generate images by describing their ideas, leveraging AI tools for creating visual content.

## Project Structure

### Main Files

1. **`app.py`**

   - The main file that initializes the application and organizes the screen flow.
   - Configures session state and redirects users between defined screens.

2. **`pantalla1.py`**

   - Contains the first screen of the application, where essential parameters for image generation are collected.
   - Enhances the user experience by validating inputs in real time, ensuring that users provide all necessary details before proceeding.
   - Key functions:
     - `generar_dropdown`: Creates dropdown selectors with dynamic options.
     - `filtrar_valores`: Filters parameters with default or invalid values.
     - `parametros_obligatorios`: Collects essential user input.

3. **`pantalla2.py`**

   - Sets up the second screen of the application, where the generated prompt based on user input is displayed and edited.
   - Main functionalities:
     - Display the generated prompt.
     - Allow editing.
     - Copy the prompt to the clipboard and translate it to other languages.

4. **`prompt_generator.py`**

   - Implements the logic for generating detailed and coherent prompts based on user input parameters.
   - Uses structures like `TEMPLATE_BASE`, `TIPOS_MAPPING`, and `PROPOSITOS_MAPPING` to customize prompts.

### Configuration and Style Files

1. **`config.toml`**

   - Contains visual theme configurations, such as primary colors, background, and fonts.
   - Server configuration (port, headless mode, etc.).

2. **`styles.css`**

   - Defines custom styles for the application, including global CSS variables for colors, fonts, and spacing.
   - Applies styles to elements like buttons, text inputs, and headers.

3. **`style_config.py`**

   - Provides utilities or configurations related to visual style.
   - Still requires verification to determine its specific functionality.

### Other Files

1. **`pantalla1.py`** and **`pantalla2.py`**
   - Already validated and functional according to the latest confirmation.

## Requirements

- **Python 3.8 or higher**
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-URL>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Features

- **Spanish-to-English Translation**: The application includes functionality to translate generated prompts from Spanish to English, ensuring flexibility for a broader audience.
- **Real-Time Validations**: Ensures that all required inputs are provided before moving to the next screen, reducing user errors.

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Navigate through the screens to generate and customize prompts.

## Customization

- To modify the visual theme, edit the `config.toml` file.
- Adjust global styles in `styles.css` to customize interface elements.

## Contribution

1. Create a branch for your changes:
   ```bash
   git checkout -b feature/new-functionality
   ```
2. Commit your changes and submit a pull request.

## Credits

This project was developed to explore the integration of AI with interactive interfaces, focusing on personalized image generation through detailed prompts.
