import pygame
import sys
import os

pygame.init()

size = (400, 300)
position = (0, 0)

width, height = size
x, y = position

# 設置窗口位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_mode(size, pygame.NOFRAME, 0, 0)

# 提取出size和position中的元素

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.display.update()