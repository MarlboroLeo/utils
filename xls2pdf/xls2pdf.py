# coding=utf-8
# @Time    : 2019/6/19 10:48
# @Author  : Leau
# @File    : xls2pdf.py
try:
    import os,shutil    # shutil模块主要是用于拷贝文件

    os.chdir(r'./')
    from win32com.client import Dispatch, constants, gencache
    # if not os.path.exists('./pdf'):
    #     os.mkdir('./pdf')
except Exception as e:
    print(str(e))


def excel2Pdf(excelFile, pdfFile):
    try:
        print('Begin Excel Export ...')
        xlApp = Dispatch('Excel.Application')
        books = xlApp.Workbooks.Open(excelFile)
        books.ExportAsFixedFormat(0, pdfFile)
        print("pdfFile:", pdfFile)
        xlApp.Quit()
    except Exception as e:
        print(str(e))


def ExportExcel():
    try:
        excelFiles = [fn for fn in os.listdir('.') if fn.endswith(('.xls', '.xlsx'))]
        for excelFile in excelFiles:
            # print("excelFiles:",excelFiles)
            excelFile = os.path.abspath(excelFile)
            index = excelFile.rindex('.')
            pdfFile = excelFile[:index] + '.pdf'
            excel2Pdf(excelFile, pdfFile)
    except Exception as e:
        print(str(e))

def move_pdf():

    # 取得当前目录下的文件名称列表
    files_list = os.listdir('./')
    # 取得python脚本的名字
    # __file__是取得当前脚本路径,如果路径是“\anaconda3\python”这样的格式，则要使用“\\”做切分
    py_name = __file__.split('/')[-1]

    for file in files_list:
        # 如果是文件是当前执行的py脚本，则跳过
        if file == py_name:
            continue
        # 如果当前文件格式不是一个文件如“.”，则跳过
        if not os.path.isfile(file):
            continue

        # 取得当前文件名称的格式，（切分文件名，取最后的列表元素）
        file_type = file.split('.')[-1]
        # 如果没有某个格式的文件夹，则创建这个文件夹
        if not os.path.exists(file_type):
            os.mkdir(file_type)

        # 获取当前路径
        path = os.getcwd()
        # 获取分类文件夹路径
        subdir = os.path.join(path, '%s' % file_type)
        # 进入分类文件夹
        os.chdir(subdir)
        if os.path.exists(file):
            # 如果文件夹存在当前文件，则跳过
            continue
        else:
            # 返回之前文件夹进行归类
            os.chdir(path)
            # shutil.move(源文件，指定路径):递归移动一个文件
            shutil.move(file, file_type)


if __name__ == '__main__':
    print('-'*30)
    print('| 表格转换程序v1.0 |')
    print('-'*30)

    print('='*10, "开始导出", '='*10)
    ExportExcel()
    print('='*10, "导出完成", '='*10)
    print('='*10, '归类文件中', '='*10)
    move_pdf()
    print('='*10, '归类文件完成', '='*10)
    # 让程序停在这里等待回车键退出
    input('Please press enter key to exit ...')
