import sqlite3

from PyQt5.QtWidgets import QWidget

from new_config import Config
from windows_design import design_of_tntfi


class Take_new_task_from_id(QWidget):
    def __init__(self, data, parent):
        super().__init__()
        self.parent = parent
        self.initUI(data)

    def initUI(self, data):
        design_of_tntfi(self, data)

    def image_searching(self, data):
        print(data)
        selected_picture = data[0][-2]

        print('pictures/' + str(selected_picture) + '.png')
        return 'pictures/' + str(selected_picture) + '.png'\

    def return_answer(self, data):
        config = Config()
        CoAn = data[0][-3]
        self.input_answer.setReadOnly(True)

        if str(CoAn) != self.input_answer.text():
            self.correct_answer.setText(f'Неверно!!\nВерный ответ: {CoAn}')
            config.setValue('false', int(config.getValue('false')) + 1)

        else:
            self.correct_answer.setText("Верно!!!")
            config.setValue('true', int(config.getValue('true')) + 1)
        config.setValue('was_decided', int(config.getValue('was_decided')) + 1)
        config.setValue('average_rating', (int(config.getValue('false')) * 2 +
                                           int(config.getValue('true')) * 5) //
                        (int(config.getValue('false')) + int(config.getValue('true'))))
        self.correct_answer.setStyleSheet('font-size: 20px;')

    def number_of_task(self):
        con = sqlite3.connect('kim.db')
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM main
                            WHERE id = {self.line_edit.text()}""").fetchall()
        self.number.setText(f'Номер: ')

    def Back(self):
        self.close()
        self.parent.show()