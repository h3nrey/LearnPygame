import pygame
from sys import exit
from random import randint, choice

def DisplayScore(startTime):
    deltaTime = pygame.time.get_ticks() - startTime;
    displayTime = int(deltaTime / 100);
    font = pygame.font.Font("font/Pixeltype.ttf", 40);
    scoreText = font.render(f"{displayTime}", False, "#ffaaaa");
    scoreRect = scoreText.get_rect(center = (400, 50));
    screen.blit(scoreText, scoreRect);
    return displayTime;

def HandleCollision():
    if(pygame.sprite.spritecollide(player.sprite, obstacleGroup, False)):
        obstacleGroup.empty();
        return False;
    return True;

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        walk1 = pygame.image.load("Assets/Graphics/Player/player_walk_1.png").convert_alpha();
        walk2 = pygame.image.load("Assets/Graphics/Player/player_walk_2.png").convert_alpha();
        self.walk = [walk1, walk2];
        self.playerIndex = 0;
        self.jump = pygame.image.load("Assets/Graphics/Player/jump.png").convert_alpha();
        self.jumpSound = pygame.mixer.Sound("Assets/audio/jump.mp3");

        self.image = self.walk[self.playerIndex];
        self.rect = self.image.get_rect(midbottom = (100,300));
        self.gravity = 0;
    
    def playerInput(self):
        keys = pygame.key.get_pressed();
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20;
            self.jumpSound.play();
            self.jumpSound.set_volume(0.5)

    def handleAnimation(self):
        if(self.rect.bottom < 300):
            self.image = self.jump;
        else:
            self.playerIndex += 0.1
            if(self.playerIndex >= len(self.walk)): self.playerIndex = 0
            self.image = self.walk[int(self.playerIndex)]

    def applyGravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if(self.rect.bottom >= 300):
            self.rect.bottom = 300;

    def destroy(self):
        if(self.rect.x <= 50):
            self.kill();

    def update(self):
        self.playerInput();
        self.applyGravity();
        self.handleAnimation();
        self.destroy();

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if(type == "fly"):
            fly1 = pygame.image.load("Assets/Graphics/Fly/fly1.png").convert_alpha();
            fly2 = pygame.image.load("Assets/Graphics/Fly/fly2.png").convert_alpha();
            self.frames = [fly1, fly2];
            yPos = 210;
        elif(type == "snail"):
            snail1 = pygame.image.load("Assets/Graphics/Snail/snail1.png").convert_alpha();
            snail2 = pygame.image.load("Assets/Graphics/Snail/snail2.png").convert_alpha();
            self.frames = [snail1, snail2];
            yPos = 300

        self.framesIndex = 0;
        self.image = self.frames[self.framesIndex]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), yPos));
    
    def HandleAnimation(self):
        self.framesIndex += 0.1
        if(self.framesIndex >= len(self.frames)): self.framesIndex = 0;
        self.image = self.frames[int(self.framesIndex)];

    def update(self):
        self.HandleAnimation();
        self.rect.x += -6;
        self.destroy();

    def destroy(self):
        if(self.rect.x <= -300):
            self.kill();
            

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
bgMusic = pygame.mixer.Sound("Assets/audio/music.wav");
# bgMusic.play(loops=6);


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

# Groups
player = pygame.sprite.GroupSingle();
player.add(Player());

obstacleGroup = pygame.sprite.Group();

# Intro Screen
titleBg = pygame.image.load("Assets/Graphics/TitleBG.png").convert();
titleFont = pygame.font.Font("font/Pixeltype.ttf", 60);
titleText = titleFont.render("Python runner", False, "#dddddd");
titleRect = titleText.get_rect(center = (400, 70))

startFont = pygame.font.Font("font/Pixeltype.ttf", 40);
startText = startFont.render("Press SPACE to start", "False", "#ccccff");
startRect = startText.get_rect(center = (400, 300));
scoreText = startFont.render(f"Score: {score}", False, "#ccccff");

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
        else:  
            # Timers
            if(event.type == obstacleTimer):
                obstacleType = choice(["fly", "snail", "snail", "snail"]);            
                obstacleGroup.add(Obstacle(obstacleType));
    
    if(gameActive):
        screen.blit(skySurface, (0,0));
        screen.blit(groundSurface, (0,300));
        score = DisplayScore(startTime);
        
        player.draw(screen);
        player.update()

        obstacleGroup.draw(screen);
        obstacleGroup.update();

        # Collision
        gameActive = HandleCollision();
    else:
        screen.blit(titleBg, (0,0));
        screen.blit(titleText, titleRect);

        if(score == 0):
            screen.blit(startText, startRect);
        else:
            screen.blit(scoreText, startRect);
        startTime = pygame.time.get_ticks();

    # Draw all elements
    pygame.display.update();
    # update everything
    clock.tick(FPS);

