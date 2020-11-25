from PyQt5.QtWidgets import QWidget

from new_config import Config
from windows_design import design_of_Progress


class Progress(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        design_of_Progress(self)

    def Back(self):
        self.parent.show()
        self.close()