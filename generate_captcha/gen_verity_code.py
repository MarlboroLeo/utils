# coding=utf-8
# @Time    : 2019/6/3 14:34
# @Author  : Leau
# @File    : gen_verity_code.py
import random


class GenVerifyCode(object):
    """生成随机验证码"""

    def __init__(self):
        self.veri_list = []

    def A_str(self):
        """取随机大写字母A-Z"""
        for i in range(4):
            veri_num1 = random.randint(65, 90)  # 取值65-90随机一个整数
            veri_str1 = chr(veri_num1)
            self.veri_list.append(veri_str1)

    def a_str(self):
        """取随机小写字母a-z"""
        for i in range(4):
            veri_num2 = random.randint(97, 122)  # 取值98-122随机一个整数
            veri_str2 = chr(veri_num2)  # 转换小写字母a-z的随机
            self.veri_list.append(veri_str2)

    def num_1(self):
        """取随机数字0-9"""
        for i in range(4):
            veri_num3 = random.randint(48, 57)
            veri_str3 = chr(veri_num3)
            self.veri_list.append(veri_str3)

    def main(self):
        """主函数"""
        # A_str()
        self.a_str()
        self.num_1()
        veri_res = random.sample(self.veri_list, 4)
        # print(veri_res)
        # print(self.veri_list)
        # print(''.join(veri_res))
        return ''.join(veri_res)


if __name__ == '__main__':
    veri = GenVerifyCode()
    print(veri.main())
