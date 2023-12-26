import numpy as np

def generate_points_on_line(point1, point2, num_points):
    # 将端点转换为NumPy数组
    point1 = np.array(point1)
    point2 = np.array(point2)

    # 生成均匀分布的参数值（从0到1）
    t_values = np.linspace(0, 1, num_points)

    # 根据参数值计算点的坐标
    points = [point1 + t * (point2 - point1) for t in t_values]

    return points

# 示例：定义两个端点
endpoint1 = [0.0, 0.0, 0.0]
endpoint2 = [1.0, 1.0, 1.0]

# 生成均匀分布的100个点
line_points = generate_points_on_line(endpoint1, endpoint2, num_points=10)

# 打印生成的点坐标
for i, point in enumerate(line_points):
    print(f"Point {i+1}: {point}")
