import sqlite3
import sys

from PyQt5.QtWidgets import *

from take_new_task_from_id import Take_new_task_from_id
from windows_design import desing_of_SearchTasksByID


class STByID(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        desing_of_SearchTasksByID(self)

    def take_task(self):
        con = sqlite3.connect('kim.db')
        cur = con.cursor()

        try:
            data = cur.execute(f"""SELECT * FROM main
                                        WHERE id = {str(self.line_edit.text())}""").fetchall()

            if len(data) == 0:
                self.wrong_input.setStyleSheet('font-size: 15px;')
                self.wrong_input.setText('Введен не существующий ID!')

            else:
                if data[0][1] == 1:
                    self.first_form = Take_new_task_from_id(data, self)
                    self.first_form.show()
                    self.close()
        except sqlite3.OperationalError:
            self.wrong_input.setText('Введен не существующий ID!!!')

    def Back_to_menu(self):
        self.close()
        self.parent.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = STByID()
    ex.show()
    sys.exit(app.exec())
