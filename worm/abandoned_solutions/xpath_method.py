import requests
from lxml import etree


def HTTP_get(url):
    """
    返回网页文本
    """
    resp = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
    resp.encoding = 'utf-8'
    return resp.text, resp.status_code


def movie_crawler(url):
    """
    爬取电影分区
    """
    movie_text = HTTP_get(url)
    # print(movie_text)

    print('movie_crawler  ------  2')
    html = etree.HTML(movie_text)
    movie_links = html.xpath("//*[@id='app']/div[2]/div[1]/ul[2]")
    return movie_links


if __name__ == '__main__':
    url = 'https://www.bilibili.com/bangumi/play/ss41540?from_spmid=666.23.0.0'

    resp = HTTP_get(url)
    # print(resp)

    res_text, status = HTTP_get(url)
    print(status)

    html = etree.HTML(res_text)
    movie_name = html.xpath('//*[@id="media_module"]/div/a/@title')
    print(movie_name)

    # movies = movie_crawler(url)
    #
    # for movie in movies:
    #     print(movie)
