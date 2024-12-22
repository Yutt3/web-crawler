import requests
from bs4 import BeautifulSoup
import jieba
from pyecharts.charts import WordCloud

# Assign the website link to the url
url = "https://nocturne-spider.baicizhan.com/2020/09/02/coco/"

# Assign User-Agent as a dict. key pair to headers. This is necessary because we need to disguise our identity to prevent the site from realizing we're crawling.
# The value of this key 可以由"F12"的检查功能获得
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

# Add the url and headers parameters to requests.get(), pass the dictionary headers to the headers parameter, and assign it to response.
response = requests.get(url, headers=headers)

# Convert the server response into a string and assign it to html
html = response.text

# Use BeautifulSoup() to pass in the variable html and the parser lxml, assign it to soup
soup = BeautifulSoup(html, "lxml")

# Use find_all() to query for name=“em” in soup and assign them to content_all.
# name="em" can be checked by pressing "F12" on a website. 
# if we want to find "class", we need to use "class_".
content_all = soup.find_all(name="em")

# Create a blank list wordList, 目的是为了计入所有字词
wordList = []

# for loop content_all, content_all is a list.
for content in content_all:
    # 获取每个节点中标签内容，赋值给contentString
    contentString = content.string
    # 使用jieba.lcut()将contentString(中文句子)进行分词分割，赋值给words
    words = jieba.lcut(contentString)
    # 通过list + list可以合并列表的特性，将列表wordList和列表words进行累加
    wordList = wordList + words

# 创建一个空白字典wordDict, 目的是为了统计字词出现的频率
wordDict = {}
# for loop 之前创建的wordList；是计入了所有字词的列表，且它已经由jieba.lcut完成分割.
for word in wordList:
    #设置了一个条件，只有字词长度大于1的，才会被记入Dictionary. 
    if len(word)>1:
        #当Dictionary中还没有此key时，使用Dict添加法，添加此key和设定新的它的value
        if word not in wordDict.keys():
            wordDict[word] = 1
        #当Dictionary中已有此key时，把此key的value加1，以达到统计的目的.
        else:
            wordDict[word] +=1

# 创建WordCloud对象，赋值给wordCloud
wordCloud = WordCloud()

# 对创建的WordCloud对象进行操作，调用 add() 函数设置 series_name的值为空；data_pair 的值为字典 wordDict 转换成由元组组成的列表；将 word_size_range 的值设置为 [20, 80]。
# add() 函数可以设置词云图的内容，例如：展示文字，字体大小等。
# series_name指的是数据的统称，例如：降水量、蒸发量. series_name 为必须填入的参数，但可为空.
# data_pair 参数是指传入词云图中的数据，它的值的格式为：[(word1, count1), (word2, count2)], word为字词，count为字词的频率
# data_pair = wordDict.items()是调用了Dictionary的.items()功能，它将Dict中的每对 key 和 value 组成一个tuple，并把这些tuple放在list中返回。正好就是data_pair需要的格式。
# width和height是稍后出现的词云图的长宽.
# word_size_range是词云图中，字体大小范围，以list形式出现。30代表着词云图中频率最低的词语大小，70代表着词云图中频率最高的词语大小.
wordCloud.add(series_name = "", data_pair = wordDict.items(), width = 800, height = 500, word_size_range = [30,70])

# 使用wordCloud.render()存储文件，设置文件名为wordcloud.html，文件会保存在你代码所在的目录
wordCloud.render("dream.html")

# 使用print输出 success
print("success")
