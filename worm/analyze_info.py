from pyecharts.charts import *
from pyecharts import options as opts
import numpy as np
from pyecharts.globals import CurrentConfig, NotebookType
from pyecharts.commons.utils import JsCode
import matplotlib.pyplot as plt

CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
CurrentConfig.ONLINE_HOST
color_js = """
            new echarts.graphic.LinearGradient(
                                0, 
                                1, 
                                0, 
                                0,
                                [{offset: 0, color: '#008B8B'}, 
                                 {offset: 1, color: '#FF6347'}], 
                                false)
           """

# 用一维数组存储数据
coins = np.zeros(8)  # 总投币数 0~2000，2000~5000，5000~10000，10000~20000，20000~50000，50000~100000，100000~500000，>500000
thumbs = np.zeros(8)  # 总点赞数 0~2000，2000~5000，5000~10000，10000~20000，20000~50000，50000~100000，100000~500000，>500000
viewing = np.zeros(7)  # 总播放数 0~10000，10000~100000，100000~1000000，1000000~2000000，
# 2000000~5000000，5000000~10000000，>10000000
danMu = np.zeros(6)  # 总弹幕量 0~1000，1000~10000，10000~100000，100000~500000，500000~1000000，>1000000
scores = np.zeros(8)  # 总评分 >=9.8，9.8~9.5，9.5~9.0，9.0~8.0，8.0~7.0，7.0~6.0，6.0~5.0，<5.0

# 标签分类 25个
tag_list = ['短片', '喜剧', '奇幻', '冒险', '动作', '动画', '家庭', '灾难', '剧情', '犯罪', '悬疑', '惊悚', '战争',
            '历史', '传记', '漫画改', '小说改', '爱情', '科幻', '恐怖', '歌舞', '都市', '刑侦', '励志', '纪实']

# 二维数组
# 投币、评分、个数
coin_thumb = np.zeros((8, 8))
# 播放、评分、个数
view_score = np.zeros((7, 8))
# 弹幕、点赞、个数
danMu_thumb = np.zeros((6, 8))


def data_analyze(aList):
    """
    解析源文件信息
    """
    view = int(aList[1])
    danmu = int(aList[2])
    coin = int(aList[4])
    thumb = int(aList[5])
    try:
        score = float(aList[7])
    except ValueError:
        score = 0.0

    # 分类播放量
    if view < 10000:
        view_index = 0
    elif view < 100000:
        view_index = 1
    elif view < 1000000:
        view_index = 2
    elif view < 2000000:
        view_index = 3
    elif view < 5000000:
        view_index = 4
    elif view < 10000000:
        view_index = 5
    else:
        view_index = 6

    # 分类弹幕
    if danmu < 1000:
        danmu_index = 0
    elif danmu < 10000:
        danmu_index = 1
    elif danmu < 100000:
        danmu_index = 2
    elif danmu < 500000:
        danmu_index = 3
    elif danmu < 1000000:
        danmu_index = 4
    else:
        danmu_index = 5

    # 分类投币
    if coin < 2000:
        coin_index = 0
    elif coin < 5000:
        coin_index = 1
    elif coin < 10000:
        coin_index = 2
    elif coin < 20000:
        coin_index = 3
    elif coin < 50000:
        coin_index = 4
    elif coin < 100000:
        coin_index = 5
    elif coin < 500000:
        coin_index = 6
    else:
        coin_index = 7

    # 分类点赞
    if thumb < 2000:
        thumb_index = 0
    elif thumb < 5000:
        thumb_index = 1
    elif thumb < 10000:
        thumb_index = 2
    elif thumb < 20000:
        thumb_index = 3
    elif thumb < 50000:
        thumb_index = 4
    elif thumb < 100000:
        thumb_index = 5
    elif thumb < 500000:
        thumb_index = 6
    else:
        thumb_index = 7

    # 分类评分
    if score < 5.0:
        score_index = 0
    elif score < 6.0:
        score_index = 1
    elif score < 7.0:
        score_index = 2
    elif score < 8.0:
        score_index = 3
    elif score < 9.0:
        score_index = 4
    elif score < 9.5:
        score_index = 5
    elif score < 9.8:
        score_index = 6
    else:
        score_index = 7

    coin_thumb[coin_index, thumb_index] += 1
    view_score[view_index, score_index] += 1
    danMu_thumb[danmu_index, thumb_index] += 1

    coins[coin_index] += 1
    thumbs[thumb_index] += 1
    viewing[view_index] += 1
    danMu[danmu_index] += 1
    scores[score_index] += 1


