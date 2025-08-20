import sys
import os

from PySide6 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")
        self.grid = QtWidgets.QVBoxLayout()
        
        self.set_layout = QtWidgets.QWidget()
        self.set_layout.setLayout(self.grid)
        
        # self.setLayout(self.grid)
        
        self.setCentralWidget(self.set_layout)
        
        two_button = ["1","2"]

        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.setExclusive(True)  # Only one button can be checked

        for item in two_button:
            button = QtWidgets.QPushButton(item)
            button.setCheckable(True)
            button.setChecked(False)
            self.button_group.addButton(button)
            button.clicked.connect(self.the_button_was_toggled)
            self.grid.addWidget(button)


    def the_button_was_toggled(self):
        # Find which button is checked
        for button in self.button_group.buttons():
            if button.isChecked():
                print(f"Button {button.text()} is checked")
                

app = QtWidgets.QApplication(sys.argv)

# Membuat window
window = MainWindow()
window.show()

# memulai event loop
app.exec()




