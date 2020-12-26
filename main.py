
import logging
from windows import MainWindow


class Main:
    def __init__(self):
        self.log = logging.getLogger("")
        self.log.setLevel(logging.INFO)

        MainWindow()

if __name__ == '__main__':
    Main()
