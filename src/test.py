import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QObject, Signal, Slot


app = QApplication(sys.argv)

# define a new slot that receives a string and has
# 'saySomeWords' as its name
@Slot(str)
def say_some_words(words):
    print(words)

class Communicate(QObject):
    # create a new signal on the fly and name it 'speak'
    speak = Signal(str)

someone = Communicate()

# connect signal and slot
someone.speak.connect(say_some_words)

# emit 'speak' signal
someone.speak.emit("Hello everybody!")
