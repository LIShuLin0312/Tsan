import requests
import re
'''
请求方式:get、post、put…
参数：params、headers、proxies、cookies、data
'''
rsp=requests.get("https://www.hellobi.com/")
ck=requests.utils.dict_from_cookiejar(rsp.cookies)
title=re.compile("<title>(.*?)</title>",re.S).findall(rsp.text)
hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
px={"http":"http://127.0.0.1:8888",
    "https":"http://127.0.0.1:8888",}
rsp=requests.get("https://www.hellobi.com/",proxies=px,headers=hd,cookies=ck)
key={"wd":"韦玮",
     }
rsp=requests.get("http://www.baidu.com/s",headers=hd,cookies=ck,params=key)
title=re.compile("<title>(.*?)</title>",re.S).findall(rsp.text)

postdata={"name":"测试账号",
          "pass":"测试密码"}
rsp=requests.post("http://www.iqianyue.com/mypost/",data=postdata)
