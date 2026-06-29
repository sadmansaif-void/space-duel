import pygame
import random
import time
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()
#Define the height and width of window
WIDTH , HEIGHT = 600,600
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50,50
FPS = 60
SPACESHIP_VEL = 6
BULLET_VEL = 9
#Load the background and scale it
BG = pygame.transform.scale(pygame.image.load("bg.jpg"),(WIDTH,HEIGHT))
#Set up the window, sound, font and Caption
pygame.display.set_caption("Space Duel")
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)
BULLET_FIRE = pygame.mixer.Sound(os.path.join('Assets', "Gun+Silencer.mp3"))
BULLET_HIT = pygame.mixer.Sound(os.path.join('Assets', "Grenade+1.mp3"))

#PLAYER 1 ATTRIBUTES
YELLOW_SPACESHIP= pygame.transform.scale(pygame.image.load(os.path.join("Assets","spaceship_yellow.png")),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
YELLOW_SPAWN_X,YELLOW_SPAWN_Y = WIDTH/2 - YELLOW_SPACESHIP.get_width()/2, 0
YELLOW_HIT = pygame.USEREVENT + 2

#PLAYER 2 ATTRIBUTES 
RED_SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets","spaceship_red.png")), (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP_IMAGE, 180)
RED_SPAWN_X,RED_SPAWN_Y = WIDTH/2 - RED_SPACESHIP_IMAGE.get_width()/2 ,HEIGHT - RED_SPACESHIP_IMAGE.get_height()
RED_HIT = pygame.USEREVENT + 1

def main():
    clock = pygame.time.Clock()
    red = pygame.Rect(RED_SPAWN_X, RED_SPAWN_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_bullets = []
    red_health = 5
    yellow = pygame.Rect(YELLOW_SPAWN_X, YELLOW_SPAWN_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_bullets = []
    yellow_health = 5
    run = True
    #Game loop
    while run:
        clock.tick(FPS)
        #Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    yellow_bullet = pygame.Rect(yellow.x + yellow.width/2 - 2, yellow.y + yellow.height, 5,10)
                    yellow_bullets.append(yellow_bullet)
                    BULLET_FIRE.play()
                if event.key == pygame.K_RCTRL:
                    red_bullet = pygame.Rect(red.x + red.width/2 - 2 , red.y , 5,10)
                    red_bullets.append(red_bullet)
                    BULLET_FIRE.play()
            if event.type == RED_HIT:
                BULLET_HIT.play()
                red_health -= 1

            if event.type == YELLOW_HIT:
                BULLET_HIT.play()
                yellow_health -= 1    


        keys = pygame.key.get_pressed()

        red_movement(keys, red)

        yellow_movement(keys, yellow)

        handle_bullet(yellow_bullets,red_bullets,yellow,red)
        win_massege =""

        if red_health == 0:
            win_massege = "Yellow Won!"


        if yellow_health == 0:
            win_massege = "Red Won!"  


        draw(red, yellow, yellow_bullets, red_bullets, yellow_health, red_health)
        if win_massege != "":
            win_text = FONT.render(win_massege, 1, "white")
            WIN.blit(win_text, (WIDTH/2 - win_text.get_width()/2,HEIGHT/2 - win_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break      


    pygame.quit()    



#RED spaceship movement
def red_movement(keys, red): 
    if keys[pygame.K_LEFT] and red.x -SPACESHIP_VEL >=0:
        red.x -=SPACESHIP_VEL
    if keys[pygame.K_RIGHT] and red.x + red.width+ SPACESHIP_VEL <= WIDTH:
        red.x +=SPACESHIP_VEL
    if keys[pygame.K_UP] and red.y - SPACESHIP_VEL >= HEIGHT - HEIGHT/4:
        red.y -=SPACESHIP_VEL
    if keys[pygame.K_DOWN] and red.y + red.height + SPACESHIP_VEL <= HEIGHT:
        red.y +=SPACESHIP_VEL



#YELLOW spaceship movement        
def yellow_movement(keys,yellow):
    if keys[pygame.K_a] and yellow.x -SPACESHIP_VEL >=0:
        yellow.x -=SPACESHIP_VEL
    if keys[pygame.K_d] and yellow.x + yellow.width+ SPACESHIP_VEL <= WIDTH:
        yellow.x +=SPACESHIP_VEL    
    if keys[pygame.K_s] and yellow.y +yellow.height+ SPACESHIP_VEL <= HEIGHT/4:
        yellow.y +=SPACESHIP_VEL
    if keys[pygame.K_w] and yellow.y - SPACESHIP_VEL >= 0:
        yellow.y -=SPACESHIP_VEL



def handle_bullet(yellow_bullets, red_bullets, yellow, red):


    for bullet in yellow_bullets[:]:
        bullet.y += BULLET_VEL
        if red.colliderect(bullet) :
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.y >= HEIGHT:
            yellow_bullets.remove(bullet)     


    for bullet in red_bullets[:]:
        bullet.y -= BULLET_VEL
        if yellow.colliderect(bullet) :
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.y + bullet.height <= 0:
            red_bullets.remove(bullet)         

#Drawing on the window and Update
def draw(red, yellow,yellow_bullets, red_bullets, yellow_health, red_health):
    WIN.blit(BG, (0,0))
    red_text = FONT.render(str(red_health), 1, "red")
    yellow_text = FONT.render(str(yellow_health), 1, "yellow")
    WIN.blit(red_text, (0,HEIGHT/2))
    WIN.blit(yellow_text, (WIDTH- yellow_text.get_width(),HEIGHT/2))
    WIN.blit(RED_SPACESHIP, (red.x,red.y) )
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y) )
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, "yellow", bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, "red", bullet)    
    pygame.display.update()
                


if __name__ == "__main__":
    main()