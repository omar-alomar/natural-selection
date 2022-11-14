import pygame

WIDTH = 900
HEIGHT = 600

class Base(pygame.sprite.Sprite):
    def __init__(self, type: str):
        super().__init__()
        self.type = type

        if type == 'doux':
            self.image = pygame.image.load('assets/img/doux_base1.png').convert_alpha()  # 44x45 top
            self.image = self.makeTiledImage(349.5, self.image.get_height(), 5, 0)
            self.rect = self.image.get_rect(topleft=(100,-10))
        if type == 'mort': 
            self.image = pygame.image.load('assets/img/mort_base1.png').convert_alpha()  # 44x45 bottom
            self.image = self.makeTiledImage(349.5, self.image.get_height(), 5, 0)
            self.rect = self.image.get_rect(topleft=(100,HEIGHT - 80))
        if type == 'tard':
            self.image = pygame.image.load('assets/img/tard_base1.png').convert_alpha()  # 46x42 right
            self.image = self.makeTiledImage(self.image.get_width(), 200, 0, 5)
            self.rect = self.image.get_rect(topleft=(WIDTH - 79, 100))
        if type == 'vita': 
            self.image = pygame.image.load('assets/img/vita_base1.png').convert_alpha()  # 46x42 left
            self.image = self.makeTiledImage(self.image.get_width(), 200, 0, 5)
            self.rect = self.image.get_rect(topleft=(-15,100))

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
