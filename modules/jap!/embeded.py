from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Embed Matplotlib In PyQt5"
        top = 400
        left = 400
        width = 900
        height = 500


        self.setWindowTitle(title)
        self.setGeometry(top,left, width, height)

        self.MyUI()



    def MyUI(self):

        canvas = Canvas(self, width=8, height=4)
        canvas.move(0,0)

        button = QPushButton( "Click Me", self)
        button.move(100, 450)

        button = QPushButton("Click Me Two", self)
        button.move(250, 450)


class Canvas(FingureCanvas):
    def __init__(self, parent = None, width =5, height = 5, dpi =100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FingureCanvas.__init__(self, fig)
        self.setParent(parent)


        self.plot()



    def plot(self):
        x = np.array([50, 30, 25])

        labels = ['Apples', 'Bananas', 'Melons']
        ax = self.figure.add_subplot(111)

        ax.pie(x, labels=labels)





app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()