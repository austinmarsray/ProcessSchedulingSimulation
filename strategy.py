import queue
import process
#####################################################################################
TimeLine = []
X = []
Y = [] #可视化用
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
        X.append([now,now+serve])
        Y.append([index,index])
        TimeLine.extend([index]*serve)
        print(TimeLine)
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
        X.append([now, now + serve])
        Y.append([index, index])
        TimeLine.extend([index]*serve)
        print(TimeLine)
        Plist.append(process.process(arrive, serve, now, now + serve, index))
        now = now + serve
        input.remove([arrive, serve, index])
        prepare.remove([arrive, serve, index])

def RR(input):
    global X,Y
    input.sort(key=get_arrive)
    prepare = []
    now=0
    input = [[x[0],x[1],x[2],x[1]] for x in input]
    X = [[] for x in range(len(input))]
    Y = [[] for x in range(len(input))]
    while True:
        for x in input:
            if x[0]<=now and x[3]>0:
                prepare.append(x)
        [arrive, serve, index, left] = prepare[0]
        X
def recover():
    X.clear()
    Y.clear()
    TimeLine.clear()
    Plist.clear()