import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(330, 200)
        self.setWindowTitle("Testing")

def create_window() -> MainWindow:  # This is the function that we will test with pytest
    window = MainWindow()
    window.show()
    return window

def main():
    app = QApplication(sys.argv)
    window = create_window()
    app.exec()

if __name__ == '__main__':
    main()
