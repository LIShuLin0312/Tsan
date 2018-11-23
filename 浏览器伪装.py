import urllib.request
url="https://www.qiushibaike.com/"
#头文件格式header=("User-Agent",具体用户代理值)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()

import urllib.request
url="https://www.qiushibaike.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Content-Type":"application/javascript",
         }
opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)

opener.addheaders=headall
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()

import urllib.request
url="https://www.qiushibaike.com/"
req0 = urllib.request.Request(url)
req0.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req0data=urllib.request.urlopen(req0).read().decode("utf-8","ignore")

