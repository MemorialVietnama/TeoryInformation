import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import os


os.chdir("C:\\TeoryInformation\\TeoryInformation\\9\\")


class Window(QMainWindow):

    model = None
    db = None

    def __init__(self) -> None:
        super().__init__()

        uic.loadUi("main.ui", self)

        self.menu_open.triggered.connect(self.open_table)
        self.menu_close.triggered.connect(self.close_table)
        self.menu_exit.triggered.connect(self.window_exit)

        self.btn_add.clicked.connect(self.button_add)
        self.btn_del.clicked.connect(self.button_del)
        self.btn_save.clicked.connect(self.button_save)
        self.btn_cancel.clicked.connect(self.button_cancel)
        self.btn_refresh.clicked.connect(self.button_refresh)

        self.setFixedSize(800, 580)

    def open_table(self):

        self.close_table()

        (fileName, type) = QFileDialog.getOpenFileName(self, "Открыть базу данных", filter="DataBase (*.db)")
        self.db = QSqlDatabase.addDatabase('QSQLITE', 'db')
        self.db.setDatabaseName(fileName)

        if not self.db.open():
            self.msg("Could not open the database")

            return

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('Users')
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.user_view.setModel(self.model)
        
    def close_table(self):

        if self.db is None:
            return

        del self.model

        self.db.close()
        del self.db
        
        QSqlDatabase.removeDatabase('db')

        self.user_view.setModel(self.model)

    def button_add(self):

        if self.model:
            self.model.insertRow(0)

    def button_del(self):
        if self.model:
            index = self.user_view.selectionModel().currentIndex()
            self.model.removeRow(index.row())

    def button_save(self):
        if self.model:
            self.model.submitAll()

    def button_cancel(self):
        if self.model:
            self.model.revertAll()

    def button_refresh(self):
         if self.model:
            self.model.select()

    def msg(self, text):
        msg = QMessageBox(self)
        msg.setText(text)
        msg.exec()

    def window_exit(self):
        self.close()

if __name__ == '__main__':
    print(os.getcwd())
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
