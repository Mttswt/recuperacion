import pygame
from dibujable import *
# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Creación del menú
menu = pygame.Surface((ancho_pantalla, 50))
pygame.draw.rect(menu, (255, 0, 0), pygame.Rect(0, 0, ancho_pantalla / 3, 50)) # Botón del círculo
pygame.draw.rect(menu, (0, 255, 0), pygame.Rect(ancho_pantalla / 3, 0, ancho_pantalla / 3, 50)) # Botón del rectángulo
pygame.draw.rect(menu, (0, 0, 255), pygame.Rect(2 * ancho_pantalla / 3, 0, ancho_pantalla / 3, 50)) # Botón del triángulo

# Variables para el control del programa
corriendo = True
dibujando = False
figuras = []
tipo_figura = Circulo

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: # Botón izquierdo del ratón
                if evento.pos[1] <= 50: # Click en el menú
                    if evento.pos[0] < ancho_pantalla / 3:
                        tipo_figura = Circulo
                    elif evento.pos[0] < 2 * ancho_pantalla / 3:
                        tipo_figura = Rectangulo
                    else:
                        tipo_figura = Triangulo
                else: # Click en el área de dibujo
                    inicio_dibujo = evento.pos
                    dibujando = True
        elif evento.type == pygame.MOUSEBUTTONUP and dibujando:
            figuras.append(tipo_figura(inicio_dibujo, evento.pos))
            dibujando = False

    # Limpia la pantalla y dibuja el menú
    pantalla.fill((255, 255, 255))
    pantalla.blit(menu, (0, 0))

    # Dibuja las figuras
    for figura in figuras:
        figura.dibujar(pantalla)

    # Dibuja la figura actual si se está dibujando una figura
    if dibujando:
        tipo_figura(inicio_dibujo, pygame.mouse.get_pos()).dibujar(pantalla)

    # Actualiza la pantalla
    pygame.display.flip()

pygame.quit()