import pygame
import math

# Definición de la interfaz Dibujable
class Dibujable:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def dibujar(self, superficie):
        pass

# Definición de las clases de figuras
class Circulo(Dibujable):
    def dibujar(self, superficie):
        radio = int(math.hypot(self.fin[0]-self.inicio[0], self.fin[1]-self.inicio[1]))
        pygame.draw.circle(superficie, (255, 0, 0), self.inicio, radio)

class Rectangulo(Dibujable):
    def dibujar(self, superficie):
        x = min(self.inicio[0], self.fin[0])
        y = min(self.inicio[1], self.fin[1])
        ancho = abs(self.fin[0] - self.inicio[0])
        alto = abs(self.fin[1] - self.inicio[1])
        pygame.draw.rect(superficie, (0, 255, 0), pygame.Rect(x, y, ancho, alto))

class Triangulo(Dibujable):
    def dibujar(self, superficie):
        pygame.draw.polygon(superficie, (0, 0, 255), [self.inicio, self.fin, (self.inicio[0], self.fin[1])])
