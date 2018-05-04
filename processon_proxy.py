import random
import string
import re
import time
import requests

import proxy
# this is a simple example
import logging
# define the log file, file mode and logging level
logging.basicConfig(filename='example.log', filemode="a", level=logging.DEBUG)
max_num = 51;
url = 'https://www.processon.com/i/593f9a35e4b04d4c799be64d';
proxies = {'http': 'HTTP://101.81.141.175:9999', 'https': 'HTTP://101.81.141.175:9999',}
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


def po(user, domain, proxies, url):

    ss_po = requests.Session()
    ss_po.get(url, proxies=proxies)

    fullname = ''.join(random.sample(string.ascii_letters + string.digits, 14))
    password = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    processon = {"email": user + domain, "pass": password, "fullname": fullname}

    rsp_po = ss_po.post(
        "https://www.processon.com/signup/submit", data=processon, proxies=proxies
    )

    fmt = "\nemail: {}\npassword: {}\nnickname: {}\n"
    print(fmt.format(processon.get("email"), password, fullname))


def mail(user, domain,proxies):

    ss_mail = requests.Session()
    rsp_get = ss_mail.get("https://temp-mail.org/zh/option/change/", proxies=proxies)
    csrf = re.findall(r'name="csrf" value="(\w+)', rsp_get.text)[0]

    tempmail = {"csrf": csrf, "mail": user, "domain": domain}

    ss_mail.post("https://temp-mail.org/zh/option/change/", data=tempmail, proxies=proxies)

    rsp_refresh = ss_mail.get("https://temp-mail.org/zh/option/refresh/", proxies=proxies)
    url_box = re.findall(r"https://temp-mail.org/zh/view/\w+", rsp_refresh.text)
    while url_box == []:
        print('wait...')
#        time.sleep(1)
        rsp_refresh = ss_mail.get("https://temp-mail.org/zh/option/refresh/", proxies=proxies)
        url_box = re.findall(r"https://temp-mail.org/zh/view/\w+", rsp_refresh.text)

    rsp_message = ss_mail.get(url_box[0], proxies=proxies)
    url_verify = re.findall(
        r"https://www.processon.com/signup/verification/\w+", rsp_message.text
    )[
        0
    ]
    rsp_verify = ss_mail.get(url_verify)

    global num

    if rsp_verify.status_code == 200:
        num += 1
        print("Number of successes: {}".format(num))


num = 0

if __name__ == "__main__":

    while num <= max_num:
        user = getuser()
        domain = getdomain()
        print(proxies)
#        proxies = proxy.get()
#        print(proxies)
        po(user, domain, proxies, url)
        mail(user, domain,proxies)
        print('Surplus:',max_num - num,' count *3')