import math

from PySide6.QtWidgets import QFileDialog, QMainWindow

from ui.roadway import Ui_RoadwayWin
from PySide6 import QtWidgets
import zhao_xi.tools
import json


class RoadWayWin(QtWidgets.QWidget, Ui_RoadwayWin):
    def __init__(self, interactor):
        super().__init__()
        self.setupUi(self)
        self.interactor = interactor
        self.bind()

        # 标志位
        self.roadway_loaded = False

        # 文件过滤
        self.file_filter = "Text files (*.json)"

    def bind(self):
        self.pushButton_generate_roadway.clicked.connect(self.load_roadway)
        self.pushButton_loadInfo.clicked.connect(self.load_info)
        self.pushButton_saveInfo.clicked.connect(self.save_info)

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
                                       float(self.spinBox_workspace_width.value()),
                                       float(self.spinBox_workspace_height.value()),
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
        # self.save_roadway_info()

    def save_info(self):
        roadway_info = {
            'sx1': self.spinBox_sx1.value(),
            'sy1': self.spinBox_sy1.value(),
            'sz1': self.spinBox_sz1.value(),
            'ex1': self.spinBox_ex1.value(),
            'ey1': self.spinBox_ey1.value(),
            'ez1': self.spinBox_ez1.value(),
            'sx2': self.spinBox_sx2.value(),
            'sy2': self.spinBox_sy2.value(),
            'sz2': self.spinBox_sz2.value(),
            'ex2': self.spinBox_ex2.value(),
            'ey2': self.spinBox_ey2.value(),
            'ez2': self.spinBox_ez2.value(),
            'sx3': self.spinBox_sx3.value(),
            'sy3': self.spinBox_sy3.value(),
            'sz3': self.spinBox_sz3.value(),
            'ex3': self.spinBox_ex3.value(),
            'ey3': self.spinBox_ey3.value(),
            'ez3': self.spinBox_ez3.value(),
        }
        window = QMainWindow()
        json_file_path, _ = QFileDialog.getSaveFileName(window, "选择文件", filter=self.file_filter)
        # 保存相机信息到JSON文件
        with open(json_file_path, 'w') as file:
            json.dump(roadway_info, file)

    def load_info(self):
        window = QMainWindow()
        json_file_path, _ = QFileDialog.getOpenFileName(window, "选择文件", filter=self.file_filter)
        if not json_file_path:
            return
        # 从JSON文件加载相机信息
        with open(json_file_path, 'r') as file:
            roadway_info = json.load(file)

        # 设置相机参数为加载的信息
        self.spinBox_sx1.setValue(roadway_info['sx1'])
        self.spinBox_sy1.setValue(roadway_info['sy1'])
        self.spinBox_sz1.setValue(roadway_info['sz1'])
        self.spinBox_ex1.setValue(roadway_info['ex1'])
        self.spinBox_ey1.setValue(roadway_info['ey1'])
        self.spinBox_ez1.setValue(roadway_info['ez1'])
        self.spinBox_sx2.setValue(roadway_info['sx2'])
        self.spinBox_sy2.setValue(roadway_info['sy2'])
        self.spinBox_sz2.setValue(roadway_info['sz2'])
        self.spinBox_ex2.setValue(roadway_info['ex2'])
        self.spinBox_ey2.setValue(roadway_info['ey2'])
        self.spinBox_ez2.setValue(roadway_info['ez2'])
        self.spinBox_sx3.setValue(roadway_info['sx3'])
        self.spinBox_sy3.setValue(roadway_info['sy3'])
        self.spinBox_sz3.setValue(roadway_info['sz3'])
        self.spinBox_ex3.setValue(roadway_info['ex3'])
        self.spinBox_ey3.setValue(roadway_info['ey3'])
        self.spinBox_ez3.setValue(roadway_info['ez3'])
