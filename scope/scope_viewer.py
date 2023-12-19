import numpy as np
import time
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui_scope import Ui_ScopeViewer
import fake_scope


class ScopeThread(QtCore.QThread):

    new_plot = QtCore.pyqtSignal(object, object)

    def __init__(self, scope, parent=None):
        super().__init__()
        self.scope = scope
        self.scope.current_plot.connect(self.send_new_plot)

    def __del__(self):
        self.wait()

    def stop_thread(self):
        self.running = False

    def start_thread(self):
        self.running = True

    def send_new_plot(self, t, amplitude):
        self.new_plot.emit(t, amplitude)

    def run(self):
        while (self.running):
            self.scope.get_plot()
            time.sleep(0.05)


class ScopeViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):

        super().__init__()
        self.ui = Ui_ScopeViewer()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushbutton_connect.clicked.connect(self.connect)
        self.ui.pushbutton_start.clicked.connect(self.start)
        self.ui.pushbutton_stop.clicked.connect(self.stop)

        # Set display
        self.plot = self.ui.widget_plot.addPlot(labels={'left': 'Voltage (V)', 'bottom': 'Time (s)'})
        self.plot.showGrid(True, True)


    def connect(self):
        self.scope = fake_scope.FakeScope()
        self.scope_thread = ScopeThread(self.scope)
        self.scope_thread.new_plot.connect(self.display_new_plot)
        print("Camera connected")

    def start(self):
        self.scope_thread.start_thread()
        self.scope_thread.start()

    def stop(self):
        self.scope_thread.stop_thread()

    def display_new_plot(self, time, amplitude):
        self.time = time
        self.amplitude = amplitude
        self.plot.clear()
        self.plot.plot(self.time, self.amplitude)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ScopeViewer()
    window.show()
    sys.exit(app.exec_())
