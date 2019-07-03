from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba

#分词
def trans_CN(text):
    word_list = jieba.cut(text)
    result = " ".join(word_list)
    return result

with open("textfile.txt",'r',encoding='utf-8') as f:
    text = f.read()
    text = trans_CN(text)
    mask = np.array(image.open("./03.jpg"))
    wordcloud = WordCloud(
        mask=mask,
        font_path="C:\Windows\Fonts\STXINGKA.TTF"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()