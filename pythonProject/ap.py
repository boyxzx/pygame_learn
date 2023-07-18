import pygame
import math


# 画降落伞的函数
def jls(x, y, color):
    w = 100
    h = 100
    rect = x, y, w, h  # Rect(left, top, width, height)
    start_angle = math.radians(0)  # 根据度数求出弧
    stop_angle = math.radians(180)
    width = 1  # 线条粗细

    # 画弧形
    pygame.draw.arc(screen, color, rect, start_angle, stop_angle, width)
    abch = math.sqrt(100 ** 2 * 3 / 4)  # 100**2表示100的2次方，3/4表示4分之三，这里是根据勾股定理来求出三角形的高
    # 用连续线段画个等边三角形
    pygame.draw.lines(screen, color, False, [[x, y + 50], [x + 100, y + 50], [x + 50, y + 50 + abch], [x, y + 50]], 1)
    # 用连续线段画个等边四边形
    pygame.draw.lines(screen, color, False, [[x + 25, y + 50 + abch], [x + 75, y + 50 + abch], [x + 75, y + 100 + abch],
                                             [x + 25, y + 100 + abch], [x + 25, y + 50 + abch]], 1)


pygame.init()  # 初始化
screen = pygame.display.set_mode((800, 600))  # 设置窗口的大小
pygame.display.set_caption("这是一个给我们画画用的窗口")

fclock = pygame.time.Clock()  # 控制时间间隔

mx = 300
my = 200
going = True
while going:

    jls(mx, my, (0, 0, 0))  # 删除上次画的图
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            going = False

    if (mx < 0):
        mx = 800
    if (my < 0):
        my = 600
    mx -= 1
    my -= 1
    jls(mx, my, (255, 0, 255))
    pygame.display.update()

    fclock.tick(200)

pygame.quit()