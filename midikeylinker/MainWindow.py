import sys, os
import pandas as pd
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QListWidgetItem,
    QWidget,
    QGridLayout,
    QPushButton,
    QVBoxLayout,
    QLayout,
    QStyle,QFileDialog, QMenu
)
from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtGui import QIcon, QPixmap, QFont, QColor, QPicture, QCursor, QAction
from PyQt6 import QtSvg

# Import the UI class from the 'main_ui' module
from views.main import Ui_MainWindow
from TableModel import TableModel
import json

# Define a custom MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        # Set window properties
        self.setWindowIcon(QIcon("./resources/icon/logo.svg"))
        self.setWindowTitle("MIDI KeyLinker")
        self.listWidget = self.ui.listWidget
        self.detail_btn = self.ui.pushButton
        self.detail_btn.setCheckable(True)
        self.detail_btn.setChecked(False)
        self.tv_midimessages = self.ui.tv_midimessages

        self.linkButton = self.ui.linkButton
        self.linkButton.clicked.connect(self.linkButtonAction)

        self.listMidiDevices = [] 
        self.listMidiMessages = pd.DataFrame(
            [
                [4, 9, 2],
                [1, 0, 0],
                [2, 5, 0],
                [2, 3, 2],
                [7, 8, 9],
            ],
            columns=["DATA", "CMD", "CH"],
        )
        
        self.init_single_slot()
        self.init_tv_midimessages()

        self.label_keyboard_computer = self.ui.label_2
        self.label_keyboard_computer.setPixmap(QPixmap("./resources/images/keyboard.svg"))
        self.label_keyboard_computer.update()

        self.installEventFilter(self)
 
        self.qaction = self.ui.actionQuit 
        self.qaction.triggered.connect(self.quit)
        self.openFileAction = self.ui.openFileAction 
        self.openFileAction.triggered.connect(self.openFile)
        self.saveFileAction = self.ui.saveAction 
        self.saveFileAction.triggered.connect(self.saveFile)
        self.saveFileAsAction = self.ui.saveAsAction 
        self.saveFileAsAction.triggered.connect(self.saveFileAs)
        

        #TODO validate file exist
        self.loadFile(os.path.join(os.getcwd(), "midikeylinker/midikeylinker.pref"))
        

    def saveFile(self):
        print("save")

    def saveFileAs(self):
        print("save")
        #options = QFileDialog.options
        #options = QFileDialog.nativeParentWidget
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files(*);;Text Files(*.pref)" )
        if fileName:
            with open(fileName, 'w') as f:
                f.write("este texto")
            self.fileName = fileName
            self.setWindowTitle(str(os.path.basename(fileName)) + " - Notepad Alpha[*]")
 
    def openFile(self):    
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.',"Image files (*.pref)") 
        #print(fname)
        if type(fname) == tuple: 
            self.loadFile(fname[0]) 
    
    def loadFile(self, fname):
        print(fname)
         
        f = open(fname)
        data = json.load(f)

        self.listMidiDevices = data['devices']
        self.init_list_widget()

        for i in data['devices']:
            print("-")
        
        # Closing file
        f.close()

    def quit(self): 
        #app.quit()
        print("quit")

    
    def linkButtonAction(self):
        print("save link")

    def init_tv_midimessages(self):
        # self.listWidget.clear()
        self.model = TableModel(self.listMidiMessages)
        self.tv_midimessages.setModel(self.model)
        for msg in self.listMidiMessages:
            print("----- ", msg)

    def init_single_slot(self):
        self.detail_btn.toggled["bool"].connect(self.listWidget.setHidden)
        self.detail_btn.toggled.connect(self.button_icon_change)

    def createDeviceContextMenu(self ):
        print("creating context menu for element ")
        self.context_menu = QMenu()
        action1 = self.context_menu.addAction("Action1") 
        action1.triggered.connect(self.test)
        self.show()

    def test(self):
        print("this is a test") 

    def init_list_widget(self):
        self.listWidget.clear()
        print(self.listMidiDevices)

        for menu in self.listMidiDevices:

            itemN = QListWidgetItem()
            # Create widget
            widget = QWidget()
            widget.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
 
            widgetText = QLabel("")
            if len(menu.get("icon")) != 0:
                pixmap = QPixmap(menu.get("icon"))
                
            else:
                pixmap = QPixmap("./resources/icon/generic-midi-device.svg")
            pixmap.scaledToHeight(100)
            pixmap.scaledToWidth(150)
            widgetText.setPixmap(pixmap)
            widgetText.setFixedSize(150, 100)
            widgetText.setScaledContents(True)
            widgetText.setStyleSheet("margin-bottom:0; color:white")

            widgetLabel = QLabel(menu.get("name"))
            widgetLabel.setStyleSheet("margin-top:0; color:white; padding-top:10")
            widgetLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            widgetLayout = QVBoxLayout()
            widgetLayout.addWidget(widgetText)
            widgetLayout.addWidget(widgetLabel)
            widgetLayout.setContentsMargins(0, 0, 0, 0)
            widgetLayout.setSpacing(0)

            # widgetLayout.setSizeConstraint(QLayout.)
            widget.setLayout(widgetLayout)
            widget.setStyleSheet("margin: 10; ")
            
            itemN.setSizeHint(widget.sizeHint())
            itemN.setBackground(QColor(45, 44, 44, 0))
            itemN.text= 'x'
            widget.setStatusTip( menu.get("name"))  

            self.popMenu = QMenu(self)
            self.popMenu.addAction(QAction('test0', self))

            # Add widget to QListWidget funList
            self.listWidget.addItem(itemN) 
            self.listWidget.setItemWidget(itemN, widget)
            self.listWidget.setCurrentRow(0)

        self.listWidget.installEventFilter(self)
 

    def init_stackwidget(self):
        print("content")

    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.detail_btn.setIcon(QIcon("./resources/icon/arrow-next.svg"))
        else:
            self.detail_btn.setIcon(QIcon("./resources/icon/arrow-prev.svg"))

    def delete_device(self):
        item = self.listWidget.currentItem()
        index = self.listWidget.indexFromItem(item).row()
        self.listWidget.takeItem(index)
         
    def edit_device(self): 
        print('edit_device')
        
    def test_device(self): 
        print('test_device')

    def eventFilter(self, source, event): 
        #self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)

        if event.type() == QEvent.Type.KeyRelease:
            print("KeyPress: ",  event.type(), "    ", event.key(), "    ", source)
            #self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
 
        if event.type() ==  QEvent.Type.ContextMenu and source is self.listWidget:
            menu = QMenu()
            
            edit_device_action = QAction("Edit", None)
            edit_device_action.triggered.connect(self.edit_device)
            menu.addAction(edit_device_action)  

            test_device_Action = QAction("Test", None)
            test_device_Action.triggered.connect(self.test_device)
            menu.addAction(test_device_Action)

            delete_device_Action = QAction("Delete", None)
            delete_device_Action.triggered.connect(self.delete_device)
            menu.addAction(delete_device_Action)           
 
            menu.exec(event.globalPos())
 
            return True
        
        return super().eventFilter(source, event)