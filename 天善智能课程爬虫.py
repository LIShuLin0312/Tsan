import urllib.request
import re
for i in range(0,1000):
    thisurl="https://edu.hellobi.com/course/"+str(i+1)
    data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
    title_pat='<li class="active"(.*?)</li>'
    teacher_pat='class="lec-name">(.*?)<'
    price_pat='div class="course-price">.*?<sub>￥</sub>(.*?)</span>'
    title=re.compile(title_pat,re.S).findall(data)
    if(len(title)>0):
        title=title[0]
    else:
        continue
    teacher=re.compile(teacher_pat,re.S).findall(data)
    if(len(teacher)>0):
        teacher=teacher[0]
    else:
        teacher="缺失"
    price=re.compile(price_pat,re.S).findall(data)
    if(len(price)>0):
        price=price[0]
    else:
        price="免费"
    print(title)
    print(teacher)
    print(price)
    print("--------------")
