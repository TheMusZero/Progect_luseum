import sqlite3

from PyQt5.QtWidgets import QWidget

from windows_design import design_of_Random_Number
import random

class Random_Number(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.random_number = random.randrange(1, 42)
        self.parent = parent
        con = sqlite3.connect('kim.db')
        cur = con.cursor()
        self.data2 = cur.execute(f"""SELECT * FROM main
                                            WHERE id = {self.random_number}""").fetchall()
        self.initUI()

    def initUI(self):
        design_of_Random_Number(self)

    def image_searching(self):
        selected_picture = self.data2[0][-2]
        return 'pictures/' + str(selected_picture) + '.png'\

    def Back(self):
        self.close()
        self.parent.show()
