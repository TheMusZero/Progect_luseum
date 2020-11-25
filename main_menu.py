import sys

from PyQt5.QtWidgets import *

from Progress import Progress
from Random_Number import Random_Number
from SearchTasksByID import STByID
from get_option import Get_Opton
from windows_design import desing_of_main_menu


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        desing_of_main_menu(self)

    def StbI(self):
        self.stbi = STByID(self)
        self.stbi.show()
        self.close()

    def Prog(self):
        self.prog = Progress(self)
        self.prog.show()
        self.close()

    def RanNum(self):
        self.rannum = Random_Number(self)
        self.rannum.show()
        self.close()

    def Option(self):
        self.option = Get_Opton(self)
        self.option.show()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
