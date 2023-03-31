import pygame
from sys import exit
pygame.init(); # initialize pygame

# Screen setup
width = 800;
height = 400;
screen = pygame.display.set_mode((width, height)) # Create a screen for one frame
pygame.display.set_caption("Super runner cool"); #Defing a title for the game screen

# Tick do Game
clock = pygame.time.Clock();
FPS = 60;

# FONTS
textFont = pygame.font.Font("font/Pixeltype.ttf", 30);


# SURFACES
skySurface = pygame.image.load("Assets/Graphics/Sky.png").convert();
groundSurface = pygame.image.load("Assets/Graphics/ground.png").convert()
scoreText = textFont.render('Score: 100', False, "red");

playerSurf = pygame.image.load("Assets/Graphics/Player/player_walk_1.png").convert_alpha();
playerRect = playerSurf.get_rect(midbottom = (50, 300));
 
snailSurf = pygame.image.load("Assets/Graphics/snail/snail1.png").convert_alpha()
snailRect = snailSurf.get_rect(midbottom = (750, 300))
snailPosX = 700

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            exit(); # this is just a more acurate way of put a break here
    
    screen.blit(skySurface, (0,0));
    screen.blit(groundSurface, (0,300));
    screen.blit(scoreText, (20, 10));
    
    screen.blit(playerSurf, playerRect);

    snailSpeed = 7;
    snailRect.left -= snailSpeed;
    if (snailRect.left <= -100): snailRect.left = 750;
    screen.blit(snailSurf, snailRect);

    # if(playerRect.colliderect(snailRect)):
    #     print("player touched snail")

    mousePos = pygame.mouse.get_pos();
    if(playerRect.collidepoint(mousePos)):
        print("mouse hovering player")

    # Draw all elements
    pygame.display.update();
    # update everything
    clock.tick(FPS);