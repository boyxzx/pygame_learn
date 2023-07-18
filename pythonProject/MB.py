import pygame
import random

# 画小车的函数
def bus(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 100, 50), 0)  # 画一个长方形做车体
    pygame.draw.circle(screen, color, [x + 15, y + 65], 15)  # 画一个圆形做轮胎
    pygame.draw.circle(screen, color, [x + 85, y + 65], 15)  # 画一个圆形做轮胎


pygame.init()  # 初始化
screen = pygame.display.set_mode((800, 600))  # 设置窗口的大小
pygame.display.set_caption("这是一个给我们画画用的窗口")

fclock = pygame.time.Clock()  # 控制时间间隔

x = 300
y = 500
color = 155, 155, 155
going = True
apple_x = 200
apple_y = 0
apple_cunt = 0
while going:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            going = False
        if event.type == pygame.KEYDOWN:  # 判断获取时间是否为按钮按下的类型
            if event.key == pygame.K_RIGHT:  # 判断是否按了右方向键
                x += 50
            if event.key == pygame.K_LEFT:  # 判断是否按了左方向键
                x -= 50

    bus(x, y, color)

    apple_y += 1
    if (apple_y > 600):  # 当圆超出界面之后从上边继续掉下来
        apple_y = 0
        apple_x = random.randint(1, 800)

    if (apple_x>x and apple_x<x+100 and apple_y>y-15 and apple_y<y+80):
        apple_y = 0
        apple_cunt += 1
        apple_x = random.randint(1, 800)
    myfont = pygame.font.Font(None, 50)
    textImage = myfont.render('apple:' + str(apple_cunt), True, (255, 255, 255))
    screen.blit(textImage, (50, 50))
    pygame.draw.circle(screen, (255, 0, 0), [apple_x, apple_y], 15)  # 画一个圆形做苹果

    pygame.display.update()
    fclock.tick(200)

pygame.quit()