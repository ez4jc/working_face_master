import vtk

# 创建一个VTK渲染器和渲染窗口
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# 创建一个VTK渲染窗口交互工具
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# 创建一个线段源
line_source = vtk.vtkLineSource()
line_source.SetPoint1(0, 0, 0)
line_source.SetPoint2(1, 1, 1)

# 创建一个线段的映射器
line_mapper = vtk.vtkPolyDataMapper()
line_mapper.SetInputConnection(line_source.GetOutputPort())

# 创建一个线段的演员
line_actor = vtk.vtkActor()
line_actor.SetMapper(line_mapper)

# 在线段上显示文字
text_actor = vtk.vtkTextActor()
text_actor.SetTextScaleModeToNone()  # 设置文本比例模式
text_actor.SetTextScaleModeToNone()
text_actor.SetPosition(0.5, 0.5)  # 设置文本位置（相对于窗口的百分比）
text_actor.SetTextScaleModeToNone()
text_actor.GetTextProperty().SetFontSize(16)  # 设置文本字体大小
text_actor.SetInput("Your Text Here")

# 将演员和文字演员添加到渲染器中
renderer.AddActor(line_actor)
renderer.AddActor(text_actor)

# 设置渲染器的背景颜色
renderer.SetBackground(1.0, 1.0, 1.0)

# 设置渲染窗口的大小
render_window.SetSize(600, 600)

# 将渲染窗口交互工具连接到渲染窗口
render_window.SetInteractor(render_window_interactor)

# 渲染并启动交互
render_window.Render()
render_window_interactor.Start()
