import pygame, cv2, random, os
from game_model.model import Tile, Game

pygame.init()

FPS = 60
pygame.display.set_caption('XOLO-TILES')

clock = pygame.time.Clock()

game = Game()

running = True
while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

    game.update(event_list)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()