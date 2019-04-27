import os
from urllib import request

import requests
from bs4 import BeautifulSoup
from cmdb import models


def get_history(i):
    url = 'https://book.douban.com/top250?start='+ str(25 * i)
    html = requests.get(url)
    datas = BeautifulSoup(html.text, 'lxml').find('div',  class_='indent').find_all('table')

    a = 0
    for data in datas:
        try:
            data_bookname = data.find('div', class_='pl2').find('a').get_text()
            data_infos= data.find('p', class_='pl').get_text()
            data_appraise = data.find('span', class_='rating_nums').get_text()
            data_peoplenum = data.find('span', class_='pl').get_text()
            if data.find('span', class_='inq').get_text():
                data_content = data.find('span', class_='inq').get_text()
            else:
                data_content = "无"
            # data_picture=data.find_all('img')
            #
            #
            # # 封面图片保存路径和文件名
            # pic_name = './static/imgs/' + str(i * 25 + a + 1) + '.jpg'
            #
            # # 下载封面图片到本地，路径为pic_name
            # if not os.path.exists(pic_name):
            #     request.urlretrieve(data_picture, filename=pic_name)

            # 插入数据到数据库
            models.bookInfo.objects.create(ranking=str(i * 25 + a + 1),
                                            bookname=data_bookname,
                                            infos=data_infos,
                                            appraise=data_appraise,
                                            peoplenum=data_peoplenum,
                                            content=data_content)
        except:
            continue
        finally:
            a += 1


def static_historyworm_main():
    for i in range(10):
        get_history(i)


