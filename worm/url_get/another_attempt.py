import requests
from lxml import etree


def HTTP_get(url):
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                    'Chrome/103.0.0.0 Safari/537.36 '
                                      })
    return resp, resp.status_code


if __name__ == '__main__':
    url_head = "https://www.bilibili.com/bangumi/play/ss"
    url_tail = "?from_spmid=666.23.0.0"

    with open("../url_src/movie_1w_2w.txt", "w+") as f:
        for index in range(12781, 50000):
            url = url_head + str(index) + url_tail
            res, status_code = HTTP_get(url)

            if status_code != 404:
                res.encoding = 'utf-8'
                res_text = res.text

                html = etree.HTML(res_text)
                movie_name = html.xpath('//*[@id="media_module"]/div/a/@title')
                # print(movie_name)
                try:
                    f.write(movie_name[0])
                    f.write('\t')
                    f.write(url)
                    f.write("\n")
                except IndexError:
                    pass

            if index % 100 == 99:
                print('已完成：' + str((index - 9999) / 100) + '%')
