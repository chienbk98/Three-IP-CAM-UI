from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QGridLayout, \
    QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon, QPalette, QImage, QPixmap, QMouseEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QTimer

from datetime import datetime
from os import path
import numpy as np
import time
import sys
import cv2
import os

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

IP_CAM_ADDRESS = {'CAM1': 0, 'CAM2':'http://192.168.1.6:8080/video', 'CAM3': 'http://192.168.1.8:8080/video'}
class Ui_Form(QWidget):
  def __init__(self):
      super().__init__()
      self.points_CAM1 = []
      self.points_CAM2 = []
      self.points_CAM3 = []
  def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(580, 580)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.multiTab = QtWidgets.QWidget()
        self.multiTab.setObjectName("multiTab")
# cam1
        self.cam_1 = QtWidgets.QWidget(self.multiTab)
        self.cam_1.setObjectName("cam_1")
        self.CAM1 = QtWidgets.QLabel(self.cam_1)
        self.CAM1.setFrameShape(QtWidgets.QFrame.Box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CAM1.sizePolicy().hasHeightForWidth())
        self.CAM1.setSizePolicy(sizePolicy)
        self.CAM1.setMinimumSize(QtCore.QSize(320, 240))
        self.CAM1.setMaximumSize(QtCore.QSize(400, 320))
        self.CAM1.setSizeIncrement(QtCore.QSize(3, 2))
        self.CAM1.setScaledContents(True)
        self.CAM1.setObjectName("CAM1")
        self.startCAM1 = QtWidgets.QPushButton(self.cam_1)
        self.startCAM1.setObjectName("startCAM1")
        self.stopCAM1 = QtWidgets.QPushButton(self.cam_1)
        self.stopCAM1.setObjectName("stopCAM1")
        self.reIDBtn_1 = QtWidgets.QPushButton(self.cam_1)
        self.reIDBtn_1.setObjectName("reIDBtn_1")
        self.falldetectionBtn_1 = QtWidgets.QPushButton(self.cam_1)
        self.falldetectionBtn_1.setObjectName("falldetectionBtn_1")
        self.peoplecntBtn_1 = QtWidgets.QPushButton(self.cam_1)
        self.peoplecntBtn_1.setObjectName("peoplecntBtn_1")
        self.areaprotectionBtn_1 = QtWidgets.QPushButton(self.cam_1)
        self.areaprotectionBtn_1.setObjectName("areaprotectionBtn_1")

        layoutCam_1 = QGridLayout(self.cam_1)
        layoutCam_1.addWidget(self.CAM1, 0,0,7,3)
        layoutCam_1.addWidget(self.startCAM1, 8, 0)
        layoutCam_1.addWidget(self.stopCAM1, 9, 0)
        layoutCam_1.addWidget(self.reIDBtn_1, 8,1)
        layoutCam_1.addWidget(self.falldetectionBtn_1, 8, 2)
        layoutCam_1.addWidget(self.peoplecntBtn_1, 9,1)
        layoutCam_1.addWidget(self.areaprotectionBtn_1, 9,2)
        self.cam_1.setLayout(layoutCam_1)

# Setting Multi_tab Cam 2        
        self.cam_2 = QtWidgets.QWidget(self.multiTab)
        self.cam_2.setObjectName("cam_2")
        self.CAM2 = QtWidgets.QLabel(self.cam_2)
        self.CAM2.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM2.setSizePolicy(sizePolicy)
        self.CAM2.setMinimumSize(QtCore.QSize(320, 240))
        self.CAM2.setMaximumSize(QtCore.QSize(400, 320))
        self.CAM2.setSizeIncrement(QtCore.QSize(3, 2))
        self.CAM2.setObjectName("CAM2")
        self.CAM2.setScaledContents(True)
        self.peoplecntBtn_2 = QtWidgets.QPushButton(self.cam_2)
        self.peoplecntBtn_2.setObjectName("peoplecntBtn_2")
        self.falldetectionBtn_2 = QtWidgets.QPushButton(self.cam_2)
        self.falldetectionBtn_2.setObjectName("falldetectionBtn_2")
        self.reIDBtn_2 = QtWidgets.QPushButton(self.cam_2)
        self.reIDBtn_2.setObjectName("reIDBtn_2")
        self.stop_CAM2 = QtWidgets.QPushButton(self.cam_2)
        self.stop_CAM2.setObjectName("stop_CAM2")
        self.start_CAM2 = QtWidgets.QPushButton(self.cam_2)
        self.start_CAM2.setObjectName("start_CAM2")
        self.areaprotectionBtn_2 = QtWidgets.QPushButton(self.cam_2)
        self.areaprotectionBtn_2.setObjectName("areaprotectionBtn_2")

        layoutCam_2 = QGridLayout(self.cam_2)
        layoutCam_2.addWidget(self.CAM2, 0,0,7,3)
        layoutCam_2.addWidget(self.start_CAM2, 8, 0)
        layoutCam_2.addWidget(self.stop_CAM2, 9, 0)
        layoutCam_2.addWidget(self.reIDBtn_2, 8,1)
        layoutCam_2.addWidget(self.falldetectionBtn_2, 8, 2)
        layoutCam_2.addWidget(self.peoplecntBtn_2, 9,1)
        layoutCam_2.addWidget(self.areaprotectionBtn_2, 9,2)
        self.cam_2.setLayout(layoutCam_2)
        

