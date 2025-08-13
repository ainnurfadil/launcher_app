# Mengimport componen dari Qt
import sys
import os

from PySide6 import QtWidgets, QtCore, QtGui
# import library as library

# UI
class LauncherApps(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apps Launcher")

        panel_button = ButtonAppsHolder()
        panel_info = InfoSidePanel()
        panel_list = DepartmentList()
        panel_search = EditText()

        # layout apps content
        layout_content = QtWidgets.QHBoxLayout()
        layout_content.addWidget(panel_button)
        layout_content.addWidget(panel_info)

        content_widget = QtWidgets.QWidget()
        content_widget.setLayout(layout_content)

        # apps content combine with search bar
        layout_content_vertical = QtWidgets.QVBoxLayout()
        layout_content_vertical.addWidget(panel_search)
        layout_content_vertical.addWidget(content_widget)

        right_side_content = QtWidgets.QWidget()
        right_side_content.setLayout(layout_content_vertical)

        # Final layout
        all_layout_result = QtWidgets.QHBoxLayout()
        all_layout_result.addWidget(panel_list)
        all_layout_result.addWidget(right_side_content)

        result = QtWidgets.QWidget()
        result.setLayout(all_layout_result)

        # menampung sinyal
        panel_list.path_selected.connect(panel_button.select_department)

        self.setCentralWidget(result)

# Button apps
class ButtonAppsHolder(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # apps1Button = QPushButton(icon=QIcon("icon\owl.png"),text="apps 1",parent=self)
        # apps1Button.setFixedSize(100,100)
        self.root_dir = None
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)

    def select_department(self, department):
        self.update_root_dir(department)

    def update_root_dir(self, path):
        self.root_dir = path
        print(f"selected dir : {self.root_dir}")

        self.cleanup_button()

        # ubah jadi long hand
        
        # self.getListDir = [f for f in os.listdir(self.root_dir) if os.path.isdir(os.path.join(self.root_dir, f))]
        self.getListDir = []
        for f in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir, f)
            if os.path.isdir(full_path):
               self.getListDir.append(f)
            
        # self.positions = [(i,j) for i in range(4) for j in range(3)] i and j change to row and col
        self.positions = []
        for row in range(4):
            for col in range(3):
                self.positions.append((row,col))

        for positions, getDir in zip(self.positions, self.getListDir):
            button = QtWidgets.QPushButton(getDir)
            button.setFixedSize(200, 100)
            button.setCheckable(True)
            self.grid.addWidget(button, *positions)

    def cleanup_button(self):
        for i in reversed(range(1, self.grid.count())):
            if i == 0:
                continue  
            widget = self.grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)

# List Department
class DepartmentList(QtWidgets.QWidget):
    path_selected = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

        list_department = QtWidgets.QListWidget()

        self.root_dir = r"I:\workspace-devstage\RND\fadil\launcher_app\lmn_tools"

        self.list_dir = []
        for item in os.listdir(self.root_dir):
            temp_dir = os.path.join(self.root_dir, item)
            if os.path.isdir(temp_dir):
                self.list_dir.append(item)

        list_department.addItems(self.list_dir)
        list_department.itemClicked.connect(self.get_list_dir_name)

        list_layout = QtWidgets.QVBoxLayout()
        list_layout.addWidget(list_department)

        self.setLayout(list_layout)

    def get_list_dir_name(self, item):
        self.item_text = item.text()
        self.path_department = os.path.join(self.root_dir, self.item_text)
        self.path_selected.emit(self.path_department)

# Info Panel
class InfoSidePanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Label Judul Applikasi
        title_apps = QtWidgets.QLabel("Apps 1")
        title_apps.setFixedSize(500, 50)

        # Label Icon applikasi
        icon_apps = QtWidgets.QLabel()
        icon_apps.setFixedSize(500, 500)
        icon_apps.setPixmap(QtGui.QPixmap("icon\owl.png"))

        # Information Window
        apps_description = QtWidgets.QPlainTextEdit()
        apps_description.setFixedSize(500, 50)
        apps_description.insertPlainText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet tortor nec velit facilisis finibus. Quisque quis gravida leo, vitae blandit est. Suspendisse potenti. Duis mattis odio a turpis congue pharetra. Aliquam erat ex, tincidunt ut hendrerit a, vehicula scelerisque risus. Fusce fermentum mauris ac lacus mollis, et iaculis elit scelerisque. Mauris eu pharetra magna. Suspendisse vestibulum sagittis urna, ut suscipit ligula efficitur ut.")

        # Button Run
        run_button = QtWidgets.QPushButton("RUN")
        run_button.setFixedSize(500, 50)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title_apps)
        layout.addWidget(icon_apps)
        layout.addWidget(apps_description)
        layout.addWidget(run_button)

        self.setLayout(layout)

# Search Bar
class EditText(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        textBar = QtWidgets.QLineEdit("Search Here")
        textBar.setFixedSize(500, 50)

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(textBar)

        self.setLayout(layout)


# seperti pembungkus dari semua program untuk di jalankan programnya
app = QtWidgets.QApplication(sys.argv)

# Membuat window
window = LauncherApps()
window.show()

# memulai event loop
app.exec()
