from PySide6 import QtWidgets

from ui.CoalCutter import Ui_CoalCutter


class CoalCutterWin(QtWidgets.QWidget, Ui_CoalCutter):
    def __init__(self, interactor):
        super().__init__()
        self.setupUi(self)
        self.interactor = interactor

        self.bind()

    def bind(self):
        self.pushButton_loadCoalCutter.clicked.connect(self.loadCoalCutter)
        self.pushButton_fitSeamSurface.clicked.connect(self.fitSeamSurface)

    def loadCoalCutter(self):
        self.pushButton_loadCoalCutter.setEnabled(False)
        self.interactor.coalCutter_init()
        self.checkBox_showCoalCutter.setEnabled(True)
        self.checkBox_showCoalCutter.setChecked(True)
        self.checkBox_showCoalCutter.clicked.connect(self.interactor.coal_cutter_actor.show_model)

    def fitSeamSurface(self):
        self.interactor.coal_cutter_actor.roll_yoz(self.interactor.roadway_actors[0].theta)
