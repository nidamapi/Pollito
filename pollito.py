import pygame
import random
import sys
# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Cuida al pollito')

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
GRIS = (169, 169, 169)
blanco = (255, 255, 255)
negro = (0,0,0)
cielo = (135, 206, 235)
gris = (50, 50, 50)
amarillo = (255,255,0)


# Tamaños de los elementos
CASA_ANCHO = 100
CASA_ALTO = 80
CARRIL_ANCHO = 150
CARRO_TAM = 40
CUADRADO_AMARILLO_TAM = 30

# Posiciones de las casas
casa_izquierda = (100, 500)
casa_central = (350, 500)
casa_derecha = (600, 500)

# Definir el rectángulo de la avenida (carriles)
carril_superior_y = 150
carril_inferior_y = 350

# Carros que se mueven en la avenida
carros_superiores = [
    pygame.Rect(random.randint(0, ANCHO - CARRO_TAM), carril_superior_y, CARRO_TAM, CARRO_TAM)
    for _ in range(5)
]
carros_inferiores = [
    pygame.Rect(random.randint(0, ANCHO - CARRO_TAM), carril_inferior_y, CARRO_TAM, CARRO_TAM)
    for _ in range(5)
]

# Cuadrado amarillo
cuadrado_amarillo = pygame.Rect(ANCHO // 2 - CUADRADO_AMARILLO_TAM // 2, ALTO - CUADRADO_AMARILLO_TAM - 10, CUADRADO_AMARILLO_TAM, CUADRADO_AMARILLO_TAM)

# Velocidades de los carros
velocidad_carros_superiores = 3
velocidad_carros_inferiores = 3
velocidad_cuadrado_amarillo = 5

# Vidas del jugador
vidas = 3
fuente = pygame.font.SysFont('Arial', 30)

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    pantalla.fill(cielo)

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas para mover el cuadrado amarillo
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        cuadrado_amarillo.x -= velocidad_cuadrado_amarillo
    if keys[pygame.K_RIGHT]:
        cuadrado_amarillo.x += velocidad_cuadrado_amarillo
    if keys[pygame.K_UP]:
        cuadrado_amarillo.y -= velocidad_cuadrado_amarillo
    if keys[pygame.K_DOWN]:
        cuadrado_amarillo.y += velocidad_cuadrado_amarillo

    # Limitar el movimiento del cuadrado amarillo dentro de la pantalla
    if cuadrado_amarillo.left < 0:
        cuadrado_amarillo.left = 0
    if cuadrado_amarillo.right > ANCHO:
        cuadrado_amarillo.right = ANCHO
    if cuadrado_amarillo.top < 0:
        cuadrado_amarillo.top = 0
    if cuadrado_amarillo.bottom > ALTO:
        cuadrado_amarillo.bottom = ALTO

    # Dibujar las casas
    pygame.draw.rect(pantalla, blanco, (0,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (100,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (200,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (300,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (400,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (500,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (600,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (700,0,70, 100))
    pygame.draw.rect(pantalla, blanco, (0,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (100,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (200,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (300,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (400,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (500,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (600,500,70, 100))
    pygame.draw.rect(pantalla, blanco, (700,500,70, 100))
    

    # Dibujar la avenida (carriles)
    avenida = pygame.draw.rect(pantalla, negro, (0,150,800, 250))
    # Andèn
    pygame.draw.rect(pantalla, gris, (0,400,800, 40))
    pygame.draw.rect(pantalla, gris, (0,110,800, 40))

    # Lìneas amarillas de la carretera
    pygame.draw.rect(pantalla, amarillo, (0,260,100, 20))
    pygame.draw.rect(pantalla, amarillo, (140,260,100, 20))
    pygame.draw.rect(pantalla, amarillo, (280,260,100, 20))
    pygame.draw.rect(pantalla, amarillo, (420,260,100, 20))
    pygame.draw.rect(pantalla, amarillo, (560,260,100, 20))
    pygame.draw.rect(pantalla, amarillo, (700,260,100, 20))
    for carro in carros_superiores:
        pygame.draw.rect(pantalla, ROJO, carro)
        carro.x -= velocidad_carros_superiores
        if carro.right < 0:
            carro.left = ANCHO
        # Verificar si el carro colisiona con el cuadrado amarillo
        if carro.colliderect(cuadrado_amarillo):
            vidas -= 1
            carro.left = ANCHO  # Reaparece el carro en el lado opuesto

    # Dibujar los carros inferiores
    for carro in carros_inferiores:
        pygame.draw.rect(pantalla, AZUL, carro)
        carro.x += velocidad_carros_inferiores
        if carro.left > ANCHO:
            carro.right = 0
        # Verificar si el carro colisiona con el cuadrado amarillo
        if carro.colliderect(cuadrado_amarillo):
            vidas = 0
            carro.right = 0  # Reaparece el carro en el lado opuesto
            
    # Dibujar el cuadrado amarillo
    pygame.draw.rect(pantalla, AMARILLO, cuadrado_amarillo)

    # Mostrar el contador de vidas
    texto_vidas = fuente.render(f'Vidas: {vidas}', True, negro)
    pantalla.blit(texto_vidas, (10, 10))
    fuente = pygame.font.Font(None, 36)  
    if vidas == 0:
        print("¡Juego terminado! La gallina se quedó sin vidas.")


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la tasa de cuadros por segundo
    clock.tick(60)

# Cerrar Pygame
pygame.quit()