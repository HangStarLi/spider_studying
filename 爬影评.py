import requests
from bs4 import BeautifulSoup
import time
import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plot

def getHtml(url):
    try:
        r = requests.get(url,headers={'Userr-Agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("filed")

f = open("movieComment.txt",'wb+')
def getData(html):
    soup = BeautifulSoup(html,"html.parser")
    comment_list = soup.find('div',attrs={'class':'mod-bd'})
    for comment in comment_list.find_all('div',attrs={'class':'comment-item'}):
        comment_content = comment.find('span',attrs={'class':'short'}).get_text()
        f.write(comment_content.encode("utf-8"))



def wordcloud():
    image = Image.open("03.jpg",'r')
    img = np.array(image)
    cut_text = open("movieComment.txt",'r',encoding="utf-8").read()
    wordcloud = WordCloud(
        mask=img,
        height=2000,
        width=4000,
        background_color='white',
        max_words=1000,
        max_font_size=400,
        font_path="C:\Windows\Fonts\msyh.ttc",

    ).generate(cut_text)

    plot.imshow(wordcloud,interpolation='bilinear')
    plot.axis('off')
    plot.show()
    #plot.savefig('wc1.jpg')
if __name__ == '__main__':
    k = 0
    i = 0
    while k<200:
        url = 'https://movie.douban.com/subject/26752088/comments?start=' + str(k) +'&limit=20&sort=new_score&status=P'
        k+=20
        i+=1
        print("正在爬取第"+str(i)+"页的数据")
        html = getHtml(url)
        getData(html)
    wordcloud()
