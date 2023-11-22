import typing

import vtkmodules.all as vtk
import zhao_xi.tools
import zhao_xi.mine_device


class HorizontalPlaneActor(vtk.vtkActor):
    def __init__(self, type):
        super().__init__()
        # 1.创建一个水平平面设置分辨率并增加网格线
        self.plane = vtk.vtkPlaneSource()
        length = 1000  # 网格最大覆盖面
        # 设置平面的大小和位置
        self.plane.SetCenter(0, 0, 0)
        if type == "XY":
            self.plane.SetOrigin(-length, -length, 0.0)  # 左下角点
            self.plane.SetPoint1(length, -length, 0.0)  # 右下角点
            self.plane.SetPoint2(-length, length, 0.0)  # 左上角点
        elif type == "YZ":
            self.plane.SetOrigin(0.0, -length, -length)  # 左下角点
            self.plane.SetPoint1(0.0, -length, length)  # 右下角点
            self.plane.SetPoint2(0.0, length, -length)  # 左上角点
        elif type == "XZ":
            self.plane.SetOrigin(-length, 0.0, -length)  # 左下角点
            self.plane.SetPoint1(-length, 0.0, length)  # 右下角点
            self.plane.SetPoint2(length, 0.0, -length)  # 左上角点
        resolution = 1000  # 平面分辨率
        self.plane.SetResolution(resolution, resolution)  # 设置平面的分辨率
        self.plane_mapper = vtk.vtkPolyDataMapper()
        self.plane_mapper.SetInputConnection(self.plane.GetOutputPort())
        self.SetMapper(self.plane_mapper)
        # 创建网格线属性，应用于plane。网格实际上是平面设置了网格属性所呈现。
        self.grid_property = vtk.vtkProperty()
        self.grid_property.SetRepresentationToWireframe()  # 设置网格线表示为线框
        self.grid_property.LightingOff()  # 禁用网格的光照效果
        self.SetProperty(self.grid_property)  # 设置平面表示为表面


class CubeAxesActor(vtk.vtkCubeAxesActor2D):
    def __init__(self, interactor):
        super().__init__()
        self.SetCamera(interactor.renderer.GetActiveCamera())  # 关联渲染器的相机
        self.SetFlyModeToOuterEdges()  # 设置坐标轴显示在场景边缘


class SphereActor(vtk.vtkActor):
    def __init__(self):
        super().__init__()
        env_image = "1.jpg"
        # 球体几何数据
        sphere = vtk.vtkSphereSource()
        sphere.SetThetaResolution(100)  # 经线数量
        sphere.SetPhiResolution(100)  # 纬线数量        球的分辨率设置
        sphere.SetRadius(10)
        # 球体坐标映射滤波器
        text_coordinates = vtk.vtkTextureMapToSphere()
        text_coordinates.SetInputConnection(sphere.GetOutputPort())
        text_coordinates.PreventSeamOn()
        text_coordinates.AutomaticSphereGenerationOn()
        # 球体映射到几何形状
        sphere_mapper = vtk.vtkPolyDataMapper()
        sphere_mapper.SetInputConnection(text_coordinates.GetOutputPort())
        # 环境图片读入
        env_image_reader = vtk.vtkJPEGReader()
        env_image_reader.SetFileName(env_image)
        # 映射到纹理
        env_texture = vtk.vtkTexture()
        env_texture.SetInputConnection(env_image_reader.GetOutputPort())
        # 演员设置几何形状、纹理
        self.SetMapper(sphere_mapper)
        self.SetTexture(env_texture)


class GyroActor(vtk.vtkActor):
    def __init__(self):
        super().__init__()

        # 创建xoy演员
        self.xoy_circle_actor = self.gen_circle([0, 0, 0], [0, 0, 1], [0, 0, 1])

        # 创建zox的映射器和演员
        self.zox_circle_actor = self.gen_circle([0, 0, 0], [0, 1, 0], [0, 1, 0])

        # 创建yoz映射器和演员
        self.yoz_circle_actor = self.gen_circle([0, 0, 0], [1, 0, 0], [1, 0, 0])

    def get_actor(self):
        return [self.xoy_circle_actor, self.zox_circle_actor, self.yoz_circle_actor]

    @staticmethod
    def gen_circle(center: typing.List, vector: typing.List, color: typing.List):
        # 创建zox的圆
        zox_circle = vtk.vtkRegularPolygonSource()
        zox_circle.SetCenter(center[0], center[1], center[2])
        zox_circle.SetRadius(1.0)
        zox_circle.SetNumberOfSides(50)  # 可以根据需要调整边数
        zox_circle.SetNormal(vector[0], vector[1], vector[2])  # 设置法向量为Y轴，使其垂直于横向圆
        # 创建zox映射器和演员
        circle_mapper = vtk.vtkPolyDataMapper()
        circle_mapper.SetInputConnection(zox_circle.GetOutputPort())

        circle_actor = vtk.vtkActor()
        circle_actor.SetMapper(circle_mapper)
        circle_actor.GetProperty().SetColor(color)
        circle_actor.GetProperty().SetRepresentationToWireframe()

        return circle_actor


