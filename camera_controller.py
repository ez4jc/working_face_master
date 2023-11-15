import vtkmodules.all as vtk
import math


class CameraController:
    def __init__(self, camera):
        self.camera = camera
        # 摄像头初始位置
        # self.camera.SetPosition(-30, -30, 50)
        # self.camera.Roll(53)
        # self.my_elevation(35)

        self.moving_forward = False
        self.moving_backward = False
        self.moving_left = False
        self.moving_right = False
        self.fly_moveSpeed = 0.1  # 漫游移动速度，对应滑条初始值10
        self.view_moveSpeed = 0.5  # 审视移动速度,对应滑条初始值50

        self.limitedX = False
        self.limitedY = False
        self.limitedRoll = False
        self.unlimited = True
        self.is_rotating = False

        self.last_x = 0
        self.last_y = 0

    def keypress_processor(self, ev):
        if True:  # if self.fly_mode
            if ev.key() in [87, 83, 65, 68]:
                if ev.key() == 87:  # 'w'
                    self.moving_forward = True
                elif ev.key() == 83:  # 's'
                    self.moving_backward = True
                elif ev.key() == 65:  # 'a'
                    self.moving_left = True
                elif ev.key() == 68:  # 'd'
                    self.moving_right = True
                self.UpdateCameraPosition()

    def keyRelease_processor(self, ev):
        if True:  # if self.fly_mode
            if ev.key() in [87, 83, 65, 68]:
                if ev.key() == 87:  # 'w'
                    self.moving_forward = False
                elif ev.key() == 83:  # 's'
                    self.moving_backward = False
                elif ev.key() == 65:  # 'a'
                    self.moving_left = False
                elif ev.key() == 68:  # 'd'
                    self.moving_right = False
                self.UpdateCameraPosition()

    def wheelEvent_processor(self, ev):
        if False:  # if self.fly_mode
            return
        else:
            if ev.angleDelta().y() > 0:
                self.OnMouseWheelForward()
            else:
                self.OnMouseWheelBackward()

    def UpdateCameraPosition(self):
        position = list(self.camera.GetPosition())
        focal_point = list(self.camera.GetFocalPoint())
        view_up = list(self.camera.GetViewUp())
        view_direction = [focal_point[i] - position[i] for i in range(3)]

        if self.moving_forward:
            for i in range(3):
                position[i] += self.fly_moveSpeed * view_direction[i]
                focal_point[i] += self.fly_moveSpeed * view_direction[i]
        if self.moving_backward:
            for i in range(3):
                position[i] -= self.fly_moveSpeed * view_direction[i]
                focal_point[i] -= self.fly_moveSpeed * view_direction[i]
        if self.moving_left:
            right = [view_up[1] * view_direction[2] - view_up[2] * view_direction[1],
                     view_up[2] * view_direction[0] - view_up[0] * view_direction[2],
                     view_up[0] * view_direction[1] - view_up[1] * view_direction[0]]
            vtk.vtkMath.Normalize(right)
            for i in range(3):
                position[i] += self.fly_moveSpeed * right[i]
                focal_point[i] += self.fly_moveSpeed * right[i]
        if self.moving_right:
            right = [view_up[1] * view_direction[2] - view_up[2] * view_direction[1],
                     view_up[2] * view_direction[0] - view_up[0] * view_direction[2],
                     view_up[0] * view_direction[1] - view_up[1] * view_direction[0]]
            vtk.vtkMath.Normalize(right)
            for i in range(3):
                position[i] -= self.fly_moveSpeed * right[i]
                focal_point[i] -= self.fly_moveSpeed * right[i]

        self.camera.SetPosition(position)
        self.camera.SetFocalPoint(focal_point)

    def OnMouseWheelForward(self):
        # 向前滚动鼠标滚轮，模拟放大效果
        position = list(self.camera.GetPosition())
        focal_point = list(self.camera.GetFocalPoint())
        view_up = list(self.camera.GetViewUp())
        view_direction = [focal_point[i] - position[i] for i in range(3)]
        for i in range(3):
            position[i] += self.view_moveSpeed * view_direction[i]
            focal_point[i] += self.view_moveSpeed * view_direction[i]
        self.camera.SetPosition(position)
        self.camera.SetFocalPoint(focal_point)

    def OnMouseWheelBackward(self):
        # 向后滚动鼠标滚轮，模拟缩小效果
        position = list(self.camera.GetPosition())
        focal_point = list(self.camera.GetFocalPoint())
        view_up = list(self.camera.GetViewUp())
        view_direction = [focal_point[i] - position[i] for i in range(3)]
        for i in range(3):
            position[i] -= self.view_moveSpeed * view_direction[i]
            focal_point[i] -= self.view_moveSpeed * view_direction[i]
        self.camera.SetPosition(position)
        self.camera.SetFocalPoint(focal_point)

    def rotate_x(self, ev):
        if self.is_rotating:
            x = ev.pos().x()
            dx = x - self.last_x
            self.camera.Azimuth(-dx / 10.0)  # 左右旋转
            self.last_x = x

    def rotate_y(self, ev):
        if self.is_rotating:
            y = ev.pos().y()
            dy = y - self.last_y
            self.my_elevation(dy / 10.0)
            # self.camera.Elevation(dy / 10.0)  # 上下旋转,这个自带的上下旋转函数有俯仰角90度的限制
            self.last_y = y

    def roll(self, ev, center_x, center_y):
        if self.is_rotating:
            theta = self.calculate_roll_theta(ev, center_x, center_y)
            self.camera.Roll(theta)

    def my_elevation(self, dy):
        # 获取当前摄像机的位置、焦点和视向矢量
        position = list(self.camera.GetPosition())
        focal_point = self.camera.GetFocalPoint()
        view_up = self.camera.GetViewUp()

        # 计算摄像机到焦点的矢量
        view_vector = [focal_point[i] - position[i] for i in range(3)]

        # 计算旋转轴，这将是视向矢量的垂直方向
        rotation_axis = [0.0, 0.0, 0.0]
        vtk.vtkMath.Cross(view_vector, view_up, rotation_axis)
        vtk.vtkMath.Normalize(rotation_axis)

        # 计算旋转角度，根据垂直方向的偏移 dy
        rotation_angle = dy  # 可以根据需要调整旋转速度

        # 创建一个旋转变换
        transform = vtk.vtkTransform()
        transform.PostMultiply()

        # 计算绕旋转轴的旋转
        transform.RotateWXYZ(rotation_angle, rotation_axis[0], rotation_axis[1], rotation_axis[2])

        # 应用旋转变换到视向矢量
        view_vector = transform.TransformVector(view_vector)

        # 更新摄像机的位置
        for i in range(3):
            position[i] = focal_point[i] - view_vector[i]

        # 设置更新后的摄像机位置
        self.camera.SetPosition(position)

        # 计算新的焦点位置
        new_focal_point = [position[i] + view_vector[i] for i in range(3)]

        # 设置更新后的焦点位置
        self.camera.SetFocalPoint(new_focal_point)
        self.camera.OrthogonalizeViewUp()  # 应时刻根据新的焦点和当前位置计算新的ViewUp向量

    def custom_set_view(self, position, view_vector):
        self.camera.SetPosition(position[0], position[1], position[2])
        focal_point = self.camera.GetFocalPoint()
        self.camera.SetFocalPoint(position + view_vector)
        self.camera.OrthogonalizeViewUp()  # 应时刻根据新的焦点和当前位置计算新的ViewUp向量

    def calculate_roll_theta(self, ev, center_x, center_y):
        x = ev.pos().x()
        y = ev.pos().y()
        theta_1 = math.atan2(self.last_y - center_y, self.last_x - center_x)
        theta_2 = math.atan2(y - center_y, x - center_x)
        self.last_x = x
        self.last_y = y
        return self.radians_to_positive_degrees(theta_1 - theta_2)

    @staticmethod
    def radians_to_positive_degrees(radians):
        # 将弧度转换为正的角度，范围在 0 到 360 度之间
        degrees = radians * 180 / math.pi
        if degrees < 0:
            degrees += 360
        return degrees

    def change_viewSpeed(self, value):
        self.view_moveSpeed = value / 100.0

    def change_flySpeed(self, value):
        self.fly_moveSpeed = value / 100.0

    def switch_limitedX(self):
        self.limitedX = True
        self.limitedY = False
        self.limitedRoll = False
        self.unlimited = False

    def switch_limitedY(self):
        self.limitedY = True
        self.limitedX = False
        self.limitedRoll = False
        self.unlimited = False

    def switch_limitedRoll(self):
        self.limitedRoll = True
        self.limitedX = False
        self.limitedY = False
        self.unlimited = False

    def switch_unlimited(self):
        self.unlimited = True
        self.limitedX = False
        self.limitedY = False
        self.limitedRoll = False
