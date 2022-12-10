import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self,path):
        super().__init__()
        self.img = pygame.image.load(path)
        self.rect = self.img.get_rect()
        self.height = self.img.get_height()
        self.width = self.img.get_width()
        