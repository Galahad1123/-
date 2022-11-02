# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# option = webdriver.EdgeOptions()
# option.add_experimental_option("detach", False)
#
# # edge浏览器
# driver = webdriver.Edge()
# driver.get('https://www.bilibili.com/bangumi/play/ss12548?from_spmid=666.23.0.0')
# print(driver.find_element(By.XPATH, '//*[@id="media_module"]/div/div[1]').text)
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By


def _process_str_(s):
    if '万' in s:
        _s = s.replace('万', '')
        fl = float(_s)
        fl = fl * 10000
        return str(int(fl))
    return s


if __name__ == '__main__':
    # Edge浏览器模拟
    option = webdriver
    option.add_experimental_option("detach", False)

    _chr = ' '
    driver = webdriver.Edge()

    # 打开文件
    file = open('movie_names.txt', 'r')
    read = file.read()
    content = read.split('\n')

    # 待写文件
    file_edit = open('data.csv', 'w')
    file_edit.write('电影名字,播放数量,弹幕数量,追剧数量,\n')

    # 调试用,imax为处理网页数量
    imax = 100

    for enum in content:
        if (len(enum) != 0):  # 判断该行是否为空

            name_url = enum.split('\t')  # 取出该行数据

            driver.get(name_url[1])  # 进入网页

            _text = driver.find_element(By.XPATH, '//*[@id="media_module"]/div/div[1]').text  # 提取信息

            # 格式化输出
            nospace_text = _text.replace('\t', '').replace(chr(32), '')
            result = nospace_text.split('·')
            result[0] = _process_str_(result[0].replace('播放', ''))
            result[1] = _process_str_(result[1].replace('弹幕', ''))
            result[2] = _process_str_(result[2].replace('追剧', '').replace('系列', '').replace('追番', ''))

            file_edit.write(name_url[0] + ',' + result[0] + ',' + result[1] + ',' + result[2] + ',\n')

            # 预览
            print(result)
            imax -= 1
            if (imax == 0):
                break

    driver.close()
    file.close()
    file_edit.close()
