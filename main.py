import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from Uiter import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor


class First(QMainWindow):  # Экран приветсвия
    def __init__(self):  # иницилизация
        super(First, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.flag = None
        self.ui.press.clicked.connect(self.flag_on)

    def flag_on(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag is True:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            x = random.randint(5, 500)
            y = random.randint(5, 500)
            qp.drawEllipse(x, x, y, y)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = First()
    w.show()  # открываем начальное окно - приветсвия
    sys.exit(app.exec_())
