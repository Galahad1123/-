import json
from lxml import etree
import requests


def HTTP_get(url):
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                    'Chrome/103.0.0.0 Safari/537.36 '
                                      })
    resp.encoding = 'utf-8'
    return resp.text


def xpath_json(resp):
    print('xpath_json  ------  2')
    html = etree.HTML(resp)
    str_list = html.xpath("//script[@id='captain-config']/text()")
    str_list = str_list[0].replace('\'', '')  # 去掉 '' 单引发
    str_list = str_list.encode('utf-8')  # 转码字符集，转码中文
    # str_list = str_list.encode('utf-8').decode('unicode_escape')  # 转码字符集，转码中文
    json_list = json.loads(str_list)

    return json_list


if __name__ == '__main__':
    url = 'https://www.jd.com/?cu=true&utm_source=haosou-search&utm_medium=cpc&utm_campaign=t_262767352_haosousearch&' \
          'utm_term=15885841661_0_368c98e61b4c489189b72ad4583b096c'

    # 请求HTTP
    resp = HTTP_get(url)
    print(resp)

    # # 解析数据
    # json_list = xpath_json(resp)
    #
    # """ 这个代码就可以删掉了，毕竟他只是让我们更好的解析数据和清洗数据
    # # 加上这样一个代码，之后会去掉的，只是方便 我们清洗数据，看清这个json格式
    with open('JsonData.json', 'w+', encoding='utf-8') as f:
        f.write(str(resp))
    # """
    # # 清洗数据
    # domesticData(json_list)
    #
    # # outsideData(json_list)
