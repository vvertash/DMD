import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from queries import *


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
        button1 = QPushButton('Query 1', self)
        button1.move(10, 10)
        button1.resize(120, 50)

        # textbox for queries
        self.textbox = QLineEdit(self)
        self.textbox.move(150, 10)
        self.textbox.resize(120, 50)

        # label for textbox
        self.label = QLabel(self)
        self.label.setText("Write data in format")
        self.label.move(150, 70)
        self.label = QLabel(self)
        self.label.setText("dd-mm-yyyy")
        self.label.move(150, 80)

        # button of the second query
        button2 = QPushButton('Query 2', self)
        button2.move(10, 70)
        button2.resize(120, 50)

        # button of the third query
        button3 = QPushButton('Query 3', self)
        button3.move(10, 130)
        button3.resize(120, 50)

        # button of the forth query
        button4 = QPushButton('Query 4', self)
        button4.move(10, 190)
        button4.resize(120, 50)

        # button of the fifth query
        button5 = QPushButton('Query 5', self)
        button5.move(10, 250)
        button5.resize(120, 50)

        # button of the sixth query
        button6 = QPushButton('Query 6', self)
        button6.move(10, 310)
        button6.resize(120, 50)

        # button of the seventh query
        button7 = QPushButton('Query 7', self)
        button7.move(10, 370)
        button7.resize(120, 50)

        # button of the eighth query
        button8 = QPushButton('Query 8', self)
        button8.move(10, 430)
        button8.resize(120, 50)

        # button of the ninth query
        button9 = QPushButton('Query 9', self)
        button9.move(10, 490)
        button9.resize(120, 50)

        # button of the tenth query
        button10 = QPushButton('Query 10', self)
        button10.move(10, 550)
        button10.resize(120, 50)

        # connect button to function on_click
        button1.clicked.connect(self.on_click1)
        button2.clicked.connect(self.on_click2)
        button3.clicked.connect(self.on_click3)
        button4.clicked.connect(self.on_click4)
        button5.clicked.connect(self.on_click5)
        button6.clicked.connect(self.on_click6)
        button7.clicked.connect(self.on_click7)
        button8.clicked.connect(self.on_click8)
        button9.clicked.connect(self.on_click9)
        button10.clicked.connect(self.on_click10)

        self.show()

    @pyqtSlot()
    def on_click1(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query1())
        m.move(150, 120)
        m.show()


    @pyqtSlot()
    def on_click2(self):
        input_data = str(self.textbox.text())
        m = PlotCanvas(self, width=5, height=3, input_data=query2(input_data))
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click3(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query3())
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click4(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query4())
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click5(self):
        input_data = str(self.textbox.text())
        m = PlotCanvas(self, width=5, height=3, input_data=query5(input_data))
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click6(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query6())
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click7(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query7())
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click8(self):
        input_data = str(self.textbox.text())
        m = PlotCanvas(self, width=5, height=3, input_data=query8(input_data))
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click9(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query9())
        m.move(150, 120)
        m.show()

    @pyqtSlot()
    def on_click10(self):
        m = PlotCanvas(self, width=5, height=3, input_data=query10())
        m.move(150, 120)
        m.show()

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, input_data="a"):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.printer(input_data=input_data)

    def printer(self, input_data="26-11-2018"):
        # label for textbox
        self.label = QLabel(self)
        self.label.setText(input_data)
        self.label.move(12, 12)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
