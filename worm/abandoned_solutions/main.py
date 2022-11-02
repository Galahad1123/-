import requests
from lxml import etree


def HTTP_get(url):
    """
    返回网页文本
    """
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                    'Chrome/103.0.0.0 Safari/537.36 '
                                      })
    resp.encoding = 'utf-8'
    return resp.text


def xpath_json(resp):
    """
    返回b站分区和对应链接
    """
    print('xpath_json  ------  1')
    html = etree.HTML(resp)
    class_list = html.xpath("//*[@id='i_cecream']/div[2]/div[1]/div[3]/div[2]/div[1]/a/text()")
    link_list = html.xpath("//*[@id='i_cecream']/div[2]/div[1]/div[3]/div[2]/div[1]/a/@href")

    return class_list, link_list


def movie_crawler(url):
    """
    爬取电影分区
    """
    movie_text = HTTP_get(url)
    print('movie_crawler  ------  2')
    html = etree.HTML(movie_text)
    movie_links = html.xpath("//*[@id='app']/div[2]/div[1]/ul[2]/li/a/@href")



if __name__ == '__main__':
    url = 'https://www.bilibili.com/'

    resp = HTTP_get(url)
    # print(resp)

    # with open('bilibili.json', "w", encoding='utf-8') as f:
    #     f.write(resp)

    json_list, link_list = xpath_json(resp)
    for i in range(0, min(len(json_list), len(link_list))):
        link_list[i] = 'https:' + link_list[i]
        print(json_list[i] + ": " + link_list[i])

