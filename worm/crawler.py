import sys
import time

import selenium.common.exceptions
from lxml import etree

import requests
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def _process_str_(s):
    if '万' in s:
        _s = s.replace('万', '')
        fl = float(_s)
        fl = fl * 10000
        return str(int(fl))
    if '亿' in s:
        _s = s.replace('亿', '')
        fl = float(_s)
        fl = fl * 100000000
        return str(int(fl))
    return s


def http_get(url):
    """
    return http_text
    """
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                    'Chrome/103.0.0.0 Safari/537.36 '
                                      })
    resp.encoding = 'utf-8'
    return resp.text


if __name__ == '__main__':
    path = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    # Edge浏览器模拟
    # option = webdriver
    # option.add_experimental_option("detach", False)
    options = Options()
    options.add_argument("--mute-audio")
    options.page_load_strategy = 'normal'
    # options.page_load_strategy = 'eager'
    driver = webdriver.Edge(options=options)
    _chr = ' '
    # driver = webdriver.Edge()

    # 打开文件
    file = open('all_movies.txt', 'r', encoding='UTF-8')
    # file =open('Test.txt','r',encoding='UTF-8')
    read = file.read()
    content = read.split('\n')

    # 待写文件
    file_edit = open(path, 'a+', encoding='UTF-8')
    file_edit.write(
        '电影名字,播放数量,弹幕数量,追剧数量,投币数量,点赞数量,标签,分数,打分人数,影片时长(分钟),长评数量,短评数量,简介,\n')

    nums = 1
    print(
        "[电影名字,播放数量,弹幕数量,追剧数量,投币数量,点赞数量,标签,分数,打分人数,影片时长(分钟),长评数量,短评数量,简介]")
    length = len(content)  # 一共12158部
    print(length)
    for index in range(start, end):  # range(x,y)即选取txt文件内x~y-1行的电影进行爬取
        if (len(content[index]) != 0):  # 判断该行是否为空

            name_url = content[index].split('\t')  # 取出该行数据

            try:
                driver.get(name_url[1])  # 进入网页
            except selenium.common.exceptions.InvalidArgumentException:
                continue
            time.sleep(0.3)
            try:
                _text = driver.find_element(By.XPATH, '//*[@id="media_module"]/div/div[1]').text  # 提取信息
            except Exception as e:
                print(e.args)
                continue
            print(index, ' ', nums, end=' ')
            nums += 1
            try:
                _coin = driver.find_element(By.XPATH, '//*[@class="coin-info"]').text  # 投币数
                _like = driver.find_element(By.XPATH, '//*[@class="like-info"]').text  # 点赞数
                # _comm = driver.find_element(By.XPATH, '//*[@id="comment_module"]/div[1]/span[1]').text

                text = http_get(name_url[1])  # 详情页面地址获取
                html = etree.HTML(text)
                detail_page_url = html.xpath('//*[@id="media_module"]/a/@href')[0]
                # try:
                #     detail_page_url = html.xpath('//*[@id="media_module"]/a/@href')[0]
                # except Exception as e:
                #     print(e.args)
                #     print(name_url)
                #     try:
                #         detail_page_url = html.xpath('//*[@id="media_module"]/div/a').text
                #         print(detail_page_url)
                #     except Exception as e:
                #         continue
                detail_page_url = 'https:' + detail_page_url
                driver.get(detail_page_url)  # 进入详情页面
                # 获取标签
                _tags = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[2]').text
                # 获取日期
                _date = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/span[1]').text
                # 获取时长
                _time = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/span[2]').text
                # 获取评分及评分人数
            except Exception as e:
                print("Wrong")
                continue
            try:
                _score = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]').text
                _score_people = driver.find_element(By.XPATH,
                                                    '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]').text
            except selenium.common.exceptions.NoSuchElementException:
                _score = '暂无评分'
                _score_people = '评分人数不足'
            # 获取简介
            _intro = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[4]/span').text
            # 获取长评短评数量
            try:
                _longcomm = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/ul/li[2]').text
                _shortcomm = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[1]/ul/li[3]').text
            except selenium.common.exceptions.NoSuchElementException:
                _longcomm = '无'
                _shortcomm = '无'

            # 格式化输出
            nospace_text = _text.replace('\t', '').replace(chr(32), '')
            result = nospace_text.split('·')
            result[0] = _process_str_(result[0].replace('播放', ''))
            result[1] = _process_str_(result[1].replace('弹幕', ''))
            result[2] = _process_str_(result[2].replace('追剧', '').replace('系列', '').replace('追番', ''))
            result.append(_process_str_(_coin))
            result.append(_process_str_(_like))
            result.append(_tags)
            result.append(_score)
            result.append(_score_people.replace('人评', ''))
            result.append(_time.replace('分钟', ''))
            result.append(_longcomm.replace('长评 ( ', '').replace(' )', '').replace('长评', '0'))
            result.append(_shortcomm.replace('短评 ( ', '').replace(' )', '').replace('短评', '0'))
            result.insert(0, name_url[0])
            # 预览
            print(result)
            result.append(_intro)
            # result.append(_process_str_(_comm))

            # 写入文件
            for i in result:
                file_edit.write(i + ',')
            file_edit.write('\n')

    driver.close()
    file.close()
    file_edit.close()
