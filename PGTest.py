
import sys, pygame
import random as R

#Player
class PlayerBase(pygame.sprite.Sprite):

    def __init__(self, playerImg = '', HP = 0, X = 0, Y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.playerImg = pygame.image.load(playerImg)
        self.rect = self.playerImg.get_rect()
        self.score = 0
        self.HP = HP
        self.X = X
        self.Y = Y
        self.playerSpeed = 0
        self.lKey = False
        self.rKey = False

    def UpdatePosition(self,X,Y):
        #Player movement and quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or (event.key == pygame.K_LEFT and event.key == pygame.K_SPACE):
                        self.playerSpeed = -0.1
                        self.lKey = True
                        print('lkey down')
                    if event.key == pygame.K_RIGHT:
                        self.playerSpeed = 0.1
                        self.rKey = True
                        print('rkey down')
                    if event.key == pygame.K_SPACE:
                        self.Fire()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.lKey = False
                    elif event.key == pygame.K_RIGHT:
                        self.rKey = False
                    if self.lKey == False and self.rKey == False:
                        self.playerSpeed = 0
        #Adjust speed based on above input
        self.X += self.playerSpeed
        #Screen bounds for going off screen
        if self.X <= 20:
            self.X = 620
        elif self.X >= 620:
            self.X = 20
        #Updae Screen
        screen.blit(self.playerImg, (self.X-32,self.Y-32))


    def Fire(self):
            proj = BasePlayerProjectile(self.X-24, self.Y-50)
            proj.updateProj()
            print('fired')



class BasePlayerProjectile(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        self.speed = 1
        self.damage = 10
        self.X = x
        self.Y = y

    def updateProj(self):
        while self.Y > -10:
            screen.blit(self.image,(self.X,self.Y))
            self.Y -= .1


#Enemy
class EnemyBase(pygame.sprite.Sprite):
    def __init__(self, enemyImg='', HP = 0, score = 0, enemyX=300 ,enemyY=780):
        pygame.sprite.Sprite.__init__(self)
        self.enemyImg = pygame.image.load(enemyImg)
        self.rect = self.enemyImg.get_rect()
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
#start point in middle bottom of screen

#Enemy Stuff
enemyCount = 0

def Enemy():
    enemy1 = EnemyBase('ufo.png', 10, 10, 250,250)
    screen.blit(enemy1.enemyImg,(enemy1.X - 32,enemy1.Y - 32))
#defualt spawn location is 300,780
player1 = PlayerBase('PlayerImg.png', 10, 300, 780)
#Game Loop
running = True

while running:
    #screen color controls backgrounnd color and adjusts pixels when other objects move over portions of the screen that we do not want to change
    screen.fill((255,200,0))
    #Move Player and screen bounds
    player1.UpdatePosition(player1.X,player1.Y)
    Enemy()
    pygame.display.update()
