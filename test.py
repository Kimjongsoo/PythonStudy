import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("test.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 버튼 클릭 시 호출할 메서드 연결
        self.pushButton_1.clicked.connect(lambda: self.add_to_expression('1'))
        self.pushButton_2.clicked.connect(lambda: self.add_to_expression('2'))
        self.pushButton_3.clicked.connect(lambda: self.add_to_expression('3'))
        self.pushButton_4.clicked.connect(lambda: self.add_to_expression('4'))
        self.pushButton_5.clicked.connect(lambda: self.add_to_expression('5'))
        self.pushButton_6.clicked.connect(lambda: self.add_to_expression('6'))
        self.pushButton_7.clicked.connect(lambda: self.add_to_expression('7'))
        self.pushButton_8.clicked.connect(lambda: self.add_to_expression('8'))
        self.pushButton_9.clicked.connect(lambda: self.add_to_expression('9'))

        # 사칙연산 버튼 연결
        self.pushButton_plus.clicked.connect(lambda: self.add_to_expression('+'))
        self.pushButton_minus.clicked.connect(lambda: self.add_to_expression('-'))
        self.pushButton_multiply.clicked.connect(lambda: self.add_to_expression('*'))
        self.pushButton_divide.clicked.connect(lambda: self.add_to_expression('/'))

        # 결과 버튼 연결
        self.pushButton_equals.clicked.connect(self.calculate_result)

    def add_to_expression(self, value):
        current_text = self.lineEdit.text()
        self.lineEdit.setText(current_text + value)

    def calculate_result(self):
        expression = self.lineEdit.text()
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result))
        except Exception as e:
            self.lineEdit.setText("Error")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()