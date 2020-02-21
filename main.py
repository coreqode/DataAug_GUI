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
from prepare_dataset import jpg_to_png


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 500, 500)
        self.image_path = None
        self.mask_path = None
        self.dest_path = None
        self.style_image_path = None
        self.style_mask_path = None
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

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftGroupBox()
        self.createBottomRightGroupBox()
        disableWidgetsCheckBox.toggled.connect(
            self.prepare_dataset.setDisabled)
        disableWidgetsCheckBox.toggled.connect(
            self.instructions.setDisabled)
        disableWidgetsCheckBox.toggled.connect(
            self.controls.setDisabled)
        disableWidgetsCheckBox.toggled.connect(
            self.instructions2.setDisabled)
        


        topLayout = QHBoxLayout()
        topLayout.addStretch(1)
        topLayout.addWidget(disableWidgetsCheckBox)


        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.prepare_dataset, 1, 0)
        mainLayout.addWidget(self.instructions, 1, 1)
        mainLayout.addWidget(self.controls, 2,0 )
        mainLayout.addWidget(self.instructions2, 2,1 )
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("DataAug Tool")
    
    def folder_picker(self, string):
        filename = QFileDialog.getExistingDirectory(self, 'Pick Folder Path')
        if string == 'Image Directory':
            self.image_path = filename
        elif string == 'Masks Directory':
            self.mask_path = filename
        elif string == 'Destination Directory':
            self.dest_path = filename

    def file_picker(self, string):
        filename = QFileDialog.getOpenFileName(self, 'Pick file name')[0]
        if string == "Style Image Path":
            self.style_image_path = filename
        elif string == "Style Mask Path":
            self.style_mask_path = filename


    def runScript(self, use_cpu, image_size, alpha,e, d, s, a, unpooling ):
        self.image_size = image_size
        self.cpu = use_cpu
        self.unpool= unpooling
        self.e = e
        self.d = d
        self.s = s
        self.a = a
        self.alpha = alpha
        transfer.main(self.image_size, self.cpu, self.unpool, self.e, self.d, self.s, self.a, self.alpha)
    
    def preparedDataset(self, string):
        path = os.getcwd()
        if string == "Fog1":
            self.style_image_path = path + "/styles/images/fog/0.png"
            self.style_mask_path = path + "/styles/masks/fog/0.png"
        elif string == "Fog2":
            self.style_image_path = path + "/styles/images/fog/2.png"
            self.style_mask_path = path + "/styles/masks/fog/2.png"
        elif string == "Fog3":
            self.style_image_path = path + "/styles/images/fog/5.png"
            self.style_mask_path = path + "/styles/masks/fog/5.png"
        elif string == 'Snow1':
            self.style_image_path = path + "/styles/images/snowy/0.png"
            self.style_mask_path = path + "/styles/masks/snowy/0.png"
        elif string == 'Snow2':
            self.style_image_path = path + "/styles/images/snowy/2.png"
            self.style_mask_path = path + "/styles/masks/snowy/2.png"
        elif string == 'Snow3':
            self.style_image_path = path + "/styles/images/snowy/5.png"
            self.style_mask_path = path + "/styles/masks/snowy/5.png"
        elif string == 'Shadow':
            self.style_image_path = path + "/styles/images/shadow/1.png"
            self.style_mask_path = path + "/styles/masks/shadow/1.png"
        elif string == 'Night':
            self.style_image_path = path + "/styles/images/night/2.png"
            self.style_mask_path = path + "/styles/masks/night/2.png"
        elif string == 'Dusk':
            self.style_image_path = path + "/styles/images/dusk/0.png"
            self.style_mask_path = path + "/styles/masks/dusk/0.png"


        jpg_to_png(self.image_path, self.mask_path, self.dest_path, self.style_image_path, self.style_mask_path, string)


    def createTopLeftGroupBox(self):
        self.prepare_dataset = QGroupBox("PREPARE DATASET")

        self.customCheck = QCheckBox('Custom')

        self.pushButton1 = QPushButton("Image Directory")
        self.pushButton2 = QPushButton("Masks Directory")
        self.pushButton3 = QPushButton("Style Image Path")
        self.pushButton3.setDisabled(True)
        self.pushButton4 = QPushButton("Style Mask Path")
        self.pushButton4.setDisabled(True)
        self.pushButton5 = QPushButton("Destination Directory")
        text = QLabel("Choose the style :")
        prepareDataset = QPushButton("Prepare Dataset")
        prepareDataset.setStyleSheet("background-color: grey")
        comboBox = QComboBox()
        comboBox.addItem('Fog1')
        comboBox.addItem('Fog2')
        comboBox.addItem('Fog3')
        comboBox.addItem('Dusk')
        comboBox.addItem('Snow1')
        comboBox.addItem('Snow2')
        comboBox.addItem('Snow3')
        comboBox.addItem('Shadow')
        comboBox.addItem('Night')


        layout =QVBoxLayout()
        layout_H = QHBoxLayout()
        layout_H.addWidget(text)
        layout_H.addWidget(comboBox)

        layout.addWidget(self.customCheck)
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        layout.addWidget(self.pushButton3)
        layout.addWidget(self.pushButton4)
        layout.addLayout(layout_H, stretch=True)
        layout.addWidget(self.pushButton5)
        layout.addWidget(prepareDataset)

        self.pushButton1.clicked.connect(
            lambda: self.folder_picker(self.pushButton1.text()))
        self.pushButton2.clicked.connect(
            lambda: self.folder_picker(self.pushButton2.text()))        
        self.pushButton3.clicked.connect(
            lambda: self.file_picker(self.pushButton3.text()))        
        self.pushButton4.clicked.connect(
            lambda: self.file_picker(self.pushButton4.text()))        
        self.pushButton5.clicked.connect(
            lambda: self.folder_picker(self.pushButton5.text()))        

        prepareDataset.clicked.connect(
            lambda: self.preparedDataset(comboBox.currentText()))  

        self.customCheck.toggled.connect(self.pushButton3.setEnabled)
        self.customCheck.toggled.connect(self.pushButton4.setEnabled)
        self.customCheck.toggled.connect(text.setDisabled)
        self.customCheck.toggled.connect(comboBox.setDisabled)

        self.prepare_dataset.setLayout(layout)

    def createTopRightGroupBox(self):
        self.instructions = QGroupBox("INTRUCTIONS")
        text_label1 = QLabel("1. The model needs target image,\n"
        "    target mask, style image and style\n"
        "    mask for using the style transfer.\n"
        "                                  \n"
        "2.  You can choose few predefined\n"
        "     styles from the dropdown menu.\n"
        "                                 \n"
        "3.  Check the custom button to chose\n"
        "     your own style.\n"
        "                                   \n"
        "4.  Choose the destination directory\n"
        "     and prepare the dataset.\n"
        "                                   \n"
        "5.  Check the CPU button for using it\n"
        )
        # text_label1.setStyleSheet("font: 4pt Comic Sans MS")


        text_label1.setAlignment(Qt.AlignJustify)
        layout = QVBoxLayout()
        layout.addWidget(text_label1)
        self.instructions.setLayout(layout)
    
    def createBottomLeftGroupBox(self):
        self.controls = QGroupBox("CONTROLS")

        use_cpu = QCheckBox('CPU')
        e = QCheckBox('e')
        e.setChecked(True)
        d = QCheckBox('d')
        s = QCheckBox('s')
        a = QCheckBox('a')
        comboBox1 = QComboBox()
        comboBox1.addItem('sum')
        comboBox1.addItem('cat5')
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
        layout.addWidget(comboBox1)
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
            comboBox1.currentText()))

        self.controls.setLayout(layout)
    


    def createBottomRightGroupBox(self):
            self.instructions2 = QGroupBox()
            text_label1 = QLabel(
        "6.  e: style transfer at encoder\n"
        "     d: Style transfer at decoder\n"
        "     s: Style transfer at sumation\n"
        "     a: All images\n"
        "                                   \n"
        "7.  sum: Summation of skip connection\n"
        "     cat5: Concatenation\n"
        "                                   \n"
        "8.  Choose the image size of output\n"
        "                                   \n"
        "9.  Choose the blending ratio alpha\n"
        "                                   \n"
        "10. Run Script and Enjoy :)"
        )

            text_label1.setAlignment(Qt.AlignJustify)
            layout = QVBoxLayout()
            layout.addWidget(text_label1)
            self.instructions2.setLayout(layout)



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    gallery = MainWindow()
    gallery.show()

    sys.exit(app.exec_())
