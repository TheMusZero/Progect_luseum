from PyQt5.QtWidgets import QWidget, QLabel

from new_config import Config


class Final_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        config = Config()
        self.setWindowTitle('final_window')
        self.setGeometry(703, 457, 400, 300)

        self.lable_1 = QLabel(self)
        self.lable_1.setGeometry(80, 20, 291, 31)

        self.correct_label = QLabel(self)
        self.correct_label.setGeometry(30, 83, 311, 41)
        self.correct_label.setText(f'{config.getValue("true_in_option")} задачь было решено верно')

        self.incorrect_label = QLabel(self)
        self.incorrect_label.setGeometry(30, 140, 321, 41)
        self.incorrect_label.setText(f'{config.getValue("false_in_option")} задачь было решено неверно')

        self.mark_label = QLabel(self)
        self.mark_label.setGeometry(90, 230, 241, 51)

        config.setValue('mark', (int(config.getValue("false_in_option")) * 2
                                 + int(config.getValue("true_in_option")) * 5)
                        // (int(config.getValue("false_in_option"))
                            + int(config.getValue("true_in_option"))))
        self.mark_label.setText(f'Ваша оценка - {config.getValue("mark")}')

        config.setValue("false_in_option", 0)
        config.setValue("true_in_option", 0)
        config.setValue("mark", 0)
