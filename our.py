#! python3

import random
import config
import send_mail
import create_image

# 我们
our = config.She + config.Me

# 幸运
def luck(count,max_num):
    num_list = []

    # 循环一万遍，一遍代表一年
    for i in range(0,10000):
        # 从“我们”中依次取出2个数组合成1个幸运数
        lucky_number = our[random.randint(0,len(our)-1)]
        lucky_number = lucky_number + our[random.randint(0,len(our)-1)]
        # 如果幸运数是0，继续下一个循环
        if int(lucky_number) == 0:
            continue
        # 如果幸运数已集齐（双色球6个，大乐透5个），退出循环
        if len(num_list) == count:
            break
        # 幸运数不大于（双色球红气球<=33，蓝球<=16 大乐透前区<=35，后区<=12）
        if int(lucky_number) <= max_num:
            if lucky_number not in num_list:
                num_list.append(lucky_number)
                num_list.sort()
        
    return num_list

# 生成幸运号码
def get_ball(reb_count,red_max,blue_count,blue_max):
    # 循环一百遍，一遍代表一年
    for i in range(0,100):
        # 红球（5个，最大35）
        red_ball = luck(reb_count,red_max)
        red_ball.append('-')

        # 篮球（2个，最大12）
        blue_ball = luck(blue_count,blue_max)
        # 如果第3个红球<=10，则再生成一次
        if red_ball[2] <= '10':
            continue
        else:
            # 幸运号码
            ball_list = red_ball+blue_ball
            # 把号码格式化一下，好看点
            beautiful_ball = ''
            for j in range(0,len(ball_list)):
                beautiful_ball += ball_list[j] + ' '
            print(beautiful_ball)

            # 生成图片
            create_image.create_image(beautiful_ball)

            # 发送邮件
            send_mail.send_mail()
            break
