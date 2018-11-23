#淘宝商品图片爬虫
import urllib.request
import re
keyname="春季裙"
key=urllib.request.quote(keyname)
for i in range(1,101):
    try:
        print("--------正在爬第"+str(i)+"页------------")
        url="https://s.taobao.com/search?q="+key+"&s="+str((i-1)*44)
        data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
        pat='"pic_url":"//(.*?)"'
        imglist=re.compile(pat).findall(data)
        for j in range(0,len(imglist)):
            try:
                thisimg=imglist[j]
                thisimgurl="http://"+thisimg
                localfile="D:/我的教学/Python/天善智能-爬虫/3/图片数据/"+str(i)+"_"+str(j)+".jpg"
                urllib.request.urlretrieve(thisimgurl,filename=localfile)
            except Exception as err:
                pass
    except Exception as err:
        pass
