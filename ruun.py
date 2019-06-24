from PyQt5 import QtWidgets
from PyQt5 import QtGui
from objdetect import Ui_GroupBox


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainwindows = QtWidgets.QGroupBox()
    mainwindows.setWindowIcon(QtGui.QIcon('avatar.png'))
    ui = Ui_GroupBox()
    ui.setupUi(mainwindows)
    mainwindows.show()
    sys.exit(app.exec_())
