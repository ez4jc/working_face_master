import time

from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QProgressDialog
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class WorkerThread(QThread):
    update_progress = Signal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.interactor = parent

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            progress_value = int((i + 1) * 5)
            self.update_progress.emit(progress_value)


def noniterative_processBar(interactor: QVTKRenderWindowInteractor):
    def wrapper(fun):
        def inner():
            progress_dialog = QProgressDialog(interactor)
            progress_dialog.setCancelButton(None)  # 禁用取消按钮
            progress_dialog.setWindowFlags(interactor.windowFlags() | Qt.WindowStaysOnTopHint)
            worker_thread = WorkerThread(interactor)
            worker_thread.update_progress.connect(progress_dialog.setValue)
            progress_dialog.canceled.connect(worker_thread.terminate)
            progress_dialog.finished.connect(fun)
            worker_thread.start()
            progress_dialog.exec()

            fun()

            return inner
        return wrapper
