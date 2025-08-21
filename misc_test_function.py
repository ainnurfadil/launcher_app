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




class LauncherApps(QtWidgets.QMainWindow):
    def _init_(self):
        super()._init_()
        self._init_private_properties()
        self._setup_ui()
        self._setup_events()

    def _init_private_properties(self):
        self.panel_button = ButtonAppsHolder()
        self.panel_info = InfoSidePanel()
        self.panel_list = DepartmentList()
        self.panel_search = EditText()

    def _setup_ui(self):
        self.setWindowTitle("Apps Launcher")
        self.setFixedSize(1500, 900)
        self.panel_button.setFixedSize(700, 800)
        self.panel_info.setFixedSize(500, 800)
        self.panel_list.setFixedSize(300, 900)
        self.panel_search.setFixedSize(1170, 60)

        layout_content = QtWidgets.QHBoxLayout()
        layout_content.addWidget(self.panel_button)
        layout_content.addWidget(self.panel_info)
        content_widget = QtWidgets.QWidget()
        content_widget.setLayout(layout_content)
        content_widget.setFixedSize(1200, 800)

        layout_content_vertical = QtWidgets.QVBoxLayout()
        layout_content_vertical.addWidget(self.panel_search)
        layout_content_vertical.addWidget(content_widget)
        right_side_content = QtWidgets.QWidget()
        right_side_content.setLayout(layout_content_vertical)
        right_side_content.setFixedSize(1200, 850)

        all_layout_result = QtWidgets.QHBoxLayout()
        all_layout_result.addWidget(self.panel_list)
        all_layout_result.addWidget(right_side_content)
        result = QtWidgets.QWidget()
        result.setLayout(all_layout_result)
        result.setFixedSize(1500, 900)
        self.setCentralWidget(result)

    def _setup_events(self):
        self.panel_list.path_selected.connect(self.panel_button.select_department)
        self.panel_button.list_transfer.connect(self.panel_info.get_connect_from_button)
        self.panel_search.search_text_signal.connect(self.panel_button.get_signal_from_search)


class ButtonAppsHolder(QtWidgets.QWidget):
    list_transfer = QtCore.Signal(list)

    def _init_(self, parent=None):
        super()._init_(parent)
        self._init_private_properties()
        self._setup_ui()
        self._setup_events()

    def _init_private_properties(self):
        self.root_dir = None
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.setExclusive(True)
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

    def _setup_ui(self):
        self.grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.grid.setContentsMargins(10, 10, 10, 10)

    def _setup_events(self):
        pass  # Add event connections if needed

    # ...rest of your methods...


class DepartmentList(QtWidgets.QWidget):
    path_selected = QtCore.Signal(str)

    def _init_(self):
        super()._init_()
        self._init_private_properties()
        self._setup_ui()
        self._setup_events()

    def _init_private_properties(self):
        self.root_dir = "lmn_tools"
        self.list_dir = []

    def _setup_ui(self):
        self.list_department = QtWidgets.QListWidget()
        self.list_department.setFixedSize(290, 850)
        for item in os.listdir(self.root_dir):
            temp_dir = os.path.join(self.root_dir, item)
            if os.path.isdir(temp_dir):
                self.list_dir.append(item)
        self.list_department.addItems(self.list_dir)
        list_layout = QtWidgets.QVBoxLayout()
        list_layout.addWidget(self.list_department)
        self.setLayout(list_layout)

    def _setup_events(self):
        self.list_department.itemClicked.connect(self.get_list_dir_name)

    def get_list_dir_name(self, item):
        self.item_text = item.text()
        self.path_department = os.path.join(self.root_dir, self.item_text)
        print(f"emmit{self.path_department}")
        self.path_selected.emit(self.path_department)


class InfoSidePanel(QtWidgets.QWidget):
    def _init_(self):
        super()._init_()
        self._init_private_properties()
        self._setup_ui()
        self._setup_events()

    def _init_private_properties(self):
        self.info_layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(450, 800)

    def _setup_ui(self):
        self.setLayout(self.info_layout)

    def _setup_events(self):
        pass  # Add event connections if needed

    # ...rest of your methods...


class EditText(QtWidgets.QWidget):
    search_text_signal = QtCore.Signal(str)

    def _init_(self):
        super()._init_()
        self._init_private_properties()
        self._setup_ui()
        self._setup_events()

    def _init_private_properties(self):
        pass

    def _setup_ui(self):
        self.text_bar = QtWidgets.QLineEdit()
        self.text_bar.setPlaceholderText("Search Here")
        self.text_bar.setFixedSize(1130, 50)
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.text_bar)
        self.setLayout(layout)

    def _setup_events(self):
        self.text_bar.textChanged.connect(self.get_signal_text)

    def get_signal_text(self, text):
        self.search_text_signal.emit(text)
