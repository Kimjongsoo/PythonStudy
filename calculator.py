import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QGridLayout, QWidget

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # 창 제목 설정
        self.setWindowTitle('Calculator')

        # 위젯과 레이아웃 설정
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)

        # 텍스트 상자 (결과 표시)
        self.result_field = QLineEdit(self)
        self.layout.addWidget(self.result_field, 0, 0, 1, 4)

        # 버튼 추가
        self.create_buttons()

    def create_buttons(self):
        buttons = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
            '0': (4, 0), 'C': (4, 1), '=': (4, 2), '+': (4, 3),
        }

        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text, self)
            button.clicked.connect(lambda _, text=btn_text: self.on_click(text))
            self.layout.addWidget(button, pos[0], pos[1])

    def on_click(self, text):
        current_text = self.result_field.text()

        if text == 'C':
            # Clear 버튼: 입력 초기화
            self.result_field.clear()
        elif text == '=':
            # 결과 계산
            try:
                result = str(eval(current_text))
                self.result_field.setText(result)
            except Exception as e:
                self.result_field.setText('Error')
        else:
            # 버튼 클릭 시 텍스트 추가
            self.result_field.setText(current_text + text)

# 프로그램 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


