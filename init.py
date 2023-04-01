import pygame
from sys import exit
from random import randint

def DisplayScore(startTime):
    deltaTime = pygame.time.get_ticks() - startTime;
    displayTime = int(deltaTime / 100);
    font = pygame.font.Font("font/Pixeltype.ttf", 40);
    scoreText = font.render(f"{displayTime}", False, "#ffaaaa");
    scoreRect = scoreText.get_rect(center = (400, 50));
    screen.blit(scoreText, scoreRect);
    return displayTime;

def MoveObstacles(obstacleList):
    if(obstacleList):
        for rect in obstacleList:
            rect.x -= 5;
            surf = snailSurf
            if(rect.y < 250): surf = flySurf;

            screen.blit(surf, rect);
        
        obstacleList = [rect for rect in obstacleList if rect.x > -100]
        return obstacleList
    else: return []

def HandleCollision(player, obstacleList):
    if(obstacleList):
        for rect in obstacleList:
            if player.colliderect(rect):
                return False;
    return True;

def PlayerAnimation():
    global playerSurf, playerIndex

    if(playerRect.bottom < 300):
        playerSurf = jump;
    else:
        playerIndex += 0.1;
        if(playerIndex > len(walk)): playerIndex = 0;
        playerSurf = walk[int(playerIndex)]


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
gameActive = False;
startTime = 0;
score = 0;

# FONTS
textFont = pygame.font.Font("font/Pixeltype.ttf", 40);

# Events 
obstacleTimer = pygame.USEREVENT + 1;
pygame.time.set_timer(obstacleTimer, 1500);

snailTimer = pygame.USEREVENT + 2;
pygame.time.set_timer(snailTimer, 500);

flyTimer = pygame.USEREVENT + 3;
pygame.time.set_timer(flyTimer, 200);


# SURFACES
skySurface = pygame.image.load("Assets/Graphics/Sky.png").convert();
groundSurface = pygame.image.load("Assets/Graphics/ground.png").convert()

walk1 = pygame.image.load("Assets/Graphics/Player/player_walk_1.png").convert_alpha();
walk2 = pygame.image.load("Assets/Graphics/Player/player_walk_2.png").convert_alpha();
walk = [walk1, walk2];
jump = pygame.image.load("Assets/Graphics/Player/jump.png").convert_alpha();
playerIndex = 0;

playerSurf = walk[playerIndex];
playerRect = playerSurf.get_rect(midbottom = (50, 300));
gravity = 0;
jumpForce = -20;
canJump = True;

# Obstacles
snailFrame1 = pygame.image.load("Assets/Graphics/snail/snail1.png").convert_alpha();
snailFrame2 = pygame.image.load("Assets/Graphics/snail/snail2.png").convert_alpha();
snailFrames = [snailFrame1, snailFrame2];
snailFrameIndex = 0;
snailSurf = snailFrames[snailFrameIndex];

flyFrame1 = pygame.image.load("Assets/Graphics/Fly/fly1.png").convert_alpha();
flyFrame2 = pygame.image.load("Assets/Graphics/Fly/fly2.png").convert_alpha();
flyFrames = [flyFrame1, flyFrame2];
flyFrameIndex = 0;
flySurf = flyFrames[flyFrameIndex];

obstaclesRectList = []

# Intro Screen
titleBg = pygame.image.load("Assets/Graphics/TitleBG.png").convert();
titleFont = pygame.font.Font("font/Pixeltype.ttf", 60);
titleText = titleFont.render("Python runner", False, "#dddddd");
titleRect = titleText.get_rect(center = (400, 70))

startFont = pygame.font.Font("font/Pixeltype.ttf", 40);
startText = startFont.render("Press SPACE to start", "False", "#ccccff");
startRect = startText.get_rect(center = (400, 300));
scoreText = startFont.render(f"Score: {score}", False, "#ccccff");

line = pygame.Surface((10,10))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            exit(); # this is just a more acurate way of put a break here
        if(gameActive == False):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
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

            # Timers
            if(event.type == obstacleTimer):
                obstacleType = randint(0,1);
                surf = "";
                yPos = 0;

                if(obstacleType == 0):
                    surf = snailSurf;
                    yPos = 300;
                else:
                    surf = flySurf;
                    yPos = 210;
                obstaclesRectList.append(surf.get_rect(bottomright = (randint(900, 1100), yPos)));

            if(event.type == snailTimer):
                if(snailFrameIndex == 0): snailFrameIndex = 1;
                else: snailFrameIndex = 0;
                snailSurf = snailFrames[snailFrameIndex];
    
            if(event.type == flyTimer):
                if(flyFrameIndex == 0): flyFrameIndex = 1;
                else: flyFrameIndex = 0;
                flySurf = flyFrames[flyFrameIndex];
    
    if(gameActive):
        screen.blit(skySurface, (0,0));
        screen.blit(groundSurface, (0,300));
        score = DisplayScore(startTime);

        # Obstacle
        obstaclesRectList = MoveObstacles(obstaclesRectList)

        # Player
        gravity += 1;
        playerRect.y += gravity;

        if(playerRect.bottom >= 300): 
            canJump = True;
            playerRect.bottom = 300;
        PlayerAnimation();
        screen.blit(playerSurf, playerRect);

        # Collision
        gameActive = HandleCollision(playerRect, obstaclesRectList);
    else:
        screen.blit(titleBg, (0,0));
        screen.blit(titleText, titleRect);
        obstaclesRectList.clear();

        if(score == 0):
            screen.blit(startText, startRect);
        else:
            screen.blit(scoreText, startRect);
        startTime = pygame.time.get_ticks();

    # Draw all elements
    pygame.display.update();
    # update everything
    clock.tick(FPS);

