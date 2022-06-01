import pygame, sys
from settings import *
from level import Level

# set base pygame parameters
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
level = Level(level_map,screen)

# camera setup
camera_group = pygame.sprite.Group()

# Customize Window Layout
pygame.display.set_caption('Snale\'s Life')
window_icon = pygame.image.load("assets/snale_right.png")
pygame.display.set_icon(window_icon)

# Main Game Loop
while True:
    
    # close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    # Draw Level Layout
    screen.fill((86, 125, 70))
    level.run()

    pygame.display.update()
    clock.tick(60)

