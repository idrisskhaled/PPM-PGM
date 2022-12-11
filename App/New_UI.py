import os

from PIL import Image
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QFileDialog, QMainWindow
import numpy as np
import matplotlib.pyplot as plt
from App.methods import *


class UiMainWindow(QMainWindow):
    def __init__(self, MainWindow:QMainWindow):
        super(UiMainWindow, self).__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setFixedSize(706,433)
        MainWindow.setWindowIcon(QIcon("Images\App.jpg"))
        self.BackgroundWidget = QtWidgets.QWidget(self.centralwidget)
        self.MainWidget = QtWidgets.QWidget(self.centralwidget)
        self.HelpWidget = QtWidgets.QWidget(self.centralwidget)
        self.SettingsWidget = QtWidgets.QWidget(self.centralwidget)
        self.language1 = QtWidgets.QLabel(self.MainWidget)
        self.comboBox1 = QtWidgets.QComboBox(self.MainWidget)
        self.speed_value = QtWidgets.QLabel(self.MainWidget)
        self.speed = QtWidgets.QLabel(self.MainWidget)
        self.slider = QtWidgets.QSlider(self.MainWidget)
        self.treshold_red = QtWidgets.QLineEdit(self.MainWidget)
        self.treshold_green = QtWidgets.QLineEdit(self.MainWidget)
        self.treshold_blue = QtWidgets.QLineEdit(self.MainWidget)
        self.treshold_method = QtWidgets.QLineEdit(self.MainWidget)

        self.menubar = QtWidgets.QMenuBar(self.centralwidget)
        self.MainWindow = MainWindow
        self.checkBox1 = QtWidgets.QCheckBox(self.MainWidget)
        self.checkBox2 = QtWidgets.QCheckBox(self.MainWidget)
        self.checkBox3 = QtWidgets.QCheckBox(self.MainWidget)
        self.checkBox4 = QtWidgets.QCheckBox(self.MainWidget)
        self.checkBox5 = QtWidgets.QCheckBox(self.MainWidget)
        self.checkBox6 = QtWidgets.QCheckBox(self.MainWidget)
        self.checkBox7 = QtWidgets.QCheckBox(self.MainWidget)
        self.result_label = QtWidgets.QLabel(self.MainWidget)
        self.generateButton = QtWidgets.QPushButton(self.MainWidget)
        self.lineEdit = QtWidgets.QLineEdit(self.MainWidget)
        self.progressBar = QtWidgets.QProgressBar(self.MainWidget)
        self.text_edit = QtWidgets.QTextEdit(self.MainWidget)
        self.dir = QtWidgets.QLineEdit(self.SettingsWidget)
        self.comboBox = QtWidgets.QComboBox(self.SettingsWidget)
        self.language = QtWidgets.QLabel(self.SettingsWidget)
        self.dir_label = QtWidgets.QLabel(self.SettingsWidget)
        self.SaveButton = QtWidgets.QPushButton(self.SettingsWidget)
        self.CancelButton = QtWidgets.QPushButton(self.SettingsWidget)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.HelpWidget)
        self.setup_UI(MainWindow)
        self.setStyleSheets()
    def setup_UI(self, MainWindow:QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 450)
        MainWindow.setWindowTitle("XtoYextension")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 50))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainAction = QAction(QIcon("Images\homeicon.png"), "&Main", self)
        MainAction.triggered.connect(self.go_to_Mainwidget)
        self.menubar.addAction(MainAction)
        MainAction1 = QAction(QIcon("Images\settingsicon.png"), "&Settings", self)
        MainAction1.triggered.connect(self.go_to_settings)
        self.menubar.addAction(MainAction1)
        MainAction2 = QAction(QIcon("Images\helpicon.png"), "&Help", self)
        MainAction2.triggered.connect(self.go_to_help)
        self.menubar.addAction(MainAction2)
        self.BackgroundWidget.setGeometry(QtCore.QRect(0, 0, 706, 433))
        self.BackgroundWidget.setObjectName("backwidget")
        self.treshold_red.setGeometry(QtCore.QRect(245, 230, 50, 21))
        self.treshold_green.setGeometry(QtCore.QRect(297, 230, 50, 21))
        self.treshold_blue.setGeometry(QtCore.QRect(349, 230, 50, 21))
        self.treshold_method.setGeometry(QtCore.QRect(401, 230, 50, 21))
        self.slider.setGeometry(QtCore.QRect(75, 40, 105, 20))
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.setMaximum(200)
        self.slider.setSliderPosition(100)
        self.speed.setGeometry(QtCore.QRect(0, 40, 55, 20))
        self.slider.setTickInterval(25)
        self.slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.slider.setPageStep(25)
        self.slider.valueChanged.connect(self.set_speed)
        self.speed_value.setGeometry(QtCore.QRect(200, 40, 30, 15))
        self.comboBox1.setGeometry(QtCore.QRect(75, 70, 69, 22))
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.language1.setGeometry(QtCore.QRect(0, 70, 55, 20))
        self.language1.setObjectName("label_3")
        self.slider.close()
        self.speed_value.close()
        self.language1.close()
        self.comboBox1.close()
        self.speed.close()
        self.lineEdit.setGeometry(QtCore.QRect(50, 30, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.generateButton.setGeometry(QtCore.QRect(50, 70, 111, 31))
        self.generateButton.setObjectName("generateButton")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openButton = QtWidgets.QPushButton(self.MainWidget)
        self.openButton.setGeometry(QtCore.QRect(173, 70, 48, 31))
        self.openButton.setObjectName("openButton")
        self.openButton.setIcon(QtGui.QIcon('Images\open.jpg'))
        self.openButton.setIconSize(QtCore.QSize(28,28))
        self.startButton = QtWidgets.QPushButton(self.MainWidget)
        self.startButton.setGeometry(QtCore.QRect(460, 150, 93, 25))
        self.startButton.setObjectName("pushButton")
        self.startButton.setIcon(QtGui.QIcon("Images\Start-icon.png"))
        self.cancelButton = QtWidgets.QPushButton(self.MainWidget)
        self.cancelButton.setGeometry(QtCore.QRect(460, 180, 93, 25))
        self.cancelButton.setObjectName("pushButton_2")
        self.cancelButton.setIcon(QtGui.QIcon("Images\cancel.png"))
        self.cancelButton.setIconSize(QtCore.QSize(18,18))
        self.text_edit.setGeometry(QtCore.QRect(50, 270, 521, 101))
        self.text_edit.setObjectName("scrollArea")
        self.text_edit.setReadOnly(True)
        self.progressBar.setGeometry(QtCore.QRect(50, 385, 521, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.openButton.clicked.connect(self.import_file)
        self.startButton.clicked.connect(self.start)
        self.cancelButton.clicked.connect(self.cancel)
        self.generateButton.clicked.connect(self.generate_options)
        self.result_label.setGeometry(QtCore.QRect(230, 74, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet('color:red;')
        self.result_label.setObjectName("result label")
        self.checkBox1.setGeometry(QtCore.QRect(50, 110, 200, 17))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox1.setVisible(False)

        self.checkBox2.setGeometry(QtCore.QRect(50, 130, 200, 17))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox2.setVisible(False)
        self.checkBox3.setGeometry(QtCore.QRect(50, 150, 200, 17))
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox3.setVisible(False)
        self.checkBox4.setGeometry(QtCore.QRect(50, 170, 200, 17))
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox4.setVisible(False)
        self.checkBox5.setGeometry(QtCore.QRect(50, 190, 200, 17))
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox5.setVisible(False)
        self.checkBox6.setGeometry(QtCore.QRect(50, 210, 200, 17))
        self.checkBox6.setObjectName("checkBox6")
        self.checkBox6.setVisible(False)
        self.checkBox7.setGeometry(QtCore.QRect(50, 230, 200, 17))
        self.checkBox7.setObjectName("checkBox7")
        self.checkBox7.setVisible(False)
        self.treshold_red.setVisible(False)
        self.treshold_green.setVisible(False)
        self.treshold_blue.setVisible(False)
        self.treshold_method.setVisible(False)

        #  ************************    Settings   centralwidget **************************************

        self.SettingsWidget.setGeometry(QtCore.QRect(10, 0, 681, 381))
        self.SettingsWidget.setObjectName("SettingsWidget")
        self.dir.setGeometry(QtCore.QRect(40, 30, 521, 31))
        self.dir.setObjectName("lineEdit")

        self.comboBox.setGeometry(QtCore.QRect(110, 70, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.language.setGeometry(QtCore.QRect(40, 70, 55, 20))
        self.language.setObjectName("label_2")
        self.SaveButton.setGeometry(QtCore.QRect(50, 140, 75, 23))
        self.SaveButton.setObjectName("pushButton")
        self.SaveButton.clicked.connect(self.change_settings)
        self.CancelButton.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.CancelButton.setObjectName("pushButton_2")
        self.SettingsWidget.close()

        #  ************************    Help   centralwidget **************************************

        self.HelpWidget.setGeometry(QtCore.QRect(10, 0, 681, 381))
        self.HelpWidget.setObjectName("HelpWidget")
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 10, 420, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.plainTextEdit.setMouseTracking(False)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.HelpWidget.close()
        self.retranslateUi()

    def retranslateUi(self):
        lang_index = self.comboBox.currentIndex()
        if lang_index == 1:
            self.generateButton.setText("Générer les options")
            self.lineEdit.setPlaceholderText("Directoire du fichier")
            self.startButton.setText("Commencer")
            self.cancelButton.setText("Annuler")
            self.treshold_red.setPlaceholderText("rouge")
            self.treshold_green.setPlaceholderText("vert")
            self.treshold_blue.setPlaceholderText("bleu")
            self.treshold_method.setPlaceholderText("méthode")
            self.comboBox1.setItemText(0, "Anglais")
            self.comboBox1.setItemText(1, "Français")
            self.language1.setText("Langage")
            self.speed.setText("Vitesse")
            self.speed_value.setText('x1.0')
            self.comboBox.setItemText(0, "Anglais")
            self.comboBox.setItemText(1, "Français")
            self.language.setText("Langage")
            self.dir.setPlaceholderText("Enregistrer sous... ")
            self.SaveButton.setText("Enregistrer")
            self.CancelButton.setText("Annuler")
            self.plainTextEdit.setPlainText("*   L'application XtoYextension supporte les extensions suivantes:\n"
                                            "docx,doc,ppt,pptx,mp4,gifs,pdf,txt\n"
                                            "\n"
                                            "*   Suivre les instuctions:\n"
                                            "1-Ouvrir ou entrer une directoire de fichier \n"
                                            "2-Générer les options \n"
                                            "3-Choisir un ou des option(s) \n"
                                            "4-Commencer\n"
                                            "5-Choisir où enregistrer \n"
                                            "\n"
                                            "NB: Durant la conversion à plusieurs fichiers (pngs,gifs) , veuillez choisir une directoire à y enregistrer \n"
                                            "\n"
                                            "")

        else:
            self.generateButton.setText("Generate options")
            self.lineEdit.setPlaceholderText("File directory")
            self.startButton.setText("Start")
            self.cancelButton.setText("Cancel")
            self.treshold_red.setPlaceholderText("red")
            self.treshold_green.setPlaceholderText("green")
            self.treshold_blue.setPlaceholderText("blue")
            self.treshold_method.setPlaceholderText("method")
            self.comboBox1.setItemText(0, "English")
            self.comboBox1.setItemText(1, "Frensh")
            self.language1.setText("Language")
            self.speed.setText("Speed")
            self.speed_value.setText('x1.0')

            self.comboBox.setItemText(0, "English")
            self.comboBox.setItemText(1, "Frensh")
            self.language.setText("Language")
            self.dir.setPlaceholderText("Saved files directory")
            self.SaveButton.setText("Save")
            self.CancelButton.setText("Cancel")

            self.plainTextEdit.setPlainText("*   XtoYformat App supports the following extensions:\n"
                                            "docx,doc,ppt,pptx,mp4,gifs,pdf,txt\n"
                                            "\n"
                                            "*   Follow instructions:\n"
                                            "1-Open or Enter file directory \n"
                                            "2-Generate options\n"
                                            "3-Choose option(s)  \n"
                                            "4-Start\n"
                                            "5-Choose where to save \n"
                                            "\n"
                                            "NB: During conversion to many files (pngs,gifs) , please select a directory to save to! \n"
                                            "\n"
                                            "")

    def set_speed(self, value):
        self.speed_value.setText('x' + str(value / 100))

    def go_to_settings(self):
        self.MainWidget.close()
        self.HelpWidget.close()
        self.SettingsWidget.show()

    def go_to_Mainwidget(self):
        self.SettingsWidget.close()
        self.HelpWidget.close()
        self.MainWidget.show()

    def go_to_help(self):
        self.MainWidget.close()
        self.HelpWidget.show()
        self.SettingsWidget.close()

    def change_settings(self):
        directory = self.dir.text()
        if os.path.isdir(directory):
            self.dir.setText(directory)
        else:
            self.statusBar().showMessage(self.generate_result()[3])
        self.retranslateUi()

    def import_file(self):
        for element in (self.checkBox1,self.checkBox2,self.checkBox3,self.checkBox4,self.checkBox5,self.checkBox6,self.checkBox7,self.treshold_red,self.treshold_green,self.treshold_blue,self.treshold_method):
            element.setVisible(False)
        result = QFileDialog.getOpenFileName()
        self.lineEdit.setText(result[0])

    def translate_checkboxes(self, index: int = 0, ext: str = 'pdf'):
        if index == 1:
                self.checkBox1.setText("Convertir en ppm")
                self.checkBox2.setText("Calculer l'histogramme")
                self.checkBox3.setText("Calculer l'histogramme cumulé")
                self.checkBox4.setText("Calculer l'histogramme égalisé")
                self.checkBox5.setText("Calculer la moyenne des niveaux de gris")
                self.checkBox6.setText("Calculer l'écart type des niveaux de gris")
                self.checkBox7.setText("Seuiller")
        else:
                self.checkBox1.setText("Convert to ppm")
                self.checkBox2.setText("Calculate histogram")
                self.checkBox3.setText("Calculate cumulated histogram")
                self.checkBox4.setText("Calculate egalised histogram")
                self.checkBox5.setText("Calculate mean of levels of grey")
                self.checkBox6.setText("Calculate gap of levels of grey")
                self.checkBox7.setText("Treshold")
        if ext == 'ppm':
            if index == 1:
                self.checkBox1.setText("Convertir en pgm")
            else:
                self.checkBox1.setText("Convert to pgm")


    def generate_result(self):
        lang_index = self.comboBox.currentIndex()
        if lang_index == 1:
            result = ["Veuillez séléctionner un fichier !", "Les fichiers doivent avoir la forme 'Nom.ext' !",
                      "Extension inconnue! ", "La directoire specifiée n'existe pas !"]
        else:
            result = ["Please select a file!", "Files must have the form 'Name.ext' !", "Unknown extension !",
                      "Directory does not exist !"]

        return result

    def generate_options(self):
        self.checkBox1.setVisible(False)
        self.checkBox2.setVisible(False)
        self.checkBox3.setVisible(False)
        self.checkBox4.setVisible(False)
        self.checkBox5.setVisible(False)
        self.checkBox6.setVisible(False)
        result = None
        text = self.lineEdit.text()

        if text == '':
            result = self.generate_result()[0]
        elif not os.path.isfile(text):
            result = self.generate_result()[3]
        else:
            ext_list = text.split('.')
            if len(ext_list) == 1:
                result = self.generate_result()[1]
            elif ext_list[1] not in ('pgm','ppm'):
                result = self.generate_result()[2]
            else:
                ext = ext_list[1]
                self.ext = ext
                if ext == 'ppm':
                    self.checkBox7.setVisible(True)
                    self.treshold_red.setVisible(True)
                    self.treshold_green.setVisible(True)
                    self.treshold_blue.setVisible(True)
                    self.treshold_method.setVisible(True)
                self.translate_checkboxes(self.comboBox.currentIndex(), ext)
                self.checkBox1.setVisible(True)
                self.checkBox2.setVisible(True)
                self.checkBox3.setVisible(True)
                self.checkBox4.setVisible(True)
                self.checkBox5.setVisible(True)
                self.checkBox6.setVisible(True)


                result = None
        if result is not None:
            self.result_label.setVisible(True)
            self.result_label.setText(result)
        else:
            self.result_label.close()

    def start(self):

        infile = self.lineEdit.text()
        progress_bar = self.progressBar
        logs = self.text_edit
        #progress_bar.setValue(25)
        #logs.setText(infile)
        if self.checkBox1.isChecked():
            ext = infile.split('.')[1]
            if ext == 'pgm':
                progress_bar.setValue(25)
                logs.setText("Lecture de l'image PGM")
                result = pgmread(infile)
                progress_bar.setValue(50)
                logs.setText("Ecriture sous format PPM")
                result2 = convertToPpm(result)
                ppmwrite(result2, 'result')
                progress_bar.setValue(100)
                logs.setText("Succès !")
                im = Image.open("result.ppm")
                im.show()
            else:
                progress_bar.setValue(25)
                logs.setText("Lecture de l'image PPM")
                result = ppmread(infile)
                progress_bar.setValue(50)
                logs.setText("Ecriture sous format PGM")
                res = convertToPgm(result)
                pgmwrite(res[0], 'result')
                progress_bar.setValue(100)
                logs.setText("Succès !")
                im = Image.open("result.pgm")
                im.show()
        if self.checkBox2.isChecked():
            ext = infile.split('.')[1]
            if ext == 'pgm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PGM")
                img = pgmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'histogramme")
                histo = histogram(img[0])
                progress_bar.setValue(100)
                logs.append("histogramme de l'image PGM: ")
                histo_str = ""
                for number in histo:
                    histo_str = histo_str + str(number) + " "
                logs.append(histo_str)
                x = np.arange(0, 256)
                y = histo
                # plotting
                plt.title("Histogramme")
                plt.xlabel("Nombre de pixels")
                plt.ylabel("Occurence")
                plt.plot(x, y, color="red")
                plt.show()
            elif ext == 'ppm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PPM")
                img = ppmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'histogramme")
                histo = histogram(img[0])
                progress_bar.setValue(100)
                logs.append("histogramme : ")
                histo_str = ""
                for number in histo:
                    histo_str = histo_str + str(number) + " "
                logs.append(histo_str)
                x = np.arange(0, 256)
                y = histo
                # plotting
                plt.title("Histogramme de l'image PPM")
                plt.xlabel("Niveau")
                plt.ylabel("Nombre de pixels")
                plt.plot(x, y, color="red")
                plt.show()
        if self.checkBox3.isChecked():
            ext = infile.split('.')[1]
            if ext == 'pgm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PGM")
                img = pgmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'histogramme cumulé")
                histo = cumule(img[0])
                progress_bar.setValue(100)
                logs.append("histogramme cumulé: ")
                histo_str = ""
                for number in histo:
                    histo_str = histo_str + str(number) + " "
                logs.append(histo_str)
                x = np.arange(0, 256)
                y = histo
                # plotting
                plt.title("Histogramme cumulé de l'image PGM")
                plt.xlabel("Niveau")
                plt.ylabel("Nombre de pixels cumulé")
                plt.plot(x, y, color="red")
                plt.show()
            elif ext == 'ppm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PPM")
                img = ppmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'histogramme cumulé")
                histo = cumule(img[0])
                progress_bar.setValue(100)
                logs.append("histogramme cumulé: ")
                histo_str = ""
                for number in histo:
                    histo_str = histo_str + str(number) + " "
                logs.append(histo_str)

                x = np.arange(0, 256)
                y = histo
                # plotting
                plt.title("Histogramme cumulé de l'image PPM")
                plt.xlabel("Niveau")
                plt.ylabel("Nombre de pixels cumulé")
                plt.plot(x, y, color="red")
                plt.show()
        if self.checkBox4.isChecked():
            ext = infile.split('.')[1]
            if ext == 'pgm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PGM")
                img = pgmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'histogramme égalisé")
                img = histo_egal(img[0])
                progress_bar.setValue(75)
                logs.append("Ecriture de l'image généré")
                pgmwrite(img,"result-egalised")
                progress_bar.setValue(100)
                logs.append("Succés !")
                im = Image.open("result-egalised.pgm")
                im.show()
            elif ext == 'ppm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PPM")
                img = ppmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'histogramme égalisé")
                new_img = histo_egal(img[0])
                progress_bar.setValue(75)
                logs.append("Ecriture de l'image généré")
                img[0] = new_img
                ppmwrite(img, "result-egalised")
                progress_bar.setValue(100)
                logs.append("Succés !")
                im = Image.open("result-egalised.ppm")
                im.show()
        if self.checkBox5.isChecked():
            ext = infile.split('.')[1]
            if ext == 'pgm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PGM")
                img = pgmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul du moyenne des niveaux de gris")
                moy = moyenneGris(img[0])
                progress_bar.setValue(100)
                logs.append("moyenne : " + str(moy))
            if ext == 'ppm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PPM")
                img = ppmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul du moyenne des niveaux de gris")
                moy = moyenneGris(img[0])
                progress_bar.setValue(100)
                logs.append("moyenne : " + str(moy))
        if self.checkBox6.isChecked():
            ext = infile.split('.')[1]
            if ext == 'pgm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PGM")
                img = pgmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'écart type de niveaux de gris")
                moy = ecartypeGris(img[0])
                progress_bar.setValue(100)
                logs.append("écart type : " + str(moy))
            if ext == 'ppm':
                progress_bar.setValue(25)
                logs.append("Lecture de l'image PPM")
                img = ppmread(infile)
                progress_bar.setValue(50)
                logs.append("Calcul de l'écart type de niveaux de gris")
                moy = ecartypeGris(img[0])
                progress_bar.setValue(100)
                logs.append("écart type : " + str(moy))
        if self.checkBox7.isChecked():
            progress_bar.setValue(25)
            logs.append("Lecture de l'image PPM")
            progress_bar.setValue(50)
            logs.append("seuillage")
            seuiller(infile, int(self.treshold_red.text()), int(self.treshold_green.text()),
                     int(self.treshold_blue.text()), self.treshold_method.text())
            progress_bar.setValue(100)
            logs.append("Succès!")
            im = Image.open("out-"+self.treshold_method.text()+".ppm")
            im.show()
    def cancel(self):
        self.text_edit.setText("")
        self.progressBar.setProperty("value",0)
    def setStyleSheets(self):
        self.MainWindow.setStyleSheet(".QPushButton {\n"
                                 "background-color: white; \n"   
                                 "  color: black; \n"
                                 "  border: 2px solid grey;\n"
                                 "  text-align: center;\n"
                                 "  display: inline-block;\n"
                                 "}\n"
                                 "")
        for checkbox in (self.checkBox1,self.checkBox2,self.checkBox3,self.checkBox4,self.checkBox5,self.checkBox6,self.checkBox7):
            checkbox.setStyleSheet(".QCheckBox::indicator{\n"
                                    "border:2px solid grey;\n"
                                    "\n"
                                    "}\n"
                                    ".QCheckBox::indicator::checked{\n"
                                    "background-color : grey;\n"
                                    "}")
        self.treshold_red.setStyleSheet(".QLineEdit{\n"
                                    " width: 100%;\n"
                                    "  box-sizing: border-box;\n"
                                    "  border: 2px solid grey;\n"
                                    "  border-radius: 4px;\n"
                                    "}\n"
                                    ".QLineEdit:focus{\n"
                                    "border:2px solid black;\n"
                                    "}")
        self.treshold_green.setStyleSheet(".QLineEdit{\n"
                                        " width: 100%;\n"
                                        "  box-sizing: border-box;\n"
                                        "  border: 2px solid grey;\n"
                                        "  border-radius: 4px;\n"
                                        "}\n"
                                        ".QLineEdit:focus{\n"
                                        "border:2px solid black;\n"
                                        "}")
        self.treshold_blue.setStyleSheet(".QLineEdit{\n"
                                        " width: 100%;\n"
                                        "  box-sizing: border-box;\n"
                                        "  border: 2px solid grey;\n"
                                        "  border-radius: 4px;\n"
                                        "}\n"
                                        ".QLineEdit:focus{\n"
                                        "border:2px solid black;\n"
                                        "}")
        self.treshold_method.setStyleSheet(".QLineEdit{\n"
                                        " width: 100%;\n"
                                        "  box-sizing: border-box;\n"
                                        "  border: 2px solid grey;\n"
                                        "  border-radius: 4px;\n"
                                        "}\n"
                                        ".QLineEdit:focus{\n"
                                        "border:2px solid black;\n"
                                        "}")
        self.dir.setStyleSheet(".QLineEdit{\n"
                                    " width: 100%;\n"
                                    "  box-sizing: border-box;\n"
                                    "  border: 2px solid grey;\n"
                                    "  border-radius: 4px;\n"
                                    "}\n"
                                    ".QLineEdit:focus{\n"
                                    "border:2px solid black;\n"
                                    "}")
        self.SettingsWidget.setStyleSheet(".QComboBox{\n"
                                             "   border:2px solid grey;\n"
                                              "  }\n"
                                                                  "  QComboBox::drop-down \n"
                                                                  "  { \n"
                                                                   "     border: 0px;\n"
                                                                  "  }\n"
                                                                    
                                                                 "   QComboBox::down-arrow {\n"
                                                                  "      image: url(Images//arrow.png);\n"
                                                                   "     width: 20px;\n"
                                                                      "  height: 20px;\n"
                                                                  "  }\n"
                                                                  "   QComboBox:item::hover {\n"
                                                                  "   color: grey;\n"
                                                                  "  }\n"
                                     )
        self.lineEdit.setStyleSheet(".QLineEdit{\n"
                                    " width: 100%;\n"
                                    "  box-sizing: border-box;\n"
                                    "  border: 2px solid grey;\n"
                                    "  border-radius: 4px;\n"
                                    "}\n"
                                    ".QLineEdit:focus{\n"
                                    "border:2px solid black;\n"
                                    "}")
        self.openButton.setStyleSheet(".QPushButton{\n"
                                        "border: none;\n"
                                        "\n"
                                      "}\n"
                                        "\n"
                                       )
        self.generateButton.setStyleSheet(".QPushButton{\n"
                                        "border: 2px solid grey;\n"
                                        "}\n"
                                        "\n"
                                        ".QPushButton:hover {\n"
                                        "background-color:grey;\n"
                                        "color:white;\n"
                                        "}")
        self.CancelButton.setStyleSheet(".QPushButton{\n"
                                        "border:2px solid grey;\n"
                                        "}"

                                        )
        self.cancelButton.setStyleSheet(".QPushButton{\n"
                                        "border: 2px solid grey;\n"
                                        "\n"
                                        "}\n"
                                        )
        self.text_edit.setStyleSheet(".QTextEdit{\n"
                                      " width: 100%;\n"
                                      "  box-sizing: border-box;\n"
                                      "  border: 2px solid grey;\n"
                                      "  border-radius: 4px;\n"
                                      "}")

        self.progressBar.setStyleSheet(".QProgressBar {\n"
                                       "border:2px solid #4CAF50;\n"
                                       "text-align:center;\n"
                                       "}")
        self.setStyleSheet(".QWidget{\n"
                           "background-color:red;\n"
                           ""
                           "}")
        self.BackgroundWidget.setStyleSheet(
            "background-image: url(Images//Background.png); background-repeat: no-repeat; background-position: center")
        self.plainTextEdit.setStyleSheet(".QPlainTextEdit{\n"
                                         "border:none;\n"
                                         "background-color:transparent;\n"
                                         ""
                                         ""
                                         "}")