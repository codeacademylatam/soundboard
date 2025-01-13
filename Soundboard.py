import pygame
import sys
import os

# Inicializar Pygame
pygame.init()

# Función para acceder a los recursos dentro del ejecutable o proyecto
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Directorio temporal para PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Configuración de la ventana
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soundboard")

# Colores
WHITE = (255, 255, 255)
GRAY = (245, 245, 245)
BLACK = (0, 0, 0)
RED = (255, 100, 100)

# Tamaño de los botones
BUTTON_WIDTH, BUTTON_HEIGHT = 120, 140
BUTTON_SPACING = 10  # Espacio entre los botones

# Calcular márgenes
MARGIN_X = (WIDTH - (3 * BUTTON_WIDTH + 2 * BUTTON_SPACING)) // 2
MARGIN_Y = 20

# Cargar sonidos y textos
sounds = {
    "Créditos": pygame.mixer.Sound(resource_path("sounds/directed-by.mp3")),
    "Error": pygame.mixer.Sound(resource_path("sounds/error.mp3")),
    "Exclamation": pygame.mixer.Sound(resource_path("sounds/exclamation.mp3")),
    "Wow": pygame.mixer.Sound(resource_path("sounds/long-wow.mp3")),
    "Yay": pygame.mixer.Sound(resource_path("sounds/long-yay.mp3")),
    "Ta-da": pygame.mixer.Sound(resource_path("sounds/ta-da.mp3")),
    "Timer": pygame.mixer.Sound(resource_path("sounds/timer.mp3")),
    "Momento cultural": pygame.mixer.Sound(resource_path("sounds/momento_cultural.mp3")),
    "X-Files": pygame.mixer.Sound(resource_path("sounds/expedientes.mp3")),
}

# Cargar imágenes
images = {
    "Créditos": pygame.image.load(resource_path("images/directed-by.png")),
    "Error": pygame.image.load(resource_path("images/error.png")),
    "Exclamation": pygame.image.load(resource_path("images/exclamation.png")),
    "Wow": pygame.image.load(resource_path("images/wow.png")),
    "Yay": pygame.image.load(resource_path("images/yay.png")),
    "Ta-da": pygame.image.load(resource_path("images/ta-da.png")),
    "Timer": pygame.image.load(resource_path("images/timer.png")),
    "Momento cultural": pygame.image.load(resource_path("images/momento_cultural.png")),
    "X-Files": pygame.image.load(resource_path("images/expedientes.png")),
}

# Ajustar tamaño de las imágenes
for key in images:
    images[key] = pygame.transform.scale(images[key], (80, 80))  # Tamaño más adecuado para centrado

# Crear botones
buttons = []
button_labels = list(sounds.keys())
for i in range(9):
    x = MARGIN_X + (i % 3) * (BUTTON_WIDTH + BUTTON_SPACING)
    y = MARGIN_Y + (i // 3) * (BUTTON_HEIGHT + BUTTON_SPACING)
    buttons.append(pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT))

# Botón detener
stop_button = pygame.Rect((WIDTH - 100) // 2, 500, 100, 50)  # Centrado horizontalmente

# Fuente para texto
font = pygame.font.Font(None, 24)

# Función para dibujar botones
def draw_buttons():
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, GRAY, button)
        pygame.draw.rect(screen, BLACK, button, 2)  # Borde del botón

        # Dibujar imagen (ligeramente más arriba del centro)
        image_rect = images[button_labels[i]].get_rect(center=(button.centerx, button.centery - 20))
        screen.blit(images[button_labels[i]], image_rect)

        # Dibujar texto
        if button_labels[i] == "Momento cultural":
            # Texto dividido en dos líneas
            text1 = font.render("Momento", True, BLACK)
            text2 = font.render("cultural", True, BLACK)
            text1_rect = text1.get_rect(center=(button.centerx, button.centery + 30))
            text2_rect = text2.get_rect(center=(button.centerx, button.centery + 50))
            screen.blit(text1, text1_rect)
            screen.blit(text2, text2_rect)
        else:
            # Texto en una sola línea
            text = font.render(button_labels[i], True, BLACK)
            text_rect = text.get_rect(center=(button.centerx, button.centery + 40))
            screen.blit(text, text_rect)

    # Dibujar botón "Detener"
    pygame.draw.rect(screen, RED, stop_button)
    pygame.draw.rect(screen, BLACK, stop_button, 2)
    stop_text = font.render("Detener", True, BLACK)
    stop_text_rect = stop_text.get_rect(center=stop_button.center)
    screen.blit(stop_text, stop_text_rect)

# Bucle principal
running = True
while running:
    screen.fill(WHITE)
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if stop_button.collidepoint(event.pos):
                # Detener todos los sonidos
                for sound in sounds.values():
                    sound.stop()
            else:
                # Reproducir sonido si se hace clic en un botón
                for i, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        sounds[button_labels[i]].play()

    pygame.display.flip()

# Liberar sonidos
for sound in sounds.values():
    sound.stop()  # Detener cualquier sonido en reproducción
    del sound  # Liberar memoria asignada

# Liberar imágenes
for key in images.keys():
    del images[key]

# Finalizar Pygame
pygame.quit()
