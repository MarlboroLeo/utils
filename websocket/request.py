# coding=utf-8
# @Time    : 2019/7/2 15:14
# @Author  : Leau
# @File    : request.py
import websocket

url = 'ws://127.0.0.1:9527/ws'
ws = websocket.create_connection(url)
while True:
    print(ws.recv())
