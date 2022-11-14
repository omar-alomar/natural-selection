import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.food1 = pygame.image.load('assets/img/shrub1.png').convert_alpha()
        self.food2 = pygame.image.load('assets/img/shrub2.png').convert_alpha()
        self.food3 = pygame.image.load('assets/img/shrub3.png').convert_alpha()
        self.food4 = pygame.image.load('assets/img/shrub1.png').convert_alpha()
        self.foods = [self.food1, self.food2, self.food3, self.food4]
        