# Setting Multi_tab Cam 3        
        self.cam_3 = QtWidgets.QWidget(self.multiTab)
        self.cam_3.setObjectName("cam_3")
        self.CAM3 = QtWidgets.QLabel(self.cam_3)
        self.CAM3.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM3.setSizePolicy(sizePolicy)
        self.CAM3.setMinimumSize(QtCore.QSize(320, 240))
        self.CAM3.setMaximumSize(QtCore.QSize(400, 320))
        self.CAM3.setSizeIncrement(QtCore.QSize(3, 2))
        self.CAM3.setObjectName("CAM3")
        self.CAM3.setScaledContents(True)
        self.peoplecntBtn_3 = QtWidgets.QPushButton(self.cam_3)
        self.peoplecntBtn_3.setObjectName("peoplecntBtn_3")
        self.falldetectionBtn_3 = QtWidgets.QPushButton(self.cam_3)
        self.falldetectionBtn_3.setObjectName("falldetectionBtn_3")
        self.reIDBtn_3 = QtWidgets.QPushButton(self.cam_3)
        self.reIDBtn_3.setObjectName("reIDBtn_3")
        self.stop_CAM3 = QtWidgets.QPushButton(self.cam_3)
        self.stop_CAM3.setObjectName("stop_CAM3")
        self.start_CAM3 = QtWidgets.QPushButton(self.cam_3)
        self.start_CAM3.setObjectName("start_CAM3")
        self.areaprotectionBtn_3 = QtWidgets.QPushButton(self.cam_3)
        self.areaprotectionBtn_3.setObjectName("areaprotectionBtn_3")
        
        layoutCam_3 = QGridLayout(self.cam_3)
        layoutCam_3.addWidget(self.CAM3, 0,0,7,3)
        layoutCam_3.addWidget(self.start_CAM3, 8, 0)
        layoutCam_3.addWidget(self.stop_CAM3, 9, 0)
        layoutCam_3.addWidget(self.reIDBtn_3, 8,1)
        layoutCam_3.addWidget(self.falldetectionBtn_3, 8, 2)
        layoutCam_3.addWidget(self.peoplecntBtn_3, 9,1)
        layoutCam_3.addWidget(self.areaprotectionBtn_3, 9,2)
        self.cam_3.setLayout(layoutCam_3)
        


# Setting layout multi_tab
        layoutMultitab=QGridLayout(self.multiTab)
        layoutMultitab.addWidget(self.cam_1, 0,0)
        layoutMultitab.addWidget(self.cam_2,0,1 )
        layoutMultitab.addWidget(self.cam_3,0,2)     
        self.multiTab.setLayout(layoutMultitab)
        self.tabWidget.addTab(self.multiTab, "")



