import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))                         # Setting the width and height variables for screen size.
pygame.display.set_caption("Space Game!!")                             # Setting the caption for window to be custom text.

WHITE = (255,255,255)                                                  # Setting the background color as a variable.

FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
                                                                       # The below handles getting file path without using slashes,
                                                                       # in the event of different operating system
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png")) 
                                                                       # Resizing the Image to fit the screen.
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))

def draw_window():                                                     # creating a draw method to draw objects onto the screen.
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP, (300,100))                              # Drawing the spaceship as a surface onto the screen
    pygame.display.update()


def main():                                                            # setting the main game loop and capping the FPS to 60,
                                                                       # so that it will be stable on all machines.
    clock = pygame.time.Clock()
    run = True
    while run:                                                         # Infinite loop to run the game unless quite button is pressed.
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
        
    pygame.quit()
    
    
if __name__ == "__main__":                                            # This is to prevent the file from running if imported to other files.
    main()