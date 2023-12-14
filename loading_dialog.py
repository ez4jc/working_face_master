from PySide6 import QtWidgets

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