#! python3

import our
import time

# 当前时间，返回时间元组[6]代表星期几，0星期一
current_day = time.localtime()

# 一三六，大乐透
if current_day[6] in(0,2,5):
    our.get_ball(5,35,2,12)
# 二四七，双色球
elif current_day[6] in(1,3,6):
    our.get_ball(6,33,1,16)