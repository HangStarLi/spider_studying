html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')

#以b开头
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

#列表，找到所有的a和b标签
print(soup.find_all(['a','b']))

#True可以匹配任何值，下面的代码查找所有的tag,但不返回字符串节点
for tag in soup.find_all(True):
    print(tag.string)

#方法

#find_all
soup.find_all('title')
soup.find_all("p","tilte")
soup.find_all("a")
soup.find_all(id="link2")

print(soup.find(string=re.compile('story')))
soup.find_all(href=re.compile('elsie'))

#使用多个指定名字的参数可以同时过滤tag的多个属性
soup.find_all(href = re.compile("elsie"),id='link1')

soup.find_all(attrs = {'data-foo':'value'})

print("_______________按CSS搜索__________________")
print(soup.find_all('a', class_='sister'))
soup.find_all(class_=re.compile('itl'))
#完全匹配class的值时，如果CSS的类名的顺序与实际不符，将搜索不到结果

print("==============string参数===============")
#通过string参数可以搜索文档中的字符串类容
print(soup.find_all(string='Elsie'))
print(soup.find_all(string=['Elsie','Lacie']))
soup.find_all(string = re.compile("Dormouse"))

print("-----------------limit参数-----------------")
#find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
soup.find_all('a',limit=2)

print('___________________像调用find_all()一样调用tag_______________________')
soup.find_all('a')
#等价于
soup("a")

soup.title.find_all(string=True)
soup.title(string=True)


print("______________CSS选择器________________")
print(soup.select('title'))
print(soup.select("p:nth-of-type(3)"))
#通过tag标签逐层查找
soup.select("body a")

#找到某个tag标签下的直接子标签
soup.select('head > title')
soup.select("p > #link1")

#找到兄弟节点标签
soup.select("#link1 ~ .sister")

#通过CSS的类名查找
soup.select(".sister")
soup.select("[class~=sister]")

#通过id查找：
soup.select("#link1")
soup.select("a#link2")

#同时用多种CSS选择器查询
soup.select("#link1,#link2")

#通过是否存在某个属性来查找
soup.select('a[href]')

#



