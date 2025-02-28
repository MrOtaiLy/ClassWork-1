import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import Qt

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Task2")
        self.centralwidget = QWidget(MainWindow)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.pushButton = QPushButton("Draw Circle", self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.circles = []
        self.ui.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        r = random.randint(10, 100)
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        color = QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.circles.append((x, y, r, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        for c in self.circles:
            painter.setBrush(QBrush(c[3]))
            painter.drawEllipse(c[0], c[1], c[2], c[2])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