#=============================================================================================================================        
        
        self.playRec = QtWidgets.QWidget()
        self.playRec.setObjectName("playRec")
        self.tabWidget.addTab(self.playRec, "")
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        #create videowidget object
        videowidget = QVideoWidget()
        #create open button
        self.openBtn = QtWidgets.QPushButton('Open Video')
        
        #create button for playing
        self.playBtn = QtWidgets.QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        
        self.stopBtn = QtWidgets.QPushButton()
        self.stopBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        
        self.slowBtn = QtWidgets.QPushButton()
        self.slowBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekBackward))
        
        self.fastBtn = QtWidgets.QPushButton()
        self.fastBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaSeekForward))
        
        self.volumeBtn = QtWidgets.QPushButton()
        self.volumeBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        
        self.fullscreenBtn = QPushButton("Full Screen")

        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0,100)
        self.volume_slider.setValue(100)
        
        #create label
        self.label_2_1 = QLabel()
        self.label_2_1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.label_2_2 = QLabel()
 
         #create hbox layout
        hboxLayout_2_1 = QHBoxLayout()
        hboxLayout_2_2 = QHBoxLayout()
        hboxLayout_2_3 = QHBoxLayout()
 
         #set widgets to the hbox layout
        hboxLayout_2_1.addWidget(self.slider) 
        hboxLayout_2_2.addWidget(self.openBtn)
        hboxLayout_2_2.addWidget(self.stopBtn)
        hboxLayout_2_2.addWidget(self.slowBtn)
        hboxLayout_2_2.addWidget(self.playBtn)
        hboxLayout_2_2.addWidget(self.fastBtn)
        hboxLayout_2_2.addWidget(self.volumeBtn)
        hboxLayout_2_2.addWidget(self.volume_slider)
        hboxLayout_2_2.addStretch(1)
        hboxLayout_2_2.addWidget(self.fullscreenBtn)
        
        hboxLayout_2_3.addWidget(videowidget)

        #create vbox layout
        vboxLayout_2_1 = QVBoxLayout()
        vboxLayout_2_1.addLayout(hboxLayout_2_3)
        vboxLayout_2_1.addLayout(hboxLayout_2_1)
        vboxLayout_2_1.addLayout(hboxLayout_2_2)
        vboxLayout_2_1.addWidget(self.label_2_1)
        self.playRec.setLayout(vboxLayout_2_1)
        
#===================================================================================================================================
#Tab Setting
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.tabWidget.addTab(self.setting, "")
        
        self.camSetting_1 = QtWidgets.QWidget(self.setting)
        self.camSetting_1.setObjectName("camSetting_1")
        self.CAM1_Draw = QtWidgets.QLabel(self.camSetting_1)
        self.CAM1_Draw.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM1_Draw.setSizePolicy(sizePolicy)
        self.CAM1_Draw.setMinimumSize(QtCore.QSize(320, 240))
        self.CAM1_Draw.setMaximumSize(QtCore.QSize(400, 320))
        self.CAM1_Draw.setSizeIncrement(QtCore.QSize(3, 2))
        self.CAM1_Draw.setObjectName("CAM1_Draw")
        self.draw_CAM1 = QtWidgets.QPushButton(self.camSetting_1)
        self.draw_CAM1.setObjectName("draw_CAM1")
        self.remove_CAM1 = QtWidgets.QPushButton(self.camSetting_1)
        self.remove_CAM1.setObjectName("remove_CAM1")
        
        layoutCamSetting_1 = QGridLayout()
        layoutCamSetting_1.addWidget(self.CAM1_Draw, 0,0,7,4)
        layoutCamSetting_1.addWidget(self.draw_CAM1, 8,1)
        layoutCamSetting_1.addWidget(self.remove_CAM1, 8,2)
        self.camSetting_1.setLayout(layoutCamSetting_1)
        
#camSetting 2       
        self.camSetting_2 = QtWidgets.QWidget(self.setting)
        self.camSetting_2.setObjectName("camSetting_2")
        self.CAM2_Draw = QtWidgets.QLabel(self.camSetting_2)
        self.CAM2_Draw.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM2_Draw.setSizePolicy(sizePolicy)
        self.CAM2_Draw.setMinimumSize(QtCore.QSize(320, 240))
        self.CAM2_Draw.setMaximumSize(QtCore.QSize(400, 320))
        self.CAM2_Draw.setSizeIncrement(QtCore.QSize(3, 2))
        self.CAM2_Draw.setObjectName("CAM2_Draw")
        self.draw_CAM2 = QtWidgets.QPushButton(self.camSetting_2)
        self.draw_CAM2.setObjectName("draw_CAM2")
        self.remove_CAM2 = QtWidgets.QPushButton(self.camSetting_2)
        self.remove_CAM2.setObjectName("remove_CAM2")
        
        layoutCamSetting_2 = QGridLayout()
        layoutCamSetting_2.addWidget(self.CAM2_Draw, 0,0,7,4)
        layoutCamSetting_2.addWidget(self.draw_CAM2, 8,1)
        layoutCamSetting_2.addWidget(self.remove_CAM2, 8,2)
        self.camSetting_2.setLayout(layoutCamSetting_2)
        
