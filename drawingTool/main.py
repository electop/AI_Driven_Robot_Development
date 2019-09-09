import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
import datetime
import serial
import time

#global variable for file name (does not work)
strFilename1 = "./images/screen_capture_cartoonized_mask_.jpg"
strFilename2 = "./images/screen_capture_cartoonized_.jpg"
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

# gcode sender function
# open serial port and write each gcode (and get return)
# need to install phtyon pySerial
def simpleGcodesender():
    s = serial.Serial("/dev/ttyUSB1",115200)
    #/dev/ttyUSB0
    print("Opening Serial Port")
    f = open("faceGcode.gcode","r")
    # Wake up 
    s.write(str.encode("\r\n\r\n")) # Hit enter a few times to wake the Printrbot
    time.sleep(2)   # Wait for Printrbot to initialize
    s.flushInput()  # Flush startup text in serial input
    print("Sending gcode")

    for line in f:
        l = removeComment(line)
        l = l.strip() # Strip all EOL characters for streaming
        if (l.isspace()==False and len(l)>0):
            #print("Sending: " + l)
            #s.write(l + "\n") # Send g-code block
            s.write(str.encode(l + "\n"))
            grbl_out = s.readline() # Wait for response with carriage return
            #print(" : " + grbl_out.strip())
 
    # Wait here until printing is finished to close serial port and file.
    #raw_input("  Press <Enter> to exit.")
    # Close file and serial port
    f.close()
    s.close()
    print("Drawing is over")

    


#gcode comment remover
#Eliminate gocde comment
def removeComment(string):
    if (string.find(';')==-1):
        return string
    else:
        return string[:string.index(';')]



