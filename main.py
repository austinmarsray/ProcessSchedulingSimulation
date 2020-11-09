from GUI import *
from strategy import *


if __name__ == "__main__":
    input = [[3,10,1], [0,5,2], [5,7,3], [6,12,4]]  # [到达时间,服务时间,序列号]

    #FCFS调度
    FCFS(input)
    draw(X,Y,Plist,"FCFS调度策略")
    recover()

    # SJF调度
    SJF(input)
    draw(X, Y, Plist,"SJF(非抢占式)调度策略")
    recover()

    #RR调度
    # RR(input)
    # draw(X, Y, Plist,"RR调度策略")
    # recover()