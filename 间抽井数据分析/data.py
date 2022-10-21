from matplotlib import pyplot as plt
import pandas as pd
import os

def data_plot(path):
    data=pd.read_excel(path,sheet_name='Sheet1')
    print(data)
    columns = ['井口油压(MPa)','井口套压(MPa)',
               ]
    for i in range(0,100,2):
        print(i)

    print(data)
    # sub_plots_number = len(columns)
    # counter = 1
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # for col in columns:
    #     plt.subplot(sub_plots_number,1,counter)
    #     plt.plot(df[col],label = col)
    #     counter += 1
    #     plt.legend(loc='upper right')
    # plt.show()

for roots,dirs,files in os.walk(r'间开井数据'):
    for file in files:
        path = os.path.join(roots,file)
        data_plot(path)
        break

