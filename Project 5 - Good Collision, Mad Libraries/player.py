import pygame


# Snale Class
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super(Player, self).__init__()
        self.image = pygame.Surface((64,64))
        self.image = pygame.image.load("assets/snale_right.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.facing = "right"
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0
        self.speed_y = 0

    # Animate direction of player model
    def change_direction(self):
        if self.facing == "right":
            self.image = pygame.image.load("assets/snale_right.png")
        if self.facing == "left":
            self.image = pygame.image.load("assets/snale_left.png")
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing = "right"
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing = "left"
        else:
            self.direction.x = 0
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def update(self):
        self.get_input()
        self.change_direction()
        

