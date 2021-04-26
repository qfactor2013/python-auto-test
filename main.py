import sys
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QTextEdit, QComboBox
import scraping

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.btn_quit = QPushButton('Quit', self)
        #btn_quit.move(50, 50)
        self.btn_quit.resize(self.btn_quit.sizeHint())
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)

        self.lineEdit_keyword = QLineEdit()
        # self.lineEdit_site = QLineEdit()

        self.btn_exec = QPushButton('실행', self)
        #btn_exec.move(50, 50)
        self.btn_exec.resize(self.btn_exec.sizeHint())
        self.btn_exec.clicked.connect(self.exec)

        self.cb_site = QComboBox(self)
        self.cb_site.addItem('네이버')
        self.cb_site.addItem('구글')
        self.cb_site.addItem('다음')

        #self.cb.activated[str].connect(self.onActivated)

        grid.addWidget(QLabel('검색키워드:'), 0, 0)
        grid.addWidget(QLabel('사이트:'), 1, 0)
        #grid.addWidget(QLabel('Review:'), 2, 0)

        

        grid.addWidget(self.lineEdit_keyword, 0, 1)
        grid.addWidget(self.cb_site, 1, 1)
        #grid.addWidget(QTextEdit(), 2, 1)
        grid.addWidget(self.btn_exec,2, 0)
        grid.addWidget(self.btn_quit,2, 1)

        self.setWindowTitle('My First Application')
        # self.move(300, 300)
        # self.resize(400, 200)
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def exec(self):
        keyword = self.lineEdit_keyword.text()
        site = self.cb_site.currentText()
        scraping.scraping(keyword, site).run()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec())


# 좌표 객체 얻기 
# position = pyautogui.position()

# # 화면 전체 크기 확인하기
# print(pyautogui.size())

# # x, y 좌표
# print(position.x)
# print(position.y)

# # 마우스 이동 (x 좌표, y 좌표)
# pyautogui.moveTo(500, 500)

# # 마우스 이동 (x 좌표, y 좌표 2초간)
# pyautogui.moveTo(100, 100, 2)  

# # 마우스 이동 ( 현재위치에서 )
# pyautogui.moveRel(200, 300, 2)

# # 마우스 클릭
# pyautogui.click()

# # 2초 간격으로 2번 클릭
# pyautogui.click(clicks= 2, interval=2)

# # 더블 클릭
# pyautogui.doubleClick()

# # 오른쪽 클릭
# pyautogui.click(button='right')

# # 스크롤하기 
# pyautogui.scroll(10)

# # 드래그하기
# pyautogui.drag(0, 300, 1, button='left')
