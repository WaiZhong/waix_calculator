from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from win32mica import ApplyMica, MICAMODE

from settings import font, tFont
from functions import get_trans, get_options, get_history


class HistoryWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowCloseButtonHint)

        self.options = get_options()
        self.history = get_history()
        self.trans = get_trans()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        text = QTextEdit()
        text.setFont(tFont)
        text.setText(''.join([i[:-1] + '\n\n' for i in [i + ' ' for i in self.history]]).rstrip())
        if not self.options['settings.2.option']:
            text.append('\n\n' + self.trans['text.history.disabled'])
        text.setReadOnly(True)

        hbox = QHBoxLayout()

        ok = QPushButton(self.trans['button.back'])
        ok.setFont(font)
        ok.setShortcut('Return')
        ok.clicked.connect(self.close)

        hbox.addStretch(1)
        hbox.addWidget(ok)

        layout.addWidget(text)
        layout.addLayout(hbox)

        if self.options['settings.4.option']:
            self.setAttribute(Qt.WA_TranslucentBackground)
            ApplyMica(int(self.winId()), MICAMODE.LIGHT)

        self.setLayout(layout)
        self.setWindowTitle(self.trans['window.history.title'])
        self.setWindowIcon(QIcon('resource/images/icon.jpg'))
        self.resize(600, 400)
