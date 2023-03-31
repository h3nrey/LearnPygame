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

# Fonts
textFont = pygame.font.Font("font/Pixeltype.ttf", 30);

# Surfaces
skySurface = pygame.image.load("Assets/Graphics/Sky.png");
groundSurface = pygame.image.load("Assets/Graphics/ground.png")
scoreText = textFont.render('Score: 100', False, "red");

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            exit(); # this is just a more acurate way of put a break here
    
    screen.blit(skySurface, (0,0));
    screen.blit(groundSurface, (0,300));
    screen.blit(scoreText, (20, 10));

    # Draw all elements
    # update everything
    pygame.display.update();
    clock.tick(FPS);