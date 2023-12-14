from time import sleep
from PySide6.QtWidgets import QDialog


def loading_dialog(fun):
    def inner():
        progress_dialog = QDialog()
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setWindowTitle('加载工作场景...')
        progress_dialog.setLabelText('稍等...')
        progress_dialog.setCancelButton(None)  # 禁用取消按钮
        progress_dialog.setWindowFlags(progress_dialog.windowFlags() | Qt.WindowStaysOnTopHint)
        progress_dialog.exec()
        fun()
        progress_dialog.close()


@loading_dialog
def test():
    print("进来了")
    sleep(2)
    print("出来了")


test()