import matplotlib.pyplot as plt

#####################################################################################
plt.rcParams['toolbar'] = 'None'
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#####################################################################################
colordict = {1:"darkorange",2:"limegreen",4:"purple",3:"deepskyblue"}
#####################################################################################


def draw(tl,plist,title):
    fig = plt.figure(figsize=(10,5))  # 生成画布
    fig.canvas.set_window_title(title)
    plt.grid()
    plt.xlim(0,40)
    plt.ylim(0,5)
    plt.xticks(range(0,40,2))
    plt.yticks(range(0,6),labels=["","进程1","进程2","进程3","进程4"])

    # 画到达时间线
    for i in range(4):
        plt.vlines(plist[i].arrive_time, 0, plist[i].index, colors=colordict[plist[i].index], linestyles="dashed")

    # 整体调度图像
    for i in range(0,len(tl)):
        pnum = tl[i]
        for j in range(0,10):
            start = i + j * 0.1
            end = i + (j + 1) * 0.1
            plt.plot([start, end], [pnum,pnum], color=colordict[pnum], linewidth=3)
            plt.pause(0.01)

    # 补充到达状态表达
    for i in range(4):
        plt.vlines(plist[i].arrive_time, 0, plist[i].index, colors=colordict[plist[i].index], linestyles="dashed")
        plt.plot([plist[i].arrive_time,plist[i].end_time],[plist[i].index,plist[i].index] , color=colordict[plist[i].index], linestyle="dashed")
        plt.pause(0.01)

    plt.show()