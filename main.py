# import sys
#
# from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QRadioButton
# import sys
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.resize(500, 600)
#
#         self.c1 = QCheckBox("Test1", self)
#         self.c1.setChecked(True)
#         self.c1.move(100, 100)
#         self.c2 = QCheckBox("Test1", self)
#         self.c2.move(100, 200)
#
#         btn = QPushButton('Clear', self)
#         btn.move(100, 300)
#         btn.clicked.connect(self.clear)
#
#         self.r1 = QRadioButton("Erkak", self)
#         self.r1.move(100, 400)
#         self.r2 = QRadioButton("Ayol", self)
#         self.r2.move(100, 500)
#
#     def clear(self):
#         self.c1.setChecked(False)
#         self.c2.setChecked(False)
#
#         if self.r1.isChecked():
#             print("Erkak")
#             self.r1.setChecked(False)
#         elif self.r2.isChecked():
#             print("Ayol")
#         self.r1.setChecked(True)
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = Window()
#     win.show()
#     app.exec_()