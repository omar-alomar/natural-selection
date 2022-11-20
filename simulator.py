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

def spawnFood(amount: int):
    for i in range(amount):
        food = Food(randint(120, WIDTH - 120), randint(120, HEIGHT - 120))
        foodGroup.add(food)
    return foodGroup

# SETUP
pygame.init()
pygame.display.set_caption("Dino Evolution ")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pixelFont = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

#   !!! dinos are ONLY spawned & killed through bases !!!
#       bases are what keep track of population.
#   !!!!!! killing a dino directly WILL break everything !!!!!!


# INITIAL SETTINGS:
bases = pygame.sprite.Group()
douxBase = Base('doux', 15, 10, 1.3)
mortBase = Base('mort', 15, 7, 1.7)
tardBase = Base('tard', 20, 8, 1.5)
vitaBase = Base('vita', 20, 8, 1.4)
bases.add(douxBase, mortBase, tardBase, vitaBase)

# FOOD
foodGroup = pygame.sprite.Group()
foodGroup = spawnFood(10)

dayNo = 0  # day counter
run = True  # game loop bool
dinosActive = False # true if dinos are running around
douxFlag = False 
mortFlag = False 
tardFlag = False 
vitaFlag = False 
allHome = False

spawnDinos = pygame.USEREVENT + 0
pygame.time.set_timer(spawnDinos, 2000)

# GAME LOOP
while run:
    buildArena()

    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == spawnDinos:
            if allHome:
                dayNo += 1
                for base in bases:
                    base.reproduce(0.3)
                    base.getDinoGroup().update()
                    foodGroup = spawnFood(10)
                    foodGroup.update()
                    for dino in base.getDinoGroup():
                        dino.setHunger(True)

    # DRAW BASES & DINOS
    bases.draw(screen)
    foodGroup.draw(screen)
    foodGroup.update()

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

        elif tard and vita.getSize() > tard.getSize():
            tardBase.killDino(tard.getId())
            vita.setHunger(False)

        elif tard and vita.getSize() < tard.getSize():
            vitaBase.killDino(vita.getId())
            tard.setHunger(False)
    
    for tard in tardGroup:
        mort = pygame.sprite.spritecollideany(tard, mortGroup) 

        if mort and tard.getSize() < mort.getSize():
            tardBase.killDino(tard.getId())
            tard.setHunger(False)
        elif mort and tard.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
            tard.setHunger(False)
    
    # COLLISIONS: DINO-HOME
    douxCollided = pygame.sprite.spritecollide(douxBase, douxGroup, False)
    if sorted(douxCollided, key = lambda doux: doux.getId()) == sorted(douxBase.getDinos(), key = lambda doux: doux.getId()):
        douxFlag = True
    else:
        douxFlag = False
                 
    mortCollided = pygame.sprite.spritecollide(mortBase, mortGroup, False)
    if sorted(mortCollided, key = lambda mort: mort.getId()) == sorted(mortBase.getDinos(), key = lambda mort: mort.getId()):
        mortFlag = True
    else:
        mortFlag = False
    
    tardCollided = pygame.sprite.spritecollide(tardBase, tardGroup, False)
    if sorted(tardCollided, key = lambda tard: tard.getId()) == sorted(tardBase.getDinos(), key = lambda tard: tard.getId()):
        tardFlag = True
    else:
        tardFlag = False

    vitaCollided = pygame.sprite.spritecollide(vitaBase, vitaGroup, False)
    if sorted(vitaCollided, key = lambda vita: vita.getId()) == sorted(vitaBase.getDinos(), key = lambda vita: vita.getId()):
        vitaFlag = True
    else:
        vitaFlag = False
        
    if douxFlag and mortFlag and tardFlag and vitaFlag:
        allHome = True
    else:
        allHome = False

    # COLLISIONS: DINO-BASE:
    for base in bases:
        for dino in base.getDinoGroup():
            if dino.getType() == 'doux':
                if dino.getPosY() >= HEIGHT - 120:
                    douxBase.killDino(dino.getId())
                if dino.getPosX() <= 120 or dino.getPosX() >= WIDTH - 120:
                    douxBase.killDino(dino.getId())
            if dino.getType() == 'mort':
                if dino.getPosY() <= 120:
                    mortBase.killDino(dino.getId())
                if dino.getPosX() <= 0 or dino.getPosX() >= WIDTH:
                    mortBase.killDino(dino.getId())
            if dino.getType() == 'tard':
                if dino.getPosY() >= HEIGHT or dino.getPosY() <= 0:
                    tardBase.killDino(dino.getId())
                if dino.getPosX() <= 120:
                    tardBase.killDino(dino.getId())
            if dino.getType() == 'vita':
                if dino.getPosY() >= HEIGHT or dino.getPosY() <= 0:
                    vitaBase.killDino(dino.getId())
                if dino.getPosX() >= WIDTH - 120:
                    vitaBase.killDino(dino.getId())


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
    
    # Energy system
    for base in bases:
        dinos = base.getDinos()
        for dino in base.getDinoGroup():
            if dino.getEnergy() <= 0:
                base.killDino(dino.getId())
                

    pygame.display.update()
    clock.tick(FPS_LIMIT)
