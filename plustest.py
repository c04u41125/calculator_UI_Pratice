from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from UIPLUS import Ui_Dialog
import sys 

def is_float(num):                              #判斷是否為浮點數
    try:
        float(num)
        return True
    except ValueError:
        return False
def clicked():                                  #所有按鈕點擊的動作
    x =ui.lineEdit.text()
    y =ui.lineEdit_2.text()
    val=ui.horizontalSlider.value()
    val_2=ui.horizontalSlider_2.value()
    font = QtGui.QFont()
    font.setFamily("Agency FB")
    font.setPointSize(val_2)
    ui.answer.setFont(font)
    if is_float(x)and is_float(y):
        if ui.checkBox.isChecked():
            x=ui.lineEdit_2.text()
            y=ui.lineEdit.text()
        else:
            x =ui.lineEdit.text()
            y =ui.lineEdit_2.text()
        if ui.plus.isChecked():
            z=(str((float(x)+float(y))*val))
        elif ui.sub.isChecked():
            z=(str((float(x)-float(y))*val))
        elif ui.mul.isChecked():
            z=(str((float(x)*float(y))*val))
        elif ui.div.isChecked():
            if ui.checkBox_2.isChecked() & (float(x)/float(y)).is_integer():
                z=(str((float(x)/float(y))*val))
            elif ui.checkBox_2.isChecked():
                z=(x+'/'+y+'*'+str(val))
            else:    
                z=(str((float(x)/float(y))*val))
        else:
            z='error'
            message=QMessageBox()
            message.setWindowTitle(" error ")
            message.setInformativeText("請選擇式子")
            message.exec_()       
        if ui.comboBox.currentIndex()==0:
            ui.answer.setText('答案是'+'     '+z)
        else:
            ui.answer.setText('ANSER IS'+'     '+z)
    else:
        message=QMessageBox()
        message.setWindowTitle(" error ")
        message.setInformativeText("請輸入數字")
        message.exec_()
def pic_click(event):                           #點擊圖片的動作
    message=QMessageBox()
    message.setWindowTitle('show')
    message.setInformativeText('不要亂點')
    message.exec_()
def uiinside():                                 #所有按鈕的呼叫包在一個FUNCTION
    ui.pushButton.clicked.connect(clicked)
    ui.pic.mouseReleaseEvent=pic_click
    group=QButtonGroup(widge)
    group.addButton(ui.plus)
    group.addButton(ui.sub)
    group.addButton(ui.mul)
    group.addButton(ui.div)
    ui.plus.clicked.connect(clicked)
    ui.sub.clicked.connect(clicked)
    ui.mul.clicked.connect(clicked)
    ui.div.clicked.connect(clicked)
    ui.checkBox.clicked.connect(clicked)
    ui.checkBox_2.clicked.connect(clicked)
    ui.comboBox.addItems(['中文','英文'])
    ui.comboBox.activated.connect(clicked)
    ui.horizontalSlider.setMaximum(100)
    ui.horizontalSlider.setMinimum(0)
    ui.horizontalSlider.setValue(1)
    ui.horizontalSlider.valueChanged.connect(clicked)
    ui.horizontalSlider_2.setMaximum(25)
    ui.horizontalSlider_2.setMinimum(10)
    ui.horizontalSlider_2.setValue(3)
    ui.horizontalSlider_2.valueChanged.connect(clicked)
app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge) 
uiinside()
widge.show()
sys.exit(app.exec_())
input('')