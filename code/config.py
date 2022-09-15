from PyQt5.QtGui import QFont

__version__ = '1.9.1'

symbol_lst = ['+', '-', '×', '÷', '^']
symbol_lst_2 = ['.', '/']
bracket_lst = [['(', '[', '{'], [')', ']', '}']]
symbol_turn = {'+': '+', '-': '-', '×': '*', '÷': '/', '//': '/', '^': '**', '**': '**'}
'''num_widths = {
	'1': 30.4, '2': 31.8, '3': 33.4, '4': 33.4, '5': 33.4, '6': 33.4, '7': 30.3, '8': 33.4, '9': 33.4, '0': 31.8,
	'.': 12.4, '/': 21, 'E': 30.5, 'e': 28
}  # 672 ÷ 一直输入直到窗口被拉伸的个数'''

default_options = {
	'settings.1.option.1': False,
	'settings.1.option.2': False,
	'settings.1.option.3': False,
	'settings.2.option.1': True,
	'settings.2.option.2': True,
	'settings.4.option': False,
	'settings.4.selector.1': 'Segoe UI',
	'settings.4.selector.2': '',
	'language': 'en_us',
	'window_title': 'WaiXCalc',
}

default_data = {
	'formula': ['0'],
	'calcFormula': ['0'],
	'calcFormulaStep': [],
	'frontBracketIndex': [],
	'frontBracketIndexStep': [],
	'isResult': False,
	'latest_pos_x': 0,
	'latest_pos_y': 0,
	'latest_width': 0,
	'enableDarkMode': False
}

rFont = QFont()
# font.setPointSize(8)

hFont = QFont()
hFont.setPointSize(24)

tFont = QFont()
tFont.setPointSize(10)

nFont = QFont()
nFont.setPointSize(12)

# tipFont = QFont()
# tipFont.setPointSize(4)
