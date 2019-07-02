# coding=utf-8
# @Time    : 2019/7/2 15:03
# @Author  : Leau
# @File    : extra_pdf_from_zip.py
import io
import zipfile


def extra_pdf(self, data):
    """
    从zip中提取pdf
    :param data:  zip二进制
    :return: pdf 二进制
    """
    if data is None:
        return None
    z = zipfile.ZipFile(io.BytesIO(data))
    # print(z.namelist())
    name = None
    for names in z.namelist():
        name1 = re.match(r'[\d^]+\.pdf$', names)
        if name1:
            name = name1.group()
            break
        else:
            continue
    # print(name)
    if name is None:
        print("检查zip中pdf名称匹配规则")
        return None
    pwd1 = self.identify_no[-6:].encode('utf-8')
    pwd2 = pwd1.replace(b"O", b"0")
    pwd_list = [pwd1, pwd2, self.identify_no.encode('utf-8')]
    for pwd in pwd_list:
        try:
            try:
                foo = z.read(z.namelist()[0], pwd=pwd)
                if len(foo) < 1024:
                    return None
                return foo
            except RuntimeError:
                continue
        except Exception as e:
            print("zip提取pdf error：", e)
            return None
    return None