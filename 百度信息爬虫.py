import urllib.requesturl="http://www.baidu.com/s?wd="key="马蹄糕"#对关键词进行编码，因为URL中需要对中文等进行处理key_code=urllib.request.quote(key)#带检索关键词的urlurl_key=url+key_code+"&ie=utf-8"#通过for循环爬取各页信息，这里爬取1到10页for i in range(0,10):    print("正在爬取"+str(i+1)+"页数据")    #根据刚刚总结的url规律构造当前url    thisurl=url_key+"&pn="+str(i*10)    #爬取这一页的数据    data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")    #成功得到数据    #根据正则表达式将爬到的网页列表中各网页标题进行提取    import re    pat='"title":"(.*?)"'    rst=re.compile(pat,re.S).findall(data)    #将各标题信息通过循环遍历输出    for j in range(0,len(rst)):        print("第"+str(j)+"条网页标题是:"+str(rst[j]))        print("-----------")