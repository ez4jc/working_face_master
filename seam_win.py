import time

from PySide6 import QtWidgets
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtWidgets import QProgressDialog

from ui.seam import Ui_Seam
from seam_algorithm import gen_seam


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
        # 生成煤层的进度条
        # self.show_process()
        # 实际生成煤层
        # v1.0
        # self.pushButton_generate_coalmine.setEnabled(False)
        # zhao_xi.tools.update_coalmine(self.spinBox_seamThickness.value(),
        #                               self.interactor.window.roadway_win.spinBox_ventilationShaft_width.value())
        # if not self.seam_loaded:
        #     self.interactor.seam_init()
        #     self.seam_loaded = True
        # else:
        #     self.interactor.update_seam()
        # self.interactor.GetRenderWindow().Render()
        # self.pushButton_generate_coalmine.setEnabled(True)
        # v2.0
        seam_actor = gen_seam([float(self.interactor.window.roadway_win.spinBox_sx1.value()),
                                             float(self.interactor.window.roadway_win.spinBox_sy1.value()),
                                             float(self.interactor.window.roadway_win.spinBox_sz1.value())],
                                            [float(self.interactor.window.roadway_win.spinBox_ex1.value()),
                                             float(self.interactor.window.roadway_win.spinBox_ey1.value()),
                                             float(self.interactor.window.roadway_win.spinBox_ez1.value())],
                                            [float(self.interactor.window.roadway_win.spinBox_sx2.value()),
                                             float(self.interactor.window.roadway_win.spinBox_sy2.value()),
                                             float(self.interactor.window.roadway_win.spinBox_sz2.value())],
                                            [float(self.interactor.window.roadway_win.spinBox_ex2.value()),
                                             float(self.interactor.window.roadway_win.spinBox_ey2.value()),
                                             float(self.interactor.window.roadway_win.spinBox_ez2.value())]
                                            )
        self.interactor.show_actors([seam_actor], False)
        ##############################################

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
