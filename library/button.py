from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout
import sys
import os
from . import list_department


class ButtonAppsHolder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # apps1Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 1",parent=self)
        # apps1Button.setFixedSize(100,100)

        rootDir = list_department.DepartmentList.main()

        getListDir = [f for f in os.listdir(rootDir) if os.path.isdir(os.path.join(rootDir, f))]
        
        grid = QGridLayout()

        positions = [(i,j) for i in range(4) for j in range(3)]

        for positions, getListDir in zip(positions, getListDir):
            button = QPushButton(getListDir)
            button.setFixedSize(200,100)
            button.setCheckable(True)

            grid.addWidget(button, *positions)

        self.setLayout(grid)



if __name__ == "__main__":
    app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya
    # Membuat window
    window = ButtonAppsHolder()
    window.show()
    # memulai event loop
    app.exec()