import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Car system queries'
        self.width = 720
        self.height = 640
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=6)
        m.move(0, 0)

        #button of the first query
        button = QPushButton('Query 1', self)
        button.move(10, 10)
        button.resize(120, 50)

        # textbox for queries
        self.textbox = QLineEdit(self)
        self.textbox.move(150, 10)
        self.textbox.resize(120, 50)

        # label for textbox
        self.label = QLabel(self)
        self.label.setText("Write date in format dd-mm-yyyy")
        self.label.move(290, 10)

        # button of the second query
        button = QPushButton('Query 2', self)
        button.move(10, 70)
        button.resize(120, 50)

        # button of the third query
        button = QPushButton('Query 3', self)
        button.move(10, 130)
        button.resize(120, 50)

        # button of the forth query
        button = QPushButton('Query 4', self)
        button.move(10, 190)
        button.resize(120, 50)

        # button of the fifth query
        button = QPushButton('Query 5', self)
        button.move(10, 250)
        button.resize(120, 50)

        # button of the sixth query
        button = QPushButton('Query 6', self)
        button.move(10, 310)
        button.resize(120, 50)

        # button of the seventh query
        button = QPushButton('Query 7', self)
        button.move(10, 370)
        button.resize(120, 50)

        # button of the eighth query
        button = QPushButton('Query 8', self)
        button.move(10, 430)
        button.resize(120, 50)

        # button of the ninth query
        button = QPushButton('Query 9', self)
        button.move(10, 490)
        button.resize(120, 50)

        # button of the tenth query
        button = QPushButton('Query 10', self)
        button.move(10, 550)
        button.resize(120, 50)

        # connect button to function on_click
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        input_data = str(self.textbox.text())

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, input_data="26-11-2018"):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
