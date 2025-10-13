import random
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QLabel
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

        layout = QVBoxLayout()
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
        # Текст блока с числом
        self.label = QLabel("Нажмите на кнопку для генерации чисел ⬇️ ️️️️")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgba(52, 152, 219, 0.3);
                border: 3px solid rgba(52, 152, 219, 0.5);
                border-radius: 20px;
                padding: 30px;
                font-size: 22px;
                font-weight: bold;
                color: #ecf0f1;
                margin: 10px;
                min-height: 60px;
                font-family: Times New Roman;
                }
            """)

        # Создаем кнопку
        self.button = QPushButton("🎲 Сгенерировать число")
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button.clicked.connect(self.generate_num)

        # Добавляем надпись виджет
        layout.addWidget(title_label)
        layout.addWidget(self.label)
        # Добавляем кнопку виджет
        layout.addWidget(self.button)

        self.setLayout(layout)


    def generate_num(self):
        random_num = random.randint(1, 400)
        self.label.setText(f"Случайное число: {random_num}")

        # Определение стиля в зависимости от величины числа
        if random_num > 300:
            color_style = """
                        QLabel {
                            background-color: #530FAD;
                            border: 3px solid rgba(46, 204, 113, 0.6);
                            color: #2ecc71;
                            font-size: 28px;
                        }
                    """
        elif random_num > 200:
            color_style = """
                        QLabel {
                            background-color: #3D9AD1;
                            border: 3px solid #0969A2;
                            color: #f1c40f;
                            font-size: 26px;
                        }
                    """
        else:
            color_style = """
            QLabel {
                    background-color: rgba(52, 152, 219, 0.3);
                    border: 3px solid rgba(52, 152, 219, 0.6);
                    color: #ecf0f1;
                    font-size: 24px;
                }
            """
            # Применение стиля и обновление текста
        self.label.setStyleSheet(color_style)
        self.label.setText(f"🎯 Ваше число:\n{random_num}")

        # Анимация кнопки
        self.button.setText("🔁 Генерируем...")
        self.button.setStyleSheet("""
                QPushButton {
                    background: #03436A;
                    border: none;
                    border-radius: 20px;
                    color: white;
                    padding: 15px 30px;
                    font-size: 16px;
                    font-weight: bold;
                }
            """)

        # Возврат исходного состояния кнопки через небольшой промежуток времени
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(400, self.reset_button)
    # Возвращаем начальное состояние кнопки
    def reset_button(self):
        self.button.setText("🎲 Сгенерировать число")
        self.button.setStyleSheet("""
            QPushButton {
                background: #3D9AD1;
                border: none;
                border-radius: 20px;
                color: white;
                padding: 15px 30px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: #0969A2;
            }
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomNumberGenerator()
    window.show()
    sys.exit(app.exec())

