# coding=utf-8
# @Time    : 2019/5/21 18:08
# @Author  : Leau
# @File    : spider_main.py

from models import DuBang, SunShine, TianPing, TaiPingyang, DaDi
from .auto_transfer_json_from_sql import to_json
from .dbic_spider import DbicSpider
from .sunshine_spider import SunshineSpider
from .tianping_spider import TPSpider
from .tpy_spider import TpySpider
from .picc_spider import PICCSpider
from .dadi_spider import DaDiSpider

MODEL_DICT = {
    '都邦': DuBang,
    '阳光': SunShine,
    '天平': TianPing,
    '太平洋': TaiPingyang,
    '大地': DaDi
}


def judge(msg, insur_type, policy_no):
    """判断"""
    print(policy_no, insur_type, msg)
    if msg == 'not find':
        return {"status": "2", "msg": "not find"}
    elif msg == 'error':
        return {"status": "3", "msg": "error"}
    elif msg == 'finish':
        data = to_json(MODEL_DICT.get(insur_type), policy_no)
        return {"status": "1", "msg": "success", "data": data}
    else:
        return {"status": "4", "msg": "other error"}


def main(policy_no, card_no, identify_no, frame_no, compulsory, insur_type):
    """爬虫程序API入口"""
    if insur_type == '都邦':
        db = DbicSpider(policy_no, card_no)
        msg = db.main()
        return judge(msg, insur_type, policy_no)
    elif insur_type == '阳光':
        sun = SunshineSpider(policy_no, card_no, compulsory)
        msg = sun.main()
        return judge(msg, insur_type, policy_no)
    elif insur_type == '天平':
        tp = TPSpider(policy_no, card_no, identify_no, compulsory)
        msg = tp.main()
        return judge(msg, insur_type, policy_no)
    elif insur_type == '太平洋':
        tpy = TpySpider(policy_no, identify_no, card_no, frame_no)
        msg = tpy.main()
        return judge(msg, insur_type, policy_no)
    elif insur_type == '人民':
        picc = PICCSpider(policy_no, card_no)
        msg = picc.main()
        return judge(msg, insur_type, policy_no)
    elif insur_type == '大地':
        dadi = DaDiSpider(policy_no, card_no, compulsory)
        msg = dadi.main()
        return judge(msg, insur_type, policy_no)
