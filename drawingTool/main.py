import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np

 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    # Capture Image using OpenCV
    # make gray and pencil effect
def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

def grayscale(rgb):
#    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    return np.dot(rgb[...,:3], [0.333, 0.333, 0.333])

# Using OpenCV Capture Image and make it pencil drawing effect
def imageCapture():
    img_name='./images/s.jpg'
    key = cv2. waitKey(1)
    cap = cv2.VideoCapture(0)
    while True:

        # Take each frame
        rep, frame = cap.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename=img_name, img=frame)
            print("captured image is save as s.jpg")
            cap.release()
            break
        elif key== ord('q'):
            print("Turning off camera.")
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    #open Captured Image and make it like pencil drawing
    s=cv2.imread(img_name)
    grayImage = grayscale(s)
    invertedImage = 255-grayImage
    import scipy.ndimage
    gFiltered = scipy.ndimage.filters.gaussian_filter(invertedImage,sigma=30)
    pencilImage = dodge(gFiltered,grayImage)

    # Save as s.jpg
    cv2.imshow('draw',pencilImage)
    cv2.imwrite(filename=img_name, img=pencilImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Modify pixcel point to real mili meter point
def convertPixelX2mm(i):
    return i * 210 / 680


def convertPixelY2mm(i):
    return i * 148 / 480



# Modify drawing bot coordinate point
def convertRealY(y):
    return 0-y


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
        self.capturebtn.setStyleSheet('background-color: rgb(255,255,255)')
        self.capturebtn.clicked.connect(self.captureImageDlg)
        hbox.addWidget(self.capturebtn)
       

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
        imageCapture()
        # Need to Open captured image on the right scene
        # code TBD
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
        
        self.f = open("faceGcode.gcode","w")
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
                
                print("start x %d y %d\n" %(self.start.x(), self.start.y()))
                print("start x %d y %d\n" %(self.end.x(), self.end.y()))

                #print("G02 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.start.x()),convertRealY(convertPixelY2mm(self.start.y()))
                #print("G02 X%4.3f Y%4.3f\n" %(convertPixelX2mm(self.end.x()), convertRealY(convertPixelY2mm(self.end.y())))

                # Add circle piont 
                str="G02 F300 X%4.3f Y%4.3f I%4.3f\n" %(convertPixelX2mm(self.start.x()), convertRealY(convertPixelY2mm(self.start.y() + (self.end.y() - self.start.y())/2)), convertPixelX2mm((self.end.x()-self.start.x())/2))
                self.f.write(str)

        self.f.write("M05 S10\n")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())
