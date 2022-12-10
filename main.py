import pygame,time,math,random,sys,time
from pygame.locals import *
from classes import Car
pygame.init()
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('GAME')
CAR = Car('res/SportsRacingCar_1.png')
road = pygame.image.load("res/road1.png")
roadRect = road.get_rect()
road_height = road.get_height()
scroll = 0
tiles = math.ceil(HEIGHT / road_height) + 1
print(tiles)
CAR.rect.x = 400
CAR.rect.y = 400
run = True
loop = True
rect = pygame.Surface((100,100))
rectRect = rect.get_rect()
rect.fill((255,255,255))
rectW = rect.get_width()
rectH = rect.get_height()
text = pygame.font.Font(None, 32)
dialouge = text.render("Start",True,(0,0,0))
replay = text.render("Replay",True,(0,0,0))
replayW = replay.get_width()
replayH = replay.get_height()
textW = dialouge.get_width()
textH = dialouge.get_height()
rock = pygame.image.load("res/spr_boulder_0.png")
rockRect = rock.get_rect()
rockRect.x = random.randint(250,550)
rockRect.y = random.randint(0,1)
rockcounter = 0
lives = 3
livesfont = pygame.font.Font(None,32)
youLost = False

while loop:
    if lives < 1: 
        while lives < 1:
                pygame.display.flip()
                screen.fill((0,0,0))
                screen.blit(rect,((WIDTH / 2) - (rectW / 2), (HEIGHT / 2) - (rectH / 2)))
                screen.blit(replay,((WIDTH / 2) - (replayW / 2), (HEIGHT / 2) - (replayH / 2)))   
                clock.tick(24)
                for event in pygame.event.get():
                    if event.type==QUIT:                
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            x1,y1 = pygame.mouse.get_pos()
                            if x1 >=(WIDTH / 2) - (rectW / 2) and x1 <= (WIDTH / 2) - (rectW / 2) + 150 and y1 >= (HEIGHT / 2) - (rectH / 2) and y1 <= (HEIGHT / 2) - (rectH / 2) + 150:
                                run = False
                                lives = 3
                                CAR.rect.x = 400
                                CAR.rect.y = 400
    while run == True and lives == 3:
        pygame.display.flip()
        screen.fill((0,0,0))
        screen.blit(rect,((WIDTH / 2) - (rectW / 2), (HEIGHT / 2) - (rectH / 2)))
        screen.blit(dialouge,((WIDTH / 2) - (textW / 2), (HEIGHT / 2) - (textH / 2))) 
        clock.tick(24)
        for event in pygame.event.get():
            if event.type==QUIT:                
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x1,y1 = pygame.mouse.get_pos()
                    if x1 >=(WIDTH / 2) - (rectW / 2) and x1 <= (WIDTH / 2) - (rectW / 2) + 150 and y1 >= (HEIGHT / 2) - (rectH / 2) and y1 <= (HEIGHT / 2) - (rectH / 2) + 150:
                        run = False
                        
        
                            
    
    if rockcounter == 0:
        if rockRect.y > 1000:
            rockcounter +=1
    if rockcounter == 1:
        rockRect.x = random.randrange(250 + 38,550 - 38)
        rockRect.y = random.randrange(0,1)
        rockcounter -=1
    
    screen.blit(rock,rockRect)
    screen.blit(CAR.img,(CAR.rect.x, CAR.rect.y))
    
    for event in pygame.event.get():
        if event.type==QUIT:    
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and CAR.rect.x > 250:
        CAR.rect.x -= 5
    if keys[pygame.K_RIGHT] and CAR.rect.x < 550 - CAR.width:
        CAR.rect.x += 5
    if keys[pygame.K_UP] and CAR.rect.y > 0:
        CAR.rect.y -= 5
    if keys[pygame.K_DOWN] and CAR.rect.y < HEIGHT - CAR.height - 20 :
        CAR.rect.y += 5
    pygame.display.flip()
    screen.fill((49, 23, 163))
    for i in range(0,tiles):
        screen.blit(road,(WIDTH / 2 - 150  ,(road_height   * i) + scroll))
    scroll -= 2
    rockRect.y += 1
    if abs(scroll) > road_height:
        scroll = 0      
    if pygame.Rect.colliderect(rockRect,CAR.rect) == True:
        lives -= 1
        rockcounter +=1
    text1 = livesfont.render(f"Remaining lives: {lives}",True,(0,0,0))
    livestextRect = text1.get_rect()
    screen.blit((livesfont.render(f"Remaining lives: {lives}",True,(0,0,0))),(livestextRect.x,livestextRect.y + 20))
    if lives < 1:
        run = True
        
    clock.tick(60)
pygame.quit()
            