#Importando librerias
import pygame
import time
import random

snake_speed = 10

# Window size
window_x = 720
window_y = 480

# Definiendo colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Inicializando pygame
pygame.init()

# Inicializando el juego en windows
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS Controlador
fps = pygame.time.Clock()

# Definiendo la posicion inicial de la vibora
snake_position = [100, 50]

# Definiendo los primeros 4 bloques del cuerpo
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Posicion de la fruta
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# configuracion por defecto del la direccion de la vibora
# derecha
direction = 'RIGHT'
change_to = direction

# inicializando puntaje
score = 0

# mostrando puntaje
def show_score(choice, color, font, size):
  
    # creando objeto de fuente score_font
    score_font = pygame.font.SysFont(font, size)
    
    # crear el objeto de superficie de visualización 
    # puntuación_superficie
    score_surface = score_font.render('Puntaje : ' + str(score), True, color)
    
    #  crear un objeto rectangular para el texto
    # objeto de superficie
    score_rect = score_surface.get_rect()
    
    # mostrando texto
    game_window.blit(score_surface, score_rect)

# función de fin del juego
def game_over():
  
    # creando el objeto de fuente my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    

    # crear una superficie de texto en la que el texto 
    # será sorteado
    game_over_surface = my_font.render(
        
        'Perdiste perdedor : ' + str(score), True, red)
    
    # crear un objeto rectangular para el texto
    # objeto de superficie
    game_over_rect = game_over_surface.get_rect()
    
    # establecer la posición del texto
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit dibujará el texto en la pantalla
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # después de 2 segundos saldremos del programa
    time.sleep(2)
    
    # desactivando la biblioteca pygame
    pygame.quit()
    
    # salir del programa
    quit()


# Función principal
while True:
    
    # manejo de eventos clave
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'


    # Si se presionan dos teclas simultáneamente
    # no queremos que la serpiente se divida en dos 
    # direcciones simultáneamente

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moviendo la serpiente
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Mecanismo de crecimiento del cuerpo de la serpiente.
    # si las frutas y las serpientes chocan entonces puntúa
    # se incrementará en 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Condiciones de fin del juego
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Tocando el cuerpo de la serpiente
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # mostrando la puntuación continuamente
    show_score(1, white, 'times new roman', 20)

    # Actualizar pantalla de juego
    pygame.display.update()

    # Fotogramas por segundo/frecuencia de actualización
    fps.tick(snake_speed)
