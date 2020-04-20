# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3_IP_CAM.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5.QtCore import QTimer
import cv2
import numpy as np
from datetime import datetime
import sys
import os
from os import path
import time
MONTH = { 1:'January',
          2:'February',
          3:'March',
          4:'April',
          5:'May',
          6:'June',
          7:'July',
          8:'August',
          9:'September',
          10:'October',
          11:'November',
          12:'December'}
IP_CAM_ADDRESS = {'CAM1': 0, 'CAM2':'http://192.168.1.5:8080/video', 'CAM3': 'http://192.168.1.8:8080/video'}


class Ui_Form(object):
    def __init__(self):
      super().__init__()
      self.points_CAM1 = []
      self.points_CAM2 = []
      self.points_CAM3 = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1042, 485)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.CAM1 = QtWidgets.QLabel(self.tab)
        self.CAM1.setGeometry(QtCore.QRect(10, 40, 301, 261))
        self.CAM1.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM1.setText("")
        self.CAM1.setObjectName("CAM1")
        self.CAM2 = QtWidgets.QLabel(self.tab)
        self.CAM2.setGeometry(QtCore.QRect(360, 40, 301, 261))
        self.CAM2.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM2.setText("")
        self.CAM2.setObjectName("CAM2")
        self.CAM3 = QtWidgets.QLabel(self.tab)
        self.CAM3.setGeometry(QtCore.QRect(720, 40, 301, 261))
        self.CAM3.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM3.setText("")
        self.CAM3.setObjectName("CAM3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(110, 10, 91, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(460, 10, 91, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(840, 10, 67, 17))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.startCAM1 = QtWidgets.QPushButton(self.tab)
        self.startCAM1.setGeometry(QtCore.QRect(10, 320, 51, 25))
        
        self.startCAM1.setObjectName("startCAM1")
        self.personReID_CAM1 = QtWidgets.QPushButton(self.tab)
        self.personReID_CAM1.setGeometry(QtCore.QRect(70, 320, 111, 25))
        self.personReID_CAM1.setObjectName("personReID_CAM1")
        self.faceRecognition_CAM1 = QtWidgets.QPushButton(self.tab)
        self.faceRecognition_CAM1.setGeometry(QtCore.QRect(190, 320, 121, 25))
        self.faceRecognition_CAM1.setObjectName("faceRecognition_CAM1")
        self.stopCAM1 = QtWidgets.QPushButton(self.tab)
        self.stopCAM1.setGeometry(QtCore.QRect(10, 370, 51, 25))
        self.stopCAM1.setObjectName("stopCAM1")
        self.areaProtect_CAM1 = QtWidgets.QPushButton(self.tab)
        self.areaProtect_CAM1.setGeometry(QtCore.QRect(70, 370, 121, 25))
        self.areaProtect_CAM1.setObjectName("areaProtect_CAM1")
        self.fallDetection_CAM1 = QtWidgets.QPushButton(self.tab)
        self.fallDetection_CAM1.setGeometry(QtCore.QRect(200, 370, 111, 25))
        self.fallDetection_CAM1.setObjectName("fallDetection_CAM1")
        self.start_CAM2 = QtWidgets.QPushButton(self.tab)
        self.start_CAM2.setGeometry(QtCore.QRect(360, 320, 51, 25))
        self.start_CAM2.setObjectName("start_CAM2")
        self.start_CAM3 = QtWidgets.QPushButton(self.tab)
        self.start_CAM3.setGeometry(QtCore.QRect(720, 320, 51, 25))
        self.start_CAM3.setObjectName("start_CAM3")
        self.personReID_CAM2 = QtWidgets.QPushButton(self.tab)
        self.personReID_CAM2.setGeometry(QtCore.QRect(420, 320, 111, 25))
        self.personReID_CAM2.setObjectName("personReID_CAM2")
        self.personReID_CAM3 = QtWidgets.QPushButton(self.tab)
        self.personReID_CAM3.setGeometry(QtCore.QRect(780, 320, 111, 25))
        self.personReID_CAM3.setObjectName("personReID_CAM3")
        self.faceRecognition_CAM2 = QtWidgets.QPushButton(self.tab)
        self.faceRecognition_CAM2.setGeometry(QtCore.QRect(540, 320, 121, 25))
        self.faceRecognition_CAM2.setObjectName("faceRecognition_CAM2")
        self.faceRecognition_CAM3 = QtWidgets.QPushButton(self.tab)
        self.faceRecognition_CAM3.setGeometry(QtCore.QRect(900, 320, 121, 25))
        self.faceRecognition_CAM3.setObjectName("faceRecognition_CAM3")
        self.stop_CAM2 = QtWidgets.QPushButton(self.tab)
        self.stop_CAM2.setGeometry(QtCore.QRect(360, 370, 51, 25))
        self.stop_CAM2.setObjectName("stop_CAM2")
        self.stop_CAM3 = QtWidgets.QPushButton(self.tab)
        self.stop_CAM3.setGeometry(QtCore.QRect(720, 370, 51, 25))
        self.stop_CAM3.setObjectName("stop_CAM3")
        self.areaProtection_CAM2 = QtWidgets.QPushButton(self.tab)
        self.areaProtection_CAM2.setGeometry(QtCore.QRect(420, 370, 121, 25))
        self.areaProtection_CAM2.setObjectName("areaProtection_CAM2")
        self.areaProtection_CAM3 = QtWidgets.QPushButton(self.tab)
        self.areaProtection_CAM3.setGeometry(QtCore.QRect(780, 370, 121, 25))
        self.areaProtection_CAM3.setObjectName("areaProtection_CAM3")
        self.fallDetection_CAM2 = QtWidgets.QPushButton(self.tab)
        self.fallDetection_CAM2.setGeometry(QtCore.QRect(550, 370, 111, 25))
        self.fallDetection_CAM2.setObjectName("fallDetection_CAM2")
        self.fallDetection_CAM3 = QtWidgets.QPushButton(self.tab)
        self.fallDetection_CAM3.setGeometry(QtCore.QRect(910, 370, 111, 25))
        self.fallDetection_CAM3.setObjectName("fallDetection_CAM3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(150, 0, 681, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        # self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame)
        # self.openGLWidget.setObjectName("openGLWidget")
        # self.gridLayout.addWidget(self.openGLWidget, 0, 0, 1, 1)

#=========================================================
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget(self.frame)
        self.mediaPlayer.setVideoOutput(videowidget)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
#=========================================================
        self.gridLayout.addWidget(videowidget, 0, 0, 1, 1)

        self.horizontalSlider = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(160, 390, 671, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")


        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 420, 349, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon)
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.play = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon1)
        self.play.setObjectName("play")
        self.horizontalLayout.addWidget(self.play)
        self.pause = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon2)
        self.pause.setObjectName("pause")
        self.horizontalLayout.addWidget(self.pause)
        self.stop = QtWidgets.QPushButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon3)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(460, 20, 91, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.CAM1_Draw = QtWidgets.QLabel(self.tab_3)
        self.CAM1_Draw.setGeometry(QtCore.QRect(10, 50, 301, 261))

        self.CAM1_Draw.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM1_Draw.setText("")
        self.CAM1_Draw.setObjectName("CAM1_Draw")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.CAM3_Draw = QtWidgets.QLabel(self.tab_3)
        self.CAM3_Draw.setGeometry(QtCore.QRect(720, 50, 301, 261))
        self.CAM3_Draw.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM3_Draw.setText("")
        self.CAM3_Draw.setObjectName("CAM3_Draw")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(840, 20, 67, 17))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.CAM2_Draw = QtWidgets.QLabel(self.tab_3)
        self.CAM2_Draw.setGeometry(QtCore.QRect(360, 50, 301, 261))
        self.CAM2_Draw.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM2_Draw.setText("")
        self.CAM2_Draw.setObjectName("CAM2_Draw")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(410, 350, 187, 27))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.draw_CAM2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.draw_CAM2.setObjectName("draw_CAM2")
        self.horizontalLayout_3.addWidget(self.draw_CAM2)
        self.remove_CAM2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.remove_CAM2.setEnabled(False)
        self.remove_CAM2.setObjectName("remove_CAM2")
        self.horizontalLayout_3.addWidget(self.remove_CAM2)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(780, 350, 187, 27))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.draw_CAM3 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.draw_CAM3.setObjectName("draw_CAM3")
        self.horizontalLayout_4.addWidget(self.draw_CAM3)
        self.remove_CAM3 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.remove_CAM3.setEnabled(False)
        self.remove_CAM3.setObjectName("remove_CAM3")
        self.horizontalLayout_4.addWidget(self.remove_CAM3)
        self.widget = QtWidgets.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(60, 350, 187, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.draw_CAM1 = QtWidgets.QPushButton(self.widget)
        self.draw_CAM1.setObjectName("draw_CAM1")
        self.horizontalLayout_2.addWidget(self.draw_CAM1)
        self.remove_CAM1 = QtWidgets.QPushButton(self.widget)
        self.remove_CAM1.setEnabled(False)
        self.remove_CAM1.setObjectName("remove_CAM1")
        self.horizontalLayout_2.addWidget(self.remove_CAM1)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.horizontalSlider.setRange(0, 0)
        self.horizontalSlider.sliderMoved.connect(self.set_position)
        self.open.clicked.connect(self.open_file)
        self.play.clicked.connect(self.play_video)
        self.pause.clicked.connect(self.pause_video)
        self.stop.clicked.connect(self.stop_video)



        self.startCAM1.setEnabled(True)
        self.start_CAM2.setEnabled(True)
        self.start_CAM3.setEnabled(True)

        self.stopCAM1.setEnabled(False)
        self.stop_CAM2.setEnabled(False)
        self.stop_CAM3.setEnabled(False)


        #  create a timer
        self.timer = QTimer()
        self.timer2 = QTimer()
        self.timer3 = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        self.startCAM1.clicked.connect(self.start_view)
        self.stopCAM1.clicked.connect(self.stop_view)

        self.timer2.timeout.connect(self.viewCam2)
        self.start_CAM2.clicked.connect(self.start_view2)
        self.stop_CAM2.clicked.connect(self.stop_view2)

        self.timer3.timeout.connect(self.viewCam3)
        self.start_CAM3.clicked.connect(self.start_view3)
        self.stop_CAM3.clicked.connect(self.stop_view3)

        self.CAM1_Draw.mousePressEvent = self.mouseEventCAM1
        self.CAM2_Draw.mousePressEvent = self.mouseEventCAM2
        self.CAM3_Draw.mousePressEvent = self.mouseEventCAM3


        self.draw_CAM1.clicked.connect(self.startDrawAreaCAM1)
        self.remove_CAM1.clicked.connect(self.removeAreaCAM1)

        self.draw_CAM2.clicked.connect(self.startDrawAreaCAM2)
        self.remove_CAM2.clicked.connect(self.removeAreaCAM2)

        self.draw_CAM3.clicked.connect(self.startDrawAreaCAM3)
        self.remove_CAM3.clicked.connect(self.removeAreaCAM3)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Three IP CAM"))
        self.label_4.setText(_translate("Form", "IP CAM 1"))
        self.label_5.setText(_translate("Form", "IP CAM 2"))
        self.label_6.setText(_translate("Form", "IP CAM 3"))
        self.startCAM1.setText(_translate("Form", "Start"))
        self.personReID_CAM1.setText(_translate("Form", "Person ReID"))
        self.faceRecognition_CAM1.setText(_translate("Form", "Face Recognition"))
        self.stopCAM1.setText(_translate("Form", "Stop"))
        self.areaProtect_CAM1.setText(_translate("Form", "Area Protection"))
        self.fallDetection_CAM1.setText(_translate("Form", "Fall Detection"))
        self.start_CAM2.setText(_translate("Form", "Start"))
        self.start_CAM3.setText(_translate("Form", "Start"))
        self.personReID_CAM2.setText(_translate("Form", "Person ReID"))
        self.personReID_CAM3.setText(_translate("Form", "Person ReID"))
        self.faceRecognition_CAM2.setText(_translate("Form", "Face Recognition"))
        self.faceRecognition_CAM3.setText(_translate("Form", "Face Recognition"))
        self.stop_CAM2.setText(_translate("Form", "Stop"))
        self.stop_CAM3.setText(_translate("Form", "Stop"))
        self.areaProtection_CAM2.setText(_translate("Form", "Area Protection"))
        self.areaProtection_CAM3.setText(_translate("Form", "Area Protection"))
        self.fallDetection_CAM2.setText(_translate("Form", "Fall Detection"))
        self.fallDetection_CAM3.setText(_translate("Form", "Fall Detection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "3 IP CAMs"))
        self.open.setText(_translate("Form", "Open"))
        self.play.setText(_translate("Form", "Play"))
        self.pause.setText(_translate("Form", "Pause"))
        self.stop.setText(_translate("Form", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "PLAY RECORD"))
        self.label_7.setText(_translate("Form", "IP CAM 2"))
        self.label_8.setText(_translate("Form", "IP CAM 1"))
        self.label_9.setText(_translate("Form", "IP CAM 3"))
        self.draw_CAM2.setText(_translate("Form", "Draw Area"))
        self.remove_CAM2.setText(_translate("Form", "Remove Area"))
        self.draw_CAM3.setText(_translate("Form", "Draw Area"))
        self.remove_CAM3.setText(_translate("Form", "Remove Area"))
        self.draw_CAM1.setText(_translate("Form", "Draw Area"))
        self.remove_CAM1.setText(_translate("Form", "Remove Area"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "SETTINGS"))

    def open_file(self):
      filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.tab_2, 'open')
      if filename != '':
        print(filename)
        self.mediaPlayer.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile(filename)))

    def play_video(self):
      self.mediaPlayer.play()

    def pause_video(self):
      self.mediaPlayer.pause()
    
    def stop_video(self):
      self.mediaPlayer.stop()

    def position_changed(self, position):
      self.horizontalSlider.setValue(position)

    def duration_changed(self, duration):
      self.horizontalSlider.setRange(0, duration)

    def set_position(self, position):
      self.mediaPlayer.setPosition(position)

    def image_to_QImage(self, image, label):
      image = cv2.resize(image, (label.width(), label.height()))
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      height , width, channel = image.shape
      step = channel * width
      return QImage(image.data, width, height, step, QImage.Format_RGB888)

        
    def viewCam(self):
        ret, image = self.cap.read()
        self.outVivdeo.write(image)
        self.CAM1_Draw.setPixmap(QPixmap.fromImage(self.image_to_QImage(self.drawArea(image, self.points_CAM1, self.CAM1_Draw), self.CAM1_Draw)))
        self.CAM1.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM1)))        
        
    def start_view(self):
        if not self.timer.isActive():
            self.stopCAM1.setEnabled(True)
            self.startCAM1.setEnabled(False)
            self.cap = cv2.VideoCapture(IP_CAM_ADDRESS['CAM1'])
            self.flag_CAM1 = self.cap.isOpened()
            if self.cap.isOpened():
              now = datetime.now()
              self.savePath1 = self.createDir('IP_CAM_1')
              self.startTime1 = str(now.day)+' - '+str(now.hour)+':'+str(now.minute)+ ' - '
              fourcc = cv2.VideoWriter_fourcc(*'mp4v')
              self.outVivdeo = cv2.VideoWriter(self.savePath1+'output.mp4', fourcc, 30, (int(self.cap.get(3)), int(self.cap.get(4))))
              self.timer.start(0)
            else:
              self.startCAM1.setEnabled(True)
              self.stopCAM1.setEnabled(False)
              image = cv2.imread('no-connection.jpg')
              self.CAM1.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM1)))

    def stop_view(self):
        self.startCAM1.setEnabled(True)
        self.stopCAM1.setEnabled(False)
        now = datetime.now()
        fileName = self.startTime1+str(now.hour)+':'+str(now.minute)+'.mp4'
        os.rename(self.savePath1+'output.mp4', self.savePath1+fileName)
        self.timer.stop()
        self.outVivdeo.release()
        image = cv2.imread('stopVideo.png')
        self.CAM1.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM1)))
        self.cap.release()

    def viewCam2(self):
        ret, image = self.cap2.read()
        self.outVivdeo2.write(image)
        self.CAM2_Draw.setPixmap(QPixmap.fromImage(self.image_to_QImage(self.drawArea(image, self.points_CAM2, self.CAM2_Draw), self.CAM2_Draw)))
        self.CAM2.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM2)))        
        
    def start_view2(self):
        if not self.timer2.isActive():
            self.stop_CAM2.setEnabled(True)
            self.start_CAM2.setEnabled(False)
            self.cap2 = cv2.VideoCapture(IP_CAM_ADDRESS['CAM2'])
            self.flag_CAM2 = self.cap2.isOpened()
            if self.cap2.isOpened():
              now = datetime.now()
              self.savePath2 = self.createDir('IP_CAM_2')
              self.startTime2 = str(now.day)+' - '+str(now.hour)+':'+str(now.minute)+ ' - '
              fourcc = cv2.VideoWriter_fourcc(*'mp4v')
              self.outVivdeo2 = cv2.VideoWriter(self.savePath2+'output2.mp4', fourcc, 30, (int(self.cap2.get(3)), int(self.cap2.get(4))))
              self.timer2.start(0)
            else:
              self.start_CAM2.setEnabled(True)
              self.stop_CAM2.setEnabled(False)
              image = cv2.imread('no-connection.jpg')
              self.CAM2.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM2)))           

    def stop_view2(self):
        self.start_CAM2.setEnabled(True)
        self.stop_CAM2.setEnabled(False)
        now = datetime.now()
        fileName = self.startTime2+str(now.hour)+':'+str(now.minute)+'.mp4'
        os.rename(self.savePath2+'output2.mp4', self.savePath2+fileName)     
        self.timer2.stop()
        self.outVivdeo2.release()
        image = cv2.imread('stopVideo.png')
        self.CAM2.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM2)))
        self.cap2.release()

    def viewCam3(self):
        ret, image = self.cap3.read()
        self.outVivdeo3.write(image)
        self.CAM3_Draw.setPixmap(QPixmap.fromImage(self.image_to_QImage(self.drawArea(image, self.points_CAM3, self.CAM3_Draw), self.CAM3_Draw)))
        self.CAM3.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM3)))        
        
    def start_view3(self):
        if not self.timer3.isActive():
            self.stop_CAM3.setEnabled(True)
            self.start_CAM3.setEnabled(False)
            self.cap3 = cv2.VideoCapture(IP_CAM_ADDRESS['CAM3'])
            self.flag_CAM3 = self.cap3.isOpened()
            if self.cap3.isOpened():
              now = datetime.now()
              self.savePath3 = self.createDir('IP_CAM_3')
              self.startTime3 = str(now.day)+' - '+str(now.hour)+':'+str(now.minute)+ ' - '
              fourcc = cv2.VideoWriter_fourcc(*'mp4v')
              self.outVivdeo3 = cv2.VideoWriter(self.savePath3+'output3.mp4', fourcc, 30, (int(self.cap3.get(3)), int(self.cap3.get(4))))
              self.timer3.start(0)
            else:
              self.start_CAM3.setEnabled(True)
              self.stop_CAM3.setEnabled(False)
              image = cv2.imread('no-connection.jpg')
              self.CAM3.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM3)))           

    def stop_view3(self):
        self.start_CAM3.setEnabled(True)
        self.stop_CAM3.setEnabled(False)
        now = datetime.now()
        fileName = self.startTime3+str(now.hour)+':'+str(now.minute)+'.mp4'
        os.rename(self.savePath3+'output3.mp4', self.savePath3+fileName)     
        self.timer3.stop()
        self.outVivdeo3.release()
        image = cv2.imread('stopVideo.png')
        self.CAM3.setPixmap(QPixmap.fromImage(self.image_to_QImage(image, self.CAM3)))
        self.cap3.release()
        
    def createDir(self, IP_CAM_Number: str):
      now = datetime.now()
      year = now.year
      month = MONTH[now.month]

      curPath = os.getcwd()
      if not path.exists(curPath+'/IVA'):
        os.mkdir(curPath+'/IVA')
      if not path.exists(curPath+'/IVA/'+IP_CAM_Number):
        os.mkdir(curPath+'/IVA/'+IP_CAM_Number)


      # check path exists
      if path.exists(curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)):
        if path.exists(curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month):
          return curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month + '/'
        else:
          os.mkdir(curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month)
          return curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month+'/'
      else:
        os.mkdir(curPath+'/IVA/'+IP_CAM_Number+'/'+str(year))
        if path.exists(curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month):
          return curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month + '/'
        else:
          os.mkdir(curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month)
          return curPath+'/IVA/'+IP_CAM_Number+'/'+str(year)+'/'+month+'/'


    # Create Mouse Event for draw protected area
    def mouseEventCAM1(self, event):
      if self.remove_CAM1.isEnabled() and (not self.startCAM1.isEnabled()) and self.flag_CAM1 == True:
        x = event.pos().x()
        y = event.pos().y()
        self.points_CAM1.append([x, y])
        print("Position clicked is ({}, {})".format(x, y))

    def mouseEventCAM2(self, event):
      if self.remove_CAM2.isEnabled() and (not self.start_CAM2.isEnabled()) and self.flag_CAM2 == True:
        x = event.pos().x()
        y = event.pos().y()
        self.points_CAM2.append([x, y])
        print("Position clicked is ({}, {})".format(x, y))

    def mouseEventCAM3(self, event):
      if self.remove_CAM3.isEnabled() and (not self.start_CAM3.isEnabled()) and self.flag_CAM3 == True:
        x = event.pos().x()
        y = event.pos().y()
        self.points_CAM3.append([x, y])
        print("Position clicked is ({}, {})".format(x, y))

    def startDrawAreaCAM1(self):
      self.draw_CAM1.setEnabled(False)
      self.remove_CAM1.setEnabled(True)

    def removeAreaCAM1(self):
      while len(self.points_CAM1):
        self.points_CAM1.pop()
      self.draw_CAM1.setEnabled(True)
      self.remove_CAM1.setEnabled(False)
    
    def startDrawAreaCAM2(self):
      self.draw_CAM2.setEnabled(False)
      self.remove_CAM2.setEnabled(True)
    
    def removeAreaCAM2(self):
      while len(self.points_CAM2):
        self.points_CAM2.pop()
      self.draw_CAM2.setEnabled(True)
      self.remove_CAM2.setEnabled(False)

    def startDrawAreaCAM3(self):
      self.draw_CAM3.setEnabled(False)
      self.remove_CAM3.setEnabled(True)

    def removeAreaCAM3(self):
      while len(self.points_CAM3):
        self.points_CAM3.pop()
      self.draw_CAM3.setEnabled(True)
      self.remove_CAM3.setEnabled(False)

    def drawArea(self, image, points: list, qlabel: QtWidgets.QLabel):
      image_draw = image.copy()
      image_draw = cv2.resize(image_draw, (qlabel.width(), qlabel.height()))
      # print(len(points))
      if len(points) > 1:
        cv2.polylines(image_draw, np.array([points]), 1, (255, 0, 0), 1)
        b, g, r = cv2.split(image_draw)
        cv2.fillPoly(b, np.array([points]), (0, 255, 0))
        cv2.fillPoly(r, np.array([points]), (0, 255, 0))
        image_draw = cv2.merge([b, g, r])
      return image_draw




import icons_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())