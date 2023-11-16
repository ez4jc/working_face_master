import vtk

# 读入点云数据
reader = vtk.vtkPLYReader()
reader.SetFileName("zhao_xi/support/test_support_1.ply")
reader.Update()

# 获取点云对象
pointCloud = reader.GetOutput()

# 创建平移变换
translation = vtk.vtkTransform()

# 创建动画场景
scene = vtk.vtkAnimationScene()

# 设置动画场景的时间范围
scene.SetStartTime(0)
scene.SetEndTime(100)

# 创建动画过程
cue = vtk.vtkAnimationCue()
cue.SetStartTime(0)
cue.SetEndTime(100)

i = 0


# 在每一帧更新平移变换
def update_transform(caller, event):
    translation.Translate(0.01, 0, 0)  # 在X轴方向平移
    actor.SetUserTransform(translation)
    render_window.Render()
    global i
    i += 1
    print(i)


cue.AddObserver("AnimationCueTickEvent", update_transform)

# 将动画过程添加到动画场景
scene.AddCue(cue)

# 创建渲染器和渲染窗口
renderer = vtk.vtkRenderer()
renderer.SetBackground(1, 1, 1)

render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("PointCloud Animation")
render_window.SetSize(800, 600)
render_window.AddRenderer(renderer)

# 创建交互器
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# 将点云添加到渲染器
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(pointCloud)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)

# 将渲染器添加到渲染窗口
renderer.ResetCamera()
render_window.Render()

# 开始动画
render_window_interactor.Initialize()
scene.Play()
render_window_interactor.Start()
