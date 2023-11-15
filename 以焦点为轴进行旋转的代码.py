# 获取摄像头的位置和焦点
position = camera.GetPosition()
focal_point = camera.GetFocalPoint()

# 计算观察方向矢量
view_direction = [focal_point[i] - position[i] for i in range(3)]

# 计算绕焦点旋转的中心
center_of_rotation = focal_point

# 创建一个变换对象
transform = vtk.vtkTransform()
transform.PostMultiply()

# 在变换中心点上绕观察方向旋转
rotation_angle = 10.0  # 旋转角度（以度为单位）
transform.Translate(center_of_rotation)  # 将坐标系移到旋转中心
transform.RotateWXYZ(rotation_angle, view_direction[0], view_direction[1], view_direction[2])  # 绕观察方向旋转
transform.Translate(-center_of_rotation)  # 将坐标系还原

# 应用变换到摄像头
camera.ApplyTransform(transform)
