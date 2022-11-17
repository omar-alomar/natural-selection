import pygame
from const import WIDTH, HEIGHT
from dino import Dino

class Base(pygame.sprite.Sprite):
    def __init__(self, type: str, popInit: int):
        super().__init__()
        self.type = type
        self.population = popInit
        self.dinos = []
        self.group = pygame.sprite.Group()

        if self.type != 'doux':
            for i in range(popInit):
                self.spawnDino(9.0, 2.0)
        
        if self.type == 'doux':
            for i in range(popInit):
                self.spawnDino(9.0, 1.0)

        self.setRenderOffset()

        if type == 'doux':
            self.image = pygame.image.load('assets/img/doux_base1.png').convert_alpha() 
            self.image = self.makeTiledImage(WIDTH * self.widthOffset, self.image.get_height(), 5, 0)
            self.rect = self.image.get_rect(topleft=(100, -10))

        if type == 'mort': 
            self.image = pygame.image.load('assets/img/mort_base1.png').convert_alpha()  
            self.image = self.makeTiledImage(WIDTH * self.widthOffset, self.image.get_height(), 5, 0)
            self.rect = self.image.get_rect(topleft=(100, HEIGHT - 80))

        if type == 'tard':
            self.image = pygame.image.load('assets/img/tard_base1.png').convert_alpha()  
            self.image = self.makeTiledImage(self.image.get_width(), HEIGHT * self.heightOffset, 0, 5)
            self.rect = self.image.get_rect(topleft=(WIDTH - 79, 100))

        if type == 'vita': 
            self.image = pygame.image.load('assets/img/vita_base1.png').convert_alpha()  
            self.image = self.makeTiledImage(self.image.get_width(), HEIGHT * self.heightOffset, 0, 5)
            self.rect = self.image.get_rect(topleft=(-15,100))

    # HELPER:
    # Cuts up spritesheet
    # Credit to Kingsley on stackoverflow for this handy tiled image function
    def makeTiledImage( self, width, height, xGap, yGap ):
        self.xCursor = 0
        self.yCursor = 0

        tiled_image = pygame.Surface( ( width, height ) )
        while ( self.yCursor < height ):
            while ( self.xCursor < width ):
                tiled_image.blit( self.image, ( self.xCursor, self.yCursor ) )
                self.xCursor += self.image.get_width() - xGap
            self.yCursor += self.image.get_height() - yGap
            self.xCursor = 0

        tiled_image = pygame.transform.scale2x(tiled_image)
        tiled_image.set_colorkey('Black')
        return tiled_image
    
    # HELPER:
    # Necessary to render bases properly across multiple resolutions
    def setRenderOffset(self):
        if (WIDTH >= 1920):
            self.widthOffset = 0.448
        elif (WIDTH >= 1600):
            self.widthOffset = 0.4385
        elif (WIDTH >= 1280):
            self.widthOffset = 0.421
        elif (WIDTH >= 720):
            self.widthOffset = 0.364
        
        if (HEIGHT >= 1080):
            self.heightOffset = 0.41
        elif (HEIGHT >= 900):
            self.heightOffset = 0.39
        elif (HEIGHT >= 720):
            self.heightOffset = 0.36
        elif (HEIGHT >= 480):
            self.heightOffset = 0.296
    
    def spawnDino(self, speed, size):
        dino = Dino(self.type, speed, size)
        self.group.add(dino)
        self.dinos.append(dino)
        self.population = len(self.dinos)
    
    def killDino(self, id):
        for dino in self.dinos:
            if dino.getId() == id:
                dino.kill()
                self.dinos.remove(dino)
        self.population = len(self.dinos)
    
    def getDinoGroup(self): # returns dino sprite group
        return self.group
    
    def getDinos(self): # returns array of dinos
        return self.dinos
    
    def getPopulation(self):
        return self.population
