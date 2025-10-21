#       ╔════════════════════════╗
#       ║  𝒫říběhy mé malé vydry ║
#       ╚════════════════════════╝


#       spikes


import pygame
from support import import_folder

SpikeIm = pygame.image.load("images/tilesandspikes/SpikeIm.png")

class Spikes(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.blit(SpikeIm, (0,25))
        self.rect = self.image.get_rect(topleft = pos)
    
    #def 

    def update(self,x_shift):
        self.rect.x += x_shift



        