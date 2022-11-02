import time
import urllib.request

import requests
from lxml import etree


def HTTP_get(url):
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return resp, resp.status_code


if __name__ == '__main__':
    url_head = "https://www.bilibili.com/bangumi/play/ss"
    url_tail = "?from_spmid=666.23.0.0"

    count = 12159

    with open("../url_src/movie_4w_5w.txt", "a+") as f:
        for index in range(45000, 50000):
            time.sleep(2)
            url = url_head + str(index) + url_tail
            res, status_code = HTTP_get(url)

            if status_code != 404:
                res.encoding = 'utf-8'
                res_text = res.text
                count += 1

                html = etree.HTML(res_text)
                movie_name = html.xpath('//*[@id="media_module"]/div/a/@title')
                print('find: ' + movie_name[0])
            try:
                f.write(movie_name[0])
                f.write('\t')
                f.write(url)
                f.write("\n")
            except IndexError:
                pass
            except UnicodeEncodeError:
                print("a UnicodeEncodeError, keep crawl")

            if index % 100 == 99:
                print('已完成：' + str((index - 39999) / 100) + '%' + '(4w~5w)')

        f.write('总电影数：' + str(count))
        f.write('\n')

