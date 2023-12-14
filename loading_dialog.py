from PySide6 import QtWidgets
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication

from ui.loading_dialog import Ui_LoadingDialog


class LoadingDialogWin(QtWidgets.QDialog, Ui_LoadingDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # def decorate(self, fun):
    #     def inner():
    #         self.show()
    #         fun()
    #         self.close()
    #         return inner


def load_hint(dialog):  # 这样做需要在调用此装饰器的时候传入参口（属于传参装饰器）
        def inner(fun):
            def wrapper():
                dialog.show()
                # 强制处理完当前事务，再向下执行
                QCoreApplication.processEvents()
                fun()
                dialog.close()
            return wrapper
        return inner
        

# def load_hint(fun):
#         dialog = LoadingDialogWin()
#         def wrapper():
#             dialog.show()
#             # 强制处理完当前事务，再向下执行。否则窗口可能加载未完成就往下执行。
#             QCoreApplication.processEvents()
#             fun()
#             dialog.close()
#         return wrapper
