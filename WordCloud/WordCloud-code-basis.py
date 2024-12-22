# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup
from bs4 import BeautifulSoup

# 使用import导入jieba模块
import jieba
from pyecharts.charts import WordCloud

url = "https://nocturne-spider.baicizhan.com/2020/09/02/coco/"

headers = {"Uear-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

response = requests.get(url, headers=headers)

html = response.text

soup = BeautifulSoup(html, "lxml")

content_all = soup.find_all(name="em")

wordList = []

for content in content_all:
    contentString = content.string
    words = jieba.lcut(contentString)
    wordList = wordList + words
    
wordDict = {}

for word in wordList:
    if len(word)>1:
        if word not in wordDict.keys():
            wordDict[word] = 1
        else:
            wordDict[word] +=1
wordCloud = WordCloud()

wordCloud.add(series_name = "", data_pair = wordDict.items(), width = 800, height = 500, word_size_range = [30,70])

wordCloud.render("dream.html")

print("success")
