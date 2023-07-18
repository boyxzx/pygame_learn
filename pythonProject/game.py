import random

def guess_number():
    # 生成随机数
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # 用户输入猜测的数字
        guess = int(input('猜一个1到100之间的数字: '))
        attempts += 1

        if guess < secret_number:
            print('太小了！')
        elif guess > secret_number:
            print('太大了！')
        else:
            print(f'恭喜你，你猜对了！你使用了 {attempts} 次尝试。')
            break

# 调用游戏函数
guess_number()