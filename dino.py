import pygame
from const import WIDTH, HEIGHT
from random import randint
import uuid

class Dino(pygame.sprite.Sprite):
    def __init__(self, type: str, speed: float, size: float):
        super().__init__()
        self.type = type
        self.speed = speed
        self.size = size
        self.hunger = True
        self.id = uuid.uuid4()
        self.energy = 500

        if self.type == 'doux': # blue
            self.spriteSheet = pygame.image.load('assets/img/doux.png').convert_alpha()
        if self.type == 'mort': # red
            self.spriteSheet = pygame.image.load('assets/img/mort.png').convert_alpha()
        if self.type == 'tard': # yellow
            self.spriteSheet = pygame.image.load('assets/img/tard.png').convert_alpha()
        if self.type == 'vita': # green
            self.spriteSheet = pygame.image.load('assets/img/vita.png').convert_alpha()
        # else: type = 'doux' # this line breaks drawing dinos to screen. No idea why.

        # WALK ANIMATION
        self.isAnimating = False
        self.currentAnimation = []
        self.walkSprites = [] # array of walking animations
        self.walkSpritesInverted = []
        for i in range(0, 3): # dino spritesheet walk is first 4 frames
            self.walkSprites.append(self.sheetSplicer(self.spriteSheet, i, 24, 24, self.size))
            self.walkSpritesInverted.append(
                pygame.transform.flip(
                    self.sheetSplicer(self.spriteSheet, i, 24, 24, self.size), True, False))
        self.animationIndex = 0
        self.currentAnimation = self.walkSprites
        self.image = self.currentAnimation[self.animationIndex]

        # RANDOM DINOS SPAWNS WITHIN BASE             
        xOffsetHorz = randint(100, WIDTH - 100)
        yOffsetHorzTop = randint(0, 75)
        yOffsetHorzBottom = randint(HEIGHT - 75, HEIGHT)
        xOffsetVert = randint(0, 75)
        xOffsetVertRight = randint(WIDTH - 75, WIDTH)
        yOffsetVert = randint(100, HEIGHT - 100)
        
        if type == 'doux':
            self.rect = self.image.get_rect(center=(xOffsetHorz, yOffsetHorzTop))
        if type == 'mort':
            self.rect = self.image.get_rect(center=(xOffsetHorz, yOffsetHorzBottom))
        if type == 'tard':
            self.rect = self.image.get_rect(center=( xOffsetVertRight, yOffsetVert))
        if type == 'vita':
            self.rect = self.image.get_rect(center=(xOffsetVert, yOffsetVert))

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

    def sheetSplicer(self, sheet, frame, width, height, scale=1):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey('Black')
        return image
        
    def moveRight(self):
        if self.energy > 0:
            self.energy -= self.speed / 5
            self.rect.x += self.speed * self.speed / 10
            self.currentAnimation = self.walkSprites
            self.animate()

    def moveLeft(self):
        if self.energy > 0:
            self.energy -= self.speed / 5
            self.rect.x -= self.speed * self.speed / 10
            self.currentAnimation = self.walkSpritesInverted
            self.animate()

    def moveUp(self):
        if self.energy > 0:
            self.energy -= self.speed / 5
            self.rect.y -= self.speed * self.speed / 10
            self.animate()
    
    def moveDown(self):
        if self.energy > 0:
            self.energy -= self.speed / 5
            self.rect.y += self.speed * self.speed / 10
            self.animate()
    
    def runHome(self):
        if self.type == 'doux':
            if (self.getPosY() > randint(0, 120)):
                self.moveUp()

        if self.type == 'mort':
            if (self.getPosY() < HEIGHT - randint(60, 120)):
                self.moveDown()    

        if self.type == 'tard':
            if (self.getPosX() < WIDTH - randint(60, 120)):
                self.moveRight()   

        if self.type == 'vita':
            if (self.getPosX() > randint(0, 120)):
                self.moveLeft()    
    
    # def hunt(self):


    def getPosX(self):
        return self.rect.x
    
    def getPosY(self):
        return self.rect.y
    
    def getSpeed(self):
        return self.speed
    
    def getSize(self):
        return self.size
    
    def getId(self):
        return self.id
    
    def getEnergy(self):
        return self.energy
    
    def getHunger(self):
        return self.hunger
    
    def getType(self):
        return self.type
    
    def setHunger(self, val: bool):
        self.hunger = val

