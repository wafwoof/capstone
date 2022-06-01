import pygame
from tiles import *
from settings import *
from player import *

class Level:
    def __init__(self,level_data, surface):
        # setup
        self.display_surface = surface
        self.setup_level(level_data)
        # scroll rate
        self.world_shift_x = 0
        self.world_shift_y = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # Mapping Algorithm 
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                # F = Top Fence
                if cell == "F":
                    tile = Fence_Top((x,y),tile_size)
                    self.tiles.add(tile)
                # S = Side Fence
                if cell == "S":
                    tile = Fence_Side((x,y),tile_size)
                    self.tiles.add(tile)
                # 1 = Top Left Fence
                if cell == "1":
                    tile = Fence_Top_Left((x,y),tile_size)
                    self.tiles.add(tile)
                # 2 = Top Right Fence
                if cell == "2":
                    tile = Fence_Top_Right((x,y),tile_size)
                    self.tiles.add(tile)
                # 3 = Bottom Left Fence
                if cell == "3":
                    tile = Fence_Bottom_Left((x,y),tile_size)
                    self.tiles.add(tile)
                # 4 = Bottom Right Fence
                if cell == "4":
                    tile = Fence_Bottom_Right((x,y),tile_size)
                    self.tiles.add(tile)
                # G = Grass Blades
                if cell == "G":
                    tile = Grass((x,y),tile_size)
                    self.tiles.add(tile)
                # P = Player
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
        
    def scroll(self):

        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x
        direction_y = player.direction.y

        if player_x < (screen_width / 4) and direction_x < 0:
            self.world_shift_x = 5
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift_x = -5
            player.speed = 0
        else: 
            self.world_shift_x = 0
            player.speed = 5
        if player_y < (screen_height / 4) and direction_y < 0:
            self.world_shift_y = 5
            player.speed_y = 0
        elif player_y > screen_height - (screen_height / 4) and direction_y > 0:
            self.world_shift_y = -5
            player.speed_y = 0
        else: 
            self.world_shift_y = 0
            player.speed_y = 5

    def horizontal_movement_collision(self):
        player = self.player.sprite

        # player coordinate is updated here
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.direction.x = 0

    def vertical_movement_collision(self):
            player = self.player.sprite

            # player coordinate is updated here
            player.rect.y += player.direction.y * player.speed_y

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                    elif player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift_x,self.world_shift_y)
        self.tiles.draw(self.display_surface)   
        self.scroll()

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
            
        #self.scroll_y()
            