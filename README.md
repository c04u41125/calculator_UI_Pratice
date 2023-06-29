# calculator_UI_Pratice
## 此專案為Python大數據影像辨識養成班實作練習<br/>
0542.jpg_wh300.jpg 此檔案為UI背景圖<br/>
123.ui 此檔案為透過QtDesigner設計好的ui檔<br/>
UIPLUS.py 此檔案為123.ui 經過下列指令碼轉換成py檔
```
pyuic5 -x 123.ui -o UIPLUS.py
```
---
這份專案有用到下列函式庫
```
import pyqt5
import sys
```
---
首先使用下列fuunction判斷是否為浮點數
```
def is_float(num):                              #判斷是否為浮點數
    try:
        float(num)
        return True
    except ValueError:
        return False
```
將所有會跟UI連結的動作包成一個function
```
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
```
將按鈕連結的指令包成一個function
```
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
```
---
