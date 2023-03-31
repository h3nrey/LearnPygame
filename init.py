import pygame
from sys import exit
pygame.init(); # initialize pygame

# Screen setup
width = 450;
height = 450;
screen = pygame.display.set_mode((width, height)) # Create a screen for one frame
pygame.display.set_caption("Super runner cool"); #Defing a title for the game screen

# Tick do Game
clock = pygame.time.CLock();
FPS = 60;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            exit(); # this is just a more acurate way of put a break here
    
    # Draw all elements
    # update everything
    pygame.display.update();
    clock.tick(FPS);