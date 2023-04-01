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

# Game states
gameActive = True;

# FONTS
textFont = pygame.font.Font("font/Pixeltype.ttf", 40);


# SURFACES
skySurface = pygame.image.load("Assets/Graphics/Sky.png").convert();
groundSurface = pygame.image.load("Assets/Graphics/ground.png").convert()
scoreText = textFont.render('Score: 100', False, (80,80,80));
scoreRect = scoreText.get_rect(center = (screen.get_width() / 2, 40))

playerSurf = pygame.image.load("Assets/Graphics/Player/player_walk_1.png").convert_alpha();
playerRect = playerSurf.get_rect(midbottom = (50, 300));
gravity = 0;
jumpForce = -20;
canJump = True;
 
snailSurf = pygame.image.load("Assets/Graphics/snail/snail1.png").convert_alpha()
snailRect = snailSurf.get_rect(midbottom = (750, 300))
snailPosX = 700

line = pygame.Surface((10,10))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            exit(); # this is just a more acurate way of put a break here
        if(gameActive == False):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameActive = True;
                    print(f"gameActive: {gameActive}");
        else:  
            if(canJump): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gravity = jumpForce;
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                        gravity = jumpForce;
            canJump = False;
    
    if(gameActive):
        screen.blit(skySurface, (0,0));
        screen.blit(groundSurface, (0,300));
        pygame.draw.rect(screen, "#aaa1ed", scoreRect)
        pygame.draw.rect(screen, "#aaa1ed", scoreRect, 10)
        screen.blit(scoreText, scoreRect);
        

        snailSpeed = 7;
        snailRect.left -= snailSpeed;
        if (snailRect.left <= -100): snailRect.left = 750;
        screen.blit(snailSurf, snailRect);

        # Player
        gravity += 1;
        playerRect.y += gravity;

        if(playerRect.bottom >= 300): 
            canJump = True;
            playerRect.bottom = 300;
        
        screen.blit(playerSurf, playerRect);

        # Collision
        if(playerRect.colliderect(snailRect)):
            gameActive = False;
            # print("TEste")

    else:
        screen.fill("Black")
        snailRect.left = 750;
        print("Game finished")

    # Draw all elements
    pygame.display.update();
    # update everything
    clock.tick(FPS);

