import pygame
from pygame import *


class Entity(pygame.sprite.Sprite): 
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.brick=image.load('/Users/Zahza/Desktop/Mario Block.png')
        self.brick=transform.scale(self.brick,(32,32))
        self.image = self.brick 
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)   

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        #self.Surface.blit(brick,screen,(x,y))