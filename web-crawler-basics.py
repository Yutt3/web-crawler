# 使用import导入requests模块
import requests

# 从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup

# 将URL地址赋值给变量url
url = "https://nocturne-spider.baicizhan.com/2020/08/08/%E5%9F%9F%E5%90%8D/"

# 将变量url传入requests.get()，赋值给response
response = requests.get(url)

# 将服务器响应内容转换为字符串形式，赋值给html
html = response.text

# 使用BeautifulSoup()读取html，添加lxml解析器，赋值给soup
soup = BeautifulSoup(html, "lxml")

# 使用find_all()查询soup中h2节点，赋值给content_all
content_all = soup.find_all(name="h2")

# for循环遍历content_all
for content in content_all:

    # TODO 使用.string获取节点的内容，赋值给contentString. .string只能打印单<>节点内的东西，如果有多个节点嵌套，则会打印None.
    contentString = content.string 
    
    # TODO 使用print输出contentString
    print(contentString)

    # TODO 使用.text获取节点的内容，赋值给contentString. .text会打印<>节点内的纯文本内容。 
    contentString = content.text
    
    # TODO 使用print输出contentString
    print(contentString)
