import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLabel, QPushButton)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtProperty


class ClickerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 0  # Счетчик кликов
        self.initUI()
        self.setWindowIcon(QIcon('game_control.png'))

    def initUI(self):
        # Основные настройки окна
        self.setWindowTitle("Кликер")
        self.setFixedSize(700, 600)

        # Создание центрального виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создание вертикального layout
        layout = QVBoxLayout()

        # Создание и настройка заголовка
        title = QLabel("Счётчик кликов")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
                    QLabel {
                        background: #00AF64;
                        border-radius: 25px;
                        padding: 25px;
                        color: white;
                        font-size: 28px;
                        font-weight: bold;
                        margin: 10px;
                    }
                """)

        # Создание и настройка метки счетчика
        self.counter_label = QLabel("0")
        self.counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.counter_label.setStyleSheet("""
                   QLabel {
                       background: #218359;
                       border-radius: 30px;
                       padding: 40px;
                       color: white;
                       font-size: 48px;
                       font-weight: bold;
                       border: 4px solid #2D3748;
                       margin: 10px;
                   }
               """)

        # Создание кнопки клика
        self.click_button = QPushButton("Кликни меня!")
        self.click_button.clicked.connect(self.increment_counter)
        self.click_button.setStyleSheet("""
                    QPushButton {
                        background: #0072241;
                        border: none;
                        border-radius: 25px;
                        padding: 25px;
                        color: white;
                        font-size: 22px;
                        font-weight: bold;
                        margin: 10px;
                    }
                    QPushButton:hover {
                        background: #36D7792;
                        transform: scale(1.05);
                    }
                    QPushButton:pressed {
                        background:  #61D7A4;
                        padding: 26px 24px;
                    }
                """)

        # Создание кнопки сброса
        reset_button = QPushButton("Сбросить")
        reset_button.clicked.connect(self.reset_counter)
        reset_button.setStyleSheet("""
                    QPushButton {
                        background:  #61D7A4;
                        border: none;
                        border-radius: 20px;
                        padding: 15px;
                        color: white;
                        font-size: 16px;
                        font-weight: bold;
                        margin: 10px;
                    }
                    QPushButton:hover {
                        background:  #0072241;
                    }
                """)

        # Добавление виджетов в layout
        layout.addWidget(title)
        layout.addWidget(self.counter_label)
        layout.addWidget(self.click_button)
        layout.addWidget(reset_button)

        central_widget.setLayout(layout)

        # Установка стиля для главного окна
        self.setStyleSheet("""
                QMainWindow {
                    background: rgb(137, 54, 255), rgb(145, 82, 182);
                }
            """)

    def increment_counter(self):
        """Увеличивает счетчик на 1 при каждом клике"""
        self.counter += 1
        self.counter_label.setText(str(self.counter))

    def reset_counter(self):
        """Сбрасывает счетчик к нулю"""
        self.counter = 0
        self.counter_label.setText("0")


def main():
    app = QApplication(sys.argv)
    window = ClickerApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()