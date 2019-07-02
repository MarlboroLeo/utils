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


class BaiduAuto(object):
    """百度自动搜索填写"""

    def __init__(self):
        self.hwnd = win32gui.FindWindow("IEFrame", "百度一下，你就知道 - Internet Explorer")

    def get_handle(self):
        # 获取窗口句柄，标题，大小
        # 返回上下左右坐标
        # 获取句柄
        win32gui.ShowWindow(self.hwnd, 3)
        time.sleep(0.5)
        # 获取窗口左上角和右下角坐标
        left, top, right, buttom = win32gui.GetWindowRect(self.hwnd)
        return left, right, top, buttom

    def getCopy(self):
        # 获取剪切板内容
        wc.OpenClipboard()
        t = wc.GetClipboardData(win32con.CF_UNICODETEXT)
        wc.CloseClipboard()
        return t

    def setCopy(self, str):
        # 写入剪切板内容
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardData(win32con.CF_UNICODETEXT, str)
        wc.CloseClipboard()

    def paste_str(self):
        # 粘贴
        win32api.keybd_event(0x11, 0, 0, 0)
        win32api.keybd_event(0x56, 0, 0, 0)
        win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)

    def mouse_move(self, x, y):
        windll.user32.SetCursorPos(x, y)

    def mouse_click(self, x=None, y=None):
        if not x is None and not y is None:
            self.mouse_move(x, y)
            time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def run(self):
        # setCopy("中文English,123456")
        clip_str = self.getCopy()
        print(clip_str)
        # print(getCopy())
        left, right, top, buttom = self.get_handle()
        self.mouse_click(left + 512, top + 358)  # 点击搜索栏 512，358
        self.paste_str()


if __name__ == '__main__':
    baidu = BaiduAuto()
    baidu.run()
