import sys
import random


from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QWidget, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x, self.y = 0, 0
        self.rad = 0
        self.col = []
        self.count = ''
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Координаты')
        self.pushButton = QPushButton('', self)
        self.pushButton.setText("Кнопка-кнопка")
        self.pushButton.setFixedSize(100, 50)
        self.pushButton.move(0, 50)
        self.pushButton.clicked.connect(self.lol)

    def lol(self, event):
        self.count = '1'
        self.repaint()

    def paintEvent(self, event):
        if self.count == '1':
            for i in range(3):
                self.col.append(random.randint(0, 255))
            self.x, self.y = random.randint(0, 700), random.randint(0, 500)
            self.rad = random.randint(4, 80)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(*self.col))
            qp.drawEllipse(self.x - self.rad, self.y - self.rad, 2 * self.rad, 2 * self.rad)
            self.col = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())