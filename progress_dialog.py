from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QProgressDialog, QWidget
from PySide6.QtCore import Qt, QThread, Signal


class WorkerThread(QThread):
    update_progress = Signal(int)

    def run(self):
        for i in range(101):
            self.update_progress.emit(i)
            self.msleep(50)  # 模拟一些工作


class ProgressDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Progress Dialog Example')

        layout = QVBoxLayout()

        btn_show_dialog = QPushButton('Show Progress Dialog', self)
        btn_show_dialog.clicked.connect(self.show_progress_dialog)
        layout.addWidget(btn_show_dialog)

        self.setLayout(layout)

    def show_progress_dialog(self):
        progress_dialog = QProgressDialog(self)
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setWindowTitle('正在加载工作场景')
        progress_dialog.setLabelText('稍等...')
        progress_dialog.setCancelButton(None)  # 禁用取消按钮

        worker_thread = WorkerThread()
        worker_thread.update_progress.connect(progress_dialog.setValue)

        progress_dialog.canceled.connect(worker_thread.terminate)

        worker_thread.start()
        progress_dialog.exec()


if __name__ == '__main__':
    app = QApplication([])
    main_window = ProgressDialogExample()
    main_window.show()
    app.exec()
