import numpy as np
import vtk


def create_triangle_polydata(point1: list, point2: list, point3: list) -> vtk.vtkPolyData:
    """
    生成一个三维空间的三角形。
    :param point1:
    :param point2:
    :param point3:
    :return:
    """
    # 创建vtkPoints对象，存储三个点
    points = vtk.vtkPoints()
    points.InsertNextPoint(point1)
    points.InsertNextPoint(point2)
    points.InsertNextPoint(point3)

    # 创建vtkCellArray对象，定义三角形
    triangle = vtk.vtkTriangle()
    triangle.GetPointIds().SetId(0, 0)
    triangle.GetPointIds().SetId(1, 1)
    triangle.GetPointIds().SetId(2, 2)

    # 创建vtkCellArray，将三角形添加到其中
    triangles = vtk.vtkCellArray()
    triangles.InsertNextCell(triangle)

    # 创建vtkPolyData对象，将点和三角形添加到其中
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetPolys(triangles)

    return polydata


def create_combined_actor(polydata_list: list[vtk.vtkPolyData]) -> vtk.vtkActor:
    """
    由多个polydata共同生成一个actor
    :param polydata_list:
    :return:
    """
    # 使用vtkAppendPolyData将所有vtkPolyData合并
    append_filter = vtk.vtkAppendPolyData()
    for polydata in polydata_list:
        append_filter.AddInputData(polydata)
    append_filter.Update()

    # 创建vtkPolyDataMapper和vtkActor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(append_filter.GetOutput())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


def generate_points_on_line(point1: list, point2: list, num_points: int) -> list:
    """
    在以两个三维点为端点的线段上分出指定个数的点（两端也计入个数）
    :param point1:
    :param point2:
    :param num_points:指定要分的点个数
    :return:
    """
    # 将端点转换为NumPy数组
    point1 = np.array(point1)
    point2 = np.array(point2)

    # 生成均匀分布的参数值（从0到1）
    t_values = np.linspace(0, 1, num_points)

    # 根据参数值计算点的坐标
    points = [point1 + t * (point2 - point1) for t in t_values]

    return points


def gen_surface(sp1: list, ep1: list, sp2: list, ep2: list, resolution=100) -> vtk.vtkActor:
    """
    根据三维空间的任意两条线段生成一个有限大小的曲面。
    :param resolution:
    :param sp1: 线段一的起点
    :param ep1: 线段一的终点
    :param sp2: 线段二的起点
    :param ep2: 线段二的终点
    :return:
    """
    points_1 = generate_points_on_line(sp1, ep1, resolution)
    points_2 = generate_points_on_line(sp2, ep2, resolution)
    polydata_list = []
    for i in range(resolution - 1):
        polydata_list.append(create_triangle_polydata(points_1[i], points_2[i], points_2[i + 1]))
        polydata_list.append(create_triangle_polydata(points_2[i + 1], points_1[i], points_1[i + 1]))

    # 创建包含多个三角形的vtkActor
    surface_actor = create_combined_actor(polydata_list)

    return surface_actor


def move_surface(polydata, vector: list):
    # 创建一个变换矩阵来进行平移
    transform = vtk.vtkTransform()
    transform.Translate(*vector)  # 设置平移向量

    # 应用变换到 PolyData
    transform_filter = vtk.vtkTransformPolyDataFilter()
    transform_filter.SetInputData(polydata)
    transform_filter.SetTransform(transform)
    transform_filter.Update()

    return transform_filter.GetOutput()


def gen_seam(sp1: list, ep1: list, sp2: list, ep2: list, thickness: float):
    polydata = gen_surface(sp1, ep1, sp2, ep2).GetMapper().GetInput()  # 先生成煤层的上下表面的模板（未经过平移的）
    # 创建一个变换矩阵来进行平移
    transform = vtk.vtkTransform()
    transform_filter = vtk.vtkTransformPolyDataFilter()
    transform_filter.SetInputData(polydata)
    transform_filter.SetTransform(transform)

    # 获取上表面的 PolyData
    up_polydata = move_surface(polydata, [0, 0, thickness / 2.0])

    # 获取下表面的 PolyData
    down_polydata = move_surface(polydata, [0, 0, -thickness / 2.0])

    return create_combined_actor([up_polydata, down_polydata,
                                  gen_side_surface(sp1, ep1, thickness),
                                  gen_side_surface(sp2, ep2, thickness),
                                  gen_side_surface(sp1, sp2, thickness),
                                  gen_side_surface(ep1, ep2, thickness)])


def gen_side_surface(sp1, ep1, thickness):
    sp1_up = [sp1[0], sp1[1], sp1[2] + thickness / 2.0]
    sp1_down = [sp1[0], sp1[1], sp1[2] - thickness / 2.0]
    ep1_up = [ep1[0], ep1[1], ep1[2] + thickness / 2.0]
    ep1_down = [ep1[0], ep1[1], ep1[2] - thickness / 2.0]
    return gen_surface(sp1_up, sp1_down, ep1_up, ep1_down, 2).GetMapper().GetInput()
