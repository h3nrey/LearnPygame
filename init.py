import pygame
from sys import exit
from random import randint, choice

def DisplayScore(startTime):
    deltaTime = pygame.time.get_ticks() - startTime;
    displayTime = int(deltaTime / 100);
    font = pygame.font.Font("font/Pixeltype.ttf", 60);
    scoreText = font.render(f"{displayTime}", False, "#6299E0");
    scoreRect = scoreText.get_rect(center = (400, 60));
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
        run1 = pygame.image.load("Assets/Player/Run/Run01.png").convert_alpha();
        run2 = pygame.image.load("Assets/Player/Run/Run02.png").convert_alpha();
        run3 = pygame.image.load("Assets/Player/Run/Run03.png").convert_alpha();
        run4 = pygame.image.load("Assets/Player/Run/Run04.png").convert_alpha();
        run5 = pygame.image.load("Assets/Player/Run/Run05.png").convert_alpha();
        run6 = pygame.image.load("Assets/Player/Run/Run06.png").convert_alpha();
        run7 = pygame.image.load("Assets/Player/Run/Run07.png").convert_alpha();
        run8 = pygame.image.load("Assets/Player/Run/Run08.png").convert_alpha();
        run9 = pygame.image.load("Assets/Player/Run/Run09.png").convert_alpha();
        run10 = pygame.image.load("Assets/Player/Run/Run10.png").convert_alpha();
        run11 = pygame.image.load("Assets/Player/Run/Run11.png").convert_alpha();
        run12 = pygame.image.load("Assets/Player/Run/Run12.png").convert_alpha();
        self.walk = [run1, run2, run4, run5, run6, run7, run8, run9, run10, run11, run12];
        self.playerIndex = 0;
        self.jump = pygame.image.load("Assets/Player/Jump.png").convert_alpha();
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
            self.playerIndex += 0.3
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
            bird1 = pygame.image.load("Assets/Enemies/BlueBird/Bird1.png").convert_alpha();
            bird2 = pygame.image.load("Assets/Enemies/BlueBird/Bird2.png").convert_alpha();
            bird3 = pygame.image.load("Assets/Enemies/BlueBird/Bird3.png").convert_alpha();
            bird4 = pygame.image.load("Assets/Enemies/BlueBird/Bird4.png").convert_alpha();
            bird5 = pygame.image.load("Assets/Enemies/BlueBird/Bird5.png").convert_alpha();
            bird6 = pygame.image.load("Assets/Enemies/BlueBird/Bird6.png").convert_alpha();
            bird7 = pygame.image.load("Assets/Enemies/BlueBird/Bird7.png").convert_alpha();
            bird8 = pygame.image.load("Assets/Enemies/BlueBird/Bird8.png").convert_alpha();
            bird9 = pygame.image.load("Assets/Enemies/BlueBird/Bird9.png").convert_alpha();
            self.frames = [bird1, bird2, bird3, bird4, bird5, bird6, bird7, bird8, bird9];
            yPos = 210;
        elif(type == "snail"):
            chicken1 = pygame.image.load("Assets/Enemies/Chicken/Chicken00.png").convert_alpha();
            chicken2 = pygame.image.load("Assets/Enemies/Chicken/Chicken01.png").convert_alpha();
            chicken3 = pygame.image.load("Assets/Enemies/Chicken/Chicken02.png").convert_alpha();
            chicken4 = pygame.image.load("Assets/Enemies/Chicken/Chicken03.png").convert_alpha();
            chicken5 = pygame.image.load("Assets/Enemies/Chicken/Chicken04.png").convert_alpha();
            chicken6 = pygame.image.load("Assets/Enemies/Chicken/Chicken05.png").convert_alpha();
            chicken7 = pygame.image.load("Assets/Enemies/Chicken/Chicken06.png").convert_alpha();
            chicken8 = pygame.image.load("Assets/Enemies/Chicken/Chicken07.png").convert_alpha();
            chicken9 = pygame.image.load("Assets/Enemies/Chicken/Chicken08.png").convert_alpha();
            chicken10 = pygame.image.load("Assets/Enemies/Chicken/Chicken09.png").convert_alpha();
            chicken11= pygame.image.load("Assets/Enemies/Chicken/Chicken10.png").convert_alpha();
            chicken12 = pygame.image.load("Assets/Enemies/Chicken/Chicken11.png").convert_alpha();
            chicken13 = pygame.image.load("Assets/Enemies/Chicken/Chicken12.png").convert_alpha();
            self.frames = [chicken1,
                           chicken2,
                           chicken3,
                           chicken4,
                           chicken5,
                           chicken6,
                           chicken7,
                           chicken8,
                           chicken9,
                           chicken10,
                           chicken11,
                           chicken12,
                           chicken13,];
            yPos = 300

        self.framesIndex = 0;
        self.image = self.frames[self.framesIndex]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), yPos));
    
    def HandleAnimation(self):
        self.framesIndex += 0.4
        if(self.framesIndex >= len(self.frames)): self.framesIndex = 0;
        self.image = self.frames[int(self.framesIndex)];

    def update(self):
        self.HandleAnimation();
        self.rect.x += -6;
        self.destroy();

    def destroy(self):
        if(self.rect.x <= -300):
            self.kill();
         
