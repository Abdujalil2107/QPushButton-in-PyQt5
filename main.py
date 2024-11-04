from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
import sys
class login_win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QPushButton')
        self.setFixedSize(500,350)
        self.b1()

    def b1(self):
        button = QPushButton('Done', self)
        button.setFixedSize(200,100)
        button.move(150,120)
        button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border-radius: 30px;
                font-family: "Arial"; 
                font-size: 26px;
                font-weight: bold;
                border: 4px solid black;
            }

            QPushButton:hover {
                color: blue;
                border: 4px solid blue;
            }

            QPushButton:pressed {
                color: red;
                border: 4px solid red;
            }
        """)
app = QApplication(sys.argv)
window = login_win()
window.show()
sys.exit(app.exec_())
