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
        self.title = 'Differential equation -y-x'
        self.width = 720
        self.height = 640
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=6)
        m.move(0, 0)

        # connect button to function on_click
        #button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        '''x0 = float(self.textbox_x0.text())
        y0 = float(self.textbox_y0.text())
        x_max = int(self.textbox_x.text())
        steps = int(self.textbox_x.text())
        m = PlotCanvas(self, width=5, height=6, x_max=x_max, y0=y0, x0=x0)
        m.move(0, 0)
        m.show()'''

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, x_max=10, y0=1, x0=0, steps=30):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.plot(x_max=x_max, x0=x0, y0=y0, steps=steps)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
