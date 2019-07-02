# coding=utf-8
# @Time    : 2019/5/27 9:10
# @Author  : Leau
# @File    : gen_cap.py
# 导入random模块
import random

# 导入Image,ImageDraw,ImageFont模块
from PIL import Image, ImageDraw, ImageFont

# 定义使用Image类实例化一个长为120px,宽为30px,基于RGB的(255,255,255)颜色的图片
img1 = Image.new(mode="RGB", size=(58, 18), color=(200, 200, 200))

# 实例化一支画笔
draw1 = ImageDraw.Draw(img1, mode="RGB")

# 定义要使用的字体
# font1 = ImageFont.truetype("One Chance.ttf", 28)
font1 = ImageFont.truetype("msjhbd.ttc", size=20)

for i in range(4):
    # 每循环一次,从a到z中随机生成一个字母或数字
    # 65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
    # str把生成的数字转换成字符串
    char1 = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])

    # 每循环一次重新生成随机颜色
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 画线
    # 第一个括号里面的参数是坐标,前两个数为开始坐标,后两个数为结束坐标
    # 括号里的第二个参数指定颜色,可以直接指定,也可以用RGB来表示颜色
    draw1.line((0, 0, 10, 10), fill="red")
    draw1.line((5, 5, 15, 18), fill="blue")

    # 把生成的字母或数字添加到图片上
    # 图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
    draw1.text([i * 15, -4], char1, color1, font1)

# # 把生成的图片保存为"pic.png"格式
# with open("pic.png", "wb") as f:
#     img1.save(f, format="png")

img1.show()