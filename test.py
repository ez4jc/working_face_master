from PySide6.QtWidgets import QApplication, QProgressDialog, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt, QThread, Signal


class WorkerThread(QThread):
    update_progress = Signal(int)

    def run(self):
        # Simulate a time-consuming task
        for i in range(101):
            self.update_progress.emit(i)
            self.msleep(50)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create a button to start the process
        start_button = QPushButton("Start Process")
        start_button.clicked.connect(self.start_process)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def start_process(self):
        # Create a progress dialog
        progress_dialog = QProgressDialog(self)
        progress_dialog.setWindowModality(Qt.WindowModal)
        progress_dialog.setWindowTitle('Loading...')
        progress_dialog.setLabelText('Please wait...')
        progress_dialog.setCancelButton(None)  # Disable the cancel button
        progress_dialog.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Connect the canceled signal to the terminate method of the worker thread
        progress_dialog.canceled.connect(worker_thread.terminate)

        # Connect the finished signal of the progress dialog to a custom slot
        progress_dialog.finished.connect(self.on_progress_dialog_finished)

        # Connect the custom update_progress signal of the worker thread to set the progress value
        worker_thread.update_progress.connect(progress_dialog.setValue)

        # Start the worker thread and show the progress dialog
        worker_thread.start()
        progress_dialog.exec()

    def on_progress_dialog_finished(self):
        print("Process completed!")
        # Your code to execute after the process completes


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()

    worker_thread = WorkerThread()
    app.exec_()
