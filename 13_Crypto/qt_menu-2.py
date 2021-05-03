import sys
import PyQt5

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    #Dialog
    def __init__(self, parent = None):
        #Initializer
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Input text: ', QLineEdit())
        formLayout.addRow('Shift number: ', QLineEdit())
        formLayout.addRow('Number of shift letters: ', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())