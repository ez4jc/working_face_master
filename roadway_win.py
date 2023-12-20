import math
from ui.roadway import Ui_RoadwayWin
from PySide6 import QtWidgets
import zhao_xi.tools


class RoadWayWin(QtWidgets.QWidget, Ui_RoadwayWin):
    def __init__(self, interactor):
        super().__init__()
        self.setupUi(self)
        self.interactor = interactor
        self.bind()

        # 标志位
        self.roadway_loaded = False

    def bind(self):
        self.pushButton_generate_roadway.clicked.connect(self.load_roadway)

    def load_roadway(self):
        # ‘s’：起点，’e‘：终点。
        # ‘x’：坐标轴。
        # ‘1’：通风巷，‘2’：运输巷，‘3‘：工作巷。
        zhao_xi.tools.generate_roadway([float(self.spinBox_sx1.value()),
                                        float(self.spinBox_sy1.value()),
                                        float(self.spinBox_sz1.value())],
                                       [float(self.spinBox_ex1.value()),
                                        float(self.spinBox_ey1.value()),
                                        float(self.spinBox_ez1.value())],
                                       float(self.spinBox_ventilationShaft_width.value()),
                                       float(self.spinBox_ventilationShaft_height.value()),
                                       "zhao_xi/tunnel/tongfengxiang/tongfengxiang_center_line.pcd",
                                       "zhao_xi/tunnel/tongfengxiang/tongfengxiang_vertices")
        zhao_xi.tools.generate_roadway([float(self.spinBox_sx2.value()),
                                        float(self.spinBox_sy2.value()),
                                        float(self.spinBox_sz2.value())],
                                       [float(self.spinBox_ex2.value()),
                                        float(self.spinBox_ey2.value()),
                                        float(self.spinBox_ez2.value())],
                                       float(self.spinBox_transportAlley_width.value()),
                                       float(self.spinBox_transportAlley_height.value()),
                                       "zhao_xi/tunnel/yunshuxiang/yunshuxiang_center_line.pcd",
                                       "zhao_xi/tunnel/yunshuxiang/yunshuxiang_vertices")
        zhao_xi.tools.generate_roadway([float(self.spinBox_sx3.value()),
                                        float(self.spinBox_sy3.value()),
                                        float(self.spinBox_sz3.value())],
                                       [float(self.spinBox_ex3.value()),
                                        float(self.spinBox_ey3.value()),
                                        float(self.spinBox_ez3.value())],
                                       float(self.spinBox_transportAlley_width.value()),
                                       float(self.spinBox_transportAlley_height.value()),
                                       "zhao_xi/tunnel/work_surface/work_surface_center_line.pcd",
                                       "zhao_xi/tunnel/work_surface/work_surface_vertices")
        if not self.roadway_loaded:
            self.interactor.roadway_init(
                math.atan(float(self.spinBox_ez2.value()) / float(self.spinBox_ey2.value())) * 180 / math.pi)
            self.roadway_loaded = True
        else:
            theta = math.atan(float(self.spinBox_ez2.value()) / float(self.spinBox_ey2.value())) * 180 / math.pi
            self.interactor.roadway_actors[0].update(theta)
            self.interactor.roadway_actors[1].update(theta)
            self.interactor.work_roadway.update()
            self.interactor.GetRenderWindow().Render()