# import capture function
# Function for Camera Ready
def cam(now):
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("./images/screen_capture_%s.jpg" % now, frame)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Function for cartoonizing
# based on image processing
# make it as 1 color drawing
# save jpg file in the ./images/ folder
def cartoonizer(now):
    num_down = 2       # number of downsampling steps
    num_bilateral = 7  # number of bilateral filtering steps
    
    img_rgb = cv2.imread("./images/screen_capture_%s.jpg" % now)
 
    # downsample image using Gaussian pyramid
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
    
    # repeatedly apply small bilateral filter instead of
    # applying one large filter
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9,
                                        sigmaColor=9,
                                        sigmaSpace=7)
    
    # upsample image to original size
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)

    # convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    rows, cols, channels = img_rgb.shape
    roi = img_color[0:rows, 0:cols]

    # detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY,
                                    blockSize=9,
                                    C=2)

    img_median = cv2.medianBlur(img_edge, 5)
    edge_compare = np.concatenate((img_edge, img_median), axis=1)
    cv2.imshow("edge_compare", edge_compare)
    ret, mask = cv2.threshold(img_median, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # convert back to color, bit-AND with color image
    img_edge = cv2.cvtColor(img_median, cv2.COLOR_GRAY2RGB)
    #img_cartoon = cv2.bitwise_and(img_color, img_edge)

    img_cartoon_bg = cv2.bitwise_and(roi, roi, mask = mask)
    img_cartoon_fg = cv2.bitwise_and(img_edge, img_edge, mask = mask_inv)
    dst = cv2.add(img_cartoon_fg, img_cartoon_bg)
    img_color[0:rows, 0:cols] = dst

    # display
    #cv2.imshow("original", img_rgb)
    #cv2.imshow("edge", img_edge)
    #cv2.imshow("mask_inv", mask_inv)
    #cv2.imshow("color", img_color)
    #cv2.imshow("mask", mask)
    #cv2.imshow("cartoon", img_rgb)
    result_compare = np.concatenate((img_rgb, img_color), axis=1)
    cv2.imshow("result_compare", result_compare)
    cv2.waitKey(0)

    strFilename1 = "./images/screen_capture_cartoonized_mask_" + now + ".jpg"
    strFilename2 = "./images/screen_capture_cartoonized_" + now + ".jpg"

    #cv2.imwrite("./images/screen_capture_cartoonized_mask_%s.jpg" % now, mask)
    #cv2.imwrite("./images/screen_capture_cartoonized_%s.jpg" % now, img_rgb)
    cv2.imwrite("a.jpg", mask)
    cv2.imwrite(strFilename2, img_rgb)
    cv2.destroyAllWindows()


def imageCapturenCartoonizer():
    now = str(datetime.datetime.now())[:-7]
    cam(now)
    cartoonizer(now)

# Modify pixcel point to real mili meter point
# make it actual length for X and Y
def convertPixelX2mm(i):
    return i * 210 / 680

def convertPixelY2mm(i):
    return i * 148 / 480

# Modify drawing bot coordinate point
# absolute coordinate is - Y area
def convertRealY(y):
    return 0-y

# UI design using QWidget
#
class CWidget(QWidget): 
 
    def __init__(self):
 
        super().__init__()
 
        # 전체 폼 박스
        formbox = QHBoxLayout()
        self.setLayout(formbox)
 
        # 좌, 우 레이아웃박스
        left = QVBoxLayout()
        right = QVBoxLayout()
 
        # 그룹박스1 생성 및 좌 레이아웃 배치
        gb = QGroupBox('그리기 종류')        
        left.addWidget(gb)
 
        # 그룹박스1 에서 사용할 레이아웃
        box = QVBoxLayout()
        gb.setLayout(box)        
 
        # 그룹박스 1 의 라디오 버튼 배치
        text = ['line', 'Curve', 'Rectange', 'Ellipse']
        self.radiobtns = []
 
        for i in range(len(text)):
            self.radiobtns.append(QRadioButton(text[i], self))
            self.radiobtns[i].clicked.connect(self.radioClicked)
            box.addWidget(self.radiobtns[i])
 
        self.radiobtns[0].setChecked(True)
        self.drawType = 0
         
        # 그룹박스2
        gb = QGroupBox('펜 설정')        
        left.addWidget(gb)        
 
        grid = QGridLayout()      
        gb.setLayout(grid)        
 
        label = QLabel('선굵기')
        grid.addWidget(label, 0, 0)
 
        self.combo = QComboBox()
        grid.addWidget(self.combo, 0, 1)       
 
        for i in range(1, 21):
            self.combo.addItem(str(i))
 
        label = QLabel('선색상')
        grid.addWidget(label, 1,0)        
         
        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton()        
        self.penbtn.setStyleSheet('background-color: rgb(0,0,0)')
        self.penbtn.clicked.connect(self.showColorDlg)
        grid.addWidget(self.penbtn,1, 1)

        # 그룹박스3
        gb = QGroupBox('붓 설정')        
        left.addWidget(gb)
 
        hbox = QHBoxLayout()
        gb.setLayout(hbox)
 
        label = QLabel('붓색상')
        hbox.addWidget(label)                
 
        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()        
        self.brushbtn.setStyleSheet('background-color: rgb(255,255,255)')
        self.brushbtn.clicked.connect(self.showColorDlg)
        hbox.addWidget(self.brushbtn)
 
        # 그룹박스4
        gb = QGroupBox('지우개')        
        left.addWidget(gb)
 
        hbox = QHBoxLayout()
        gb.setLayout(hbox)        
         
        self.checkbox  =QCheckBox('지우개 동작')
        self.checkbox.stateChanged.connect(self.checkClicked)
        hbox.addWidget(self.checkbox)
 
        # 그룹박스5
        gb = QGroupBox('CAPTURE')        
        left.addWidget(gb)

        hbox = QHBoxLayout()
        gb.setLayout(hbox)
 
        self.capturebtn = QPushButton()
        self.capturebtn.setIcon(QIcon(QPixmap("cam.png")))        
        #self.capturebtn.setStyleSheet('background-color: rgb(255,255,255)')
        self.capturebtn.clicked.connect(self.captureImageDlg)
        hbox.addWidget(self.capturebtn)
       
        # 그룹박스6
        gb = QGroupBox('DRAW')        
        left.addWidget(gb)

        hbox = QHBoxLayout()
        gb.setLayout(hbox)
 
        self.drawbtn = QPushButton()
        self.drawbtn.setIcon(QIcon(QPixmap("pen.png")))        
        self.drawbtn.clicked.connect(self.drawStartDlg)
        hbox.addWidget(self.drawbtn)

        left.addStretch(1)        
          
        # 우 레이아웃 박스에 그래픽 뷰 추가
        self.view = CView(self)       
        right.addWidget(self.view)        
 
        # 전체 폼박스에 좌우 박스 배치
        formbox.addLayout(left)
        formbox.addLayout(right)
 
        formbox.setStretchFactor(left, 0)
        formbox.setStretchFactor(right, 1)
         
        self.setGeometry(100, 100, 800, 500) 
         
    def radioClicked(self):
        for i in range(len(self.radiobtns)):
            if self.radiobtns[i].isChecked():
                self.drawType = i                
                break
 
    def checkClicked(self):
        pass



    def captureImageDlg(self):
    
        imageCapturenCartoonizer()

        # Capture image as a.jpg and reload on the right view              
        pic = QPixmap("a.jpg") 
        self.view.scene.addItem(QGraphicsPixmapItem(pic))  

        pass

    # no need dialogbox but start to drawing
    def drawStartDlg(self):
        str="M05 S10\nG01 F10000\nG01 X0 Y0"
        self.view.f.write(str)
        self.view.f.close()
        print("file closed")
        simpleGcodesender()
        pass
             
    def showColorDlg(self):       
         
        # 색상 대화상자 생성      
        color = QColorDialog.getColor()
 
        sender = self.sender()
 
        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if sender == self.penbtn and color.isValid():           
            self.pencolor = color
            self.penbtn.setStyleSheet('background-color: {}'.format( color.name()))
        else:
            self.brushcolor = color
            self.brushbtn.setStyleSheet('background-color: {}'.format( color.name()))
 
        
# QGraphicsView display QGraphicsScene
#
class CView(QGraphicsView):
    
    def __init__(self, parent):
 
        super().__init__(parent)       
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 2400, 1200) 
        pic = QPixmap("s.jpg") 
        self.scene.addItem(QGraphicsPixmapItem(pic))  

        self.setScene(self.scene)
 
        self.items = []
         
        self.start = QPointF()
        self.end = QPointF()
 
        self.setRenderHint(QPainter.HighQualityAntialiasing)

        # Start Writing GCode        
        self.f = open("faceGcode.gcode","w")
        self.f.write("G10 P0 L20 X0 Y0 Z0\n")
        self.f.write("M05 S10\n")
        self.f.write("G90\n")
        self.f.write("G21\n")

 
    def moveEvent(self, e):
        rect = QRectF(self.rect())
        rect.adjust(0,0,-2,-2)
 
        self.scene.setSceneRect(rect)

  
 
    def mousePressEvent(self, e):
 
        if e.button() == Qt.LeftButton:
            # 시작점 저장
            self.start = e.pos()
            self.end = e.pos()
            str="G01 F10000\nG01 X%4.3f Y%4.3f\nM03 S60\nG01 F1000\n" %(convertPixelX2mm(self.start.x()), convertRealY(convertPixelY2mm(self.start.y())))
            self.f.write(str)
 
    def mouseMoveEvent(self, e):  
         
        # e.buttons()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴 
        if e.buttons() & Qt.LeftButton:           
 
            self.end = e.pos()

 
            if self.parent().checkbox.isChecked():
                pen = QPen(QColor(255,255,255), 10)
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
                self.start = e.pos()
                return None
 
            pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
            # 직선 그리기
            if self.parent().drawType == 0:
                 
                # 장면에 그려진 이전 선을 제거            
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])                
 
                # 현재 선 추가
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())                
                self.items.append(self.scene.addLine(line, pen))
 
            # 곡선 그리기
            if self.parent().drawType == 1:
 
                
                str="G01 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.end.x()), convertRealY(convertPixelY2mm(self.end.y())))
                self.f.write(str)
                #print(str) 
                # Path 이용
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
 
                # Line 이용
                #line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                #self.scene.addLine(line, pen)
                 
                # 시작점을 다시 기존 끝점으로
                self.start = e.pos()
 
            # 사각형 그리기
            if self.parent().drawType == 2:
                brush = QBrush(self.parent().brushcolor)
 
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])
 
 
                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addRect(rect, pen, brush))
                 
            # 원 그리기
            if self.parent().drawType == 3:
                brush = QBrush(self.parent().brushcolor)
 
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del(self.items[-1])
 
 
                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addEllipse(rect, pen, brush))
 
 
    def mouseReleaseEvent(self, e):        
 
        if e.button() == Qt.LeftButton:
 
            if self.parent().checkbox.isChecked():
                return None
 
            pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
            if self.parent().drawType == 0:
 
                self.items.clear()
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                 
                self.scene.addLine(line, pen)

                # Add end point of line
                str="G01 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.end.x()), convertRealY(convertPixelY2mm(self.end.y())))
                self.f.write(str)
 
            if self.parent().drawType == 2:
 
                brush = QBrush(self.parent().brushcolor)
 
                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addRect(rect, pen, brush)

                # Add Rectangle piont 
                str="G01 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.end.x()), convertRealY(convertPixelY2mm(self.start.y())))
                self.f.write(str)
                str="G01 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.end.x()), convertRealY(convertPixelY2mm(self.end.y())))
                self.f.write(str)
                str="G01 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.start.x()), convertRealY(convertPixelY2mm(self.end.y())))
                self.f.write(str)
                str="G01 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.start.x()), convertRealY(convertPixelY2mm(self.start.y())))
                self.f.write(str)
 
 
            if self.parent().drawType == 3:
 
                brush = QBrush(self.parent().brushcolor)
 
                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addEllipse(rect, pen, brush)


                str="M05 S10\nG01 F10000\nG01 X%4.3f Y%4.3f\nM03 S60\n" %(convertPixelX2mm(self.start.x()), convertRealY(convertPixelY2mm(self.start.y() + (self.end.y() - self.start.y())/2 )))
                self.f.write(str)
                
                #print("start x %d y %d\n" %(self.start.x(), self.start.y()))
                #print("start x %d y %d\n" %(self.end.x(), self.end.y()))

                #print("G02 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.start.x()),convertRealY(convertPixelY2mm(self.start.y()))
                #print("G02 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.end.x()), convertRealY(convertPixelY2mm(self.end.y())))

                # Add circle piont 
                str="G02 F300 X%4.3f Y%4.3f I%4.3f\n" %(convertPixelX2mm(self.start.x()), convertRealY(convertPixelY2mm(self.start.y() + (self.end.y() - self.start.y())/2)), convertPixelX2mm((self.end.x()-self.start.x())/2))
                self.f.write(str)

        # When sending g code to drawing bot file is already closed. So this command cause error
        # need to flag when drawing bot is operated
        self.f.write("M05 S10\n")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())
