from PySide6.QtWidgets import QApplication, QWidget, QMainWindow     # Mengimport componen dari Qt
from list_department import MainWindow

import sys              # sys adalah modul untuk memprocess argumen command line

app = QApplication(sys.argv)        # seperti pembungkus dari semua program untuk di jalankan programnya

# Membuat window
window = MainWindow()

window.show()

# memulai event loop
app.exec()