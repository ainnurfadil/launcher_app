from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout
import sys
import os

class DepartmentList(QWidget):
    def __init__(self):
        super().__init__()
        listDepartment = QListWidget()

        rootDir = "C:\workspace\learning\lmn_tools"

        getListDir = [f for f in os.listdir(rootDir) if os.path.isdir(os.path.join(rootDir, f))]

        listDepartment.addItems(getListDir)
 
        # listDepartment.itemClicked.connect()

        listLayout = QVBoxLayout()
        listLayout.addWidget(listDepartment)

        # self

        self.setLayout(listLayout)

    # def getListDirName(self):


    # def selected_item(self):


        
if __name__ == "__main__":
    app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya
    # Membuat window
    window = DepartmentList()
    window.show()
    # memulai event loop
    app.exec()

