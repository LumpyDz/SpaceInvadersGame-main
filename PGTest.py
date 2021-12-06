
import sys, pygame
import random as R

class PlayerBase:
    def __init__(self, playerImg = '', HP = 0, X = 0, Y = 0):
        self.playerImg = playerImg
        self.HP = HP
        self.X = X
        self.Y = Y
        self.playerSpeed = 0

    def UpdatePosition(self,X,Y):
        screen.blit(self.playerImg, (X,Y))

class EnemyBase:
    def __init__(self, enemyImg='', HP = 0, score = 0, enemyX=300 ,enemyY=780):
        self.enemyImg = pygame.image.load(enemyImg)
        self.HP = HP
        self.score = score
        self.X = enemyX
        self.Y = enemyY

    #def Move(self,X,Y):
#BLAHB

pygame.init()
#create screen
screen = pygame.display.set_mode((600,800))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('SpaceInvadersLogo.png')
pygame.display.set_icon(icon)

#PlayerStuff
PlayerImg = pygame.image.load('PlayerImg.png')
playerX = 300
playerY = 780
playerSpeed = 0
lKey = False
rKey = False

#Enemy Stuff
enemyCount = 0

def Player(x,y):
    screen.blit(PlayerImg, (x-32,y-32))
def Enemy():
    enemy1 = EnemyBase('ufo.png', 10, 10, R.randint(200,250),R.randint(200,250))
    screen.blit(enemy1.enemyImg,(enemy1.X - 32,enemy1.Y - 32))

player1 = PlayerBase(PlayerImg, 10, 280, 780)
#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Controlling player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerSpeed = -0.1
                lKey = True
                print('Moved left',playerX,lKey)
            if event.key == pygame.K_RIGHT:
                playerSpeed = 0.1
                rKey = True
                print('Moved right',playerX,rKey)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                lKey = False
            if event.key == pygame.K_RIGHT:
                rKey = False
            if lKey == False and rKey == False:
                playerSpeed = 0
    #screen color
    screen.fill((255,200,0))
    #Move Player and screen bounds
    playerX += playerSpeed
    if playerX <= 20:
        playerX = 620
    elif playerX >= 620:
        playerX = 20
    player1.UpdatePosition(playerX,playerY)
    Player(playerX,playerY)
    Enemy()
    pygame.display.update()
