# This is where tiles are defined such as: rocks, grass, etc.

import pygame

class Fence_Top(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/fence_tile_top.png")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift


class Fence_Side(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/fence_tile_left.png")

        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift


class Fence_Top_Right(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/fence_tile_topright.png")

        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift


class Fence_Top_Left(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/fence_tile_topleft.png")

        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift


class Fence_Bottom_Right(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/fence_tile_bottomright.png")

        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift


class Fence_Bottom_Left(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/fence_tile_bottomleft.png")

        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift


class Grass(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        # obstacles
        self.image = pygame.Surface((size,size))
        self.image = pygame.image.load("assets/grass1.png")

        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift