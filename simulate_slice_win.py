from PySide6 import QtWidgets

from ui.simulate_slice import Ui_SliceWin
from zhao_xi.tools import slicer


class SliceWin(QtWidgets.QWidget, Ui_SliceWin):
    def __init__(self, interactor):
        super().__init__()
        self.setupUi(self)
        self.interactor = interactor
        self.slicer = slicer()
        self.bind()

    def bind(self):
        self.pushButton_sliceSeam.clicked.connect(
            lambda: self.slicer.slice_seam(self.lineEdit_sliceThickness.value()))  # slice_seam是zhao_xi.tools模块里的函数
        self.pushButton_pushCutter.clicked.connect(
            lambda: self.interactor.coal_cutter_actor.move(self.lineEdit_sliceThickness.value()))
        self.pushButton_pushSupports.clicked.connect(self.push_supports())

    def push_supports(self):
        pass
