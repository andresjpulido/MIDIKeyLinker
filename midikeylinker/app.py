import sys
from PyQt6.QtWidgets import ( 
    QApplication
) 

from MainWindow import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)

   # Load style file
    with open("./midikeylinker/style.qss") as f:
        style_str = f.read()
        app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
