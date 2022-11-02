from pyecharts.charts import *
from pyecharts import options as opts
import numpy as np
from pyecharts.globals import CurrentConfig, NotebookType
from pyecharts.commons.utils import JsCode
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

view_max_index = 9
view_divisor = 100000
danmu_max_index = 50
danmu_divisor = 100
coin_max_index = 50
coin_divisor = 100
thumb_max_index = 100
thumb_divisor = 50
# 二维数组
# 投币、点赞、个数, 1~50w, 1~50w
coin_thumb = np.zeros((coin_max_index + 1, thumb_max_index + 1))
# 播放、评分、个数, 1~1000w, 1~10
view_score = np.zeros((10, 10))
# 弹幕、点赞、个数， 1~100w, 1~50w
danMu_thumb = np.zeros((danmu_divisor + 1, thumb_max_index + 1))


def create_3d_figure(x_y, x_label, y_label, title):
    x = np.arange(len(list(x_y)))
    y = np.arange(len(list(x_y[0])))
    x, y = np.meshgrid(x, y)
    z = x_y

    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1)
    ax.contourf(x, y, z, zdir='z', offset=-2)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel('num of movies')
    ax.set_title(title)

    return plt


def data_analyze(alist):
    view = int(alist[1])
    danmu = int(alist[2])
    coin = int(alist[4])
    thumb = int(alist[5])
    try:
        score = int(float(alist[7]))
    except ValueError:
        score = 0

    view_index = int(view / view_divisor)
    if view_index > view_max_index:
        view_index = view_max_index
    danmu_index = int(danmu / danmu_divisor)
    if danmu_index > danmu_max_index:
        danmu_index = danmu_max_index
    coin_index = int(coin / coin_divisor)
    if coin_index > coin_max_index:
        coin_index = coin_max_index
    thumb_index = int(thumb / thumb_divisor)
    if thumb_index > thumb_max_index:
        thumb_index = thumb_max_index

    coin_thumb[coin_index, thumb_index] += 1
    view_score[view_index, score] += 1
    danMu_thumb[danmu_index, thumb_index] += 1


if __name__ == '__main__':
    # 获取数据
    src_file = open('1000-Data.csv', 'r', encoding='gb18030')
    src_list = src_file.readline()
    src_list = src_file.readline()
    while src_list != '':
        info_list = src_list.split(',')
        data_analyze(info_list)
        src_list = src_file.readline()

    # plt = create_3d_figure(coin_thumb, 'num of coins(x10^2)', 'num of thumbs(x10^2)', 'coin-thumb')
    # plt.show()
    plt = create_3d_figure(view_score, 'num of views(x10^5)', 'num of score(x10^2)', 'view-score')
    plt.show()
    # plt = create_3d_figure(danMu_thumb, 'num of danmu(x10^2)', 'num of thumbs(x10^2)', 'danmu-thumb')
    # plt.show()

    print(coin_thumb)
    print(view_score)
    print(danMu_thumb)
