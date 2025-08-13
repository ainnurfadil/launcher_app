import sys
from PySide6.QtCore import pyqtSignal, QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
import os

class LauncherApps(QListWidget):
    def __init__(self):
        dir_path = r"I:\workspace-devstage\RND\fadil\launcher_app\lmn_tools\01 General"


    def get_file_png_path(self):
        pass



app = QApplication(sys.argv)

# Membuat window
window = LauncherApps()
window.show()

# memulai event loop
app.exec()