from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget     # Mengimport componen dari Qt
from search_bar import EditText
from info_panel import InfoSidePanel
from list_department import DepartmentList
from button import ButtonAppsHolder
import sys              # sys adalah modul untuk memprocess argumen command line

class LauncherApps(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Apps Launcher")

        panelButton = ButtonAppsHolder()
        panelInfo = InfoSidePanel()
        panelList = DepartmentList()
        panelSearch = EditText()

        # layout apps content
        layoutContent = QHBoxLayout()
        layoutContent.addWidget(panelButton)
        layoutContent.addWidget(panelInfo)

        contentWidget = QWidget()
        contentWidget.setLayout(layoutContent)
        
        # apps content combine with search bar
        layoutContentVertical = QVBoxLayout()
        layoutContentVertical.addWidget(panelSearch)
        layoutContentVertical.addWidget(contentWidget)

        rightSideContent = QWidget()
        rightSideContent.setLayout(layoutContentVertical)

        # Final layout
        allLayoutResult = QHBoxLayout()
        allLayoutResult.addWidget(panelList)
        allLayoutResult.addWidget(rightSideContent)

        result = QWidget()
        result.setLayout(allLayoutResult)

        self.setCentralWidget(result)


app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya

# Membuat window
window = LauncherApps()
window.show()

# memulai event loop
app.exec()