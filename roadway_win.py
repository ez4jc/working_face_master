import math
import typing

import scene_initial_info
from ui.roadway import Ui_RoadwayWin
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import zhao_xi.tools
import open3d as o3d
from loading_dialog import load_hint


class RoadWayWin(QtWidgets.QWidget, Ui_RoadwayWin):
    def __init__(self, interactor):
        super().__init__()
        self.setupUi(self)
        self.interactor = interactor

        self.bind()

        # 标志位
        self.roadway_loaded = False
        self.seam_loaded = False

    def bind(self):
        self.pushButton_generate_roadway.clicked.connect(self.load_roadway)
        self.pushButton_generate_coalmine.clicked.connect(self.generate_coalmine)
        self.spinBox_ventilationShaft_z.valueChanged.connect(lambda:
                                                             self.spinBox_transportAlley_z.setValue(
                                                                 float(self.spinBox_ventilationShaft_z.value())))
        self.spinBox_ventilationShaft_height.valueChanged.connect(lambda:
                                                                  self.spinBox_transportAlley_height.setValue(
                                                                      float(
                                                                          self.spinBox_ventilationShaft_height.value())))
        self.spinBox_ventilationShaft_y.valueChanged.connect(lambda: self.spinBox_transportAlley_y.setValue(
            float(self.spinBox_ventilationShaft_y.value())))

    def load_roadway(self):
        self.pushButton_generate_roadway.setEnabled(False)
        zhao_xi.tools.generate_roadway([0.0, 0.0, 0.0], [float(self.spinBox_ventilationShaft_x.value()),
                                                         float(self.spinBox_ventilationShaft_y.value()),
                                                         float(self.spinBox_ventilationShaft_z.value())],
                                       float(self.spinBox_ventilationShaft_width.value()),
                                       float(self.spinBox_ventilationShaft_height.value()),
                                       "zhao_xi/tunnel/tongfengxiang/tongfengxiang_center_line.pcd",
                                       "zhao_xi/tunnel/tongfengxiang/tongfengxiang_vertices")
        zhao_xi.tools.generate_roadway([40.0, 0.0, 0.0], [float(self.spinBox_transportAlley_x.value()),
                                                          float(self.spinBox_transportAlley_y.value()),
                                                          float(self.spinBox_transportAlley_z.value())],
                                       float(self.spinBox_transportAlley_width.value()),
                                       float(self.spinBox_transportAlley_height.value()),
                                       "zhao_xi/tunnel/yunshuxiang/yunshuxiang_center_line.pcd",
                                       "zhao_xi/tunnel/yunshuxiang/yunshuxiang_vertices")
        if not self.roadway_loaded:
            self.interactor.roadway_init(
                math.atan(float(self.spinBox_transportAlley_z.value()) / float(
                    self.spinBox_transportAlley_y.value())) * 180 / math.pi)
            self.roadway_loaded = True
        else:
            self.interactor.update_roadway(
                math.atan(float(self.spinBox_transportAlley_z.value()) / float(
                    self.spinBox_transportAlley_y.value())) * 180 / math.pi)

        # #################################################################待删
        self.interactor.GetRenderWindow().Render()
        # #################################################################
        self.pushButton_generate_roadway.setEnabled(True)

    def generate_coalmine(self):
        @load_hint(self.interactor.window.loading_dialog)  # 这里是因为要用self，因此在外面又加了一层函数
        def generate_coalmine():
            self.pushButton_generate_coalmine.setEnabled(False)
            zhao_xi.tools.update_coalmine(self.spinBox_seamThickness.value(), self.spinBox_ventilationShaft_width.value())
            if not self.seam_loaded:
                self.interactor.seam_init()
                self.seam_loaded = True
            else:
                self.interactor.update_seam()
            # #################################################################待删
            self.interactor.GetRenderWindow().Render()
            # #################################################################
            self.pushButton_generate_coalmine.setEnabled(True)
        generate_coalmine()