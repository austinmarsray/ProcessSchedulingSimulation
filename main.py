from GUI import *
from strategy import *
import random

if __name__ == "__main__":
    input = []
    # 测试使用的数据
    # input = [[3,10,1], [0,5,2], [5,7,3], [6,12,4]]  # [到达时间,服务时间,序列号]

    # 随机生成数据
    r = random.randint(0,4)
    for i in range(4):
        if i==r:
            input.append([0, random.randint(5, 12), i + 1])
        else:
            input.append([random.randint(0,10),random.randint(5,12),i+1])

    #FCFS调度
    FCFS(input.copy())
    draw(TimeLine,Plist,"FCFS调度策略")
    recover()

    #SJF调度
    SJF(input.copy())
    draw(TimeLine, Plist,"SJF(非抢占式)调度策略")
    recover()

    #RR调度
    RR(input.copy())
    draw(TimeLine, Plist,"RR调度策略")
    recover()