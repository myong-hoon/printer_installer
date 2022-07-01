import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("mainUi.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    global text
    global defaultPrintDel
    global defaultPrint
    global print1_mono
    global print1_color
    global print1_name 
    global print1_ip
    global print2_mono
    global print2_color
    global print2_name
    global print2_ip
    global print3_mono
    global print3_color
    global print3_name
    global print3_ip
    global print4_mono
    global print4_color
    global print4_name
    global print4_ip
    global print5_mono
    global print5_color
    global print5_name
    global print5_ip
    global installPrintCount

    def __init__(self) :
        def setting_read():
            with open('./setData.txt','r') as f:
                datas=f.readlines()

            for i in datas:
                data = i.replace("\n","")
                dataName = data[:data.find("=")]
                dataValue= data[data.find("=")+1:]
                if dataName == 'text':
                    text = dataValue
                    self.note.setPlainText(text)
                if dataName == 'defaultPrintDel':
                    defaultPrintDel=dataValue
                    if defaultPrintDel == "0":
                        self.defaultPrintDel_o.setChecked(True)
                    else :
                        self.defaultPrintDel_x.setChecked(True)
                if dataName == 'defaultPrint':
                    defaultPrint=dataValue
                    if defaultPrint == "0":
                        self.defaultPrint_non.setChecked(True)
                    elif defaultPrint == "1":
                        self.defaultPrint_1_mono.setChecked(True)
                    elif defaultPrint == "2":
                        self.defaultPrint_1_color.setChecked(True)
                    elif defaultPrint == "3":
                        self.defaultPrint_2_mono.setChecked(True)
                    elif defaultPrint == "4":
                        self.defaultPrint_2_color.setChecked(True)
                    elif defaultPrint == "5":
                        self.defaultPrint_3_mono.setChecked(True)
                    elif defaultPrint == "6":
                        self.defaultPrint_3_color.setChecked(True)
                    elif defaultPrint == "7":
                        self.defaultPrint_4_mono.setChecked(True)
                    elif defaultPrint == "8":
                        self.defaultPrint_4_color.setChecked(True)
                    elif defaultPrint == "9":
                        self.defaultPrint_5_mono.setChecked(True)
                    elif defaultPrint == "10":
                        self.defaultPrint_5_color.setChecked(True)
                if dataName == 'print1_mono':
                    print1_mono=dataValue
                    if print1_mono == "0":
                        self.installPrint_1_mono.setChecked(False)
                    else :
                        self.installPrint_1_mono.setChecked(True)
                if dataName == 'print1_color':
                    print1_color=dataValue
                    if print1_color == "0":
                        self.installPrint_1_color.setChecked(False)
                    else :
                        self.installPrint_1_color.setChecked(True)
                if dataName == 'print1_name':
                    print1_name=dataValue
                    self.print_name_1.setText(print1_name)
       
                if dataName == 'print1_ip':
                    print1_ip=dataValue
                    self.print_ip_1.setText(print1_ip)
                if dataName == 'print2_mono':
                    print2_mono=dataValue
                    if print2_mono == "0":
                        self.installPrint_2_mono.setChecked(False)
                    else :
                        self.installPrint_2_mono.setChecked(True)
                if dataName == 'print2_color':
                    print2_color=dataValue
                    if print2_color == "0":
                        self.installPrint_2_color.setChecked(False)
                    else :
                        self.installPrint_2_color.setChecked(True)
                if dataName == 'print2_name':
                    print2_name=dataValue
                    self.print_name_2.setText(print2_name)
                if dataName == 'print2_ip':
                    print2_ip=dataValue
                    self.print_ip_2.setText(print2_ip)
                if dataName == 'print3_mono':
                    print3_mono=dataValue
                    if print3_mono == "0":
                        self.installPrint_3_mono.setChecked(False)
                    else :
                        self.installPrint_3_mono.setChecked(True)
                if dataName == 'print3_color':
                    print3_color=dataValue
                    if print3_color == "0":
                        self.installPrint_3_color.setChecked(False)
                    else :
                        self.installPrint_3_color.setChecked(True)
                if dataName == 'print3_name':
                    print3_name=dataValue
                    self.print_name_3.setText(print3_name)
                if dataName == 'print3_ip':
                    print3_ip=dataValue
                    self.print_ip_3.setText(print3_ip)
                if dataName == 'print4_mono':
                    print4_mono=dataValue
                    if print4_mono == "0":
                        self.installPrint_4_mono.setChecked(False)
                    else :
                        self.installPrint_4_mono.setChecked(True)
                if dataName == 'print4_color':
                    print4_color=dataValue
                    if print4_color == "0":
                        self.installPrint_4_color.setChecked(False)
                    else :
                        self.installPrint_4_color.setChecked(True)
                if dataName == 'print4_name':
                    print4_name=dataValue
                    self.print_name_4.setText(print4_name)
                if dataName == 'print4_ip':
                    print4_ip=dataValue
                    self.print_ip_4.setText(print4_ip)
                if dataName == 'print5_mono':
                    print5_mono=dataValue
                    if print5_mono == "0":
                        self.installPrint_5_mono.setChecked(False)
                    else :
                        self.installPrint_5_mono.setChecked(True)
                if dataName == 'print5_color':
                    print5_color=dataValue
                    if print5_color == "0":
                        self.installPrint_5_color.setChecked(False)
                    else :
                        self.installPrint_5_color.setChecked(True)
                if dataName == 'print5_name':
                    print5_name=dataValue
                    self.print_name_5.setText(print5_name)
                if dataName == 'print5_ip':
                    print5_ip=dataValue
                    self.print_ip_5.setText(print5_ip)


        super().__init__()
        self.setupUi(self)
        setting_read()
        self.start_btn.clicked.connect(self.start_btn_function)
        self.save_btn.clicked.connect(self.save_btn_function)
        

    def start_btn_function(self) :
        
        
        def loop():
            global installPrintCount
            i=0
            installPrintCount = []
            if self.installPrint_1_mono.isChecked() :  
                i=i+1
                installPrintCount.append('installPrint_1_mono')
                
            if self.installPrint_2_mono.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_2_mono')
            if self.installPrint_3_mono.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_3_mono')
            if self.installPrint_4_mono.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_4_mono')
            if self.installPrint_5_mono.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_5_mono')
            if self.installPrint_1_color.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_1_color')
            if self.installPrint_2_color.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_2_color')
            if self.installPrint_3_color.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_3_color')
            if self.installPrint_4_color.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_4_color')
            if self.installPrint_5_color.isChecked() : 
                i=i+1
                installPrintCount.append('installPrint_5_color')
            if i==0:
                installPrintCount.append('non_install')

        def readData():
            global text
            global defaultPrintDel
            global defaultPrint
            global print1_mono
            global print1_color
            global print1_name 
            global print1_ip
            global print2_mono
            global print2_color
            global print2_name
            global print2_ip
            global print3_mono
            global print3_color
            global print3_name
            global print3_ip
            global print4_mono
            global print4_color
            global print4_name
            global print4_ip
            global print5_mono
            global print5_color
            global print5_name
            global print5_ip
            text=self.note.toPlainText()
            if self.defaultPrintDel_o.isChecked() == True:
                defaultPrintDel = "0"
            else:
                defaultPrintDel = "1"
            if self.defaultPrint_1_mono.isChecked() :  defaultPrint="1"
            elif self.defaultPrint_2_mono.isChecked() : defaultPrint="3"
            elif self.defaultPrint_3_mono.isChecked() : defaultPrint="5"
            elif self.defaultPrint_4_mono.isChecked() : defaultPrint="7"
            elif self.defaultPrint_5_mono.isChecked() : defaultPrint="9"
            elif self.defaultPrint_1_color.isChecked() : defaultPrint="2"
            elif self.defaultPrint_2_color.isChecked() : defaultPrint="4"
            elif self.defaultPrint_3_color.isChecked() : defaultPrint="6"
            elif self.defaultPrint_4_color.isChecked() : defaultPrint="8"
            elif self.defaultPrint_5_color.isChecked() : defaultPrint="10"
            elif self.defaultPrint_non.isChecked() : defaultPrint="0"
            if self.installPrint_1_mono.isChecked() == True:
                print1_mono = "1"
            else:
                print1_mono = "0"
            if self.installPrint_1_color.isChecked() == True:
                print1_color = "1"
            else:
                print1_color = "0"
            print1_name= self.print_name_1.text()
            print1_ip= self.print_ip_1.text()
            if self.installPrint_2_mono.isChecked() == True:
                print2_mono = "1"
            else:
                print2_mono = "0"
            if self.installPrint_2_color.isChecked() == True:
                print2_color = "1"
            else:
                print2_color = "0"
            print2_name= self.print_name_2.text()
            print2_ip= self.print_ip_2.text()
            if self.installPrint_3_mono.isChecked() == True:
                print3_mono = "1"
            else:
                print3_mono = "0"
            if self.installPrint_3_color.isChecked() == True:
                print3_color = "1"
            else:
                print3_color = "0"
            print3_name= self.print_name_3.text()
            print3_ip= self.print_ip_3.text()
            if self.installPrint_4_mono.isChecked() == True:
                print4_mono = "1"
            else:
                print4_mono = "0"
            if self.installPrint_4_color.isChecked() == True:
                print4_color = "1"
            else:
                print4_color = "0"
            print4_name= self.print_name_4.text()
            print4_ip= self.print_ip_4.text()
            if self.installPrint_5_mono.isChecked() == True:
                print5_mono = "1"
            else:
                print5_mono = "0"
            if self.installPrint_5_color.isChecked() == True:
                print5_color = "1"
            else:
                print5_color = "0"
            print5_name= self.print_name_5.text()
            print5_ip= self.print_ip_5.text()

        def install():
            for i in installPrintCount:
                if i == 'installPrint_1_mono':
                    print(print1_name+' MONO',print1_ip)
                elif i == 'installPrint_2_mono':
                    print(print2_name+' MONO',print2_ip)
                elif i == 'installPrint_3_mono':
                    print(print3_name+' MONO',print3_ip)
                elif i == 'installPrint_4_mono':
                    print(print4_name+' MONO',print4_ip)
                elif i == 'installPrint_5_mono':
                    print(print5_name+' MONO',print5_ip)
                elif i == 'installPrint_1_color':
                    print(print1_name+' COLOR',print1_ip)
                elif i == 'installPrint_2_color':
                    print(print2_name+' COLOR',print2_ip)
                elif i == 'installPrint_3_color':
                    print(print3_name+' COLOR',print3_ip)
                elif i == 'installPrint_4_color':
                    print(print4_name+' COLOR',print4_ip)
                elif i == 'installPrint_5_color':
                    print(print5_name+' COLOR',print5_ip)

        readData()
        loop()
        install()
        
        # install(installPrintCount)
        # with open('./setData.txt','w',encoding='UTF-8') as f:
        #     print("dd")
        # f  = open('./data/driver/ASINDOH D450 Color/KMoprCnf_BACKUP.ini','r')
        # listf=f.readlines()
        # temp=[]
        # j=0
        # for io in listf:
        #     if io[:io.find("=")] == "PortName":
        #         temp.append('PortName=')
        #         print('portname')
        #         j=j+1
        #     else:
        #         temp.append(io.replace("\n",""))
        #         j=j+1
        # print(temp)
    

    def save_btn_function(self) :
        print("save")

        with open('setData.txt','w',encoding='UTF-8') as f:
            text=self.note.toPlainText()
            if self.defaultPrintDel_o.isChecked() == True:
                defaultPrintDel = "0"
            else:
                defaultPrintDel = "1"
            if self.defaultPrint_1_mono.isChecked() :  defaultPrint="1"
            elif self.defaultPrint_2_mono.isChecked() : defaultPrint="3"
            elif self.defaultPrint_3_mono.isChecked() : defaultPrint="5"
            elif self.defaultPrint_4_mono.isChecked() : defaultPrint="7"
            elif self.defaultPrint_5_mono.isChecked() : defaultPrint="9"
            elif self.defaultPrint_1_color.isChecked() : defaultPrint="2"
            elif self.defaultPrint_2_color.isChecked() : defaultPrint="4"
            elif self.defaultPrint_3_color.isChecked() : defaultPrint="6"
            elif self.defaultPrint_4_color.isChecked() : defaultPrint="8"
            elif self.defaultPrint_5_color.isChecked() : defaultPrint="10"
            elif self.defaultPrint_non.isChecked() : defaultPrint="0"
            if self.installPrint_1_mono.isChecked() == True:
                print1_mono = "1"
            else:
                print1_mono = "0"
            if self.installPrint_1_color.isChecked() == True:
                print1_color = "1"
            else:
                print1_color = "0"
            print1_name= self.print_name_1.text()
            print1_ip= self.print_ip_1.text()
            if self.installPrint_2_mono.isChecked() == True:
                print2_mono = "1"
            else:
                print2_mono = "0"
            if self.installPrint_2_color.isChecked() == True:
                print2_color = "1"
            else:
                print2_color = "0"
            print2_name= self.print_name_2.text()
            print2_ip= self.print_ip_2.text()
            if self.installPrint_3_mono.isChecked() == True:
                print3_mono = "1"
            else:
                print3_mono = "0"
            if self.installPrint_3_color.isChecked() == True:
                print3_color = "1"
            else:
                print3_color = "0"
            print3_name= self.print_name_3.text()
            print3_ip= self.print_ip_3.text()
            if self.installPrint_4_mono.isChecked() == True:
                print4_mono = "1"
            else:
                print4_mono = "0"
            if self.installPrint_4_color.isChecked() == True:
                print4_color = "1"
            else:
                print4_color = "0"
            print4_name= self.print_name_4.text()
            print4_ip= self.print_ip_4.text()
            if self.installPrint_5_mono.isChecked() == True:
                print5_mono = "1"
            else:
                print5_mono = "0"
            if self.installPrint_5_color.isChecked() == True:
                print5_color = "1"
            else:
                print5_color = "0"
            print5_name= self.print_name_5.text()
            print5_ip= self.print_ip_5.text()
            
            f.write("text=%s\ndefaultPrintDel=%s\ndefaultPrint=%s\nprint1_mono=%s\nprint1_color=%s\nprint1_name=%s\nprint1_ip=%s\nprint2_mono=%s\nprint2_color=%s\nprint2_name=%s\nprint2_ip=%s\nprint3_mono=%s\nprint3_color=%s\nprint3_name=%s\nprint3_ip=%s\nprint4_mono=%s\nprint4_color=%s\nprint4_name=%s\nprint4_ip=%s\nprint5_mono=%s\nprint5_color=%s\nprint5_name=%s\nprint5_ip=%s\n"%(text,defaultPrintDel,defaultPrint,print1_mono,print1_color,print1_name,print1_ip,print2_mono,print2_color,print2_name,print2_ip,print3_mono,print3_color,print3_name,print3_ip,print4_mono,print4_color,print4_name,print4_ip,print5_mono,print5_color,print5_name,print5_ip))
           

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()