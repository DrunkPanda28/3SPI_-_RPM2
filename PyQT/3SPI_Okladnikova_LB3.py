import random
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QLabel, QMessageBox, QLineEdit
from PyQt6.QtGui import QIcon


class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.png'))

    def initUI(self):
        self.setWindowTitle("Генератор радомных чисел")
        self.setMaximumSize(850, 700)
        self.setMinimumSize(600, 500)

        self.setStyleSheet(
            """
            QWidget {
                background-color: #1240AB;
                color: white;
                font-family: Times New Roman, Arial, sans-serif;
            }
            QLabel {
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 15px;
                padding: 20px;
                font-size: 18px;
                font-weight: bold;
                margin: 10px;
                }
            QPushButton {
                background-color: #4671D5;
                border: none;
                border-radius: 17px;
                color: white;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: bold;
                margin: 10px;
                }
            QPushButton:hover {
                background-color: #6C8CD5;
                transform: scale(1.05);
                }
            QPushButton:pressed {
            background-color: #4671D5;
                padding: 16px 29px;
                }
            """)
        #Поля для ввода начало
        self.start_label = QLabel("Начало диапозона")
        self.start_label.setStyleSheet("""
        QLabel {
            font-size: 26px;
            }""")
        self.start_input = QLineEdit()
        self.start_input.setPlaceholderText("Введите начальное число")
        self.start_input.setStyleSheet("""
        QLineEdit {
            font-size: 20px;
            color: white;
            }""")

        # Поля для ввода конец
        self.end_label = QLabel("Конец диапозона")
        self.end_label.setStyleSheet("""
                QLabel {
                    font-size: 26px;
                    }""")

        self.end_input = QLineEdit()
        self.end_input.setPlaceholderText("Введите конечное число")
        self.end_input.setStyleSheet("""
                QLineEdit {
                    font-size: 20px;
                    color: white;
                    }""")

        # Кнопка генерации
        self.generate_button = QPushButton("🎲 Сгенерировать число")
        self.generate_button.clicked.connect(self.generate_num)

        layout = QVBoxLayout()
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_input)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_input)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel("🎯 Генератор случайных чисел")

        # Выравнивание текста по центру
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Настройка стиля надписи
        title_label.setStyleSheet("""
            QLabel {
                background: #2A4480;
                border-radius: 20px;
                padding: 15px;
                font-size: 26px;
                font-weight: bold;
                margin: 5px;
                }
        """)


    def generate_num(self):
        try:
            start = int(self.start_input.text())
            end = int(self.end_input.text())

            if start > end:
                QMessageBox.warning(self, "⚠️ Ошибка!", "Начало диапозона не может быть больше конца!")
                return

            random_number = random.randint(start, end)

            QMessageBox.information(self, "🎯 Результат", f"Сгенерированное число: {random_number}")
        except ValueError:
            QMessageBox.warning(self, "⚠️ Ошибка!", "Пожалуйста, введите целые числа в оба поля!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomNumberGenerator()
    window.show()
    sys.exit(app.exec())

