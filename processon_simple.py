import random
import string
import re
import time
import requests
import datetime
#打印日志
import logging
#设置日志等级
logging.basicConfig(filename='example.log', filemode="w", level=logging.INFO)

#输入你的邀请链接
url = ''
#你需要的邀请数量
max_num = 50
num = 0
#初始化参数序列
init_num = 1


def getuser(i):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    user = ''+year+month+day+i

    return user


def getdomain():
    domain = '@yopmail.com'

    return domain

def po(user, domain, url):
    ss_po = requests.Session()
    ss_po.get(url)

    fullname = ''.join(random.sample(string.ascii_letters + string.digits, 14))
    password = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    processon = {
        'email': user + domain,
        'pass': password,
        'fullname': fullname
    }
    rsp_po = ss_po.post('https://www.processon.com/signup/submit', data=processon)

    fmt = "\nemail: {}\npassword: {}\nnickname: {}\n"
    print(fmt.format(processon.get('email'), password, fullname))
    logging.info(user)
if __name__ == "__main__":

    while num < max_num:
        user = getuser(init_num)
        domain = getdomain()
        po(user, domain, url)
        init_num += 1
        num += 1