class BG(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__();
        if(type == "bg"):
            self.image = pygame.image.load("Assets/bg.png");
            self.rect = self.image.get_rect(topleft = (0,0))
            self.parallaxAmount = 5
        elif(type == "floor"):
            self.image = pygame.image.load("Assets/floor.png");
            self.rect = self.image.get_rect(midtop = (0,300));
            self.parallaxAmount = 10

    def ApplyParalax(self):
        self.rect.x -= self.parallaxAmount;
        if(self.rect.x <= -800):
            self.rect.x = 0;

    def update(self):
        self.ApplyParalax();
pygame.init(); # initialize pygame

# Screen setup
width = 800;
height = 400;
screen = pygame.display.set_mode((width, height)) # Create a screen for one frame
pygame.display.set_caption("Mask Runner"); #Defing a title for the game screen
icon = pygame.image.load("Assets/Player/Run/Run01.png").convert_alpha();
pygame.display.set_icon(icon);

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

# Groups
player = pygame.sprite.GroupSingle();
player.add(Player());

obstacleGroup = pygame.sprite.Group();

sky = pygame.sprite.Group();
sky.add(BG("bg"));
floorGroup = pygame.sprite.Group();
floorGroup.add(BG("floor"));

# Intro Screen
titleBg = pygame.image.load("Assets/Graphics/TitleBG.png").convert();
titleFont = pygame.font.Font("font/Pixeltype.ttf", 100);
titleText = titleFont.render("Mask Runner", False, "#ffffff");
titleRect = titleText.get_rect(center = (400, 90))

startFont = pygame.font.Font("font/Pixeltype.ttf", 40);
startText = startFont.render("Press SPACE to start", "False", "#ffffff");
startRect = startText.get_rect(center = (400, 300));
scoreText = startFont.render(f"Score: {score}", False, "#ffffff");
scoreRect = scoreText.get_rect(center = (400, 300));
scoreSpeed = 1;

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
        # screen.blit(groundSurface, (0,300));
        sky.draw(screen);
        sky.update();
        floorGroup.draw(screen);
        floorGroup.update();
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
            if(startRect.x >= 280):
                scoreSpeed *= -1
            elif(startRect.x <= 220):
                scoreSpeed *= -1
            
            print(startRect.x);
            startRect.x += 1.1 * scoreSpeed;
            screen.blit(startText, startRect);
        else:
            screen.blit(scoreText, scoreRect);
        startTime = pygame.time.get_ticks();

    # Draw all elements
    pygame.display.update();
    # update everything
    clock.tick(FPS);

