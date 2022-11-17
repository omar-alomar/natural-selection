import pygame
from random import randint
from const import WIDTH, HEIGHT, FPS_LIMIT
from base import Base
from food import Food

def buildArena():
    bgSurf = pygame.Surface((WIDTH, HEIGHT))

    # Grass & shrubs
    grassTile = pygame.image.load('assets/img/grass2.png').convert() # 16x16
    grassTile = pygame.transform.scale(grassTile, (24,24))


    for i in range(0, WIDTH, 24):
        for j in range(0, HEIGHT, 24):
            bgSurf.blit(grassTile, (i, j))  # render grass
            # if (randint(0, 15) > randint(0, 100)):  # 'randomly' render some shrubs
            #     bgSurf.blit(shrubs[randint(0, 3)], (i, j))

    # Corners
    corner = pygame.image.load('assets/img/water.png').convert_alpha()
    corner = pygame.transform.scale(corner, (120, 120))
    bgSurf.blit(corner, (-25, -18))
    bgSurf.blit(corner, (WIDTH - 92, -18))
    bgSurf.blit(corner, (-25, HEIGHT - 100))
    bgSurf.blit(corner, (WIDTH - 92, HEIGHT - 100))

    screen.blit(bgSurf, (0, 0))

# SETUP
pygame.init()
pygame.display.set_caption("Dino Evolution ")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pixelFont = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

# BASES
#   !!! dinos are ONLY spawned & killed through these bases !!!
#   bases are what track each species population.
bases = pygame.sprite.Group()
douxBase = Base('doux', 15)
mortBase = Base('mort', 15)
tardBase = Base('tard', 15)
vitaBase = Base('vita', 15)
bases.add(douxBase, mortBase, tardBase, vitaBase)

# FOOD
foodGroup = pygame.sprite.Group()
for i in range(150, WIDTH - 150, 24):
        for j in range(150, HEIGHT - 150, 24):
            if (randint(0, 2) > randint(0, 100)):  # change these to increase / decrease food count
                food = Food(i, j)
                foodGroup.add(food)


dayNo = 0  # day counter
run = True  # game loop bool
dinosActive = False # true if dinos are running around
douxFlag = False 
mortFlag = False 
tardFlag = False 
vitaFlag = False 
allHome = False

# GAME LOOP
while run:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    buildArena()
    foodGroup.draw(screen)

    # DRAW BASES & DINOS
    bases.draw(screen)

    douxs = douxBase.getDinos()
    douxGroup = douxBase.getDinoGroup()
    douxGroup.draw(screen)
    douxGroup.update()

    morts = mortBase.getDinos()
    mortGroup = mortBase.getDinoGroup()
    mortGroup.draw(screen)
    mortGroup.update()

    tards = tardBase.getDinos()
    tardGroup = tardBase.getDinoGroup()
    tardGroup.draw(screen)
    tardGroup.update() 
    
    vitas = vitaBase.getDinos()
    vitaGroup = vitaBase.getDinoGroup()
    vitaGroup.draw(screen)
    vitaGroup.update()

    groups = [douxGroup, mortGroup, tardGroup, vitaGroup]

    # COLLISIONS: DINO-DINO
    for doux in douxGroup:
        mort = pygame.sprite.spritecollideany(doux, mortGroup) 
        tard = pygame.sprite.spritecollideany(doux, tardGroup) 
        vita = pygame.sprite.spritecollideany(doux, vitaGroup) 

        if mort and doux.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
            doux.setHunger(False)

        elif mort and doux.getSize() < mort.getSize():
            douxBase.killDino(doux.getId())
            mort.setHunger(False)

        elif tard and doux.getSize() > tard.getSize():
            tardBase.killDino(tard.getId())
            doux.setHunger(False)

        elif tard and doux.getSize() < tard.getSize():
            douxBase.killDino(doux.getId())
            tard.setHunger(False)

        elif vita and doux.getSize() > vita.getSize():
            vitaBase.killDino(vita.getId())
            doux.setHunger(False)

        elif vita and doux.getSize() < vita.getSize():
            douxBase.killDino(doux.getId())
            vita.setHunger(False)

    for vita in vitaGroup: 
        mort = pygame.sprite.spritecollideany(vita, mortGroup) 
        tard = pygame.sprite.spritecollideany(vita, tardGroup) 

        if mort and vita.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
            vita.setHunger(False)

        elif mort and vita.getSize() < mort.getSize():
            vitaBase.killDino(vita.getId())
            mort.setHunger(False)

        if mort and vita.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
            vita.setHunger(False)

        elif mort and vita.getSize() < mort.getSize():
            vitaBase.killDino(vita.getId())
            mort.setHunger(False)
    
    # COLLISIONS: ALL DINOS HOME
    douxCollided = pygame.sprite.spritecollide(douxBase, douxGroup, False)
    if sorted(douxCollided, key = lambda doux: doux.getId()) == sorted(douxBase.getDinos(), key = lambda doux: doux.getId()):
        douxFlag = True
                 
    mortCollided = pygame.sprite.spritecollide(mortBase, mortGroup, False)
    if sorted(mortCollided, key = lambda mort: mort.getId()) == sorted(mortBase.getDinos(), key = lambda mort: mort.getId()):
        mortFlag = True
    
    tardCollided = pygame.sprite.spritecollide(tardBase, tardGroup, False)
    if sorted(tardCollided, key = lambda tard: tard.getId()) == sorted(tardBase.getDinos(), key = lambda tard: tard.getId()):
        tardFlag = True

    vitaCollided = pygame.sprite.spritecollide(vitaBase, vitaGroup, False)
    if sorted(vitaCollided, key = lambda vita: vita.getId()) == sorted(vitaBase.getDinos(), key = lambda vita: vita.getId()):
        vitaFlag = True

    if douxFlag and mortFlag and tardFlag and vitaFlag:
        allHome = True

    # COLLISIONS: DINO-FOOD
    for food in foodGroup:
        doux = pygame.sprite.spritecollideany(food, douxGroup) 
        mort = pygame.sprite.spritecollideany(food, mortGroup) 
        tard = pygame.sprite.spritecollideany(food, tardGroup) 
        vita = pygame.sprite.spritecollideany(food, vitaGroup) 

        if doux:
            food.kill()
            doux.setHunger(False)
        elif mort:
            food.kill()
            mort.setHunger(False)
        elif tard:
            food.kill()
            tard.setHunger(False)
        elif vita:
            food.kill()
            vita.setHunger(False)

    # Hunger/movement system
    for group in groups:
        for dino in group:
            if dino.getHunger():
                if dino.getType() == 'doux':
                    dino.moveDown()
                if dino.getType() == 'mort':
                    dino.moveUp()
                if dino.getType() == 'tard':
                    dino.moveLeft()
                if dino.getType() == 'vita':
                    dino.moveRight()
            else:
                dino.runHome()

    pygame.display.update()
    clock.tick(FPS_LIMIT)
