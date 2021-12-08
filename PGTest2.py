import sys, random
import pygame, pygame_gui

#Constants
SCREENRECT = pygame.Rect(0,0,600,800)
#define our sprite groups and add them into super constructors to initiate
all = pygame.sprite.RenderUpdates()
shots = pygame.sprite.Group()
enemies = pygame.sprite.Group()

pygame.init()
clock = pygame.time.Clock()
SpawnNow = pygame.event.Event(pygame.USEREVENT + 1)
pygame.time.set_timer(SpawnNow,3000,5)

#GUI Manager
manager = pygame_gui.UIManager((600,800))
#GUi elements
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),text='Spawn Enemey',manager=manager)

#Init classes
class Player(pygame.sprite.Sprite):
    #Base player class that handles movement and a method for getting the objects pos(gunpos)
    speed = 5
    images = ''
    health_capacity = 100
    current_health = health_capacity

    def __init__(self):
        super().__init__(all)
        self.image = self.images
        self.rect = self.image.get_rect(midbottom=(300,780))
        self.reloading = 0
        self.current_health = self.health_capacity
        self.HealthBar = pygame_gui.elements.ui_screen_space_health_bar.UIScreenSpaceHealthBar(relative_rect=pygame.Rect((10,780),(100,20)),
                                                                                                    manager=manager,sprite_to_monitor=Player)
    def Move(self, direction):
        self.rect.x += (direction * self.speed)
        if self.rect.left < 0:
            self.rect.right=(600)
        elif self.rect.right > 600:
            self.rect.left=(0)

    def gunpos(self):
        pos = self.rect.midtop
        return pos

class Shot(pygame.sprite.Sprite):

    images = ''

    def __init__(self,pos):
        super().__init__(all,shots)
        self.image = self.images
        self.rect = self.image.get_rect(midbottom = pos)

    def update(self):
        self.rect.move_ip(0,-10)
        if self.rect.y <= 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    images = ''
    startdirection = 1

    def __init__(self):
        super().__init__(all,enemies)
        self.image = self.images
        self.rect = self.image.get_rect()
        self.direction = self.startdirection
        self.HP = 2

    def Spawn(self):
        self.rect.x=random.randint(100,500)
        self.rect.y=100

    def update(self):
        if self.direction > 0:
            self.rect.move_ip(1 * self.direction,0)
            if self.rect.right > 600:
                self.direction = -1
        elif self.direction < 0:
            self.rect.move_ip(1 * self.direction,0)
            if self.rect.left < 0:
                self.direction = 1
        self.rect = self.rect.clamp(SCREENRECT)


def main():
    #setup main screen
    screen = pygame.display.set_mode(SCREENRECT.size)
    #initialize the screen extras
    pygame.display.set_caption('Space Invaders Test 2')
    pygame.display.set_icon(pygame.image.load('SpaceInvadersLogo.png'))

    #setup and display the background
    background = pygame.Surface(screen.get_size())
#    background = background.convert()
    background.fill((0,0,0))
    screen.blit(background,(0,0))
    pygame.display.flip()

    #Load and prepare images
    Player.images = pygame.image.load('PlayerImg.png')
    Shot.images = pygame.image.load('bullet.png')
    Enemy.images = pygame.image.load('ufo.png')

    player = Player()

    #Create starting Sprites
    paused = False
    while player.alive():
        time_delta = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.USEREVENT + 1:
                Enemy.Spawn(Enemy())
                print('Spawned')
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        Enemy.Spawn(Enemy())
            #Pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
        if paused == True:
            continue
        else:


                #process GUI events in event loop
            manager.process_events(event)
            manager.update(time_delta)

            all.clear(screen,background)
            all.update()

            keystate = pygame.key.get_pressed()
            direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
            player.Move(direction)
            fireing = keystate[pygame.K_SPACE]
            if not player.reloading and fireing:
                Shot(player.gunpos())
            player.reloading = fireing

            #Collision detection
            for enemy in pygame.sprite.groupcollide(enemies,shots,1,1).keys():
                enemy.kill()

            #draw elements to screen
            manager.draw_ui(screen)
            dirty = all.draw(screen)
            pygame.display.update(dirty)

            #set framrate and debug and update again just in case
            pygame.display.update()
            #clock.tick(60)

if __name__ == '__main__':
    main()
    pygame.quit()
