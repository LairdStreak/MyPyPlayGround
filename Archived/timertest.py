import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.setStyleSheet('QWidget { background-color: white; }')

        # counter
        self.counter = 10

        # timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timeout)  # timeout signal
        self.timer.start(1000)  # updates every second

        # label
        self.label = QtGui.QLabel(self)
        self.label.setNum(self.counter)
        self.label.setAlignment(Qt.AlignCenter)  # centered
        self.label.setStyleSheet('QLabel { color: black; }')

        # label's font
        font = self.label.font()
        font.setPointSize(80)
        self.label.setFont(font)

        # vertical box layout
        vlayout = QtGui.QVBoxLayout()
        vlayout.addWidget(self.label)
        self.setLayout(vlayout)

    # timeout slot
    @pyqtSlot()
    def timeout(self):
        self.counter -= 1
        self.label.setNum(self.counter)
        if self.counter <= 0:
            self.label.setText('GO!')
            self.timer.stop()


application = QApplication(sys.argv)

# window
window = Window()
window.setWindowTitle('Timer')
window.resize(220, 220)
window.show()

sys.exit(application.exec_())