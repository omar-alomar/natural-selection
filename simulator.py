import pygame
from random import randint
from dino import Dino
from base import Base

# !!NEED TO CHANGE W & H VALUES IN EVERY FILE FOR NOW!!
WIDTH = 900
HEIGHT = 600
FPS_LIMIT = 60

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
dayNo = 0  # day counter
run = True  # game loop bool

# BASES
#   dinos are ONLY spawned & killed through these bases.
#   bases are what track each species population.
bases = pygame.sprite.Group()
douxBase = Base('doux', 100)
mortBase = Base('mort', 100)
tardBase = Base('tard', 100)
vitaBase = Base('vita', 100)
bases.add(douxBase,mortBase,tardBase, vitaBase)

# GAME LOOP
while run:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    buildArena()

    bases.draw(screen)

    douxs = douxBase.getDinos()
    douxBase.getDinoGroup().draw(screen)
    douxBase.getDinoGroup().update()

    morts = mortBase.getDinos()
    mortBase.getDinoGroup().draw(screen)
    mortBase.getDinoGroup().update()

    tards = tardBase.getDinos()
    tardBase.getDinoGroup().draw(screen)
    tardBase.getDinoGroup().update()

    vitas = vitaBase.getDinos()
    vitaBase.getDinoGroup().draw(screen)
    vitaBase.getDinoGroup().update()


    pygame.display.update()
    clock.tick(FPS_LIMIT)
