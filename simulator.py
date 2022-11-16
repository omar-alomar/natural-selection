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
douxBase = Base('doux', 20)
mortBase = Base('mort', 20)
tardBase = Base('tard', 20)
vitaBase = Base('vita', 20)
bases.add(douxBase,mortBase,tardBase, vitaBase)

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

    # COLLISION HANDLING
    for doux in douxs:
        mort = pygame.sprite.spritecollideany(doux, mortGroup) 
        tard = pygame.sprite.spritecollideany(doux, tardGroup) 
        vita = pygame.sprite.spritecollideany(doux, vitaGroup) 

        if mort and doux.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
        elif mort and doux.getSize() < mort.getSize():
            douxBase.killDino(doux.getId())

        elif tard and doux.getSize() > tard.getSize():
            tardBase.killDino(tard.getId())
        elif tard and doux.getSize() < tard.getSize():
            douxBase.killDino(doux.getId())

        elif vita and doux.getSize() < vita.getSize():
            vitaBase.killDino(vita.getId())
        elif vita and doux.getSize() < vita.getSize():
            douxBase.killDino(doux.getId())

    for vita in vitas: 
        mort = pygame.sprite.spritecollideany(vita, mortGroup) 
        tard = pygame.sprite.spritecollideany(vita, tardGroup) 

        if mort and vita.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
        elif mort and vita.getSize() < mort.getSize():
            vitaBase.killDino(vita.getId())

        if mort and vita.getSize() > mort.getSize():
            mortBase.killDino(mort.getId())
        elif mort and vita.getSize() < mort.getSize():
            vitaBase.killDino(vita.getId())
        
    
    for i in range(len(douxs)):
        douxs[i].moveDown()
        tards[i].moveLeft()
        # morts[i].moveUp()


    pygame.display.update()
    clock.tick(FPS_LIMIT)
