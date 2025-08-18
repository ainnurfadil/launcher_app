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
        panel_list.path_selected.connect(panel_button.select_department) # Dari sumber ke target sinyal
        panel_button.list_transfer.connect(panel_info.get_connect_from_button)

        self.setCentralWidget(result)

# Button apps
class ButtonAppsHolder(QtWidgets.QWidget):
    list_transfer = QtCore.Signal(list)

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
        
        # self.get_list_dir = [f for f in os.listdir(self.root_dir) if os.path.isdir(os.path.join(self.root_dir, f))]
        # To get Directory ptah address
        self.get_list_dir = []
        for dir in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir, dir)
            if os.path.isdir(full_path):
               self.get_list_dir.append(dir)

        # print(self.get_list_dir)
        # output ['AdvancedRenamer', 'PureRef', 'ReNamer', 'ScreenToGif', 'UpdateCinesync', 'VideoToGif']

        # get path file .png
        self.get_file_png_list = []
        for png_file in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir,png_file) # mendapatkan path directoriy
            png_found = None        # Nilai awal ketika tidak di temukan file PNG
            # print(full_path)
            if os.path.isdir(full_path):
                for a in os.listdir(full_path):
                    b = os.path.join(full_path,a)
                    # print(b)
                    if os.path.isfile(b):
                        if b.endswith(".png"):
                            png_found = b       # Ketika file PNG di temukan akan mengangkut nilai berupa path address
            
            if png_found is not None:
                self.get_file_png_list.append(png_found)    # jika terdapat nilai paath maka akan di append
            else:
                self.get_file_png_list.append("")           # jika tidak akan mengirim string kosong

        # print(self.get_file_png_list)

        # get path file .txt
        self.get_file_txt_list = []
        for txt_file in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir,txt_file) # mendapatkan path directoriy
            txt_found = None        # Nilai awal ketika tidak di temukan file TXT
            # print(full_path)
            if os.path.isdir(full_path):
                for a in os.listdir(full_path):
                    b = os.path.join(full_path,a)
                    # print(b)
                    if os.path.isfile(b):
                        if b.endswith(".txt"):
                            txt_found = b       # Ketika file TXT di temukan akan mengangkut nilai berupa path address
            
            if txt_found is not None:
                self.get_file_txt_list.append(txt_found)    # jika terdapat nilai paath maka akan di append
            else:
                self.get_file_txt_list.append("")           # jika tidak akan mengirim string kosong
       
        # get path file .lnk
        self.get_file_lnk_list = []
        for lnk_file in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir,lnk_file) # mendapatkan path directoriy
            lnk_found = None        # Nilai awal ketika tidak di temukan file TXT
            # print(full_path)
            if os.path.isdir(full_path):
                for a in os.listdir(full_path):
                    b = os.path.join(full_path,a)
                    # print(b)
                    if os.path.isfile(b):
                        if b.endswith(".lnk"):
                            lnk_found = b       # Ketika file TXT di temukan akan mengangkut nilai berupa path address
            
            if lnk_found is not None:
                self.get_file_lnk_list.append(lnk_found)    # jika terdapat nilai paath maka akan di append
            else:
                self.get_file_lnk_list.append("")           # jika tidak akan mengirim string kosong

            
        # self.positions = [(i,j) for i in range(4) for j in range(3)] i and j change to row and col
        # To get positions coloumb coordinate
        self.positions = []
        for row in range(4):
            for col in range(3):
                self.positions.append((row,col))

        # button properties
        for positions, get_dir, get_png, get_txt, get_lnk in zip(self.positions, self.get_list_dir, self.get_file_png_list, self.get_file_txt_list, self.get_file_lnk_list):
            data_list_each_button = [get_dir,get_png,get_txt,get_lnk]
            button = QtWidgets.QPushButton(icon=QtGui.QIcon(get_png),text=get_dir)
            button.setFixedSize(200, 100)
            button.setCheckable(True)
            button.clicked.connect(lambda checked, data=data_list_each_button: self.slot_data_button_checked(data))

            self.grid.addWidget(button, *positions)
            # print(self.data_list_each_button)

    def cleanup_button(self):
        for i in reversed(range(0, self.grid.count())):
            if i == 0:
                continue  
            widget = self.grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def slot_data_button_checked(self,data_list_each_button):
        get_list_data_button = data_list_each_button
        print(f"emit from slot_data_button_checked= {get_list_data_button}")
        self.list_transfer.emit(get_list_data_button)
        


# List Department
class DepartmentList(QtWidgets.QWidget):
    path_selected = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

        list_department = QtWidgets.QListWidget()

        self.root_dir = r"J:\learn code\launcher_app\lmn_tools"

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
        print(f"emmit{self.path_department}")
        self.path_selected.emit(self.path_department)

# Info Panel
class InfoSidePanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Layout
        self.info_layout = QtWidgets.QVBoxLayout()

        self.setLayout(self.info_layout)
    
    def get_connect_from_button(self, details):
        self.update_details_information(details)

    def update_details_information(self, list_details):
        list_button_details = list_details             # Urutan data list yang di dapat [get_dir,get_png,get_txt,get_lnk]
        self.title_list = list_button_details[0]
        self.icon_list = list_button_details[1]
        self.description_list = list_button_details[2]
        self.shortcut_list = list_button_details[3]

        # print(f"got data list from button: {self.title_list}")
        # print(f"got data list from button: {self.icon_list}")
        # print(f"got data list from button: {self.description_list}")
        # print(f"got data list from button: {self.shortcut_list}")
        self.delete_layout_information()

        file = open(self.description_list, mode="r")


        # Label Judul Applikasi
        title_apps = QtWidgets.QLabel(f"{self.title_list}")
        title_apps.setFixedSize(500, 50)

        # Label Icon applikasi
        icon_apps = QtWidgets.QLabel()
        icon_apps.setFixedSize(500, 250)
        icon_apps.setPixmap(QtGui.QPixmap(self.icon_list))

        # Information Window
        apps_description = QtWidgets.QPlainTextEdit()
        apps_description.setFixedSize(500, 250)
        apps_description.insertPlainText(file.read())

        # Button Run
        run_button = QtWidgets.QPushButton("RUN")
        run_button.setFixedSize(500, 50)

        self.info_layout.addWidget(title_apps)
        self.info_layout.addWidget(icon_apps)
        self.info_layout.addWidget(apps_description)
        self.info_layout.addWidget(run_button)

    def delete_layout_information(self):
        for item in reversed(range(0,self.info_layout.count())):
            if item == 0:
                continue
            widget_item = self.info_layout.itemAt(item)
            if widget_item is not None:
                widget = widget_item.widget()
                if widget is not None:
                    widget.setParent(None)


    

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
