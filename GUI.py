import matplotlib.pyplot as plt

#####################################################################################
plt.rcParams['toolbar'] = 'None'
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#####################################################################################
colordict = {1:"darkorange",2:"limegreen",4:"purple",3:"deepskyblue"}
#####################################################################################
def drawline(x,y):
    step = 0.1
    for i in range(10*(x[1]-x[0])):
        start = x[0]+i*step
        end = x[0]+(i+1)*step
        plt.plot([start,end], y, color=colordict[y[0]],linewidth=3)
        plt.pause(0.01)

def draw(x,y,plist,title):
    fig = plt.figure(figsize=(10,5))  # 生成画布
    fig.canvas.set_window_title(title)
    plt.grid()
    plt.xlim(0,50)
    plt.ylim(0,5)
    plt.xticks(range(0,50,2))
    plt.yticks(range(0,6),labels=["","进程1","进程2","进程3","进程4"])

    for i in range(len(x)):
        plt.vlines(plist[i].arrive_time, 0, y[i][0], colors=colordict[y[i][0]], linestyles="dashed")
    # 整体调度图像
    for i in range(len(x)):
        plt.vlines(x[i][0], 0, y[i][0], colors="r", linestyles="dashed")
        drawline(x[i], y[i])
        plt.vlines(x[i][1],0,y[i][0], colors="r", linestyles="dashed")
        plt.pause(0.01)

    # 补充到达状态表达
    for i in range(len(x)):
        plt.vlines(plist[i].arrive_time, 0, y[i][0], colors=colordict[y[i][0]], linestyles="dashed")
        plt.plot([plist[i].arrive_time,plist[i].end_time],[y[i][0],y[i][0]] , color=colordict[y[i][0]], linestyle="dashed")
        plt.pause(0.01)

    plt.show()