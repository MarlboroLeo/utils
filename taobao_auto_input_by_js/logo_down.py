# coding=utf-8
# @Time    : 2019/4/16 15:17
# @Author  : Leau
# @File    : logo_down.py

import requests

url = 'https://ibsbjstar.ccb.com.cn/P1StaRes/V6/STY1/CN/images/layout/index/icon/icon_jhzz.png'
headers = {
    'Referer': 'https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_10?SERVLET_NAME=B2CMainPlat_10&CCB_IBSVersion=V6&PT_STYLE=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
resp = requests.get(url, headers=headers)

with open('2.png', 'wb') as f:
    f.write(resp.content)