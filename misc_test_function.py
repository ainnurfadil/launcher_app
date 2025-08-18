# ...existing code...

class ButtonAppsHolder(QtWidgets.QWidget):
    list_transfer = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.root_dir = None
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        self.last_checked_button = None  # Track last checked button

    def select_department(self, department):
        self.update_root_dir(department)

    def update_root_dir(self, path):
        self.root_dir = path
        print(f"selected dir : {self.root_dir}")

        self.cleanup_button()

        self.get_list_dir = []
        for dir in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir, dir)
            if os.path.isdir(full_path):
               self.get_list_dir.append(dir)

        self.get_file_png_list = []
        for png_file in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir,png_file)
            png_found = None
            if os.path.isdir(full_path):
                for a in os.listdir(full_path):
                    b = os.path.join(full_path,a)
                    if os.path.isfile(b) and b.endswith(".png"):
                        png_found = b
            self.get_file_png_list.append(png_found if png_found else "")

        self.get_file_txt_list = []
        for txt_file in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir,txt_file)
            txt_found = None
            if os.path.isdir(full_path):
                for a in os.listdir(full_path):
                    b = os.path.join(full_path,a)
                    if os.path.isfile(b) and b.endswith(".txt"):
                        txt_found = b
            self.get_file_txt_list.append(txt_found if txt_found else "")

        self.get_file_lnk_list = []
        for lnk_file in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir,lnk_file)
            lnk_found = None
            if os.path.isdir(full_path):
                for a in os.listdir(full_path):
                    b = os.path.join(full_path,a)
                    if os.path.isfile(b) and b.endswith(".lnk"):
                        lnk_found = b
            self.get_file_lnk_list.append(lnk_found if lnk_found else "")

        self.positions = []
        for row in range(4):
            for col in range(3):
                self.positions.append((row,col))

        for positions, get_dir, get_png, get_txt, get_lnk in zip(self.positions, self.get_list_dir, self.get_file_png_list, self.get_file_txt_list, self.get_file_lnk_list):
            data_list_each_button = [get_dir,get_png,get_txt,get_lnk]
            button = QtWidgets.QPushButton(icon=QtGui.QIcon(get_png),text=get_dir)
            button.setFixedSize(200, 100)
            button.setCheckable(True)
            button.clicked.connect(lambda checked, btn=button, data=data_list_each_button: self.slot_data_button_checked(btn, data))
            self.grid.addWidget(button, *positions)

    def cleanup_button(self):
        for i in reversed(range(0, self.grid.count())):
            if i == 0:
                continue  
            widget = self.grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.last_checked_button = None  # Reset last checked button

    def slot_data_button_checked(self, btn, data_list_each_button):
        # Uncheck previous button
        if self.last_checked_button and self.last_checked_button != btn:
            self.last_checked_button.setChecked(False)
        # Set current button as last checked
        self.last_checked_button = btn
        print(f"emit from slot_data_button_checked= {data_list_each_button}")
        self.list_transfer.emit(data_list_each_button)

# ...existing code...

class InfoSidePanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.info_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.info_layout)
    
    def get_connect_from_button(self, details):
        self.update_details_information(details)

    def update_details_information(self, list_details):
        list_button_details = list_details
        self.title_list = list_button_details[0]
        self.icon_list = list_button_details[1]
        self.description_list = list_button_details[2]
        self.shortcut_list = list_button_details[3]

        self.delete_layout_information()

        # Safely open and read file
        description_text = ""
        if self.description_list and os.path.isfile(self.description_list):
            with open(self.description_list, mode="r", encoding="utf-8") as file:
                description_text = file.read()

        title_apps = QtWidgets.QLabel(f"{self.title_list}")
        title_apps.setFixedSize(500, 50)

        icon_apps = QtWidgets.QLabel()
        icon_apps.setFixedSize(500, 250)
        if self.icon_list and os.path.isfile(self.icon_list):
            icon_apps.setPixmap(QtGui.QPixmap(self.icon_list))

        apps_description = QtWidgets.QPlainTextEdit()
        apps_description.setFixedSize(500, 250)
        apps_description.insertPlainText(description_text)

        run_button = QtWidgets.QPushButton("RUN")
        run_button.setFixedSize(500, 50)

        self.info_layout.addWidget(title_apps)
        self.info_layout.addWidget(icon_apps)
        self.info_layout.addWidget(apps_description)
        self.info_layout.addWidget(run_button)

    def delete_layout_information(self):
        for item in reversed(range(self.info_layout.count())):
            widget_item = self.info_layout.itemAt(item)
            if widget_item is not None:
                widget = widget_item.widget()
                if widget is not None:
                    widget.setParent(None)

# ...existing code...