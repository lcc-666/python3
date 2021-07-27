import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os
from fake_useragent import UserAgent
import threading
import time



def delsql(jpg):
    con = pymysql.connect(host="127.0.0.1", user="root", password="123456", port=3306, db="jjwang",
                          charset="utf8")
    cur = con.cursor()
    sql = 'DELETE FROM suoyin WHERE jpg = %s;'
    args = (jpg,)
    cur.execute(sql, args)
    con.commit()
    cur.close()
    con.close()

def getpic(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    root="./xz/"
    path=root+url.split("/")[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url,headers=headers)
            r.raise_for_status()
            if len(r.text)>100:
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("OK")
                    delsql(url+'\n')
            else:
                print("文件小")
        else:
            print("文件已存在")
    except :
        print("爬取失败")

def get():
    con = pymysql.connect(host="127.0.0.1", user="root", password="123456", port=3306, db="jjwang",
                          charset="utf8")
    cur = con.cursor()
    sql="select * from suoyin"
    cur.execute(sql)
    reult=cur.fetchall()
    return reult
def hide():
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    return driver

def geturl(i):
    driver = hide()
    driver.get(i[0])
    driver.get(i[1].replace(" ",""))

    getpic(i[1].replace("\n", ""))

    driver.close()


ls=get()
for i in ls:
    geturl(i)





