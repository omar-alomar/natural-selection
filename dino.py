import pygame

WIDTH = 1200
HEIGHT = 900

class Dino(pygame.sprite.Sprite):
    def __init__(self, type: str, speed: float, size: float, energy: float):
        super().__init__()
        self.speed = speed
        if type == 'doux': # blue
            self.spriteSheet = pygame.image.load('assets/img/doux.png').convert_alpha()
        if type == 'mort': # red
            self.spriteSheet = pygame.image.load('assets/img/mort.png').convert_alpha()
        if type == 'tard': # yellow
            self.spriteSheet = pygame.image.load('assets/img/tard.png').convert_alpha()
        if type == 'vita': # green
            self.spriteSheet = pygame.image.load('assets/img/vita.png').convert_alpha()
        # else: type = 'doux' # this line breaks drawing dinos to screen. No idea why.

        # WALK ANIMATION
        self.isAnimating = False
        self.currentAnimation = []
        self.walkSprites = [] # array of walking animations
        self.walkSpritesInverted = []
        for i in range(0, 3): # dino spritesheet walk is first 4 frames
            self.walkSprites.append(self.sheetSplicer(self.spriteSheet, i, 24, 24, 2))
            self.walkSpritesInverted.append(
                pygame.transform.flip(
                    self.sheetSplicer(self.spriteSheet, i, 24, 24, 2), True, False))
        self.animationIndex = 0
        self.currentAnimation = self.walkSprites
        self.image = self.currentAnimation[self.animationIndex]

        # DINO SPRITE RECTS
        if type == 'doux':
            self.rect = self.image.get_rect(center=(WIDTH / 2, 50))
        if type == 'mort':
            self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT - 50))
        if type == 'tard':
            self.rect = self.image.get_rect(center=(WIDTH - 50, HEIGHT / 2))
        if type == 'vita':
            self.rect = self.image.get_rect(center=(50, HEIGHT / 2))

    def animate(self):
        self.isAnimating = True

    def update(self):
        # WALKING ANIMATION
        if self.isAnimating:
            self.animationIndex += 0.1
            if self.animationIndex >= len(self.currentAnimation):
                self.animationIndex = 0
                self.isAnimating = False
            self.image = self.currentAnimation[int(self.animationIndex)]

    def moveRight(self):
        self.rect.x += self.speed * self.speed / 10
        self.currentAnimation = self.walkSprites
        self.animate()

    def moveLeft(self):
        self.rect.x -= self.speed * self.speed / 10
        self.currentAnimation = self.walkSpritesInverted
        self.animate()

    def moveUp(self):
        self.rect.y -= self.speed * self.speed / 10
        self.animate()
    
    def moveDown(self):
        self.rect.y += self.speed * self.speed / 10
        self.animate()

    def sheetSplicer(self, sheet, frame, width, height, scale=1):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey('Black')
        return image