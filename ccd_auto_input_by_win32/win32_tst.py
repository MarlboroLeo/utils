# coding=utf-8
# @Time    : 2019/4/17 13:55
# @Author  : Leau
# @File    : win32_tst.py
import win32com.client
import time
from time import sleep

# loginurl = 'http://www.renren.com/SysHome.do'

# username = '用户名'
# password = '密码'

# ie = win32com.client.Dispatch("InternetExplorer.Application.1")  # 此电脑未注册
# ie = win32com.client.DispatchEx("{0002DF01-0000-0000-C000-000000000046}")
# w = win32com.client.Dispatch("Excel.Application")

# ie.Visible = 1 # 显示
#
# try:
#     ie.Navigate(loginurl)
#     state = ie.ReadyState
#     print(u"打开登陆页面")
#     while 1:
#         state = ie.ReadyState
#         if state == 4:
#             break
#         sleep(1)
#     print(u"页面载入完毕，输入用户名密码")
#     state = None
#
#     ie.Document.getElementById("email").value = username
#     ie.Document.getElementById("password").value = password
#     ie.Document.getElementById("login").click()
#
#     while 1:
#         state = ie.ReadyState
#         print(state)
#         if state == 4 and 'http://www.renren.com/你的人人ID' == str(ie.Document.URL):
#             break
#         sleep(1)
#
#     # sleep(4)
#     print(ie.Document.URL)
#     print(ie.Document.body.innerHTML)
#     # ie.Quit()
# except Exception as e:
#     ie.Quit()
#     print('err:', e)
#     pass
# import win32gui
#
# classname = "MozillaWindowClass"
# titlename = "百度一下，你就知道 - Internet Explorer"
# # 获取句柄
# # hwnd = win32gui.FindWindow(classname, titlename)
# hwnd = win32gui.FindWindow("IEFrame", titlename)
# print(hwnd)
# # 获取窗口左上角和右下角坐标
# left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# print(left,top,right,bottom)
# title = win32gui.GetWindowText(hwnd)
# print(title)

import win32api,win32gui,win32con,win32ui

label = '百度一下，你就知道 - Internet Explorer' #此处假设主窗口名为tt

hld = win32gui.FindWindow(None, label)
if hld > 0:

    dlg = win32gui.FindWindowEx(hld, None, 'Edit', None)#获取hld下第一个为edit控件的句柄

    buffer = '0' *50

    len = win32gui.SendMessage(dlg, win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度

    win32gui.SendMessage(dlg, win32con.WM_GETTEXT, len, buffer) #读取文本

    print(buffer[:len-1])

    #虚拟鼠标点击按钮(或者回车)

    btnhld = win32gui.FindWindowEx(hld, None,'Button', None)

    # win32gui.PostMessage(btnhld, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    # win32gui.PostMessage(btnhld, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    win32gui.PostMessage(btnhld, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)

    win32gui.PostMessage(btnhld, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    #获取显示器屏幕大小

    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)

    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    print(width, height)

#点击窗口button
# w=win32ui.FindWindow(clsname,windowtitle)
# b=w.GetDlgItem(窗口id)
# b.postMessage(win32con.BM_CLICK)


#关闭窗体
# import win32ui
# import win32con
# wnd=win32ui.FindWindow(classname,None)
# wnd.SendMessage(win32con.WM_CLOSE)  # 成功！