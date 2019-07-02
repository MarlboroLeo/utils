# coding=utf-8
# @Time    : 2019/7/2 15:01
# @Author  : Leau
# @File    : extra_words_from_pdf.py
import pdfplumber  # pdfplumber


def extra_special_promise(self):
    """从pdf提取特别约定等信息"""
    # with pdfplumber.open("../ASHJ052Y1419B000715G.pdf") as pdf:  # 测试
    assured_cer, special_promise, self.compulsory, self.tax = None, None, None, None
    with pdfplumber.open("/usr/local/spider/bx_spider/tpy_pdf/{}.pdf".format(self.policy_no)) as pdf:
        # with pdfplumber.open("./bx_spider/tpy_pdf/{}.pdf".format(self.policy_no)) as pdf:
        pages = pdf.pages
        # print(page)
        for page in pages:
            text = page.extract_text()
            if re.search(r'机动车交通事故责任强制保险单', text):
                self.compulsory = re.search(r'保险费合计.*?([\.\d]{6,7}) 元\)', text).group(1)
                self.tax = re.search(r'船 合计.*?([\.\d]{5,7}) 元\)', text).group(1)
                continue
            elif re.search(r'神行车保机动车保险单', text):
                special_promise = re.search(r'特别约定：([\s\S]*?)无其它特', text).group(1)
                assured_cer = re.search(r'（团体客户代码）.*?([A-Z\d]*)\n', text).group(1)
        return assured_cer, special_promise, self.compulsory, self.tax