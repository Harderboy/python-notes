import urllib.request

# 如果网页长时间未响应，系统判断超时，无法爬取
for i in range(1, 100):
    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.5)
        print(len(response.read().decode("utf-8")))
    except:
        print("超时，继续下一个爬取")
