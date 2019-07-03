from bs4 import  BeautifulSoup
soup = BeautifulSoup(open("index.html"))
tag = soup.b
#Tag
print(type(tag))
#Name
print(tag.name)
#Attributes
print(tag['class'])
print(tag.attrs)

#可以遍历的字符串
print(tag.string)