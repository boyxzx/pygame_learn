import pygame

pygame.init()  # 初始化
screen = pygame.display.set_mode((800, 600))  # 设置窗口的大小
pygame.display.set_caption("这是一个给我们画画用的窗口")

clock = pygame.time.Clock() # 创建一个clock对象

r = 20
x = 330
y = 200

going = True
while going:
    pygame.draw.circle(screen, (0, 0, 0), (x, y), r)  # 画一个圆形
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            going=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= r
            if event.key == pygame.K_RIGHT:
                x += r
            if event.key == pygame.K_DOWN:
                y += r
            if event.key == pygame.K_UP:
                y -= r

    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)  # 画一个圆形
    pygame.display.update()  # 更形圆
    clock.tick(10) # 刷新频率为10，也就是1s刷新10次，每个100ms刷新一次

pygame.quit()  # 结束