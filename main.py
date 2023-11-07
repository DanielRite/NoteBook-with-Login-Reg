import os
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QDialog, QWidget, QInputDialog
from PyQt5.QtGui import QIcon, QPixmap
import login
import traceback
import sqlite3
import error
import reg
import random
import regda
import RegLoginError
import PasswordError
import FileList
import SEtFileName
import qdarktheme


class NoteBook(QMainWindow, login.log):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.LoginButton.clicked.connect(self.loginbutton)
        self.RegButton.clicked.connect(self.registr)
        self.FileName = None
        self.textEdit = None
        self.dark = True
        qdarktheme.setup_theme('dark')
        self.ThemeChange.clicked.connect(self.theme_change)
        self.ThemeChange.setIcon(QIcon(QPixmap('dark-mode.png')))

    def theme_change(self):
        if self.dark:
            qdarktheme.setup_theme('light')
        else:
            qdarktheme.setup_theme('dark')
        self.dark = not self.dark

    def registr(self):
        win = Registration(self)
        win.show()
        win.exec_()
        win.setModal(True)

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        newFile = QAction(QIcon('new.png'), 'Новый Файл', self)
        newFile.triggered.connect(self.newFile)

        saveFile = QAction(QIcon('save.png'), 'Сохранить', self)
        saveFile.triggered.connect(self.saveFile)

        closeFile = QAction(QIcon('exit.png'), 'Закрыть приложение', self)
        closeFile.triggered.connect(self.closeFile)

        FileMenu = QAction(QIcon('huy_znaet.png'), 'Список файлов', self)
        FileMenu.triggered.connect(self.FileMenu)

        menubar = self.menuBar()
        Menu = menubar.addMenu('&Меню')
        Menu.addAction(newFile)
        Menu.addAction(saveFile)
        Menu.addAction(closeFile)
        Menu.addAction(FileMenu)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def newFile(self):
        self.textEdit.setText("")

    def run(self):
        Fname, ok_pressed = QInputDialog.getText(self, "Введите имя файла",
                                                 "имя файла")
        if ok_pressed:
            return Fname + ".txt"

    def saveFile(self):
        if self.FileName is None:
            self.FileName = self.run()

        fname = f"{self.login.text()}\\"

        text = self.textEdit.toPlainText()

        with open(fname + self.FileName, 'w') as f:
            f.write(text)

    def loginbutton(self):
        con = sqlite3.connect("landp.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM landp
                    WHERE login = ? AND password = ?""", (self.login.text(), self.password.text())).fetchall()

        if len(result) == 1:
            self.RegButton.move(10000, 10000)
            self.initUI()
        else:
            win = LogError(self)
            win.show()
            win.exec_()

    def closeFile(self):
        QMainWindow.close(self)

    def FileMenu(self):
        win = FiList(self, directory=self.login.text())
        win.show()
        win.exec_()
        res = win.FileName
        fname = f"{self.login.text()}\\{res}"
        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)
        self.FileName = res


class LogError(QDialog, error.LoginError):
    def __init__(self, win=None):
        super().__init__(win)
        self.Lerr(self)
        self.pushButton.clicked.connect(self.accept)
        self.setModal(True)


class Registration(QDialog, reg.Reg):
    def __init__(self, win=None):
        super().__init__(win)
        self.regist(self)
        self.pushButton.clicked.connect(self.reject)
        self.RegPushButton.clicked.connect(self.regi)
        self.setModal(True)

    def regi(self):
        flag = True
        logins = []
        con = sqlite3.connect("landp.sqlite")
        cur = con.cursor()
        idd = random.randint(1, 100000)
        result = cur.execute("""SELECT login FROM landp""").fetchall()
        for i in result:
            for j in i:
                logins.append(j)
        for i in logins:
            if str(self.loginReg.text()) == i:
                flag = False

        if not flag:
            win = PassError(self, "Логин занят!")
            win.show()
            win.exec_()
            return

        elif flag:
            if self.passwordReg.text() == self.passwordReg_2.text():
                pass

            else:
                win = PassError(self, "Пароли не совпадают!")
                win.show()
                win.exec_()
                con.commit()
                con.close()
                return

        nabor = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
                 'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
                 'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
                 'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
                 'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
                 'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'жэё']

        if len(self.passwordReg.text()) < 9:
            win = PassError(self, "Длина пароля должна\n быть более 8 символов")
            win.show()
            win.exec_()
            con.commit()
            con.close()
            return

        if self.passwordReg.text().lower() == self.passwordReg.text() \
                or self.passwordReg.text().upper() == self.passwordReg.text():
            win = PassError(self, "В пароле должна быть хоть одна\n заглавная и строчная буква")
            win.show()
            win.exec_()
            con.commit()
            con.close()
            return

        for el1 in '1234567890':
            if el1 in self.passwordReg.text():
                break
        else:
            win = PassError(self, "Пароль должен содержать хотя бы одну цифру")
            win.show()
            win.exec_()
            con.commit()
            con.close()
            return

        for el in nabor:
            if el in self.passwordReg.text().lower():
                win = PassError(self, "Ваш пароль сликшом простой")
                win.show()
                win.exec_()
                con.commit()
                con.close()
                return

        if flag:
            os.mkdir(self.loginReg.text())
            cur.execute('''INSERT INTO landp(id, login, password) VALUES(?, ?, ?)''',
                        (idd, self.loginReg.text(), self.passwordReg.text()))
            win = RegDa(self)
            win.show()
            win.exec_()
            con.commit()
            con.close()
            QWidget.close(self)


class PassError(QDialog, PasswordError.PasError):
    def __init__(self, win=None, message="неизвестная ошибка"):
        super().__init__(win)
        self.pe(self)
        self.OkRegPasswordError.clicked.connect(self.accept)
        self.setModal(True)
        self.label_2.setText(message)


class RegDa(QDialog, regda.RegDa):
    def __init__(self, win=None):
        super().__init__(win)
        self.reda(self)
        self.RegClose.clicked.connect(self.accept)
        self.setModal(True)


class RegLE(QDialog, RegLoginError.RegLogError):
    def __init__(self, win=None):
        super().__init__(win)
        self.rle(self)
        self.OkRegLoginError.clicked.connect(self.accept)
        self.setModal(True)


class FiList(QDialog, FileList.FilList):
    def __init__(self, win=None, directory=None):
        super().__init__(win)
        self.FileL(self)
        self.directory = directory
        self.Filez = os.listdir(self.directory)
        self.Filez.insert(0, "Выберите файл")
        self.Files.addItems(self.Filez)
        self.setModal(True)
        self.Files.setCurrentText("Выберите файл")
        self.Files.currentTextChanged.connect(self.onActivated)
        self.FileName = None

    def onActivated(self, text):
        self.FileName = text
        self.accept()


class SetFilName(QDialog, SEtFileName.SetFName):
    def __init__(self, win=None):
        super().__init__(win)
        self.sfname(self)
        self.FileNameText.connect(self.accept)
        self.setModal(True)


def except_hook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)


sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NoteBook()
    ex.show()
    sys.exit(app.exec_())
