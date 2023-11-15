from PySide6.QtCore import QTimer, QRect
import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class CustomCameraLabel(QLabel):
    def __init__(self, window):
        super().__init__()
        self.window = window
        # 时钟定义
        self.clockForVideo = QTimer(self)

        # 摄像头模块定义
        self.cap = cv2.VideoCapture()
        self.setGeometry(QRect(0, 0, 900, 600))
        self.clockForVideo.timeout.connect(self.update_video)

    def show_video(self):
        if not self.window.showVideo:  # 如果已经开启，则什么都不做
            flag = self.cap.open(0)
            if not flag:
                QMessageBox.information(self, "抱歉", "该摄像头未正常打开！", QMessageBox.Ok)
            self.clockForVideo.start(1)
            self.window.viewer_show("Video")
            self.window.showPointCloud = False
            self.window.showVideo = True

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            if frame is not None:
                cur_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width = cur_frame.shape[:2]
                pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(pixmap)
                ratio = max(width / self.width(), height / self.height())
                pixmap.setDevicePixelRatio(ratio)
                self.setAlignment(Qt.AlignCenter)
                self.setPixmap(pixmap)
