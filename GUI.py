import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#####################################################################################
plt.rcParams['toolbar'] = 'None'
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.rcParams['font.size'] = 15
#####################################################################################
colordict = {1:"darkorange",2:"limegreen",4:"purple",3:"deepskyblue"}
#####################################################################################


def draw(tl,plist,title):
    fig = plt.figure(figsize=(19,10))  # 生成画布


    ax1 = plt.subplot(211)
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

    ax2 = plt.subplot(212)
    ax2.axis('off')
    ax2.axis('tight')

    a = []
    columns = ["进程名称","到达时间","服务时间","开始服务时间","结束时间","周转时间","带权周转时间"]
    a.append(["进程{}".format(x.index) for x in plist])
    a.append([x.arrive_time for x in plist])
    a.append([x.serve_time for x in plist])
    a.append([x.start_time for x in plist])
    a.append([x.end_time for x in plist])
    a.append([x.end_time - x.arrive_time for x in plist])
    a.append([(x.end_time - x.arrive_time) / x.serve_time for x in plist])

    df = {columns[0]:a[0],columns[1]:a[1],columns[2]:a[2],columns[3]:a[3],columns[4]:a[4],columns[5]:a[5],columns[6]:a[6]}
    df = pd.DataFrame(df)
    tb = ax2.table(cellText=df.values,cellLoc='center',colLabels=df.columns,bbox=[0, 0, 1, 1])
    for i in range(7):
        tb[0, i].set_facecolor('#363636')
        tb[0, i].set_text_props(color='w')
    plt.pause(0.01)

    plt.show()