#IP代理池构建的第一种方案(适合于代理IP稳定的情况)
import random
import urllib.request
ippools=[
    "114.230.216.106:31912",
    "49.85.12.116:30348",
    "118.255.255.201:808",
    "127.0.0.1:8888",
    ]
def ip(ippools):
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,5):
    try:
        ip(ippools)
        url="http://www.baidu.com/"
        data1=urllib.request.urlopen(url).read()
        data=data1.decode("utf-8","ignore")
        print(len(data))
        fh=open("D:/我的教学/Python/天善智能-爬虫/4/"+str(i)+".html","wb")
        fh.write(data1)
        fh.close()
    except Exception as err:
        print(err)
