import vtk
import numpy as np

# 创建一个vtkTransform对象
transform = vtk.vtkTransform()

# 设置旋转角度和轴
angle_degrees = 90.0
axis = [0.0, 0.0, 1.0]

# 将vtkTransform对象设置为绕轴旋转
transform.RotateWXYZ(angle_degrees, *axis)

# 创建一个示例的3D向量
input_vector = [1.0, 0.0, 0.0]

# 使用vtkTransform对象将向量进行旋转
output_vector = transform.TransformDoublePoint(input_vector)

print(f"Input Vector: {input_vector}")
print(f"Output Vector after rotation: {output_vector}")
