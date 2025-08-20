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




class EditText(QtWidgets.QWidget):
    search_text_changed = QtCore.Signal(str)  # Add this signal

    def __init__(self):
        super().__init__()
        self.textBar = QtWidgets.QLineEdit("Search Here")
        self.textBar.setFixedSize(1130, 50)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.textBar)
        self.setLayout(layout)

        self.textBar.textChanged.connect(self.emit_search_text)

    def emit_search_text(self, text):
        self.search_text_changed.emit(text)




class LauncherApps(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # ...existing code...
        panel_search = EditText()
        panel_search.setFixedSize(1170, 60)
        panel_search.setSizePolicy(QtWidgets.QSizePolicy.Fixed, 
                                   QtWidgets.QSizePolicy.Fixed)

        # ...existing code...

        panel_search.search_text_changed.connect(panel_button.filter_buttons_by_name)




class ButtonAppsHolder(QtWidgets.QWidget):
    # ...existing code...

    def filter_buttons_by_name(self, text):
        for button in self.button_group.buttons():
            if text.strip() == "":
                button.show()
            elif button.text().lower() == text.strip().lower():
                button.show()
            else:
                button.hide()



class ButtonAppsHolder(QtWidgets.QWidget):
    # ...existing code...

    def update_root_dir(self, path):
        # ...existing code...
        for positions, get_dir, get_png, get_txt, get_lnk in zip(self.positions, 
                                                                 self.get_list_dir, 
                                                                 self.get_file_png_list, 
                                                                 self.get_file_txt_list, 
                                                                 self.get_file_lnk_list):
            data_list_each_button = [get_dir,get_png,get_txt,get_lnk]
            
            # Add space before uppercase letters (except the first letter)
            display_text = ''.join([' ' + c if c.isupper() and i != 0 else c for i, c in enumerate(get_dir)])
            
            button = QtWidgets.QPushButton(icon=QtGui.QIcon(get_png),
                                           text=display_text)
            # ...existing code...
