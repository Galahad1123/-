import csv

import matplotlib.pyplot as plt
import numpy
import pandas as pd
import numpy as np
import wordcloud
from PIL import Image
from wordcloud import WordCloud

all_tags = []
tag_data = []
thumb_data = []

special = ['脱口秀', '漫画改', '小说改', '动态漫', '游戏改', '布袋戏']


# 1000-Data gb18030
# 1000-Data2 utf-8-sig

def find_tag(tag):
    if len(all_tags) == 0:
        return -1
    for i in range(len(all_tags)):
        if tag == all_tags[i][0]:
            return i
    return -1


def analyze_tag(tag, thumb):
    while True:
        if len(tag) < 2 or tag.isdigit():
            break
        if len(tag) == 2:
            a = find_tag(tag)
            if a == -1:
                all_tags.append([tag, 1, int(thumb)])
            else:
                all_tags[a][1] += 1
                all_tags[a][2] += int(thumb)
            break
        elif tag[:3] in special:
            sub_tag = tag[:3]
            a = find_tag(sub_tag)
            if a == -1:
                all_tags.append([sub_tag, 1, int(thumb)])
            else:
                all_tags[a][1] += 1
                all_tags[a][2] += int(thumb)
            tag = tag[3:]
        else:
            sub_tag = tag[:2]
            a = find_tag(sub_tag)
            if a == -1:
                all_tags.append([sub_tag, 1, int(thumb)])
            else:
                all_tags[a][1] += 1
                all_tags[a][2] += int(thumb)
            tag = tag[2:]


def get_info(path, encoding=''):
    if encoding == '':
        src_datas = pd.read_csv(path)
    else:
        src_datas = pd.read_csv(path, encoding=encoding)
    tag_col = src_datas['标签']
    thumb_col = src_datas['点赞数量']
    tag_data = list(tag_col)
    thumb_data = list(thumb_col)
    # 解析tag_data thumb_data
    for i in range(len(tag_data)):
        try:
            analyze_tag(tag_data[i], thumb_data[i])
        except (TypeError, ValueError):
            print('an error')


def get_info_2(path, encoding=''):
    if encoding == '':
        src_file = open(path, 'r')
    else:
        src_file = open(path, 'r', encoding=encoding)
    reader = csv.reader(src_file)
    src_list = next(reader)
    src_list = next(reader)
    while True:
        tag_data.append(src_list[6])
        thumb_data.append(src_list[5])
        try:
            src_list = next(reader)
        except StopIteration:
            break
    # 解析tag_data thumb_data
    for i in range(len(tag_data)):
        try:
            analyze_tag(tag_data[i], thumb_data[i])
        except (TypeError, ValueError):
            print('an error')


if __name__ == '__main__':
    # 适用于 1000-Data.csv
    get_info('data/1000-Data.csv', encoding='gb18030')
    # 适用于 1000-Data2.csv
    get_info_2('data/1000-Data2.csv', encoding='utf-8-sig')
    get_info_2('data/1000-Data3.csv')
    get_info_2('data/1000-Data4.csv')
    get_info('data/1000-Data8.csv', encoding='gb18030')

    l = {}
    for tag in all_tags:
        if tag[1] < 10:
            continue
        l[tag[0]] = round(tag[2] / tag[1])

    wc = wordcloud.WordCloud(
        font_path='msyh.ttc',
        background_color='white'
        # ,max_font_size=120
    )

    wc.generate_from_frequencies(l)
    # wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    plt.figure('词云')
    plt.subplots_adjust(top=0.99, bottom=0.01, right=0.99, left=0.01,
                        hspace=0, wspace=0)
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('pictures/ciyun1+2+3+4+8')
    plt.show()
    print(all_tags)