def bar_with_multiple_axis(x_data, y_data_1, y_data_2):
    """
    画点赞-投币双y轴图
    """
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    # 添加一个Y轴
    bar.extend_axis(yaxis=opts.AxisOpts())
    # 分别指定使用的Y轴
    bar.add_yaxis('TouBi', y_data_1, yaxis_index=0)
    bar.add_yaxis('DianZan', y_data_2, yaxis_index=1)
    bar.load_javascript()
    return bar


def bar_with_linear_gradient_color(x_data, y_data):
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('score', y_data,
                  # 使用JsCode执行渐变色代码
                  itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_js)))

    return bar


def nested_pie(data_1, data_2):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 显示中文标签,处理中文乱码问题
    plt.rcParams['axes.unicode_minus'] = False  # 坐标轴负号的处理
    plt.axes(aspect='equal')  # 将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆
    data_1_labels = ['0~1w', '1w~10w', '10w~100w', '100w~200w',
                     '200w~500w', '500w~1kw', '>1kw']
    data_2_labels = ['0~1k', '1k~1w', '1w~10w', '10w~50w', '50w~100w', '>100w']
    explode = [0, 0, 0, 0, 0, 0, 0.1]

    outer_colors = list(np.arange(3)*7)
    inner_colors = list(np.arange(3)*6)
    plt.pie(
        x=data_1,  # 绘图数据
        explode=explode,  # 指定饼图某些部分的突出显示，即呈现爆炸式
        labels=data_1_labels,  # 添加标签
        autopct='%0.3f%%',
        pctdistance=0.8,  # 设置数值与圆心的距离
        labeldistance=1,  # 设置标签与圆心的距离
        radius=1.2,  # 设置饼图的半径
        counterclock=False,  # 是否逆时针，这里设置为顺时针方向
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'green', 'width': 0.4},  # 设置饼图内外边界的属性值
        textprops={'fontsize': 10, 'color': 'royalblue'},  # 设置文本标签的属性值
    )
    plt.pie(
        x=data_2, labels=data_2_labels, pctdistance=0.5, labeldistance=0.7, radius=0.8,
        counterclock=False, wedgeprops={'linewidth': 0.5, 'edgecolor': 'green', 'width': 0.3},
        textprops={'fontsize': 6, 'color': 'orange'}, autopct='%0.3f%%'
    )
    plt.title('viewing and danmu')
    return plt


if __name__ == '__main__':
    # 获取数据
    src_file = open('1000-Data.csv', 'r', encoding='gb18030')
    src_list = src_file.readline()
    src_list = src_file.readline()
    while src_list != '':
        info_list = src_list.split(',')
        data_analyze(info_list)
        src_list = src_file.readline()

    # print("coins:")
    # print(coins)
    # print("thumbs:")
    # print(thumbs)
    # chart = bar_with_multiple_axis(
    #     ['0~2000', '2000~5000', '5000~10000', '10000~20000', '20000~50000', '50000~100000', '100000~500000', '>500000'],
    #     list(coins),
    #     list(thumbs)
    # )
    # chart.render('bar.html')  # 画点赞-投币双Y图

    # sum = 1001
    # print('viewing:')
    # viewing = viewing / sum
    # print(viewing)
    # print('danMu:')
    # danMu = danMu / sum
    # print(danMu)
    # fig = nested_pie(list(viewing), list(danMu))
    # fig.savefig('viewing_danmu.png')
    # fig.show()  # 播放量-弹幕嵌套饼图

    # print('scores:')
    # print(scores)
    # chart2 = bar_with_linear_gradient_color(
    #     ['<5.0', '5.0~6.0', '6.0~7.0', '7.0~8.0', '8.0~9.0', '9.0~9.5', '9.5~9.8', '>=9.8'], list(scores))
    # chart2.render('bar2.html')  # 评分条形图

    print('coin-thumb:')
    print(coin_thumb)
    print('view-score:')
    print(view_score)
    print('danmu-thumb:')
    print(danMu_thumb)
