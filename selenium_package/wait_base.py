# coding=utf-8
# @Time    : 2019/4/16 11:19
# @Author  : Leau
# @File    : wait_base.py


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from.wait_base_settings import sleep, NC
# from .settings import (BASEDIR, MONTH, NC, UsError, json, os, sleep)


class Base(object):
    """ 浏览器基类, 保持同一个 driver """

    def __init__(self):
        # 设置 chrome_options 属性
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--log-level=3')
        # 设置代理
        # self.chrome_options.add_argument('--proxy-server=http://127.0.0.1:1080')
        # 设置浏览器窗口大小
        # self.chrome_options.add_argument('window-size=800x3000')
        # 设置全屏
        self.chrome_options.add_argument('--start-mixminzed')
        self.driver = webdriver.Chrome(
            executable_path= 'chromedriver', chrome_options=self.chrome_options)
        # 设置隐性等待时间, timeout = 20
        self.driver.implicitly_wait(20)
        # self.driver.maximize_window()
        # 设置显性等待时间, timeout = 10, 间隔 0.2s 检查一次
        self.wait = WebDriverWait(self.driver, 20, 0.2, "请求超时")

    def Wait(self, idName=None, text=None, xpath=None, css=None):
        """
        设置显性等待，每0.3s检查一次
        :param idName:默认
        :param text:需发送的信息（非NC --> 'noclick'）
        :param xpath:
        :param css:
        :return:
        """
        if idName:
            locator = ('id', idName)
        elif xpath:
            locator = ('xpath', xpath)
        elif css:
            locator = ('css', css)

        try:
            element = self.wait.until(EC.presence_of_all_elements_located(locator))
            if not text and not element.is_selected():
                element.click()
            elif text and text != NC:
                try:
                    element.clear()
                except Exception:
                    pass
                finally:
                    element.send_keys(text)
            try:
                return element
            except Exception:
                pass

        except Exception as e:
            print(f"{e}\n{locator[0]}:{locator[1]}\n" +
                  f"value:{text if text and text != NC else 'None'}\n\n")

    def choiceSelect(self, selectId=None, value=None, t=0.2):
        """
        下拉选择器， 根据value选择
        :param selectId:
        :param value:
        :param t:
        :return:
        """
        sleep(t)
        try:
            element = Select(self.Wait(selectId, text=NC))
            element.select_by_index(value)
        except Exception as e:
            print(f"{e}\nidName:{selectId}\nvalue: {value}\n\n")

        return 0

