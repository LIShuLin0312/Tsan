import urllib.request
#爬到内存中-方法1
data=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8","ignore")

#爬虫内存中-方法2
url="http://www.baidu.com"
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read().decode("utf-8","ignore")

#爬到硬盘中
urllib.request.urlretrieve(url,filename="D:/我的教学/Python/天善智能-爬虫/2/baidu.html")

#拿到状态码
file=urllib.request.urlopen("http://www.baidu.com")
print(file.getcode())