#camSeting 3
        self.camSetting_3 = QtWidgets.QWidget(self.setting)
        self.camSetting_3.setObjectName("camSetting_3")
        self.CAM3_Draw = QtWidgets.QLabel(self.camSetting_3)
        self.CAM3_Draw.setFrameShape(QtWidgets.QFrame.Box)
        self.CAM3_Draw.setSizePolicy(sizePolicy)
        self.CAM3_Draw.setMinimumSize(QtCore.QSize(320, 240))
        self.CAM3_Draw.setMaximumSize(QtCore.QSize(400, 320))
        self.CAM3_Draw.setSizeIncrement(QtCore.QSize(3, 2))
        self.CAM3_Draw.setObjectName("CAM3_Draw")
        self.draw_CAM3 = QtWidgets.QPushButton(self.camSetting_3)
        self.draw_CAM3.setObjectName("draw_CAM3")
        self.remove_CAM3 = QtWidgets.QPushButton(self.camSetting_3)
        self.remove_CAM3.setObjectName("remove_CAM3")
        
        layoutCamSetting_3 = QGridLayout()
        layoutCamSetting_3.addWidget(self.CAM3_Draw, 0,0,7,4)
        layoutCamSetting_3.addWidget(self.draw_CAM3, 8,1)
        layoutCamSetting_3.addWidget(self.remove_CAM3, 8,2)
        self.camSetting_3.setLayout(layoutCamSetting_3)
        
#layout Setting        
        layoutSetting = QGridLayout()
        layoutSetting.addWidget(self.camSetting_1, 0,0)
        layoutSetting.addWidget(self.camSetting_2, 0,1)
        layoutSetting.addWidget(self.camSetting_3, 0,2)
        
        self.setting.setLayout(layoutSetting)

        self.mediaPlayer.setVideoOutput(videowidget)
        self.openBtn.clicked.connect(self.open_file)
        self.playBtn.clicked.connect(self.play_video)
        self.stopBtn.clicked.connect(self.stop_video)
        self.fastBtn.clicked.connect(self.fast)
        self.slowBtn.clicked.connect(self.slow)
        self.volumeBtn.clicked.connect(self.mute)
        self.fullscreenBtn.clicked.connect(self.fullscreen)
        self.volume_slider.sliderMoved.connect(self.set_volume)
        self.slider.sliderMoved.connect(self.set_position)
        
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

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





