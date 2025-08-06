from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout
import sys

class DepartmentList(QWidget):
    def __init__(self):
        super().__init__()
        listDepartment = QListWidget()

        listDepartment.addItem("Concept")
        listDepartment.addItem("Modeling")
        listDepartment.addItem("Layout")
        listDepartment.addItem("Animation")

        listDepartment.itemClicked.connect()

        layout = QVBoxLayout()
        layout.addItem(listDepartment)

        self.setLayout(layout)

        



if __name__ == "__main__":
    app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya
    # Membuat window
    window = DepartmentList()
    window.show()
    # memulai event loop
    app.exec()

