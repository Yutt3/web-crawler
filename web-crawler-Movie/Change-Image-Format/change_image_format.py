# 此段代码理论上可以通过创建一个新的格式文件，然后用从新的二进制写入方法，将老图片的格式更改为新的格式。（注意，此方法还未经过复杂的检验，能否完美作为图片格式转换工具有待考究）
# 使用import导入requests模块
import requests

# 复制左侧的图片地址，赋值给变量url
url = "https://npbcz.files.wordpress.com/2020/09/4-1.jpg"

# 将 url 添加进requests.get()中，赋值给response
response = requests.get(url)

# 使用.content属性获取图片内容，并赋值给img
img = response.content

# 使用with...as语句配合open()以wb方式，打开名字为"math.png"的文件，并赋值给f 
with open("math.png","wb") as f:

    # 使用write()函数写入img
    f.write(img)