#Form.setLayout(tabWidget)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        a= QVBoxLayout()
        a.addWidget(self.tabWidget)
        Form.setLayout(a)
  def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CAM1.setText(_translate("Form", "Cam 1"))
        self.peoplecntBtn_1.setText(_translate("Form", "People Counting"))
        self.falldetectionBtn_1.setText(_translate("Form", "Fall Detection"))
        self.reIDBtn_1.setText(_translate("Form", "Person Re-ID"))
        self.stopCAM1.setText(_translate("Form", "Stop"))
        self.startCAM1.setText(_translate("Form", "Start"))
        self.areaprotectionBtn_1.setText(_translate("Form", "Area Protection"))
      
        self.CAM2.setText(_translate("Form", "cam 2"))
        self.peoplecntBtn_2.setText(_translate("Form", "People Counting"))
        self.falldetectionBtn_2.setText(_translate("Form", "Fall Detection"))
        self.reIDBtn_2.setText(_translate("Form", "Person Re-ID"))
        self.stop_CAM2.setText(_translate("Form", "Stop"))
        self.start_CAM2.setText(_translate("Form", "Start"))
        self.areaprotectionBtn_2.setText(_translate("Form", "Area Protection"))
        
        self.CAM3.setText(_translate("Form", "cam 3"))
        self.peoplecntBtn_3.setText(_translate("Form", "People Counting"))
        self.falldetectionBtn_3.setText(_translate("Form", "Fall Detection"))
        self.reIDBtn_3.setText(_translate("Form", "Person Re-ID"))
        self.stop_CAM3.setText(_translate("Form", "Stop"))
        self.start_CAM3.setText(_translate("Form", "Start"))
        self.areaprotectionBtn_3.setText(_translate("Form", "Area Protection"))
        
        self.CAM1_Draw.setText(_translate("Form", "cam 1"))
        self.draw_CAM1.setText(_translate("Form", "Draw"))
        self.remove_CAM1.setText(_translate("Form", "Clean"))
        
        self.CAM2_Draw.setText(_translate("Form", "cam 2"))
        self.draw_CAM2.setText(_translate("Form", "Draw"))
        self.remove_CAM2.setText(_translate("Form", "Clean"))
        
        self.CAM3_Draw.setText(_translate("Form", "cam 3"))
        self.draw_CAM3.setText(_translate("Form", "Draw"))
        self.remove_CAM3.setText(_translate("Form", "Clean"))
        
                
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiTab), _translate("Form", "Multi_IPCam"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playRec), _translate("Form", "Play Record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("Form", "Setting"))



  def open_file(self):
      filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

      if filename != '':
          self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
          self.playBtn.setEnabled(True)

  def play_video(self):
      if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
          self.mediaPlayer.pause()
      else:
          self.mediaPlayer.play()
  def stop_video(self):
      self.mediaPlayer.stop()

  def mediastate_changed(self, state):
      if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
          self.playBtn.setIcon(
              self.style().standardIcon(QStyle.SP_MediaPause)
          )
      else:
          self.playBtn.setIcon(
              self.style().standardIcon(QStyle.SP_MediaPlay)
          )

  def position_changed(self, position):
      self.slider.setValue(position)

  def duration_changed(self, duration):
      self.slider.setRange(0, duration)

  def set_position(self, position):
      self.mediaPlayer.setPosition(position)
      print(position)
  
  def set_volume(self, volume):
      self.mediaPlayer.setVolume(volume)
  
  def mute(self):
      if not self.mediaPlayer.isMuted():
          self.mediaPlayer.setMuted(True)
          self.volumeBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolumeMuted))
      else:
          self.mediaPlayer.setMuted(False)
          self.volumeBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))

  def handle_errors(self):
      self.playBtn.setEnabled(False)
      self.label.setText("Error: " + self.mediaPlayer.errorString())
      
      self.startCAM1.clicked.connect(self.start)
      self.stopCAM1.clicked.connect(self.stop)
      
  def fullscreen(self):
      if self.windowState() & Qt.WindowFullScreen:
          QApplication.setOverrideCursor(Qt.ArrowCursor)
          self.showNormal()
          print("no Fullscreen")
      else:
          self.showFullScreen()
          #QApplication.setOverrideCursor(Qt.BlankCursor)
          print("Fullscreen entered")

  def fast(self):
      self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10*60)

  def slow(self):
    self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10*60)


  def image_to_QImage(self, image, label):
    # image = cv2.resize(image, (label.width(), label.height()))
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
            # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.outVivdeo = cv2.VideoWriter(self.savePath1+'output.avi', fourcc, 30, (int(self.cap.get(3)), int(self.cap.get(4))))
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
      fileName = self.startTime1+str(now.hour)+':'+str(now.minute)+'.avi'
      os.rename(self.savePath1+'output.avi', self.savePath1+fileName)
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
            # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.outVivdeo2 = cv2.VideoWriter(self.savePath2+'output2.avi', fourcc, 30, (int(self.cap2.get(3)), int(self.cap2.get(4))))
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
      fileName = self.startTime2+str(now.hour)+':'+str(now.minute)+'.avi'
      os.rename(self.savePath2+'output2.avi', self.savePath2+fileName)     
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
            # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.outVivdeo3 = cv2.VideoWriter(self.savePath3+'output3.avi', fourcc, 30, (int(self.cap3.get(3)), int(self.cap3.get(4))))
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
      fileName = self.startTime3+str(now.hour)+':'+str(now.minute)+'.avi'
      os.rename(self.savePath3+'output3.avi', self.savePath3+fileName)     
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())