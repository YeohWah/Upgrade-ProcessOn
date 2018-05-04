import requests
import proxy

proxies=proxy.get()
print(proxies)
rsp = requests.get('https://www.baidu.com/', proxies=proxies)
print(rsp.status_code)
