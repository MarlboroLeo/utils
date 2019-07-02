# coding=utf-8
# @Time    : 2019/7/2 14:54
# @Author  : Leau
# @File    : fateadm_example.py
from .fateadm_api import Captcha
signal = False
cap = None
for _ in range(10):
    if signal:
        Captcha(operating=4, rsp=cap)
    millis = int(round(time.time() * 1000))
    temp = baseN(millis, 36)
    cap_resp = self.s.get(self.cap_url.format(temp), headers=self.headers, proxies=self.proxy)
    cap = Captcha(operating=1, img_data=cap_resp.content, pred_type='50100')
    self.cap_num = cap.pred_rsp.value
    main_form = {
        'autoload': 'true',
        'policyNo': self.policy_no,
        'identifyNo': self.card_no,
        'j_captcha': self.cap_num,
        'code': self.cap_num,
        'currentPageIndex': '1',
        '_action': 'query'
    }
    main_resp = self.s.post(self.query_url, headers=self.headers, data=main_form, proxies=self.proxy)
    main_dict = json.loads(main_resp.text.replace("'", '"'))
    error = main_dict.get('err')
    result = main_dict.get('result')
    if result is None:
        if error == '对不起，图形验证码输入不正确！':
            signal = True
            print("captcha error")
            continue
        elif error == '保单信息查询失败！log:保单信息查询失败！log:查询不到保单！':
            return "not find"
        elif error == '请输入与保单相同的证件号！':
            # print('请输入与保单相同的证件号！')
            return "not find"
        else:
            print("错误信息变更为：", error)
            return "error"
    else:
        for item in result.get('items'):
            if item.get('policyNo') == self.policy_no:
                self.b_contractNo = item.get('contractNo')
            elif item.get('policyNo') == self.compulsory_no:
                self.c_contractNo = item.get('contractNo')
        return 'success'