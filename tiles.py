#       ╔════════════════════════╗
#       ║  𝒫říběhy mé malé vydry ║
#       ╚════════════════════════╝


#       tiles


import pygame

BGimage = pygame.image.load("figuring out sprites/0.1level1PNG.png")

class TileSurf(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift

class TileFill1(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift

class TileFill2(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.blit(BGimage, (0,25))
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift

class TileFill3(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift
