from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

# Створення екземпляру додатка QApplication
app = QApplication([])

# Створення головного вікна (QWidget)
main_win = QWidget()

# Задання початкового розміру головного вікна
main_win.resize(300, 200)

# Встановлення заголовка головного вікна
main_win.setWindowTitle('Вірю - не вірю')

# Створення елементу мітки (QLabel) з текстом про слонів
statement = QLabel('Ссавці з найбільшими вухами - слони!')

# Створення двох кнопок "Так" і "Ні"
btn_yes = QPushButton('Так')
btn_no = QPushButton('Ні')

# Створення горизонтального лейауту для розміщення мітки в центрі
line1 = QHBoxLayout()

# Створення горизонтального лейауту для розміщення кнопок "Так" і "Ні"
line2 = QHBoxLayout()

# Додавання мітки до лейауту line1 та вирівнювання по центру
line1.addWidget(statement, alignment=Qt.AlignCenter)

# Додавання кнопок "Так" і "Ні" до лейауту line2
line2.addWidget(btn_yes)
line2.addWidget(btn_no)

# Створення вертикального лейауту для розміщення двох горизонтальних лейаутів
line3 = QVBoxLayout()

# Додавання горизонтальних лейаутів до вертикального лейауту
line3.addLayout(line1)
line3.addLayout(line2)

# Встановлення вертикального лейауту для головного вікна
main_win.setLayout(line3)

def check_answer(answer):
    correct_answer = "Так"  # Встановлюємо правильну відповідь
    if answer == correct_answer:
        statement.setText('Правильно')
    else:
        statement.setText('Неправильно')

# Призначення функцій для кнопок
btn_yes.clicked.connect(lambda: check_answer(btn_yes.text()))
btn_no.clicked.connect(lambda: check_answer(btn_no.text()))

# Відображення головного вікна
main_win.show()

# Запуск головного циклу додатка
app.exec_()



