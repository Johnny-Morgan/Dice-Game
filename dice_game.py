import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap

textFont = QFont("Times", 14)
buttonsFont = QFont("Arial", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Game")
        self.setGeometry(50, 50, 550, 500)
        self.UI()

    def UI(self):
        # Scores
        self.scoreComputerText = QLabel("Computer Score: ", self)
        self.scoreComputerText.move(30, 20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText = QLabel("Player Score: ", self)
        self.scorePlayerText.move(340, 20)
        self.scorePlayerText.setFont(textFont)

        # Images
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("images/dice_1.png"))
        self.imageComputer.move(50, 100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("images/dice_1.png"))
        self.imagePlayer.move(350, 100)

        self.imageVersus = QLabel(self)
        self.imageVersus.setPixmap(QPixmap("images/versus.png"))
        self.imageVersus.move(230, 135)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()