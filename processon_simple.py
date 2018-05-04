import random
import string
import re
import time
import requests
import datetime
#打印日志
import logging
#设置日志等级
logging.basicConfig(filename='example.log', filemode="a", level=logging.INFO)

#输入你的邀请链接
url = ''
#你需要的邀请数量
max_num = 50
num = 0
#初始化参数序列
init_num = 1

year = str(datetime.datetime.now().year)
month = str(datetime.datetime.now().month)
day = str(datetime.datetime.now().day)
def getuser(i):
    id = str(i)
    user = ''+year+month+day+id+'-'.join(random.sample(string.ascii_letters + string.digits, 4))

    return user


def getdomain():
    domain = '@yopmail.com'

    return domain

def po(user, domain, url):
    ss_po = requests.Session()
    ss_po.get(url)

    fullname = ''.join(random.sample(string.ascii_letters + string.digits, 14))
    password = '123456'

    processon = {
        'email': user + domain,
        'pass': password,
        'fullname': fullname
    }
    rsp_po = ss_po.post('https://www.processon.com/signup/submit', data=processon)

    fmt = "\nemail: {}\npassword: {}"
    print(fmt.format(processon.get('email'), password))
    logging.info(fmt.format(processon.get('email'),password))
if __name__ == "__main__":

    while num < max_num:
        user = getuser(init_num)
        domain = getdomain()
        time.sleep(5)
        po(user, domain, url)
        init_num += 1
        num += 1
