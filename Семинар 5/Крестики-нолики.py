#3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
import pygame
import sys

pygame.init()
size_block = 1000
margin = 15
width = height = size_block*3 + margin*4

size_window = (width,height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

идфсл = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)