from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pyaudio
import webbrowser



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)

        self.r = sr.Recognizer()

        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.line_horizontal = QtWidgets.QFrame(self.centralwidget)
        self.line_horizontal.setGeometry(QtCore.QRect(180, 50, 301, 20))
        self.line_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_horizontal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_horizontal.setObjectName("line_horizontal")

        self.line_vertical = QtWidgets.QFrame(self.centralwidget)
        self.line_vertical.setGeometry(QtCore.QRect(320, 80, 20, 141))
        self.line_vertical.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_vertical.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_vertical.setObjectName("line_vertical")

        self.label_selectafile = QtWidgets.QLabel(self.centralwidget)
        self.label_selectafile.setGeometry(QtCore.QRect(20, 80, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_selectafile.setFont(font)
        self.label_selectafile.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selectafile.setObjectName("label_selectafile")

        self.label_recordyourself = QtWidgets.QLabel(self.centralwidget)
        self.label_recordyourself.setGeometry(QtCore.QRect(350, 80, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_recordyourself.setFont(font)
        self.label_recordyourself.setAlignment(QtCore.Qt.AlignCenter)
        self.label_recordyourself.setObjectName("label_recordyourself")

        self.button_openfiledialogue = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: func_open_file_dialogue())
        self.button_openfiledialogue.setGeometry(QtCore.QRect(90, 120, 151, 31))
        self.button_openfiledialogue.setObjectName("button_openfiledialogue")
        def func_open_file_dialogue():
            self.file_directory = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Audio File:', 'F:\\')
            self.label_filenameselected.setText(f'{self.file_directory[0]}')
            print(f'[+] Selected Audio File: {self.file_directory}')
            self.textbox_speechtext.setPlainText('Working on it...')
            print(f'[+] Initializing STT ')

            with sr.AudioFile(self.file_directory[0]) as source:
                self.audio_data = self.r.record(source)

                try:
                    self.text = self.r.recognize_google(self.audio_data)
                    self.textbox_speechtext.setPlainText(self.text)
                    print(f'[+] Interpreted Audio: {self.text}')

                except sr.UnknownValueError:
                    self.textbox_speechtext.setPlainText('Google Speech Recognition could not understand audio :(')
                    print("[+] Google Speech Recognition could not understand audio")
                
                except sr.RequestError as e:
                    self.textbox_speechtext.setPlainText('Could not request results from Google Speech Recognition service; {0}'.format(e))
                    print("[+] Could not request results from Google Speech Recognition service; {0}".format(e))
                    
        self.label_filenameselected = QtWidgets.QLabel(self.centralwidget)
        self.label_filenameselected.setGeometry(QtCore.QRect(10, 190, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_filenameselected.setFont(font)
        self.label_filenameselected.setAlignment(QtCore.Qt.AlignCenter)
        self.label_filenameselected.setObjectName("label_filenameselected")

        self.label_fileopened = QtWidgets.QLabel(self.centralwidget)
        self.label_fileopened.setGeometry(QtCore.QRect(10, 170, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_fileopened.setFont(font)
        self.label_fileopened.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileopened.setObjectName("label_fileopened")

        self.textbox_speechtext = QtWidgets.QPlainTextEdit(self.centralwidget, readOnly=True)
        self.textbox_speechtext.setGeometry(QtCore.QRect(30, 290, 311, 181))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.textbox_speechtext.setFont(font)
        self.textbox_speechtext.setObjectName("textbox_speechtext")

        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_filename.setGeometry(QtCore.QRect(360, 290, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_filename.setFont(font)
        self.lineEdit_filename.setObjectName("lineEdit_filename")

        self.label_downloadoptions = QtWidgets.QLabel(self.centralwidget)
        self.label_downloadoptions.setGeometry(QtCore.QRect(180, 240, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.label_downloadoptions.setFont(font)
        self.label_downloadoptions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_downloadoptions.setObjectName("label_downloadoptions")

        self.button_downloadtext = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: func_download_text())
        self.button_downloadtext.setGeometry(QtCore.QRect(360, 350, 121, 31))
        self.button_downloadtext.setObjectName("button_downloadtext")
        def func_download_text():
            try:
                self.f = open(f'{self.lineEdit_filename.text()}' ,'w+')
                self.f.close()
                print(f'[+] Created File {self.lineEdit_filename.text()}')
                self.f = open(f'{self.lineEdit_filename.text()}' ,'w')
                self.f.write(f'{self.text}')
                self.f.close()
                print(f'[+] Wrote audio file contents into file')
            
            except:
                self.textbox_speechtext.setPlainText('Something happened while downloading, please input the filename WITH THE EXTENSTION again. (STT results are still saved)')
                print(f'[+] User Put in invalid file name')

        self.button_reset = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: func_reset())
        self.button_reset.setGeometry(QtCore.QRect(510, 350, 121, 31))
        self.button_reset.setObjectName("button_reset")
        def func_reset():
            self.label_filenameselected.setText('None')
            self.textbox_speechtext.setPlainText('All text derived from the selected audio file or recording will show up here...')
            self.lineEdit_filename.setText('text file name (ex. file_name.txt)')
            self.text = ''
            self.spinBox_mm.setValue(0)
            self.spinBox_ss.setValue(0)

        self.button_moreinfo = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: func_more_info())
        self.button_moreinfo.setGeometry(QtCore.QRect(640, 460, 20, 21))
        self.button_moreinfo.setObjectName("button_moreinfo")
        def func_more_info():
            webbrowser.open('https://knowing-letter-85f.notion.site/Speech-To-Text-GUI-168f55a30db247438ea162abd1d7f61b')
            print(f'[+] Opened More Info')

        self.spinBox_mm = QtWidgets.QSpinBox(self.centralwidget, minimum=0, maximum=10)
        self.spinBox_mm.setGeometry(QtCore.QRect(370, 140, 61, 22))
        self.spinBox_mm.setObjectName("spinBox_mm")

        self.label_mm = QtWidgets.QLabel(self.centralwidget)
        self.label_mm.setGeometry(QtCore.QRect(369, 120, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_mm.setFont(font)
        self.label_mm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mm.setObjectName("label_mm")

        self.label_ss = QtWidgets.QLabel(self.centralwidget)
        self.label_ss.setGeometry(QtCore.QRect(459, 120, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_ss.setFont(font)
        self.label_ss.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ss.setObjectName("label_ss")

        self.spinBox_ss = QtWidgets.QSpinBox(self.centralwidget, minimum=0, maximum=60)
        self.spinBox_ss.setGeometry(QtCore.QRect(460, 140, 61, 22))
        self.spinBox_ss.setObjectName("spinBox_ss")

        self.button_start = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_start())
        self.button_start.setGeometry(QtCore.QRect(550, 130, 81, 31))
        self.button_start.setObjectName("button_start")
        def func_start():
            self.s_time = int(self.spinBox_mm.value()) * 60 + int(self.spinBox_ss.value())

            with sr.Microphone() as source:
                self.audio_data = self.r.record(source, duration=self.s_time)
                self.textbox_speechtext.setPlainText('Working on it...')
                print(f'[+] Initializing STT ')

                try:
                    self.text = self.r.recognize_google(self.audio_data)
                    print(f'Interpreted Audio: {self.text}')
                    self.textbox_speechtext.setPlainText(self.text)

                except sr.UnknownValueError:
                    self.textbox_speechtext.setPlainText('Google Speech Recognition could not understand audio :(')
                    print("[+] Google Speech Recognition could not understand audio")
                
                except sr.RequestError as e:
                    self.textbox_speechtext.setPlainText('Could not request results from Google Speech Recognition service; {0}'.format(e))
                    print("[+] Could not request results from Google Speech Recognition service; {0}".format(e))

        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(340, 180, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(7)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speech To Text"))
        self.label_title.setText(_translate("MainWindow", "Speech To Text"))
        self.label_selectafile.setText(_translate("MainWindow", "Select a file:"))
        self.label_recordyourself.setText(_translate("MainWindow", "(Optional) Record Yourself:"))
        self.button_openfiledialogue.setText(_translate("MainWindow", "Open File Dialogue"))
        self.label_filenameselected.setText(_translate("MainWindow", "None"))
        self.label_fileopened.setText(_translate("MainWindow", "File Opened:"))
        self.textbox_speechtext.setPlainText(_translate("MainWindow", "All text derived from the selected audio file or recording will show up here..."))
        self.lineEdit_filename.setText(_translate("MainWindow", "text file name (ex. file_name.txt)"))
        self.label_downloadoptions.setText(_translate("MainWindow", "Download Options:"))
        self.button_downloadtext.setText(_translate("MainWindow", "Download Text File"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))
        self.button_moreinfo.setText(_translate("MainWindow", "?"))
        self.label_mm.setText(_translate("MainWindow", "MM"))
        self.label_ss.setText(_translate("MainWindow", "SS"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.label_info.setText(_translate("MainWindow", "The recording will show up below when it is finished processing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
