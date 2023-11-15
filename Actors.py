import vtkmodules.all as vtk


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
    def __init__(self, interator):
        super().__init__()
        self.SetCamera(interator.renderer.GetActiveCamera())  # 关联渲染器的相机
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
