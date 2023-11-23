import typing

import scene_initial_info
from ui.roadway import Ui_RoadwayWin
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
import zhao_xi.tools
import open3d as o3d


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
        self.pushButton_generate_coalmine.clicked.connect(self.generate_coalmine)
        # self.pushButton_clear_workplace.clicked.connect(self.clear_workplace)

    def load_roadway(self):
        # self.pushButton_generate_roadway.setEnabled(False)
        self.generate_roadway([0.0, 0.0, 0.0], [float(self.spinBox_ventilationShaft_x.value()),
                                                float(self.spinBox_ventilationShaft_y.value()),
                                                float(self.spinBox_ventilationShaft_z.value())],
                              float(self.spinBox_ventilationShaft_width.value()),
                              float(self.spinBox_ventilationShaft_height.value()),
                              "zhao_xi/tunnel/tongfengxiang/tongfengxiang_center_line.pcd",
                              "zhao_xi/tunnel/tongfengxiang/tongfengxiang_vertices")
        self.generate_roadway([40.0, 0.0, 0.0], [float(self.spinBox_transportAlley_x.value()),
                                                 float(self.spinBox_transportAlley_y.value()),
                                                 float(self.spinBox_transportAlley_z.value())],
                              float(self.spinBox_transportAlley_width.value()),
                              float(self.spinBox_transportAlley_height.value()),
                              "zhao_xi/tunnel/yunshuxiang/yunshuxiang_center_line.pcd",
                              "zhao_xi/tunnel/yunshuxiang/yunshuxiang_vertices")
        if not self.roadway_loaded:
            self.interactor.add_actor_and_checkbox(scene_initial_info.workplace_filename)  # 通知渲染器
            self.roadway_loaded = True
        else:
            self.interactor.update_workplace()

        # #################################################################待删
        self.interactor.renderer.GetRenderWindow().Render()
        # #################################################################
        # self.pushButton_generate_coalmine.setEnabled(True)

    def generate_roadway(self, start_point: typing.List[float], endpoint: typing.List[float], width, height,
                         line_filename,
                         roadway_filename):

        ventilationShaft_center_line = zhao_xi.tools.generate_center_line(start_point, endpoint, 0.4)
        zhao_xi.tools.save_points_to_file(ventilationShaft_center_line,
                                          line_filename)
        ventilationShaft_vertices = zhao_xi.tools.generate_the_vertices_of_boundary_of_tunnel(
            line_filename, width, height)
        zhao_xi.tools.save_the_vertices_of_the_boundary_of_tunnel_as_ply_and_vtk(
            roadway_filename, ventilationShaft_vertices)

    def generate_coalmine(self):
        # self.pushButton_generate_coalmine.setEnabled(False)
        ventilation_alley = o3d.io.read_point_cloud("zhao_xi/tunnel/tongfengxiang/tongfengxiang_vertices.ply")
        transportation_alley = o3d.io.read_point_cloud("zhao_xi/tunnel/yunshuxiang/yunshuxiang_vertices.ply")
        print(ventilation_alley, transportation_alley)
        zhao_xi.tools.update_coalmine(ventilation_alley, transportation_alley)
        # #################################################################待删
        self.interactor.update_workplace()
        # #################################################################
        # self.pushButton_generate_roadway.setEnabled(True)

    # def clear_workplace(self):
    #     self.pushButton_clear_workplace.setEnabled(False)
    #     self.pushButton_generate_roadway.setEnabled(True)
