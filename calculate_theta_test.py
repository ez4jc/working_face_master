import vtk
import numpy as np

# 创建一个示例vtkPolyData（也可以是您自己的vtkPolyData）
# sphere = vtk.vtkSphereSource()
# sphere.SetRadius(1.0)
# sphere.SetPhiResolution(100)
# sphere.Update()
reader = vtk.vtkPLYReader()
reader.SetFileName('zhao_xi/view_support/view_support_1.ply')
obj_mapper = vtk.vtkPolyDataMapper()
obj_mapper.SetInputConnection(reader.GetOutputPort())
obj_actor = vtk.vtkActor()
obj_actor.SetMapper(obj_mapper)

# 创建vtkOutlineFilter并设置输入vtkPolyData
outline_filter = vtk.vtkOutlineFilter()
outline_filter.SetInputData(obj_mapper.GetInput())
outline_filter.Update()

# 创建vtkPolyDataMapper将vtkOutlineFilter的输出连接到vtkActor
obb_mapper = vtk.vtkPolyDataMapper()
outline_polydata = outline_filter.GetOutput()
obb_mapper.SetInputData(outline_polydata)

# 创建vtkActor并将vtkPolyDataMapper连接到它
obb_actor = vtk.vtkActor()
obb_actor.SetMapper(obb_mapper)

# 创建vtkRenderer、vtkRenderWindow和vtkRenderWindowInteractor
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
renderer.SetRenderWindow(render_window)
render_window.AddRenderer(renderer)

# 将vtkActor添加到vtkRenderer
renderer.AddActor(obb_actor)
renderer.AddActor(obj_actor)

# 创建vtkPolyDataNormals
normals = vtk.vtkPolyDataNormals()
normals.SetInputData(outline_polydata)  # 使用原始vtkPolyData而不是outline_polydata
normals.ComputePointNormalsOff()
normals.ComputeCellNormalsOn()
normals.Update()

# 计算包围框各个面的法向量
face_normals = []
for i in range(0, outline_polydata.GetNumberOfCells(), 2):  # 每两个线段构成一个矩形面
    points = outline_polydata.GetCell(i).GetPoints()
    p0 = points.GetPoint(0)
    p1 = points.GetPoint(1)

    normal = [p1[j] - p0[j] for j in range(3)]  # 通过两个点计算法向量
    face_normals.append(normal)
    theta = np.arccos(np.dot(np.array(normal), [1, 0, 0]) / (np.linalg.norm(np.array(normal))))*180/np.pi
    print(
        f"Face {i // 2 + 1} Normal: {normal} theta: {theta}")

# 创建vtkGlyph3D以可视化法向量
glyph = vtk.vtkGlyph3D()
glyph.SetInputData(normals.GetOutput())
glyph.SetScaleFactor(0.1)  # 箭头的比例因子
glyph.SetSourceConnection(normals.GetOutputPort())

# 创建vtkPolyDataMapper将vtkGlyph3D的输出连接到vtkActor
glyph_mapper = vtk.vtkPolyDataMapper()
glyph_mapper.SetInputConnection(glyph.GetOutputPort())

# 创建vtkActor并将vtkPolyDataMapper连接到它
glyph_actor = vtk.vtkActor()
glyph_actor.SetMapper(glyph_mapper)

# 将可视化的法向量添加到渲染器
renderer.AddActor(glyph_actor)

# 将vtkRenderer渲染到vtkRenderWindow
render_window.Render()

# 创建vtkRenderWindowInteractor并连接到vtkRenderWindow
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# 启动交互式窗口
render_window_interactor.Start()

#################################################################

# 创建一个示例vtkPolyData（也可以是您自己的vtkPolyData）
sphere = vtk.vtkSphereSource()
sphere.SetRadius(1.0)
sphere.SetPhiResolution(100)
sphere.Update()

# 获取对象的数据范围
data_range = obj_mapper.GetInput().GetBounds()

# 计算对象的OBB中心和尺寸
obb_center = [(data_range[0] + data_range[1]) / 2,
              (data_range[2] + data_range[3]) / 2,
              (data_range[4] + data_range[5]) / 2]

obb_dimensions = [data_range[1] - data_range[0],
                  data_range[3] - data_range[2],
                  data_range[5] - data_range[4]]

print(f"OBB Center: {obb_center}")
print(f"OBB Dimensions: {obb_dimensions}")


