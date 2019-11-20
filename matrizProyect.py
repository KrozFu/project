import pygame
import json

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO = 20
ALTO = 20

# Establecemos el margen entre las celdas.
MARGEN = 2  # Color negro de las separaciones

# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.

#####
'''Tamano de la matriz (Tamanos de entrada)'''
valx = 25
valy = 25
####

grid = []
for fila in range(valx):
    # Añadimos un array vacío que contendrá cada celda
    # en esta fila
    grid.append([])
    for columna in range(valy):
        grid[fila].append(0)  # Añade una celda

# Establecemos la fila 1, celda 5 a uno. (Recuerda, los números de las filas y
# columnas empiezan en cero.)

lx = []
ly = []


def cargaDatos(lix, liy):
    lx = lix
    ly = liy
    for i in range(len(lx)):
        y = valy - ly[i]
        grid[y-1][lx[i]] = 1

    # Valores calculados para trazar paredes
    # for i in range(valy):
    #    grid[i][lx[0]] = 10


def fuction():
    # INICIALIZA PYGAME
    pygame.init()

    # Establecemos el LARGO y ALTO de la pantalla
    DIMENSION_VENTANA = [800, 700]
    pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

    # Establecemos el título de la pantalla.
    pygame.display.set_caption("Mapeo de Casa")

    # Iteramos hasta que el usuario pulse el botón de salir.
    hecho = False

    # Lo usamos para establecer cuán rápido de refresca la pantalla.
    reloj = pygame.time.Clock()

    # -------- Bucle Principal del Programa-----------
    while not hecho:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True

        # Establecemos el fondo de pantalla.
        pantalla.fill(NEGRO)

        # Dibujamos la retícula
        for fila in range(valx):
            for columna in range(valy):
                color = BLANCO
                if grid[fila][columna] == 1:
                    color = ROJO
                # if grid[fila][columna] == 10:
                #    color = VERDE
                pygame.draw.rect(pantalla, color, [
                                (MARGEN+LARGO) * columna + MARGEN, (MARGEN+ALTO) * fila + MARGEN, LARGO, ALTO])

        # Limitamos a 60 fotogramas por segundo.
        reloj.tick(60)

        # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()

    # Pórtate bien con el IDLE.

    pygame.quit()
