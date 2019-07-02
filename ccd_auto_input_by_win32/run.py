# coding=utf-8
# @Time    : 2019/4/17 17:10
# @Author  : Leau
# @File    : run.py
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from auto_input_ui import Ui_BaiduAutoInput
from auto_input_win32 import BaiduAuto


class Worker(QThread):
    finish_sin = pyqtSignal()

    def __init__(self):
        super(Worker, self).__init__()
        self.working = True
        self.baidu = BaiduAuto()

    def run(self):
        while self.working:
            self.baidu.run()
            self.working = False
        self.finish_sin.emit()

    def stop(self):
        self.working = False
        # self.quit()
        self.wait()

    def __del__(self):
        self.working = False
        self.wait()


class MainWidget(Ui_BaiduAutoInput, QWidget):
    stop_sin = pyqtSignal()

    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)
        # 连接开始按钮和槽函数
        self.pushButton.clicked.connect(self.slotStart)
        self.trriger = False

    def slotStart(self):
        if not self.trriger:
            self.trriger = True
            self.thread = Worker()
            self.thread.finish_sin.connect(self.finish)
            self.stop_sin.connect(self.thread.stop)
            self.thread.start()
        else:
            self.trriger = False
            self.stop_sin.emit()

    def slotAdd(self, file_inf):
        # 在列表控件中动态添加字符串条目
        self.textBrowser.append(file_inf)

    def finish(self):
        QMessageBox.question(self, '信息', '任务完成', QMessageBox.Ok)
        self.trriger = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())

