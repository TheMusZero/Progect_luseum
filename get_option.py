import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from final_window import Final_window
from option import Take_new_task_from_id2
from take_new_task_from_id import Take_new_task_from_id
from windows_design import design_of_get_option


class Get_Opton(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()
        self.current_task = None
        self.tasks = None
        self.first_form = None

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
                self.current_task = 0
                self.tasks = self.data
                self.show_task()

        except sqlite3.OperationalError:
            self.wrong_input.setText('Введен не существующий ID!!!')

    def show_task(self):
        if self.first_form:
            self.first_form.close()
        self.first_form = Take_new_task_from_id2(self.tasks[self.current_task], self)
        self.first_form.show()

    def next_task(self):
        self.current_task += 1
        if self.current_task == len(self.tasks):
            self.final_form = Final_window()
            self.final_form.show()
            return
        self.show_task()

    def Back_to_menu(self):
        self.close()
        self.parent.show()
