import pygame
import win32gui
import win32con
import os
from random import randrange

pygame.init()

#設定視窗位置
display_info = pygame.display.Info()
width = display_info.current_w
x,y = width-600,0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

#設定視窗
screen_width, screen_height = 600, 150
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.NOFRAME)

# 設定顏色
white = (255, 255, 255)
black = (0, 0, 0)

# 設定字體
font = pygame.font.Font(None, 36)

# 載入圖片
dinosaur_img = pygame.image.load("C:\Python\ChatGPTdinosaur\dinosaur.png")
cactus_img = pygame.image.load("C:\Python\ChatGPTdinosaur\cactus.png")

# 設定物體位置
dinosaur_x = 50
dinosaur_y = 100
cactus_x = screen_width
cactus_y = 100
jump = False

# 設定物體速度
cactus_speed = 5

# 設定分數
score = 0
ts = 0

# 遊戲迴圈
game_over = False
clock = pygame.time.Clock()



while not game_over:
    # 監聽事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True if dinosaur_y == 100 else jump

    # 更新物體位置(向前跑)
    cactus_x -= cactus_speed
    if cactus_x < -50:
        cactus_x = screen_width
        score += 1
        cactus_speed = randrange(3,10)

    #跳躍動畫
    if jump:
        if dinosaur_y <= 30:
            jump = False
        else:
            dinosaur_y -= dinosaur_y/20
    else:
        if dinosaur_y < 100:
            dinosaur_y += dinosaur_y/20
        else:
            dinosaur_y = 100

    # 繪製物體
    screen.fill(white)
    screen.blit(dinosaur_img, (dinosaur_x, dinosaur_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))

    # 繪製分數
    ts = score if score>ts else ts
    score_text = font.render(str(score) + "/" + str(ts), True, black)
    screen.blit(score_text, (10, 10))


    # 碰撞偵測
    dinosaur_rect = pygame.Rect(dinosaur_x, dinosaur_y, dinosaur_img.get_width(), dinosaur_img.get_height())
    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_img.get_width(), cactus_img.get_height())
    if dinosaur_rect.colliderect(cactus_rect):
        score = 0

    # 更新畫面
    pygame.display.update()

    # 控制遊戲速度
    clock.tick(60)

    hwnd = pygame.display.get_wm_info()['window']
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# 關閉pygame
pygame.quit()