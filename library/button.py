from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout
import sys
import os
from .list_department import DepartmentList


class ButtonAppsHolder(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # apps1Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 1",parent=self)
        # apps1Button.setFixedSize(100,100)
        
        self.rootDir = None
        self.emitFromDepartmentList = DepartmentList()
        self.emitFromDepartmentList.pathSelected.connect(self.update_root_dir)

        self.grid = QGridLayout()
                

        self.setLayout(self.grid)

    def update_root_dir(self,path):
        self.rootDir = path
        print(f"selected dir : {self.rootDir}")
        getListDir = [f for f in os.listdir(self.rootDir) if os.path.isdir(os.path.join(self.rootDir, f))]
        positions = [(i,j) for i in range(4) for j in range(3)]
    
        for positions, getListDir in zip(positions, getListDir):
            button = QPushButton(getListDir)
            button.setFixedSize(200,100)
            button.setCheckable(True)
            self.grid.addWidget(button, *positions)
        # self.show_button()
        
    # def show_button(self):

    #     # for i in reversed(range(1, self.grid.count())):
    #     #     widget = self.grid.itemAt(i).widget()
    #     #     if widget:
    #     #         widget.setParent(None)

    #     # if not self.rootDir:
    #     #     return



if __name__ == "__main__":
    app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya
    # Membuat window
    window = ButtonAppsHolder()
    window.show()
    # memulai event loop
    app.exec()