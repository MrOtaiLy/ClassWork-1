import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        r = random.randint(10, 100)
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        self.circles.append((x, y, r))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor("yellow")))
        for circle in self.circles:
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
