from PyQt5.QtWidgets import QWidget, QLabel

from new_config import Config
from windows_design import design_of_final_window


class Final_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        config = Config()
        self.setWindowTitle('final_window')
        self.setGeometry(703, 457, 400, 300)
        design_of_final_window(self)
        self.correct_label.setText(f'{config.getValue("true_in_option")} задач было решено верно')
        self.incorrect_label.setText(f'{config.getValue("false_in_option")} задач было решено неверно')
        config.setValue('mark', (int(config.getValue("false_in_option")) * 2
                                 + int(config.getValue("true_in_option")) * 5)
                        // (int(config.getValue("false_in_option"))
                            + int(config.getValue("true_in_option"))))
        self.mark_label.setText(f'Ваша оценка - {config.getValue("mark")}')
        config.setValue("false_in_option", 0)
        config.setValue("true_in_option", 0)
        config.setValue("mark", 0)
        config.setValue('solution_options', int(config.getValue('solution_options')) + 1)
