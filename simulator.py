import pygame
from random import randint
from dino import Dino

WIDTH = 1200
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
            # if (randint(0, 15) > randint(0, 100)):  # 'randomly' render some shrubs
            #     bgSurf.blit(shrubs[randint(0, 3)], (i, j))

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
        bgSurf.blit(bases[3], (-2, j))
        bgSurf.blit(bases[2], (WIDTH - 92, j))

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
buildArena()

# DINO GROUPS
douxs = pygame.sprite.Group()
doux1 = Dino('doux', 5.0, 1.0, 5.0)
douxs.add(doux1)
morts = pygame.sprite.Group()
mort1 = Dino('mort', 5.0, 1.5, 5.0) 
morts.add(mort1)
tards = pygame.sprite.Group()
tard1 = Dino('tard', 5.0, 2.0, 5.0)
tards.add(tard1)
vitas = pygame.sprite.Group()
vita1 = Dino('vita', 5.0, 3.0, 5.0)
vitas.add(vita1)



# GAME LOOP
while run:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            mort1.moveUp()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            mort1.moveLeft()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            mort1.moveUp()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            mort1.moveRight()


    buildArena()

    douxs.draw(screen)
    douxs.update()
    morts.draw(screen)
    morts.update()
    tards.draw(screen)
    tards.update()
    vitas.draw(screen)
    vitas.update()

    pygame.display.update()
    clock.tick(FPS_LIMIT)
