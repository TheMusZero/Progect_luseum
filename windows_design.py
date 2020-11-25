from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from new_config import Config


def design_of_tntfi(self, data):
    self.setWindowTitle('Вторая форма')

    pixmap = QPixmap(self.image_searching(data))
    self.setGeometry(520, 369, pixmap.width(), pixmap.height() + 100)
    self.setStyleSheet("background-color: white;")

    self.pich = QLabel(self)
    self.pich.move(0, 0)
    self.pich.resize(pixmap.width(), pixmap.height())
    self.pich.setPixmap(pixmap)

    self.input_answer = QLineEdit(self)
    self.input_answer.move(55, pixmap.height() + 25)
    self.input_answer.resize(200, 20)
    self.input_answer.returnPressed.connect(lambda: self.return_answer(data))

    self.lanswer = QLabel(self)
    self.lanswer.move(10, pixmap.height() + 20)
    self.lanswer.resize(41, 20)
    self.lanswer.setText('Ответ:')

    self.btn_back = QPushButton('Назад', self)
    self.btn_back.move(591, pixmap.height() + 25)
    self.btn_back.resize(105, 50)
    self.btn_back.clicked.connect(self.Back)
    self.btn_back.setStyleSheet("background-color: yellow;")

    self.correct_answer = QLabel(self)
    self.correct_answer.resize(170, 50)
    self.correct_answer.move(280, 20 + pixmap.height())

def desing_of_SearchTasksByID(self):
    self.setWindowTitle('test')

    self.search = QLabel('Поиск по id:', self)
    self.search.move(10, 10)
    self.search.resize(61, 21)

    self.wrong_input = QLabel(self)
    self.wrong_input.move(10, 40)
    self.wrong_input.resize(221, 20)

    self.line_edit = QLineEdit(self)
    self.line_edit.move(80, 10)
    self.line_edit.resize(251, 21)
    self.line_edit.returnPressed.connect(self.take_task)

    self.bom = QPushButton('Вернуться в меню', self)
    self.bom.move(220, 40)
    self.bom.resize(101, 23)
    self.bom.clicked.connect(self.Back_to_menu)


def desing_of_main_menu(self):
    self.setGeometry(748, 417, 300, 320)
    self.setWindowTitle('Main_menu')

    self.Choice_of_option = QPushButton('Выбор варианта', self)
    self.Choice_of_option.move(30, 30)
    self.Choice_of_option.resize(241, 51)
    self.Choice_of_option.setStyleSheet('font-size: 15px;')
    self.Choice_of_option.clicked.connect(self.Option)

    self.Search_Tasks_By_ID = QPushButton('Поиск задач по ID', self)
    self.Search_Tasks_By_ID.move(30, 100)
    self.Search_Tasks_By_ID.resize(241, 51)
    self.Search_Tasks_By_ID.setStyleSheet('font-size: 15px;')
    self.Search_Tasks_By_ID.clicked.connect(self.StbI)

    self.Random_Number = QPushButton('Случайный номер', self)
    self.Random_Number.move(30, 170)
    self.Random_Number.resize(241, 51)
    self.Random_Number.setStyleSheet('font-size: 15px;')
    self.Random_Number.clicked.connect(self.RanNum)

    self.Progress = QPushButton('Прогресс', self)
    self.Progress.move(30, 240)
    self.Progress.resize(241, 51)
    self.Progress.setStyleSheet('font-size: 15px;')
    self.Progress.clicked.connect(self.Prog)

def design_of_Progress(self):
    config = Config()
    self.setGeometry(685, 428, 491, 351)

    self.was_decided = QLabel(self)
    self.was_decided.move(20, 20)
    self.was_decided.resize(271, 41)
    self.was_decided.setText(f'За всё время было решено:   {config.getValue("was_decided")}')

    self.true_false = QLabel(self)
    self.true_false.move(20, 80)
    self.true_false.resize(531, 41)
    self.true_false.setText(f'Из них {config.getValue("true")} '
                            f'решено верно, и {config.getValue("false")} не верно')

    self.solution_options = QLabel(self)
    self.solution_options.move(20, 140)
    self.solution_options.resize(531, 41)
    self.solution_options.setText(f'Было решено {config.getValue("solution_options")} варианов')

    self.average_rating = QLabel(self)
    self.average_rating.move(20, 200)
    self.average_rating.resize(531, 41)
    self.average_rating.setText(f'Ваша средняя оценка:   {config.getValue("average_rating")}')

    self.was_decided.setStyleSheet('font-size: 20px;')
    self.true_false.setStyleSheet('font-size: 20px;')
    self.solution_options.setStyleSheet('font-size: 20px;')
    self.average_rating.setStyleSheet('font-size: 20px;')

    self.btn_back = QPushButton('Назад', self, clicked=self.Back)
    self.btn_back.move(325, 285)
    self.btn_back.resize(100, 50)


def design_of_Random_Number(self):
    self.setWindowTitle('Вторая форма')

    pixmap = QPixmap(self.image_searching())
    self.setGeometry(630, 424, pixmap.width(), pixmap.height() + 100)
    self.setStyleSheet("background-color: white;")

    self.pich = QLabel(self)
    self.pich.move(0, 0)
    self.pich.resize(pixmap.width(), pixmap.height())
    self.pich.setPixmap(pixmap)

    self.input_answer = QLineEdit(self)
    self.input_answer.move(55, pixmap.height() + 25)
    self.input_answer.resize(200, 20)
    self.input_answer.returnPressed.connect(lambda: self.get_RandomNumber())

    self.lanswer = QLabel(self)
    self.lanswer.move(10, pixmap.height() + 20)
    self.lanswer.resize(41, 20)
    self.lanswer.setText('Ответ:')

    self.btn_back = QPushButton('Назад', self)
    self.btn_back.move(591, pixmap.height() + 25)
    self.btn_back.resize(105, 50)
    self.btn_back.clicked.connect(self.Back)
    self.btn_back.setStyleSheet("background-color: yellow;")

    self.correct_answer = QLabel(self)
    self.correct_answer.resize(170, 50)
    self.correct_answer.move(280, 20 + pixmap.height())

def design_of_get_option(self):
    self.setWindowTitle('test')

    self.search = QLabel('Поиск по варианту:', self)
    self.search.move(10, 10)
    self.search.resize(61, 21)

    self.wrong_input = QLabel(self)
    self.wrong_input.move(10, 40)
    self.wrong_input.resize(221, 20)
    self.i = 0

    self.line_edit = QLineEdit(self)
    self.line_edit.move(80, 10)
    self.line_edit.resize(251, 21)
    self.line_edit.returnPressed.connect(self.take_task)

    self.bom = QPushButton('Вернуться в меню', self)
    self.bom.move(220, 40)
    self.bom.resize(101, 23)
    self.bom.clicked.connect(self.Back_to_menu)
