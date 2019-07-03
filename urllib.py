import urllib.request
file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
dataline = file.readline()
fhandle = open('./1.html','wb')
fhandle.write(data)
fhandle.close()

print("+++++++++浏览器模式+++++++++")
import urllib.request
import urllib.parse
url = 'http://www.baidu.com'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request).read()
fhadle = open('./baidu.html','wb')
fhadle.write(response)
fhadle.close()


print("++++++++++++代理服务器设置+++++++++++")
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr = '61.163.39.70:9999'
data = use_proxy(proxy_addr,'http://www.baidu.com')
