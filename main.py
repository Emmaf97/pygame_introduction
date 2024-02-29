import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))                         # Setting the width and height variables for screen size.
pygame.display.set_caption("Space Game!!")                             # Setting the caption for window to be custom text.

WHITE = (255,255,255)                                                  # Setting the background color as a variable.
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)                     # Creating a border in the center of the screen.

FPS = 60
VEL = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,55
                                                                       # The below handles getting file path without using slashes,
                                                                       # in the event of different operating system
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png")) 
                                                                       # Resizing and rotating the Image to fit the screen.
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):                                          # creating a draw method to draw objects onto the screen.
    WIN.fill((WHITE))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))                    # Drawing the spaceship as a surface onto the screen
    WIN.blit(RED_SPACESHIP, (red.x,red.y)) 
    pygame.display.update()

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
            yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
            yellow.x += VEL                                           # checking that spaceship doesn't go off screen or be drawn over border.
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
            yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:
            yellow.y += VEL

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
            red.x  += VEL
    if keys_pressed[pygame.K_UP]:
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
            red.y += VEL
            
def main():                                                            # setting the main game loop and capping the FPS to 60,
                                                                       # so that it will be stable on all machines.
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)                                                                   
    clock = pygame.time.Clock()
    run = True
    while run:                                                         # Infinite loop to run the game unless quite button is pressed.
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()                       # Storing what keys are currently being pressed down.
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        
        draw_window(red, yellow)                                      # Passing red and yellow to draw method to update positions
        
    pygame.quit()
    
    
if __name__ == "__main__":                                            # This is to prevent the file from running if imported to other files.
    main()