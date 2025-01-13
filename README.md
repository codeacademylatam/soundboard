# Soundboard

Este es un proyecto de soundboard creado con Pygame. Permite reproducir sonidos al hacer clic en los botones, con imágenes personalizadas.

## Requisitos
- Python 3.x
- Pygame (se instalará automáticamente con `requirements.txt`)

## Instalación
1. Clona el repositorio o descárgalo como ZIP.
2. Abre la terminal en la carpeta del proyecto.
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el programa:
   ```bash
   python main.py
   ```

## Opcional: Generar ejecutable
Si deseas crear un archivo `.exe` del programa, ejecuta:
   ```bash
pyinstaller --onefile --add-data "images/directed-by.png;images" --add-data "images/error.png;images" --add-data "images/exclamation.png;images" --add-data "images/wow.png;images" --add-data "images/yay.png;images" --add-data "images/ta-da.png;images" --add-data "images/timer.png;images" --add-data "images/momento_cultural.png;images" --add-data "images/expedientes.png;images" --add-data "sounds/directed-by.mp3;sounds" --add-data "sounds/error.mp3;sounds" --add-data "sounds/exclamation.mp3;sounds" --add-data "sounds/long-wow.mp3;sounds" --add-data "sounds/long-yay.mp3;sounds" --add-data "sounds/ta-da.mp3;sounds" --add-data "sounds/timer.mp3;sounds" --add-data "sounds/momento_cultural.mp3;sounds" --add-data "sounds/expedientes.mp3;sounds" Soundboard.py
   ```

Esto generará un ejecutable en la carpeta `dist/`.

---

¡Disfruta usando el soundboard! 🎵
