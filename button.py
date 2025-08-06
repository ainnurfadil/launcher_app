from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout
import sys

class ButtonAppsHolder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        apps1Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 1",parent=self)
        apps1Button.setFixedSize(100,100)
        
        apps2Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 2",parent=self)
        apps2Button.setFixedSize(100,100)

        apps3Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 3",parent=self)
        apps3Button.setFixedSize(100,100)
        
        apps4Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 4",parent=self)
        apps4Button.setFixedSize(100,100)
        
        apps5Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 5",parent=self)
        apps5Button.setFixedSize(100,100)
        
        grid = QGridLayout()
        grid.addWidget(apps1Button, 0, 0)
        grid.addWidget(apps2Button, 0, 2)
        grid.addWidget(apps3Button, 1, 0)
        grid.addWidget(apps4Button, 1, 1)
        grid.addWidget(apps5Button, 1, 2)
        
        self.setLayout(grid)


if __name__ == "__main__":
    app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya
    # Membuat window
    window = ButtonAppsHolder()
    window.show()
    # memulai event loop
    app.exec()