# coding=utf-8
# @Time    : 2019/4/17 13:37
# @Author  : Leau
# @File    : auto_input.py
import time
from ctypes import windll

import win32api
import win32gui
import win32clipboard as wc
import win32con


def get_handle():
    # 获取窗口句柄，标题，大小
    # 返回上下左右坐标

    # classname = "MozillaWindowClass"
    classname = "IEFrame"
    titlename = "百度一下，你就知道 - Internet Explorer"
    # 获取句柄
    # hwnd = win32gui.FindWindow(classname, titlename)
    hwnd = win32gui.FindWindow(classname, titlename)
    print(hwnd)
    # 检查窗口是否最小化，如果是最大化
    # if win32gui.IsIconic(hwnd):
    #         # win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    #     win32gui.ShowWindow(hwnd, 8)
    # else:
    win32gui.ShowWindow(hwnd, 3)
    time.sleep(0.5)
    # 获取窗口左上角和右下角坐标
    left, top, right, buttom = win32gui.GetWindowRect(hwnd)
    print(left, top, right, buttom)
    title = win32gui.GetWindowText(hwnd)
    print(title)
    return left, right, top, buttom,

# 获取剪切板内容
def getCopy():
    wc.OpenClipboard()
    t = wc.GetClipboardData(win32con.CF_UNICODETEXT)
    wc.CloseClipboard()
    return t

def split_clip_str(str):
    # 切割从剪切板中提取的字符串
    li = str.split(",")
    username = li[0]
    password = li[1]
    return username, password

# 写入剪切板内容
def setCopy(str):
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_UNICODETEXT, str)
    wc.CloseClipboard()

def paste_str():
    # 粘贴
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x11,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(0x56,0,win32con.KEYEVENTF_KEYUP,0)


def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)


def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def run():
    setCopy("中文English,123456")
    clip_str = getCopy()
    print(clip_str)
    username, password = split_clip_str(clip_str)
    print(username + "\n" + password)
    # print(getCopy())
    left, right, top, buttom = get_handle()
    mouse_click(left+512, top+358)  # 点击搜索栏 512，358
    paste_str()
    # mouse_click()


if __name__ == '__main__':
    run()
    # get_handle()