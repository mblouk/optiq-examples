import numpy as np
from PyQt5 import QtCore
import time

class FakeScope(QtCore.QObject):

    current_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, parent=None):
        super().__init__(parent)

    def get_plot(self):
        N = 512
        t = np.linspace(0, 10, N)
        plot = np.random.random(np.shape(t))
        self.current_plot.emit(t, plot)
