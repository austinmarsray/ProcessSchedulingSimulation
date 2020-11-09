import queue
import process
#####################################################################################
TimeLine = []
Plist = [] #综合统计
#####################################################################################
def get_arrive(x):
    return x[0]
def get_serve(x):
    return x[1]


def FCFS(input):
    q = queue.PriorityQueue()
    for item in input:
        q.put(item)
    now = 0
    while not q.empty():
        [arrive,serve,index] = q.get()
        TimeLine.extend([index]*serve)
        Plist.append(process.process(arrive, serve, now, now + serve, index))
        now = now + serve

def SJF(input):#非抢占型
    input.sort(key=get_arrive)
    prepare = []
    now = 0
    while len(input)!=0:
        # 准备就绪队列
        for x in input:
            if x[0]<=now and (x not in prepare):
                prepare.append(x)
        prepare.sort(key=get_serve)
        [arrive, serve, index] = prepare[0]
        TimeLine.extend([index]*serve)
        Plist.append(process.process(arrive, serve, now, now + serve, index))
        now = now + serve
        input.remove([arrive, serve, index])
        prepare.remove([arrive, serve, index])

def RR(input):
    input.sort(key=get_arrive)
    prepare = []
    start_record = [-1,-1,-1,-1]
    now=0
    Data = [[x[0],x[1],x[2],x[1]] for x in input]
    while len(Data)!=0:
        for x in Data:
            if x[0]<=now and x[3]>0 and (x not in prepare):
                prepare.append(x)
        [arrive, serve, index, left] = prepare[0]
        if start_record[index-1] == -1:#记录每个进程的开始时间
            start_record[index-1] = now
        TimeLine.append(index)
        prepare.remove([arrive, serve, index, left])
        Data.remove([arrive, serve, index, left])
        if left>1:
            Data.append([arrive, serve, index, left-1])
        else:
            Plist.append(process.process(arrive, serve, start_record[index-1], now+1, index))
        now = now + 1

def recover():
    TimeLine.clear()
    Plist.clear()