import pygame

# 画小车的函数
def bus(x, y, color,yy):
    pygame.draw.rect(screen, (233, 21, 67), (x, y, 100, 50), 0)  # 画一个长方形做车体

    pygame.draw.circle(screen, (255, 255, 255), [x + 15, y + 20], 10)
    pygame.draw.circle(screen, (255, 255, 255), [x + 85, y + 20], 10)

    pygame.draw.circle(screen, (0, 0, 0), [x + 15+ yy, y + 20], 5)
    pygame.draw.circle(screen, (0, 0, 0), [x + 85+ yy, y + 20], 5)

    pygame.draw.rect(screen, (0, 0, 0), (x+40, y+30, 20, 5), 0)
    pygame.draw.rect(screen, (0, 0, 0), (x + 40, y + 20, 5, 10), 0)

    pygame.draw.circle(screen, color, [x + 15, y + 65], 15)  # 画一个圆形做轮胎
    pygame.draw.circle(screen, color, [x + 85, y + 65], 15)  # 画一个圆形做轮胎

pygame.init()  # 初始化
screen = pygame.display.set_mode((800, 600))  # 设置窗口的大小
pygame.display.set_caption("这是一个给我们画画用的窗口")

fclock = pygame.time.Clock()  # 控制时间间隔

x = 300
y = 200
color = 250, 180, 90
yy=3
going = True
aa = 0
while going:
    screen.fill((0,0,0))
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            going = False

    x += 1
    if (x > 800):  # 当小车跑出画布之后，我们让它从最左边出来
        x = 0

    if yy==3:
        if aa>100:
           yy = -3
           aa = 0
        else:
            aa += 1
    else:
        if aa>100:
           yy = 3
           aa = 0
        else:
            aa += 1
    bus(x, y, color,yy)
    pygame.display.update()
    fclock.tick(200)

pygame.quit()