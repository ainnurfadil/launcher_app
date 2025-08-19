# ...existing code...

class LauncherApps(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apps Launcher")
        self.setFixedSize(1400, 900)  # Set fixed window size

        panel_button = ButtonAppsHolder()
        panel_button.setFixedSize(700, 800)
        panel_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        panel_info = InfoSidePanel()
        panel_info.setFixedSize(500, 800)
        panel_info.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        panel_list = DepartmentList()
        panel_list.setFixedSize(300, 800)
        panel_list.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        panel_search = EditText()
        panel_search.setFixedSize(1100, 50)
        panel_search.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # layout apps content
        layout_content = QtWidgets.QHBoxLayout()
        layout_content.addWidget(panel_button)
        layout_content.addWidget(panel_info)

        content_widget = QtWidgets.QWidget()
        content_widget.setLayout(layout_content)
        content_widget.setFixedSize(1200, 800)

        # apps content combine with search bar
        layout_content_vertical = QtWidgets.QVBoxLayout()
        layout_content_vertical.addWidget(panel_search)
        layout_content_vertical.addWidget(content_widget)

        right_side_content = QtWidgets.QWidget()
        right_side_content.setLayout(layout_content_vertical)
        right_side_content.setFixedSize(1200, 850)

        # Final layout
        all_layout_result = QtWidgets.QHBoxLayout()
        all_layout_result.addWidget(panel_list)
        all_layout_result.addWidget(right_side_content)

        result = QtWidgets.QWidget()
        result.setLayout(all_layout_result)
        result.setFixedSize(1400, 900)

        # menampung sinyal
        panel_list.path_selected.connect(panel_button.select_department)
        panel_button.list_transfer.connect(panel_info.get_connect_from_button)

        self.setCentralWidget(result)

# ...existing code...