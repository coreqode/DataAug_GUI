

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog, )
from PyQt5.QtGui import QFont

import test
import transfer
import copy
import os


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 500, 500)
        self.value1 = None
        self.value2 = None
        self.value3 = None
        self.value4 = None
        self.output = None
        self.image_size = None
        self.cpu = True
        self.unpool= None
        self.e = None
        self.d = None
        self.s = None
        self.a = None
        self.alpha = None

        self.originalPalette = QApplication.palette()

        self.myFont = QFont()
        self.myFont.setBold(True)

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox(
            "&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")
        generate_folder = QPushButton("Generate Folders")
        generate_folder.clicked.connect(lambda: self.generate_folder())

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftGroupBox()
        disableWidgetsCheckBox.toggled.connect(
            self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(
            self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(
            self.bottomLeftGroupBox.setDisabled)
        


        topLayout = QHBoxLayout()
        topLayout.addStretch(1)
        topLayout.addWidget(generate_folder)
        topLayout.addWidget(disableWidgetsCheckBox)


        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftGroupBox, 2,0 )
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("DataAug Tool")

    def generate_folder(self):
        directory = os.getcwd()
        path = directory + '/DataAugOutputs'
        os.mkdir(os.path.join(directory, 'DataAugOutputs'))
        os.mkdir(os.path.join(path, 'target_image'))
        os.mkdir(os.path.join(path, 'target_masks'))
        os.mkdir(os.path.join(path, 'style_image'))
        os.mkdir(os.path.join(path, 'style_masks'))
    
    def file_picker(self, string):
        filename = QFileDialog.getExistingDirectory(self, 'Pick Folder Path')
        if string == 'Target Image folder path':
            self.value1 = filename
        elif string == 'Target Image masks folder path':
            self.value2 = filename
        elif string == 'Style Image folder path':
            self.value3 = filename
        elif string == 'Style Image masks folder path':
            self.value4 = filename
        print(string)

    def runScript(self, use_cpu, image_size, alpha,e, d, s, a, unpooling ):
        print(use_cpu)
        print(image_size)
        print(alpha)
        print(e, d, s, a)
        print(unpooling)

        # transfer.main(self.value1, self.value2, self.value3, self.value4)

    def createTopLeftGroupBox(self):
################# CUSTOM #######################################
        self.custom = QGroupBox()
        pushButton1 = QPushButton("Target Image folder path")
        pushButton2 = QPushButton("Target Image masks folder path")
        pushButton3 = QPushButton("Style Image folder path")
        pushButton4 = QPushButton("Style Image masks folder path")
        layout = QVBoxLayout()
        layout.addWidget(pushButton1)
        layout.addWidget(pushButton2)
        layout.addWidget(pushButton3)
        layout.addWidget(pushButton4)
        pushButton1.clicked.connect(
            lambda: self.file_picker(pushButton1.text()))
        pushButton2.clicked.connect(
            lambda: self.file_picker(pushButton2.text()))
        pushButton3.clicked.connect(
            lambda: self.file_picker(pushButton3.text()))
        pushButton4.clicked.connect(
            lambda: self.file_picker(pushButton4.text()))

        self.custom.setLayout(layout)

###################################### SNOW ###########################
        self.snow = QGroupBox()
        self.topLeftGroupBox = QTabWidget()

        self.fog = QGroupBox()
        self.topLeftGroupBox = QTabWidget()
        self.topLeftGroupBox.addTab(self.custom, 'Custom')
        self.topLeftGroupBox.addTab(self.fog, 'Fog')
        self.topLeftGroupBox.addTab(self.snow, 'Snow')

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("INTRUCTIONS")

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        # layout.addWidget(defaultPushButton)
        # layout.addWidget(togglePushButton)
        # layout.addWidget(flatPushButton)
        # layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)
    
    def createBottomLeftGroupBox(self):
        self.bottomLeftGroupBox = QGroupBox("CONTROLS")

        use_cpu = QCheckBox('CPU')
        use_cpu.setChecked(True)
        e = QCheckBox('e')
        e.setChecked(True)
        d = QCheckBox('d')
        s = QCheckBox('s')
        a = QCheckBox('a')
        comboBox = QComboBox()
        comboBox.addItem('SUM')
        comboBox.addItem('CAT5')
        text1 = QLabel('Choose the unpooling options:')
        text2 = QLabel('Image Size:')
        text3 = QLabel('alpha:')
        text_box1 = QLineEdit('512')
        text_box2 = QLineEdit('1')

        runScript = QPushButton('Run Script')
        runScript.setStyleSheet("background-color: grey")
        layout = QVBoxLayout()
        layout_H1 = QHBoxLayout()
        layout_H2 = QHBoxLayout()

  
        layout_H1.addWidget(use_cpu)
        layout_H1.addWidget(e)
        layout_H1.addWidget(d)
        layout_H1.addWidget(s)
        layout_H1.addWidget(a)
        layout_H1.addStretch(1)

        layout.addLayout(layout_H1, stretch=True)
        layout.addWidget(text1)
        layout.addWidget(comboBox)
        layout_H2.addWidget(text2)
        layout_H2.addWidget(text_box1)
        layout_H2.addWidget(text3)
        layout_H2.addWidget(text_box2)
        layout.addLayout(layout_H2, stretch=True)
        layout.addStretch(1)
        layout.addWidget(runScript)
        runScript.clicked.connect(lambda: self.runScript(
            use_cpu.isChecked(), text_box1.text(), text_box2.text(),
            e.isChecked(), d.isChecked(), s.isChecked(), a.isChecked(),
            comboBox.currentText(),))

        self.bottomLeftGroupBox.setLayout(layout)
    


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    gallery = MainWindow()
    gallery.show()

    sys.exit(app.exec_())
