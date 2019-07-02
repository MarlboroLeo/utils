# coding=utf-8
# @Time    : 2019/7/2 15:27
# @Author  : Leau
# @File    : handle_gif_cap.py
from PIL import Image
import os


def gif_handle(gifFileName):
    # gifFileName = '3.gif'
    #使用Image模块的open()方法打开gif动态图像时，默认是第一帧
    im = Image.open(gifFileName)
    pngDir = gifFileName[:-4]
    #创建存放每帧图片的文件夹
    os.mkdir(pngDir)
    try:
      while True:
        #保存当前帧图片
        current = im.tell()
        im.save(pngDir+'/'+str(current)+'.png')
        #获取下一帧图片
        im.seek(current+1)
    except EOFError:
        pass

