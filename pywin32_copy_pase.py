# coding=utf-8
# @Time    : 2019/6/3 11:04
# @Author  : Leau
import win32api
import win32gui
import win32clipboard as wc
import win32con


def setCopy(str):
    # 写入剪切板内容
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_UNICODETEXT, str)
    wc.CloseClipboard()


def paste_str():
    # 粘贴
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)

    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    
if __name__ == '__main__':
    setCopy(r'E:\1.png')
    # hld = win32gui.GetForegroundWindow()
    # print(hld)
    sleep(1)
    paste_str()
