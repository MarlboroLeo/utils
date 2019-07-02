# coding=utf-8
# @Time    : 2019/6/12 16:32
# @Author  : Leau
# @File    : xici.py
import requests,random
from lxml import etree
import threading
import time

angents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

def get_all_xici_urls(start_num,stop_num):
    xici_urls = []
    for num in range(start_num,stop_num+1):
        xici_http_url = 'http://www.xicidaili.com/wn/'
        xici_http_url += str(num)
        xici_urls.append(xici_http_url)
    print('获取所有待爬取xici url 已完成...')
    return xici_urls
def get_all_http_ip(xici_http_url,headers,proxies_list):
    try:
        all_ip_xpath = '//table//tr/child::*[2]/text()'
        all_prot_xpath = '//table//tr/child::*[3]/text()'
        response = requests.get(url=xici_http_url,headers=headers)
        html_tree = etree.HTML(response.text)
        ip_list = html_tree.xpath(all_ip_xpath)
        port_list = html_tree.xpath(all_prot_xpath)
        # print(ip_list)
        # print(prot_list)
        new_proxies_list = []
        for index in range(1,len(ip_list)):
            # print('http://{}:{}'.format(ip_list[index],port_list[index]))
            proxies_dict = {}
            proxies_dict['https'] = 'https://{}:{}'.format(str(ip_list[index]),str(port_list[index]))
            new_proxies_list.append(proxies_dict)
        proxies_list += new_proxies_list
        return proxies_list
    except Exception as e:
        print('发生了错误：url为 ',xici_http_url,'错误为 ',e)

if __name__ == '__main__':
    start_num = int(input('请输入起始页面：').strip())
    stop_num = int(input('请输入结束页面：').strip())
    print('开始爬取...')
    t_list = []
    # 容纳需要使用的西刺代理ip
    proxies_list = []
    # 使用多线程
    xici_urls = get_all_xici_urls(start_num,stop_num)
    for xici_get_url in xici_urls:
        #随机筛选一个useragent
        headers = {'User-Agent': random.choice(angents)}
        t = threading.Thread(target=get_all_http_ip, args=(xici_get_url, headers, proxies_list))
        t_list.append(t)
    for j in t_list:
        j.start()
        j.join()
    print('所有需要的代理ip已爬取完成...')
    print(proxies_list)
    print(len(proxies_list))
