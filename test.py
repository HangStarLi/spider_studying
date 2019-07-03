import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'https://music.163.com/#/song?id=571338279'
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('span',class_='short')
    print(html)