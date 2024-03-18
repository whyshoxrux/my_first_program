import sys

from PyQt5.QtCore import QSize, QFile, QTextStream, QUrl, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QGraphicsOpacityEffect, QMessageBox, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap, QFont
import sys

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget



with open('users.txt') as f:
    check_user = f.readline()

users_info = [
    {"username": "admin", "password": "123456"},
    {"username": "boss", "password": "777"},
    {"username": "1", "password": "1"}
]



class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon('logoo.png'))

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('imagee.png'))

        self.center_box = QLabel(self)
        self.center_box.setFixedSize(400, 600)
        self.center_box.move(300, 100)
        self.center_box.setStyleSheet('background-color: lightblue; border-radius: 15px;')
        self.opasity = QGraphicsOpacityEffect(self)
        self.opasity.setOpacity(0.3)
        self.center_box.setGraphicsEffect(self.opasity)

        self.title = QLabel("Login", self)
        self.font_title = QFont("Arial", 30, 80)
        self.title.setFont(self.font_title)
        self.title.setFixedSize(200, 80)
        self.title.move(420, 120)
        self.title.setStyleSheet('border: 1px; color: white;')

        self.username = QLineEdit(self)
        self.username.setFixedSize(300, 50)
        self.username.setStyleSheet('border: 1px solid blue; border-radius: 10px; font-size: 22px;')
        self.username.setPlaceholderText('Username')
        self.username.move(350, 240)

        self.password = QLineEdit(self)
        self.password.setFixedSize(300, 50)
        self.password.setStyleSheet('border: 1px solid blue; border-radius: 10px; font-size: 22px;')
        self.password.setPlaceholderText('Password')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(350, 340)

        self.login_button = QPushButton("Login", self)
        self.login_button.setFixedSize(250, 50)
        self.login_button.setStyleSheet('border: 3px solid blue; border-radius: 10px;')
        self.login_button.setFont(QFont('Arial', 15, 50))
        self.login_button.move(370, 440)
        self.login_button.clicked.connect(self.go_main_window)

        self.go_registration_button = QPushButton("Registration", self)
        self.go_registration_button.clicked.connect(self.go_registration)
        self.go_registration_button.setStyleSheet('border: 1px; color: solid black; font-size: 25px;')
        self.go_registration_button.move(440, 540)


    def go_main_window(self):
        username = self.username.text()
        password = self.password.text()
        if username and password in check_user or users_info:
            global main_win
            main_win = MainWindow()
            self.close()
            main_win.show()
        else:
            self.password.setStyleSheet('border: 3px solid red; border-radius: 10px; font-size: 22px;')
            QMessageBox.critical(self, "Error", "Username or Password is incorrect")

    def go_registration(self):

        global registration
        registration = Registration()
        self.close()
        registration.show()
    


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Registration")
        self.setWindowIcon(QIcon('logoo.png'))

        self.btn1 = QPushButton("login", self)
        self.btn1.clicked.connect(self.go_registration)

        self.setFixedSize(1000, 800)
        self.background_imagee = QLabel(self)
        self.background_imagee.setPixmap(QPixmap("image.png"))

        self.center_box = QLabel(self)
        self.center_box.setFixedSize(400, 600)
        self.center_box.move(300, 100)
        self.center_box.setStyleSheet('background-color: gray; border-radius: 15px;')
        self.opasity = QGraphicsOpacityEffect(self)
        self.opasity.setOpacity(0.3)
        self.center_box.setGraphicsEffect(self.opasity)


        self.title = QLabel("Registration", self)
        self.font_title = QFont("Arial", 20, 80)
        self.title.setFont(self.font_title)
        self.title.setFixedSize(230, 80)
        self.title.move(420, 120)
        self.title.setStyleSheet('border: 1px; color: white;')


        self.username = QLineEdit(self)
        self.username.setFixedSize(300, 40)
        self.username.setStyleSheet('border: 1px gray; border-radius: 10px; font-size: 22px;')
        self.username.setPlaceholderText('username')
        self.username.move(350, 240)


        self.email = QLineEdit(self)
        self.email.setFixedSize(300, 50)
        self.email.setStyleSheet('border: 1px gray; border-radius: 10px; font-size: 22px;')
        self.email.setPlaceholderText('email')
        self.email.move(350, 305)



        self.password = QLineEdit(self)
        self.password.setFixedSize(300, 50)
        self.password.setStyleSheet('border: 1px gray; border-radius: 10px; font-size: 22px;')
        self.password.setPlaceholderText('password')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(350, 375)



        self.password2 = QLineEdit(self)
        self.password2.setFixedSize(300, 50)
        self.password2.setStyleSheet('border: 1px gray; border-radius: 10px; font-size: 22px;')
        self.password2.setPlaceholderText('confirm password')
        self.password2.setEchoMode(QLineEdit.Password)
        self.password2.move(350, 445)


        self.account_button = QPushButton("Create account", self)
        self.account_button.setFixedSize(250, 50)
        self.account_button.setStyleSheet('border: 3px ; border-radius: 10px;')
        self.account_button.setFont(QFont('Arial', 15, 50))
        self.account_button.move(370, 530)
        self.account_button.clicked.connect(self.save)



        self.login = QPushButton("Login", self)
        self.login.setFixedSize(200, 50)
        self.login.setStyleSheet('border: 3px; border-radius: 10px;')
        self.login.setFont(QFont("Amasis MT Pro Black", 15, 50))
        self.login.move(390, 600)
        self.login.clicked.connect(self.go_login)
   


    def save(self):
        fayl_nomi = 'users.txt'
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        password2 = self.password2.text()

        fayl = QFile(fayl_nomi)
        if fayl.open(QFile.Append | QFile.Text):
            if password == password2:
                if email.endswith('@gmail.com'):
                    if not username in 'users.txt':
                        tekst = QTextStream(fayl)
                        tekst << username << " "
                        tekst << password << " "
                        tekst << email << "\n"
                        fayl.close()
                        self.username.clear()
                        self.email.clear()
                        self.password.clear()
                        self.password2.clear()
                        QMessageBox.about(self, "Congratulations", "Your data have been succesfully created")
                    else:
                        self.username.setStyleSheet('border: 3px solid red; border-radius: 10px; ')
                        QMessageBox.critical(self, "Error", "This username is already exists;")

                else:
                    self.email.setStyleSheet('border: 3px solid red; border-radius: 10px; ')
                    QMessageBox.critical(self, "Error", "Please check your email;")
            else:
                self.password2.setStyleSheet('border: 3px solid red; border-radius: 10px; ')
                QMessageBox.critical(self, "Error", "Please check your password")
            


    def go_registration(self):

        global registration
        registration = Registration()
        self.close()
        registration.show()


    def go_login(self):
        global login
        login = Login()
        self.close()
        login.show()


    



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Autosalon")
        self.setWindowIcon(QIcon('logoo.png'))

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('background.jpg'))


        self.center_box = QLabel(self)
        self.center_box.setFixedSize(900, 700)
        self.center_box.move(50, 50)
        self.center_box.setStyleSheet('background-color: lightblue; border-radius: 15px;')
        self.opasity = QGraphicsOpacityEffect(self)
        self.opasity.setOpacity(0.3)
        self.center_box.setGraphicsEffect(self.opasity)


        self.lock_button = QPushButton(self)
        self.lock_button.setFixedSize(70, 70)
        self.lock_button.move(930, 0)
        self.lock_button.setIcon(QIcon('lock.jpg'))
        self.lock_button.setIconSize(QSize(50, 50))
        self.lock_button.setStyleSheet('border: 2px solid white; border-radius: 35px;')
        self.lock_button.clicked.connect(self.go_login)



        self.porsche = QPushButton(self)
        self.view = QPushButton("View car", self)
        self.view.setFixedSize(200, 50)
        self.view.move(100, 330)
        self.view.setFont(QFont('Impact', 25, 50))
        self.view.setStyleSheet('border: 2px solid black; background-color: #c9c25b; border-radius: 10px')
        self.view.clicked.connect(self.go_porsche)
        self.porsche.setFixedSize(200, 250)
        self.porsche.move(100, 100)
        self.porsche.setIcon(QIcon('porshe.jpg'))
        self.porsche.setIconSize(QSize(170, 220))
        self.porsche.setStyleSheet('border: 2px solid black; background-color: #FC3D0D; border-radius: 10px;')
        self.porsche.clicked.connect(self.go_porsche)


        self.nexia2 = QPushButton(self)

        self.view_nexia2 = QPushButton("View car", self)
        self.view_nexia2.setFixedSize(200, 50)
        self.view_nexia2.move(400, 330)
        self.view_nexia2.setFont(QFont('Impact', 25, 50))
        self.view_nexia2.setStyleSheet('border: 2px solid black; background-color: #c9c25b; border-radius: 10px')
        self.nexia2.clicked.connect(self.go_chevrolet)
        
        self.nexia2.setFixedSize(200, 250)
        self.nexia2.move(400, 100)
        self.nexia2.setIcon(QIcon('chevrolet.jpg'))
        self.nexia2.setIconSize(QSize(170, 220))
        self.nexia2.setFont(QFont('Impact', 15, 20))
        self.nexia2.setStyleSheet('border: 2px solid black; background-color:#040203; border-radius: 10px;')


        self.ferrari = QPushButton(self)
        self.view_ferrari = QPushButton("View car", self)
        self.view_ferrari.setFixedSize(200, 50)
        self.view_ferrari.move(700, 330)
        self.view_ferrari.setFont(QFont('Impact', 25, 50))
        self.view_ferrari.setStyleSheet('border: 2px solid black; background-color: #c9c25b; border-radius: 10px')
        self.ferrari.setFixedSize(200, 250)
        self.ferrari.move(700, 100)
        self.ferrari.setIcon(QIcon('ferrari.jpg'))
        self.ferrari.setIconSize(QSize(170, 220))
        self.ferrari.setStyleSheet('border: 2px solid black; background-color: #CC0202; border-radius: 10px;')

        self.ferrari.clicked.connect(self.go_ferrari)



        self.mers = QPushButton(self)
        self.view_mers = QPushButton("View car", self)
        self.view_mers.setFixedSize(200, 50)
        self.view_mers.move(100, 630)
        self.view_mers.setFont(QFont('Impact', 25, 50))
        self.view_mers.setStyleSheet('border: 2px solid black; background-color: #c9c25b; border-radius: 10px')
        self.mers.setFixedSize(200, 250)
        self.mers.move(100, 400)
        self.mers.setIcon(QIcon('mers.jpg'))
        self.mers.setIconSize(QSize(170, 220))
        self.mers.setStyleSheet('border: 2px solid black; background-color: #1A1A1A; border-radius: 10px;')
        self.mers.clicked.connect(self.go_mers)


        self.lambo = QPushButton(self)
        self.view_lambo = QPushButton("View car", self)
        self.view_lambo.setFixedSize(200, 50)
        self.view_lambo.move(400, 630)
        self.view_lambo.setFont(QFont('Impact', 25, 50))
        self.view_lambo.setStyleSheet('border: 2px solid black; background-color: #c9c25b; border-radius: 10px')
        self.lambo.setFixedSize(200, 250)
        self.lambo.move(400, 400)
        self.lambo.setIcon(QIcon('lambo.png'))
        self.lambo.setIconSize(QSize(180, 230))
        self.lambo.setStyleSheet('border: 2px solid black; background-color: #03DF03; border-radius: 10px;')
        self.lambo.clicked.connect(self.go_lambo)




        self.bmw = QPushButton(self)
        self.view_bmw = QPushButton("View car", self)
        self.view_bmw.setFixedSize(200, 50)
        self.view_bmw.move(700, 630)
        self.view_bmw.setFont(QFont('Impact', 25, 50))
        self.view_bmw.setStyleSheet('border: 2px solid black; background-color: #c9c25b; border-radius: 10px')
        self.bmw.setFixedSize(200, 250)
        self.bmw.move(700, 400)
        self.bmw.setIcon(QIcon('bmw.jpg'))
        self.bmw.setIconSize(QSize(180, 230))
        self.bmw.setStyleSheet('border: 2px solid black; background-color: #000000; border-radius: 10px;')
        self.bmw.clicked.connect(self.go_bmw)








    def go_login(self):
        global login
        login = Login()
        self.close()
        login.show()


    def go_porsche(self):
        global porsche
        porsche = Porshe()
        self.close()
        porsche.show()  

    def go_chevrolet(self):
        global chevrolet
        chevrolet = Chevrolet()
        self.close()
        chevrolet.show()

    def go_ferrari(self):
        global ferrarii
        ferrarii = Ferrari()
        self.close()
        ferrarii.show()   

    def go_mers(self):
        global merss
        merss = Mers()
        self.close()
        merss.show()  

    def go_lambo(self):
        global lamboo
        lamboo = Lambo()
        self.close()
        lamboo.show()

    def go_bmw(self):
        global bmww
        bmww = Bmw()
        self.close()
        bmww.show()    


class Porshe(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Porsche")
        self.setWindowIcon(QIcon('p.jpg')) 

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('porsche.jpg'))
        

        # self.center_box = QLabel(self)
        # self.center_box.setFixedSize(900, 700)
        # self.center_box.move(50, 50)
        # self.center_box.setStyleSheet('background-color: lightblue; border-radius: 15px;')
        # self.opasity = QGraphicsOpacityEffect(self)
        # self.opasity.setOpacity(0.3)
        # self.center_box.setGraphicsEffect(self.opasity)

class Chevrolet(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Chevrolet")
        self.setWindowIcon(QIcon('ch.png')) 

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('legenda.webp'))


class Ferrari(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Ferrari")
        self.setWindowIcon(QIcon('f.png')) 

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('fer.jpg'))


class Mers(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Mercedes Benz")
        self.setWindowIcon(QIcon('m.jpg')) 

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('merc.jpg'))

class Lambo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("Lamorghini")
        self.setWindowIcon(QIcon('logoo.png')) 

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('huracan.jpg'))


class Bmw(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 800)
        self.setWindowTitle("BMW")
        self.setWindowIcon(QIcon('b.jpg')) 

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap('bmww.jpg'))











if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    app.exec_()