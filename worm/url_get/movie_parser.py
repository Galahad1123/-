import requests
from bs4 import BeautifulSoup
from lxml import etree


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


def get_urls(path):
    """
    get urls from file
    return url_list
    """
    url_list = []
    # 注意编码
    with open(path, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            index = line.find('https')
            # -1是去换行
            line = line[index:-1]
            url_list.append(line)

    return url_list


def get_content(url):
    """
    get contents from url
    return content list
    attention: number elements usually contain Chinese words, they need special conversion
    """
    text = http_get(url)
    html = etree.HTML(text)
    detail_page_url = html.xpath('//*[@id="media_module"]/a/@href')[0]
    # 详情页的url
    detail_page_url = 'https:' + detail_page_url
    detail_text = http_get(detail_page_url)
    detail_html = etree.HTML(detail_text)

    thumbs = html.xpath('//*[@id="toolbar_module"]/div[1]/span/text()')[0]  # 点赞数
    coins = html.xpath('//*[@id="toolbar_module"]/div[2]/span/text()')[0]  # 投币数
    comments = html.xpath('//*[@id="comment_module"]/div[1]/span[1]/text()')  # 评论数
    num_of_watching = html.xpath('//*[@id="bilibili-player"]/div/div/div[1]/div[2]/div/div[1]/div[1]/b/text()')  # 在看人数

    total_watching = \
        detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span[1]/em/text()')  # 总播放
    subscribes = detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span[2]/em/text()')  # 追剧人数
    barrages = detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/span[3]/em/text()')  # 弹幕数
    release_date = \
        detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/span[1]/text()')  # 上映时间
    time_length = detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/span[2]/text()')  # 时长
    score = detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/text()')  # 评分
    comment_people = \
        detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/text()')  # 评分人数
    tag_list = detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[2]/span')  # 电影标签列表
    introduction = detail_html.xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[4]/span/text()')  # 简介
    long_comments = detail_html.xpath('//*[@id="app"]/div[2]/div[1]/ul/li[2]/text()')  # 长评
    short_comments = detail_html.xpath('//*[@id="app"]/div[2]/div[1]/ul/li[3]/text()')  # 短评
    actors = detail_html.xpath(
        '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/span[2]/p/text()')  # 演员表
    production_info = detail_html.xpath(
        '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/span[2]/p/text()')  # 制作信息

    return [thumbs, coins, comments, num_of_watching, total_watching, subscribes, barrages, release_date, time_length,
            score, comment_people, tag_list, introduction, long_comments, short_comments, actors, production_info]


if __name__ == '__main__':
    # urls = get_urls('url_src/ten_urls.txt')
    # content_list = get_content(urls[0])
    # print('点赞数: ' + content_list[0])
    # print('投币数: '+content_list[1])
    # print('评论数: '+content_list[2])
    # print('正在观看: '+content_list[3])
    # print('播放量: '+content_list[4])
    # print('追番数: '+content_list[5])
    # print('弹幕数: '+content_list[6])
    # print('上映日期: '+content_list[7])
    # print('时长: '+content_list[8])
    # print('评分: '+content_list[9])
    # print('评分人数: '+content_list[10])
    # print('标签: '+content_list[11])
    # print('简介: '+content_list[12])
    # print('长评: '+content_list[13])
    # print('短评: '+content_list[14])
    # print('演员表: '+content_list[15])
    # print('制作信息: '+content_list[16])
    #

    print(http_get('https://api.bilibili.com/pgc/web/season/stat?season_id=10007'))
    # print(http_get('https://s1.hdslb.com/bfs/static/review/media/asserts/weixin-hover.svg'))