class SupporterActor(vtk.vtkActor):
    def __init__(self, filename, interactor):
        super().__init__()
        self.interactor = interactor
        self.filename = filename
        self.init()
        # 包围框
        self.wraparound_actor = self.generate_wraparound_frame()
        # 绝对包围框
        self.static_wraparound_actor = self.generate_static_wraparound_frame()
        # 标签（本身是演员列表组成的演员）
        self.label_actors = []
        self.generate_3D_label()  # 此方法会添加标签到self.label_actor
        # 陀螺仪（本身是演员列表组成的演员）
        self.gyro = GyroActor().get_actor()
        self.axis_x, self.axis_y, self.axis_z = zhao_xi.tools.get_supporter_axis(self.filename)

        # 标志位
        self.model_flag = True
        self.wraparound_actor_flag = False
        self.static_wraparound_actor_flag = False
        self.label_flag = False
        self.gyro_flag = False

    def init(self):
        self.SetMapper(self.interactor.create_single_actor(self.filename))
        self.SetProperty(self.interactor.base_property)

    def move(self, dis):
        zhao_xi.mine_device.Support.move_actor(self, dis)
        zhao_xi.mine_device.Support.move_actor(self.wraparound_actor, dis)

    def generate_wraparound_frame(self):
        polydata = zhao_xi.tools.drawing_the_bounding_box(
            zhao_xi.tools.sort_obb_of_support(zhao_xi.tools.support_standard,
                                              zhao_xi.tools.get_obb_size(self.filename)))
        poly_mapper = vtk.vtkPolyDataMapper()
        poly_mapper.SetInputData(polydata)
        wraparound_frame_property = vtk.vtkProperty()
        wraparound_frame_property.SetColor(1, 0, 0)
        # 包围框演员
        actor = vtk.vtkActor()
        actor.SetMapper(poly_mapper)
        actor.SetProperty(wraparound_frame_property)
        return actor

    def generate_static_wraparound_frame(self):
        polydata = zhao_xi.tools.drawing_the_directional_box_of_support([0, 0, 1],
                                                                        zhao_xi.tools.sort_obb_of_support(
                                                                            zhao_xi.tools.support_standard,
                                                                            zhao_xi.tools.get_obb_size(self.filename)))
        poly_mapper = vtk.vtkPolyDataMapper()
        poly_mapper.SetInputData(polydata)
        wraparound_frame_property = vtk.vtkProperty()
        wraparound_frame_property.SetColor(0, 1, 0)
        # 包围框演员
        actor = vtk.vtkActor()
        actor.SetMapper(poly_mapper)
        actor.SetProperty(wraparound_frame_property)
        return actor

    def generate_3D_label(self):
        lines = zhao_xi.tools.drawing_the_box_line(
            zhao_xi.tools.sort_obb_of_support(zhao_xi.tools.support_standard,
                                              zhao_xi.tools.get_obb_size(self.filename)))
        for line in lines:
            self.generate_line_label(line[0], line[1], line[2])

    def generate_line_label(self, point1, point2, text):
        middel_point = (point2 + point1) / 2.0
        x = middel_point[0]
        y = middel_point[1]
        z = middel_point[2]
        # 提示线
        line_source = vtk.vtkLineSource()
        line_source.SetPoint1(point1)
        line_source.SetPoint2(point2)
        line_mapper = vtk.vtkPolyDataMapper()
        line_mapper.SetInputConnection(line_source.GetOutputPort())
        line_actor = vtk.vtkActor()
        line_actor.SetMapper(line_mapper)
        line_property = vtk.vtkProperty()
        line_property.SetColor(1, 0, 0)
        line_actor.SetProperty(line_property)
        self.label_actors.append(line_actor)
        # 文本
        text_actor = vtk.vtkOpenGLBillboardTextActor3D()
        text_actor.GetTextProperty().SetColor(0, 0, 1)
        text_actor.SetInput(text)
        text_actor.GetTextProperty().SetFontSize(12)
        text_actor.SetPosition(x, y, z)
        self.label_actors.append(text_actor)

    def show_model(self):
        self.show_items([self], self.model_flag)
        self.model_flag = not self.model_flag

    def show_wraparound_frame(self):
        self.show_items([self.wraparound_actor], self.wraparound_actor_flag)
        self.wraparound_actor_flag = not self.wraparound_actor_flag

    def show_static_wraparound_frame(self):
        self.show_items([self.static_wraparound_actor], self.static_wraparound_actor_flag)
        self.static_wraparound_actor_flag = not self.static_wraparound_actor_flag

    def show_label(self):
        self.show_items(self.label_actors, self.label_flag)
        self.label_flag = not self.label_flag

    def show_gyro(self):
        self.show_items(self.gyro, self.gyro_flag)
        self.gyro_flag = not self.gyro_flag

    def show_items(self, items: list[vtk.vtkActor], flag):  # 直接调用代表interactor是此方法的观察者
        if not flag:
            for actor in items:
                self.interactor.renderer.AddActor(actor)
        else:
            for actor in items:
                self.interactor.renderer.RemoveActor(actor)
        self.notice_render_window()

    def roll_xoy(self, theta):
        tick = 60
        for i in range(tick):
            zhao_xi.mine_device.Support.rotate_actor(self, theta / tick, self.axis_z)
            print(self.axis_z)
            self.notice_render_window()

    def notice_render_window(self):
        self.interactor.GetRenderWindow().Render()
