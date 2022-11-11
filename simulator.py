import pygame
from random import randint

WIDTH = 900
HEIGHT = 900
FPS_LIMIT = 60


def buildArena():
    bgSurf = pygame.Surface((WIDTH, HEIGHT))

    # Grass & shrubs
    grassTile = pygame.image.load('assets/img/grass2.png').convert() # 16x16
    grassTile = pygame.transform.scale(grassTile, (24,24)) 
    shrub1 = pygame.image.load('assets/img/shrub1.png').convert_alpha()
    shrub2 = pygame.image.load('assets/img/shrub2.png').convert_alpha()
    shrub3 = pygame.image.load('assets/img/shrub3.png').convert_alpha()
    shrub4 = pygame.image.load('assets/img/shrub1.png').convert_alpha()
    shrubs = [shrub1, shrub2, shrub3, shrub4]

    for i in range(0, WIDTH, 24):
        for j in range(0, HEIGHT, 24):
            bgSurf.blit(grassTile, (i, j))  # render grass
            if (randint(0, 15) > randint(0, 100)):  # 'randomly' render some shrubs
                bgSurf.blit(shrubs[randint(0, 3)], (i, j))

    # Bases
    douxBase = pygame.image.load('assets/img/doux_base.png').convert_alpha()  # 44x45 top
    douxBase = pygame.transform.scale2x(douxBase)
    mortBase = pygame.image.load('assets/img/mort_base.png').convert_alpha()  # 44x45 bottom
    mortBase = pygame.transform.scale2x(mortBase)
    tardBase = pygame.image.load('assets/img/tard_base.png').convert_alpha()  # 46x42 right
    tardBase = pygame.transform.scale2x(tardBase)
    vitaBase = pygame.image.load('assets/img/vita_base.png').convert_alpha()  # 46x42 left
    vitaBase = pygame.transform.scale2x(vitaBase)
    bases = [douxBase, mortBase, tardBase, vitaBase]

    for i in range(0, WIDTH, 88):
        bgSurf.blit(bases[0], (i, 0))
        bgSurf.blit(bases[1], (i, HEIGHT - 90))
    for j in range(0, HEIGHT, 84):
        bgSurf.blit(bases[3], (0, j))
        bgSurf.blit(bases[2], (WIDTH - 92, j))

    # Corners
    corner = pygame.image.load('assets/img/water.png').convert_alpha()
    corner = pygame.transform.scale(corner, (90, 92))
    bgSurf.blit(corner, (0, 0))
    bgSurf.blit(corner, (WIDTH - 92, 0))
    bgSurf.blit(corner, (0, HEIGHT - 90))
    bgSurf.blit(corner, (WIDTH - 92, HEIGHT - 90))

    screen.blit(bgSurf, (0, 0))


pygame.init()
pygame.display.set_caption("Dino Evolution ")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pixelFont = pygame.font.Font('assets/font/Pixeltype.ttf', 50)

dayNo = 0  # day counter
day = True  # true if day, false if night
run = True  # game loop bool


buildArena()

# GAME LOOP
while run:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    pygame.display.update()
    clock.tick(FPS_LIMIT)
