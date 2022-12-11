import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PIL import Image

from App.New_UI import UiMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UiMainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
