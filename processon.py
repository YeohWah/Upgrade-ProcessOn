import random
import string
import re
import time
import requests
import argparse
#打印日志
import logging
#设置日志等级
logging.basicConfig(filename='example.log', filemode="a", level=logging.DEBUG)

#输入你的邀请链接
url = ''
#你需要的邀请数量
max_num = 50


def getuser():

    user = ''.join(random.sample(string.ascii_letters + string.digits, 20))

    return user


def getdomain():
    domains = [
        "@aditus.info",
        "@storiqax.com",
        "@air2token.com",
        "@b2bx.net",
        "@stelliteop.info",
        "@bitwhites.top",
        "@ethersportz.info",
        "@2odem.com",
        "@storiqax.top",
        "@gifto12.com",
    ]


    domain = random.choice(domains)

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


def mail(user, domain):

    ss_mail = requests.Session()
    rsp_get = ss_mail.get("https://temp-mail.org/zh/option/change/")
    csrf = re.findall(r'name="csrf" value="(\w+)', rsp_get.text)[0]

    tempmail = {"csrf": csrf, "mail": user, "domain": domain}

    ss_mail.post("https://temp-mail.org/zh/option/change/", data=tempmail)

    rsp_refresh = ss_mail.get("https://temp-mail.org/zh/option/refresh/")
    url_box = re.findall(r"https://temp-mail.org/zh/view/\w+", rsp_refresh.text)
    while url_box == []:
        time.sleep(1)
        print('wait...')
        rsp_refresh = ss_mail.get("https://temp-mail.org/zh/option/refresh/")
        url_box = re.findall(r"https://temp-mail.org/zh/view/\w+", rsp_refresh.text)

    rsp_message = ss_mail.get(url_box[0])
    url_verify = re.findall(
        r"https://www.processon.com/signup/verification/\w+", rsp_message.text
    )[0]
    rsp_verify = ss_mail.get(url_verify)

    global num

    if rsp_verify.status_code == 200:
        num += 1
        print("Number of successes：{}".format(num))


num = 0

if __name__ == "__main__":

    while num <= max_num:
        user = getuser()
        domain = getdomain()
        po(user, domain, url)
        mail(user, domain)
