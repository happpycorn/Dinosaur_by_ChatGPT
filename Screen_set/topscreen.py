import pygame
import win32gui
import win32con
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 將 Pygame 窗口設置為最上層
    hwnd = pygame.display.get_wm_info()['window']
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # 繪製遊戲畫面
    screen.fill((255, 255, 255))
    pygame.display.flip()