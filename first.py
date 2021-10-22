import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1250, 1150)
    w.move(1300, 1300)
    w.setWindowTitle('Анализатор движения финансов')
    w.show()

    sys.exit(app.exec_())