import pygame
from sys import exit
pygame.init(); # initialize pygame

# Screen setup
width = 450;
height = 450;
screen = pygame.display.set_mode((width, height)) # Create a screen for one frame
pygame.display.set_caption("Super runner cool"); #Defing a title for the game screen

# Tick do Game
clock = pygame.time.Clock();
FPS = 60;

testSurface = pygame.Surface((200, 100));
testSurface.fill("pink");

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            exit(); # this is just a more acurate way of put a break here
    
    screen.blit(testSurface, (50,50));

    # Draw all elements
    # update everything
    pygame.display.update();
    clock.tick(FPS);