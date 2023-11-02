from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton,QListWidget
app = QApplication([])
window = QWidget()
window.setWindowTitle("easy editor")
window.resize(1000,700)

folder = QPushButton()
folder.setText("Папка")

lineH = QHBoxLayout
lineV1 = QVBoxLayout
lineV2 = QVBoxLayout
lineH1 = QHBoxLayout

lineV1.addWidget(folder)
lineH.addLayout(lineV1)
window.setLayout(lineH)







window.show()
app.exec_()