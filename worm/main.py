import json

# import requests
# import lxml
# from lxml import etree
# from lxml import html
#
# def HTTP_get(url):
#     resp = requests.get(url,headers={'user-agent':'Mozilla/5.0'})
#     resp.encoding ='utf-8'
#     return resp.text
#
# def url_content(url):
#     cont = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}).text
#     html = etree.HTML(cont)
#     # str_list = html.xpath('/html/body/div[@class="wrapper"]/div/div[@class="grid_view"]')
#     str_list = html.xpath('//*[@id="content"]/div')
#     str_list = str_list[0].replace('\'', '')
#     str_list = str_list.encode('utf-8')  # 转码字符集，转码中文
#     json_list = json.loads(str_list)
#     return json_list
#
# def xpath_json_(resp):
#     print('xpath_json  ------  2')
#     html = etree.HTML(resp)
#     str_list =html.xpath('//ol[@class="grid_view"]//text()')
#     # str_list =html.xpath('//div[@id="content"]//text()')
#     # str_list = str_list[0].replace('\'', '')  # 去掉 '' 单引发
#     # str_list = str_list.encode('utf-8')  # 转码字符集，转码中文
#     # json_list = json.loads(str_list)
#     return str_list
#
# def xpath_json(resp):
#     print('xpath_json  ------  2')
#     html = etree.HTML(resp)
#     str_list =html.xpath("//script[@id='captain-config']/text()")
#     str_list = str_list[0].replace('\'', '')  # 去掉 '' 单引发
#     str_list = str_list.encode('utf-8')  # 转码字符集，转码中文
#     json_list = json.loads(str_list)
#     return str_list
#
#
# # 数据清洗
# def domesticData(json_list):
#     domestic = json_list['component'][0]['caseList']  # 国内疫情情况
#     result=["",""]
#     prov = "省,现有确诊,累计确诊,累计治愈,累计死亡,\n"
#     cit = "市,现有确诊,累计确诊,累计治愈,累计死亡,\n"
#     # 省循环
#     for province in domestic:
#
#         temp_province = []
#         # temp_province.append(province['confirmedRelative'])       #  新增确诊
#         # temp_province.append(province['nativeRelative'])  # 新增本土
#         # temp_province.append(province['overseasInputRelative'])   #  新增境外
#         # temp_province.append(province['asymptomaticRelative'])    #  新增无症状
#         # temp_province.append(province['curConfirm'])  # 现有确症
#         # temp_province.append(province['confirmed'])  # 累计确诊
#         # temp_province.append(province['crued'])  # 累计治愈
#         # temp_province.append(province['died'])  # 累计死亡
#
#         # 给空数据赋默认值
#         if  province['curConfirm'] == "":
#             province['curConfirm'] = '0'
#         if  province['confirmed'] == "":
#             province['confirmed'] = '0'
#         if  province['crued'] == "":
#             province['crued'] = '0'
#         if  province['died'] == "":
#             province['died'] = '0'
#
#         # print("省：" + province["area"])
#         # print('现有确症:' + province['curConfirm'])
#         # print('累计确诊:' + province['confirmed'])
#         # print('累计治愈:' + province['crued'])
#         # print('累计死亡:' + province['died'])
#         item=""
#         item+=province["area"]+','+province['curConfirm']+','+province['confirmed']+','+province['crued']+','+province['died']+',\n'
#         prov+=str(item);
#         # 市循环
#         for city in province['subList']:
#
#             # 去除掉一些不需要的杂乱数据
#             if city['city'] == '境外输入':
#                 continue
#             elif city['city'] == '待确认':
#                 continue
#             elif city['city'].find('外') != -1 and city['city'].find('来') != -1:
#                 continue
#             elif city['city'] == '涉冬（残）奥闭环人员':
#                 continue
#             # temp_city = []
#             # temp_city.append(city['nativeRelative'])  # 新增本土
#             # temp_city.append(city['asymptomaticRelative'])      #新增无症状
#             # temp_city.append(city['confirmedRelative'])  # 新增确诊
#             # temp_city.append(city['curConfirm'])  # 现有确症
#             # temp_city.append(city['confirmed'])  # 累计确诊
#             # temp_city.append(city['crued'])  # 累计治愈
#             # temp_city.append(city['died'])  # 累计死亡
#             # temp_city.append(province['noNativeRelativeDays'])  #连续有无新增
#             # temp_city.append(city['overseasInputRelative'])   #新增境外
#
#             # 判断不能为空
#             if city['curConfirm'] == "":
#                 city['curConfirm'] = '0'
#             if city['confirmed'] == "":
#                 city['confirmed'] = '0'
#             if city['crued'] == "":
#                 city['crued'] = '0'
#             if city['died'] == "":
#                 city['died'] = '0'
#
#             # print("城市：" + city["city"])
#             # print('现有确症:' + city['curConfirm'])
#             # print('累计确诊:' + city['confirmed'])
#             # print('累计治愈:' + city['crued'])
#             # print('累计死亡:' + city['died'])
#             item_ = ""
#             item_ += city["city"] + ',' + city['curConfirm'] + ',' + city['confirmed'] + ',' + city['crued'] + ',' + city['died'] + ',\n'
#             cit += str(item_);
#     result[0]=prov
#     result[1]=cit
#     return result
#
# if __name__ == '__main__':
#     # url ='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner&city='
#
#     # resp =HTTP_get(url)
#     # print(resp)
#     # json_list =xpath_json(resp)
#     # print(json_list)
#     # data=domesticData(json_list)//清洗
#     # print(data[0])
#     # with open('Province-Data.csv','w+',encoding='utf-8')as f:
#     #     f.write(str(data[0]))
#     #
#     # with open('City-Data.csv','w+',encoding='utf-8')as f:
#     #     f.write(str(data[1]))
#     # url = 'https://movie.douban.com/top250'
#     # url ='https://www.bilibili.com/?spm_id_from=444.41.0.0'
#     url='https://www.bilibili.com/movie/index/?from_spmid=666.7.index.0#st=2&order=2&area=-1&style_id=-1&release_date=-1&season_status=-1&sort=0&page=2'
#     print(HTTP_get(url))
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
    file_edit = open('data/1000-Data4.csv', 'a+', encoding='UTF-8')
    # file_edit.write(
    #     '电影名字,播放数量,弹幕数量,追剧数量,投币数量,点赞数量,标签,分数,打分人数,影片时长(分钟),长评数量,短评数量,简介,\n')

    nums = 1;
    print(
        "[电影名字,播放数量,弹幕数量,追剧数量,投币数量,点赞数量,标签,分数,打分人数,影片时长(分钟),长评数量,短评数量,简介]")
    length = len(content)  # 一共12158部
    print(length)
    for index in range(9000, 10000):  # range(x,y)即选取txt文件内x~y-1行的电影进行爬取
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
