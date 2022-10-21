# @Time     :2022/10/20 10:01
# @Author   :LuXin
# @Function :对间开井数据进行画图

import os
import pandas as pd
import matplotlib.pyplot as plt


"""
fig = plt.subplots(nrows=2, ncols=2)在一个图形对象中设置一组带有网格(2,2)的子图
返回值是这样的元组
(fig,[ax1,ax2,ax3,ax4])
返回值第一个元素是画布，第二个值是numpy数组，数组储存了子图的轴
"""

plt.rcParams['font.sans-serif'] = ['SimHei']
save_dir = 'test'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
for roots,dirs,files in os.walk('间开井数据'):
    for file in files:
        fig_name = file.split('.')[0]
        print(fig_name)
        path = os.path.join(roots,file)
        data = pd.read_excel(path,sheet_name='Sheet1')


        index = []
        for i in range(0,len(data),120):
            index.append(i)
        data = data.loc[index]
        print(data)
        fig,ax=plt.subplots(2,1,figsize=(15, 10))
        ax[0].plot(data['时间'],data['井口油压(MPa)'],
                   label='井口油压',c='#4D85BD')
        ax[0].legend()
        f2 = ax[1].plot(data['时间'], data['井口套压(MPa)'],
                        label='井口套压',c='#F7903D')
        ax[1].legend()

        xticks = list(range(0, len(data['时间']), 500))
        xlabels = [data['时间'].iloc[x] for x in xticks]
        xlabels = [date.split(' ')[0] for date in xlabels]
        ax[1].set_xticks(xticks)
        ax[1].set_xticklabels(xlabels, rotation=40)
        ax[0].set_xticks(xticks)
        ax[0].set_xticklabels(xlabels, rotation=40)

        ax[0].set_ylabel('井口油压(MPa)')
        ax[1].set_ylabel('井口套压(MPa)')
        ax[1].set_xlabel('时间')

        ax[0].set_title(fig_name)
        plt.show()
        # save_path = os.path.join(save_dir,fig_name+'.png')
        # plt.savefig(save_path)
        # plt.close()

