import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("mainUi.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        f  = open('./setData.txt','r')
        data = f.readline().replace("\n","")
        self.note.setPlainText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.default_printer_del_o.setChecked(True)
        else :
            self.default_printer_del_x.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.default_print_non.setChecked(True)
        elif data[data.find("=")+1:] == "1":
            self.default_print_1_mono.setChecked(True)
        elif data[data.find("=")+1:] == "2":
            self.default_print_1_color.setChecked(True)
        elif data[data.find("=")+1:] == "3":
            self.default_print_2_mono.setChecked(True)
        elif data[data.find("=")+1:] == "4":
            self.default_print_2_color.setChecked(True)
        elif data[data.find("=")+1:] == "5":
            self.default_print_3_mono.setChecked(True)
        elif data[data.find("=")+1:] == "6":
            self.default_print_3_color.setChecked(True)
        elif data[data.find("=")+1:] == "7":
            self.default_print_4_mono.setChecked(True)
        elif data[data.find("=")+1:] == "8":
            self.default_print_4_color.setChecked(True)
        elif data[data.find("=")+1:] == "9":
            self.default_print_5_mono.setChecked(True)
        elif data[data.find("=")+1:] == "10":
            self.default_print_5_color.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_1_mono.setChecked(False)
        else :
            self.install_print_1_mono.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_1_color.setChecked(False)
        else :
            self.install_print_1_color.setChecked(True)
        data = f.readline().replace("\n","")
        self.print_name_1.setText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        self.print_ip_1.setText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_2_mono.setChecked(False)
        else :
            self.install_print_2_mono.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_2_color.setChecked(False)
        else :
            self.install_print_2_color.setChecked(True)
        data = f.readline().replace("\n","")
        self.print_name_2.setText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        self.print_ip_2.setText(data[data.find("=")+1:])
        
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_3_mono.setChecked(False)
        else :
            self.install_print_3_mono.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_3_color.setChecked(False)
        else :
            self.install_print_3_color.setChecked(True)
        data = f.readline().replace("\n","")
        self.print_name_3.setText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        self.print_ip_3.setText(data[data.find("=")+1:])

        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_4_mono.setChecked(False)
        else :
            self.install_print_4_mono.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_4_color.setChecked(False)
        else :
            self.install_print_4_color.setChecked(True)
        data = f.readline().replace("\n","")
        self.print_name_4.setText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        self.print_ip_4.setText(data[data.find("=")+1:])

        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_5_mono.setChecked(False)
        else :
            self.install_print_5_mono.setChecked(True)
        data = f.readline().replace("\n","")
        if data[data.find("=")+1:] == "0":
            self.install_print_5_color.setChecked(False)
        else :
            self.install_print_5_color.setChecked(True)
        data = f.readline().replace("\n","")
        self.print_name_5.setText(data[data.find("=")+1:])
        data = f.readline().replace("\n","")
        self.print_ip_5.setText(data[data.find("=")+1:])

        f.close()
        self.start_btn.clicked.connect(self.start_btn_function)
        self.save_btn.clicked.connect(self.save_btn_function)
        
       

    def start_btn_function(self) :
        i=0
        if self.install_print_1_mono.isChecked() :  
            print("default_print_1_mono Checked")
            i=i+1
        
        if self.install_print_2_mono.isChecked() : 
            print("default_print_2_mono Checked")
            i=i+1
        if self.install_print_3_mono.isChecked() : 
            print("default_print_3_mono Checked")
            i=i+1
        if self.install_print_4_mono.isChecked() : 
            print("default_print_4_mono Checked")
            i=i+1
        if self.install_print_5_mono.isChecked() : 
            print("default_print_5_mono Checked")
            i=i+1
        if self.install_print_1_color.isChecked() : 
            print("default_print_1_color Checked")
            i=i+1
        if self.install_print_2_color.isChecked() : 
            print("default_print_2_color Checked")
            i=i+1
        if self.install_print_3_color.isChecked() : 
            print("default_print_3_color Checked")
            i=i+1
        if self.install_print_4_color.isChecked() : 
            print("default_print_4_color Checked")
            i=i+1
        if self.install_print_5_color.isChecked() : 
            print("default_print_5_color Checked")
            i=i+1
            with open('./setData.txt','w',encoding='UTF-8') as f:
                print("dd")
            f  = open('./data/driver/ASINDOH D450 Color/KMoprCnf_BACKUP.ini','r')
            listf=f.readlines()
            temp=[]
            j=0
            for io in listf:
                if io[:io.find("=")] == "PortName":
                    temp.append('PortName=')
                    print('portname')
                    j=j+1
                else:
                    temp.append(io.replace("\n",""))
                    j=j+1
            print(temp)
        if i<1:
            print("non install")



    

    def save_btn_function(self) :
        print("save")

        with open('setData.txt','w',encoding='UTF-8') as f:
            line1=self.note.toPlainText()
            if self.default_printer_del_o.isChecked() == True:
                line2 = "0"
            else:
                line2 = "1"
            if self.default_print_1_mono.isChecked() :  line3="1"
            elif self.default_print_2_mono.isChecked() : line3="3"
            elif self.default_print_3_mono.isChecked() : line3="5"
            elif self.default_print_4_mono.isChecked() : line3="7"
            elif self.default_print_5_mono.isChecked() : line3="9"
            elif self.default_print_1_color.isChecked() : line3="2"
            elif self.default_print_2_color.isChecked() : line3="4"
            elif self.default_print_3_color.isChecked() : line3="6"
            elif self.default_print_4_color.isChecked() : line3="8"
            elif self.default_print_5_color.isChecked() : line3="10"
            elif self.default_print_non.isChecked() : line3="0"
            if self.install_print_1_mono.isChecked() == True:
                line4 = "1"
            else:
                line4 = "0"
            if self.install_print_1_color.isChecked() == True:
                line5 = "1"
            else:
                line5 = "0"
            line6= self.print_name_1.text()
            line7= self.print_ip_1.text()
            if self.install_print_2_mono.isChecked() == True:
                line8 = "1"
            else:
                line8 = "0"
            if self.install_print_2_color.isChecked() == True:
                line9 = "1"
            else:
                line9 = "0"
            line10= self.print_name_2.text()
            line11= self.print_ip_2.text()
            if self.install_print_3_mono.isChecked() == True:
                line12 = "1"
            else:
                line12 = "0"
            if self.install_print_3_color.isChecked() == True:
                line13 = "1"
            else:
                line13 = "0"
            line14= self.print_name_3.text()
            line15= self.print_ip_3.text()
            if self.install_print_4_mono.isChecked() == True:
                line16 = "1"
            else:
                line16 = "0"
            if self.install_print_4_color.isChecked() == True:
                line17 = "1"
            else:
                line17 = "0"
            line18= self.print_name_4.text()
            line19= self.print_ip_4.text()
            if self.install_print_5_mono.isChecked() == True:
                line20 = "1"
            else:
                line20 = "0"
            if self.install_print_5_color.isChecked() == True:
                line21 = "1"
            else:
                line21 = "0"
            line22= self.print_name_5.text()
            line23= self.print_ip_5.text()
            
            f.write("text=%s\ndefault_print_del=%s\ndefault_print=%s\nprint1_mono=%s\nprint1_color=%s\nprint1_name=%s\nprint1_ip=%s\nprint2_mono=%s\nprint2_color=%s\nprint2_name=%s\nprint2_ip=%s\nprint3_mono=%s\nprint3_color=%s\nprint3_name=%s\nprint3_ip=%s\nprint4_mono=%s\nprint4_color=%s\nprint4_name=%s\nprint4_ip=%s\nprint5_mono=%s\nprint5_color=%s\nprint5_name=%s\nprint5_ip=%s\n"%(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20,line21,line22,line23))
           
    def default_print_function(self) :
        
        if self.default_print_1_mono.isChecked() :  print("default_print_1_mono Checked") 
        elif self.default_print_2_mono.isChecked() : print("default_print_2_mono Checked")
        elif self.default_print_3_mono.isChecked() : print("default_print_3_mono Checked")
        elif self.default_print_4_mono.isChecked() : print("default_print_4_mono Checked")
        elif self.default_print_5_mono.isChecked() : print("default_print_5_mono Checked")
        elif self.default_print_1_color.isChecked() : print("default_print_1_color Checked")
        elif self.default_print_2_color.isChecked() : print("default_print_2_color Checked")
        elif self.default_print_3_color.isChecked() : print("default_print_3_color Checked")
        elif self.default_print_4_color.isChecked() : print("default_print_4_color Checked")
        elif self.default_print_5_color.isChecked() : print("default_print_5_color Checked")



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()