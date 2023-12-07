import sys
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
import time

class MoveThread(QThread):
    # 定义一个信号，用于在线程中完成任务后通知主线程更新UI
    finished_signal = Signal()

    def __init__(self, move_function, *args, **kwargs):
        super().__init__()
        self.move_function = move_function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        # 在 run 方法中执行任务
        self.move_function(*self.args, **self.kwargs)

        # 发送任务完成信号
        self.finished_signal.emit()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("任务执行中...")

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # 传递参数到 self.move 函数
        move_args = (1, 2, 3)  # 你需要传递的参数
        move_kwargs = {"param1": "value1", "param2": "value2"}  # 你需要传递的关键字参数

        # 创建并启动线程
        self.move_thread = MoveThread(self.move, *move_args, **move_kwargs)
        self.move_thread.finished_signal.connect(self.update_ui)  # 连接信号以在任务完成时更新UI
        self.move_thread.start()

    def move(self, *args, **kwargs):
        # 在这里执行带有参数的 self.move 函数
        print("Move function with args:", args)
        print("Move function with kwargs:", kwargs)
        time.sleep(3)  # 模拟耗时操作

    @Slot()
    def update_ui(self):
        # 在主线程中更新UI
        self.label.setText("任务完成！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
