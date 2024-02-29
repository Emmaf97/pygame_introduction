import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))                                          # Setting the width and height variables for screen size.
pygame.display.set_caption("Space Game!!")                                              # Setting the caption for window to be custom text.

WHITE = (255,255,255)                                                                   # Setting the background color as a variable.
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (0,255,255)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)                                      # Creating a border in the center of the screen.

FPS = 60
VEL = 3

BULLET_SPEED = 4
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,55

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
                                                                                        # The below handles getting file path without using slashes,
                                                                                        # in the event of different operating system
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png")) 
                                                                                         # Resizing and rotating the Image to fit the screen.
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow,red_bullets, yellow_bullets):                                                            # creating a draw method to draw objects onto the screen.
    WIN.fill((WHITE))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))                                      # Drawing the spaceship as a surface onto the screen
    WIN.blit(RED_SPACESHIP, (red.x,red.y)) 
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
            yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
            yellow.x += VEL                                                              # checking that spaceship doesn't go off screen or be drawn over border.
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
            yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:
            yellow.y += VEL

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL +  red.width < WIDTH:
            red.x  += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:
            red.y += VEL
            
def handle_bullets(yellow_bullets, red_bullets, yellow, red):                            # handling bullet logic and collision logic
    for bullet in yellow_bullets:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):                                                      # checking if rectangle of spaceship and bullet collide.
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)                                                # if so removing bullet.
    
    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):                                                   # checking if rectangle of spaceship and bullet collide.
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet) 
            
def main():                                                                              # setting the main game loop and capping the FPS to 60,
                                                                                         # so that it will be stable on all machines.
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  
    red_bullets = []   
    yellow_bullets = []                                                              
    clock = pygame.time.Clock()
    run = True
    while run:                                                                          # Infinite loop to run the game unless quite button is pressed.
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:      # Creating and centering the bullet onto the yellow spaceship.
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                yellow_bullets.append(bullet)
                
                
            if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                red_bullets.append(bullet)
                
                
        keys_pressed = pygame.key.get_pressed()                                        # Storing what keys are currently being pressed down.
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        draw_window(red, yellow, red_bullets, yellow_bullets)                                                       # Passing red and yellow to draw method to update positions
        
    pygame.quit()
    
    
if __name__ == "__main__":                                                             # This is to prevent the file from running if imported to other files.
    main()