import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        newFile = QAction(QIcon('new.png'), 'Новый Файл', self)
        newFile.triggered.connect(self.newFile)

        openFile = QAction(QIcon('open.png'), 'Открыть', self)
        openFile.triggered.connect(self.openFile)

        saveFile = QAction(QIcon('save.png'), 'Сохранить', self)
        saveFile.triggered.connect(self.saveFile)

        closeFile = QAction(QIcon('exit.png'), 'Закрыть приложение', self)
        closeFile.triggered.connect(self.closeFile)

        menubar = self.menuBar()
        Menu = menubar.addMenu('&Меню')
        Menu.addAction(newFile)
        Menu.addAction(openFile)
        Menu.addAction(saveFile)
        Menu.addAction(closeFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def newFile(self):
        self.textEdit.setText("")

    def saveFile(self):
        fname = QFileDialog.getSaveFileName(self, 'Save', '/Newfile')[0]

        text = self.textEdit.toPlainText()

        with open(fname + '.txt', 'w') as f:
            f.write(text)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def closeFile(self):
        QMainWindow.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
