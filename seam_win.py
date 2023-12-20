import time

from PySide6 import QtWidgets
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QProgressDialog

from ui.seam import Ui_Seam
import zhao_xi.tools


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


class SeamWin(QtWidgets.QWidget, Ui_Seam):
    def __init__(self, interactor):
        super().__init__()
        self.setupUi(self)
        self.interactor = interactor
        self.bind()

        # 标志位
        self.seam_loaded = False

    def bind(self):
        self.pushButton_generate_coalmine.clicked.connect(self.generate_coalmine)

    def generate_coalmine(self):
        self.show_process()
        self.pushButton_generate_coalmine.setEnabled(False)
        zhao_xi.tools.update_coalmine(self.spinBox_seamThickness.value(),
                                      self.interactor.window.roadway_win.spinBox_ventilationShaft_width.value())
        if not self.seam_loaded:
            self.interactor.seam_init()
            self.seam_loaded = True
        else:
            self.interactor.update_seam()
        self.interactor.GetRenderWindow().Render()
        self.pushButton_generate_coalmine.setEnabled(True)

    def show_process(self):
        progress_dialog = QProgressDialog(self.interactor)
        progress_dialog.setCancelButton(None)  # 禁用取消按钮
        progress_dialog.setLabelText("煤层生成中，勿操作。")
        progress_dialog.setWindowFlags(Qt.WindowStaysOnTopHint)

        worker_thread = WorkerThread(self.interactor)
        worker_thread.update_progress.connect(progress_dialog.setValue)

        progress_dialog.canceled.connect(worker_thread.terminate)

        worker_thread.start()
        progress_dialog.exec()
