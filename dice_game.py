import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)
computerScore = 0
playerScore = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Game")
        self.setGeometry(50, 50, 550, 500)
        self.UI()

    def UI(self):
        # Scores
        self.scoreComputerText = QLabel("Computer Score:   ", self)
        self.scoreComputerText.move(30, 20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText = QLabel("Player Score:   ", self)
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

        # Buttons
        btnStart = QPushButton("Start", self)
        btnStart.setFont(buttonFont)
        btnStart.move(150, 250)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.setFont(buttonFont)
        btnStop.move(260, 250)
        btnStop.clicked.connect(self.stop)

        # Timer
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playGame)
        self.show()

    def start(self):
        self.timer.start()

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer == self.rndPlayer:
            QMessageBox.information(self, "Information", "Draw Game")
        elif self.rndComputer > self.rndPlayer:
            QMessageBox.information(self, "Information", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(computerScore))
            self.scorePlayerText.setText("Player Score: {}".format(playerScore))
        else:
            QMessageBox.information(self, "Information", "You win")
            playerScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(computerScore))
            self.scorePlayerText.setText("Player Score: {}".format(playerScore))

        if computerScore == 5:
            QMessageBox.information(self, "Information", "Game Over\nComputer wins")
            sys.exit()
        elif playerScore == 5:
            QMessageBox.information(self, "Information", "Game Over\nYou win")
            sys.exit()


    def playGame(self):
        self.rndComputer = randint(1, 6)
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("images/dice_1.png"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("images/dice_2.png"))
        elif self.rndComputer == 3:
            self.imageComputer.setPixmap(QPixmap("images/dice_3.png"))
        elif self.rndComputer == 4:
            self.imageComputer.setPixmap(QPixmap("images/dice_4.png"))
        elif self.rndComputer == 5:
            self.imageComputer.setPixmap(QPixmap("images/dice_5.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("images/dice_6.png"))

        self.rndPlayer = randint(1, 6)
        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("images/dice_1.png"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("images/dice_2.png"))
        elif self.rndPlayer == 3:
            self.imagePlayer.setPixmap(QPixmap("images/dice_3.png"))
        elif self.rndPlayer == 4:
            self.imagePlayer.setPixmap(QPixmap("images/dice_4.png"))
        elif self.rndPlayer == 5:
            self.imagePlayer.setPixmap(QPixmap("images/dice_5.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("images/dice_6.png"))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()