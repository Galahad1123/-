from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

base_url = 'https://www.bilibili.com/movie/index/?from_spmid=666.7.index.0#area=-1&style_id=-1&release_date=-1' \
           '&season_status=-1&order=2&st=2&sort=0&page='

# for i in range(1, 200):
for i in range(1, 2):

    url = base_url + str(i)

    # if requests.get(url).status_code != 200:
    #     continue

    html = urlopen(url).read().decode('utf-8')
    # print(html)

    soup = BeautifulSoup(html, features='lxml')

    # find valid urls
    # sub_urls = soup.find_all("a", {"target": "_blank",
    #                                "href": re.compile("//www.bilibili.com/bangumi/play/ss([0-9]{5})" +
    #                                                   "?from_spmid=666.23.0.0"),
    #                                "class": "cover-wrapper"})
    #
    # for url in sub_urls:
    #     print(url)

    # axs = soup.find_all("ul", {'class': 'bangumi-list clear fix'})
    # for ax in axs:
    #     print(ax)
    #     print('\n')
    axs = soup.find_all("div", {'class': 'filter-body'})
    for ax in axs:
        print(ax)
        print('\n')
