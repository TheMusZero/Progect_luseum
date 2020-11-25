import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from take_new_task_from_id import Take_new_task_from_id
from windows_design import design_of_get_option


class Get_Opton(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        design_of_get_option(self)

    def take_task(self):
        con = sqlite3.connect('kim.db')
        cur = con.cursor()
        self.flag = False

        try:
            self.data = cur.execute(f"""SELECT * FROM main
                                        WHERE option = {str(self.line_edit.text())}""").fetchall()

            if len(self.data) == 0:
                self.wrong_input.setStyleSheet('font-size: 15px;')
                self.wrong_input.setText('Введен не существующий вариант!')
            else:
                for self.i in self.data:
                    self.first_form = Take_new_task_from_id(self.i, self)
                    self.first_form.show()
                    self.close()



        except sqlite3.OperationalError:
            self.wrong_input.setText('Введен не существующий ID!!!')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.first_form = Take_new_task_from_id(self.i, self)
            self.first_form.show()
            self.close()
            self.flag = True

    def Back_to_menu(self):
        self.close()
        self.parent.show()
