import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                             QLabel, QSlider, QPushButton, QWidget, QFileDialog,
                             QFrame, QSizePolicy)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform, QPainter


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        #Исходное изображение
        self.original_image = None
        # image после изменений
        self.current_image = None
        # Угол поворота
        self.rotation_angle = 0
        # Текущий QPixmap для отображения
        self.current_pixmap = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Редактор изображений")
        self.setGeometry(100, 100, 1000, 700)

        # Установка стилей для всего приложения
        self.setStyleSheet("""
                QMainWindow {
                    background-color: #f5f5f5;
                }
                QPushButton {
                    background-color: #4CAF50;
                    border: none;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:checked {
                    background-color: #2196F3;
                }
                QPushButton:pressed {
                    background-color: #1976D2;
                }
                QSlider::groove:horizontal {
                    border: 1px solid #999999;
                    height: 6px;
                    background: #e0e0e0;
                    border-radius: 3px;
                }
                QSlider::handle:horizontal {
                    background: #4CAF50;
                    width: 16px;
                    border-radius: 8px;
                    margin: -5px 0;
                }
                QLabel {
                    color: #333333;
                    font-family: Arial;
                }
                QFrame {
                    background-color: white;
                    border-radius: 5px;
                }
            """)
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Верхняя панель с кнопками
        self.create_top_panel(layout)

        # Область для отображения img
        self.create_image_display(layout)

        # Панель управления
        self.create_panel(layout)

    def create_top_panel(self, layout):
        """Создание верхней панели с кнопками управления"""
        top_layout = QHBoxLayout()

        # Кнопка открытия img
        self.open_button = QPushButton("📁 Открыть изображение")
        self.open_button.clicked.connect(self.open_file)
        top_layout.addWidget(self.open_button)

        # Кнопка сброса к исходному состоянию
        self.reset_button = QPushButton("🔄 Сбросить")
        self.reset_button.clicked.connect(self.reset_image)
        self.reset_button.setEnabled(False)
        top_layout.addWidget(self.reset_button)

        # Растягивающееся пространство
        top_layout.addStretch()
        layout.addLayout(top_layout)

    def create_image_display(self, layout):
        """Создание области для image"""
        image_frame = QFrame()
        image_frame.setFrameStyle(QFrame.Shape.Box)
        image_frame.setLineWidth(1)
        image_frame.setMinimumSize(600, 400)
        image_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f8f8;
                border: 2px solid #dddddd;
            }
        """)
        layout.addWidget(image_frame)

        frame_layout = QVBoxLayout(image_frame)

        # QLabel для отображения изображения
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumSize(400, 300)
        self.image_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 3px;
            }
        """)
        self.image_label.setText("Откройте изображение для редактирования")
        frame_layout.addWidget(self.image_label)

    def create_panel(self, layout):
        """Создание панели управления с настройками"""
        # Панель прозрачности
        transparency_layout = QHBoxLayout()
        transparency_label = QLabel("Прозрачность")
        transparency_label.setStyleSheet("font-weight: bold; color: #333;")
        transparency_layout.addWidget(transparency_label)

        # Слайдер для регулировки прозрачности
        self.transparency_slider = QSlider(Qt.Orientation.Horizontal)
        self.transparency_slider.setRange(0, 100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.valueChanged.connect(self.apply_all_effects)
        transparency_layout.addWidget(self.transparency_slider)

        layout.addLayout(transparency_layout)

        # Панель поворота
        rotation_layout  = QHBoxLayout()

        # кнопки поворота
        self.rotate_left_btn = QPushButton("↶ Повернуть налево (-90°)")
        self.rotate_left_btn.clicked.connect(self.rotate_left)
        rotation_layout .addWidget(self.rotate_left_btn)

        self.rotate_right_btn = QPushButton("↷ Повернуть направо (+90°)")
        self.rotate_right_btn.clicked.connect(self.rotate_right)
        rotation_layout .addWidget(self.rotate_right_btn)

        rotation_layout .addStretch()
        layout.addLayout(rotation_layout)

        # Панель цветовых каналов
        channels_layout = QHBoxLayout()
        channels_label = QLabel("Настройка цвета:")
        channels_label.setStyleSheet("font-weight: bold; color: #333;")
        channels_layout.addWidget(channels_label)

        # Кнопки для выбора цвета
        # Кнопки для выбора цветовых каналов (включаются/выключаются)
        self.red_btn = QPushButton('🔴 Красный')
        self.red_btn.setCheckable(True)
        self.red_btn.setChecked(True)
        self.red_btn.clicked.connect(self.apply_all_effects)
        channels_layout.addWidget(self.red_btn)

        self.green_btn = QPushButton('🟢 Зеленый')
        self.green_btn.setCheckable(True)
        self.green_btn.setChecked(True)
        self.green_btn.clicked.connect(self.apply_all_effects)
        channels_layout.addWidget(self.green_btn)

        self.blue_btn = QPushButton('🔵 Синий')
        self.blue_btn.setCheckable(True)
        self.blue_btn.setChecked(True)
        self.blue_btn.clicked.connect(self.apply_all_effects)
        channels_layout.addWidget(self.blue_btn)

        # Кнопка для быстрого выбора всех каналов
        self.all_channels_btn = QPushButton('🌈 Все каналы')
        self.all_channels_btn.clicked.connect(self.select_all_channels)
        channels_layout.addWidget(self.all_channels_btn)

        channels_layout.addStretch()
        layout.addLayout(channels_layout)

    def open_file(self):
        """Открытие диалога выбора файла и загрузка изображения"""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть изображение",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        if file_name:
            # Загружаем изобр с помощью QImage
            self.original_image = QImage(file_name)
            if not self.original_image.isNull():
                # Создаем копию для работф
                self.current_image = self.original_image.copy()
                self.rotation_angle = 0
                self.apply_all_effects()
                self.reset_button.setEnabled(True)
            else:
                self.image_label.setText("Ошибка загрузки изображения!")

    def reset_image(self):
        """Сброс изображения к исходному состоянию"""
        if self.original_image:
            # Востанавливаем исходное image
            self.current_image = self.original_image.copy()
            self.rotation_angle = 0
            # Сбрасываем значения контролов
            self.transparency_slider.setValue(100)
            self.red_btn.setChecked(True)
            self.green_btn.setChecked(True)
            self.blue_btn.setChecked(True)
            self.apply_all_effects()

    def rotate_left(self):
        """ Поворот image на 90 на лево"""
        self.rotation_angle = (self.rotation_angle - 90) % 360
        self.apply_all_effects()

    def rotate_right(self):
        """ Поворот image на 90 на право"""
        self.rotation_angle = (self.rotation_angle + 90) % 360
        self.apply_all_effects()

    def select_all_channels(self):
        """Выбор всех цветовых каналов"""
        self.red_btn.setChecked(True)
        self.green_btn.setChecked(True)
        self.blue_btn.setChecked(True)
        self.apply_all_effects()

    def apply_color_channels(self, image):
        """Применение выбранных цветовых каналов к изображению"""
        # Если выбраны не все каналы, обрабатываем изображение
        if not (self.red_btn.isChecked() and self.green_btn.isChecked() and self.blue_btn.isChecked()):
            # Создаем новое изображение с форматом ARGB32
            result_image = QImage(image.size(), QImage.Format.Format_ARGB32)
            # Заполняем прозрачность
            result_image.fill(Qt.GlobalColor.transparent)

            # Обработка по пиксельно
            for x in range(image.width()):
                for y in range(image.height()):
                    color = QColor(image.pixel(x, y))
                    # Устанавливаем компоненты цвета в 0, если канал не выбран
                    r = color.red() if self.red_btn.isChecked() else 0
                    g = color.green() if self.green_btn.isChecked() else 0
                    b = color.blue() if self.blue_btn.isChecked() else 0
                    a = color.alpha()

                    # Устанавливаем обработаный пиксель
                    result_image.setPixel(x, y, QColor(r, g, b, a).rgba())

            return result_image
        return image

    def apply_rotation(self, image):
        """Применение поворота к изображению"""
        if self.rotation_angle != 0:
            # Создаем трансформацию для поворота
            transform = QTransform()
            transform.rotate(self.rotation_angle)
            # Применяем поворот с сглаживанием
            return image.transformed(transform, Qt.TransformationMode.SmoothTransformation)
        return image

    def apply_all_effects(self):
        """Применение всех эффектов к изображению и его отображение"""
        if not self.current_image:
            return

        # Начинаем с оригинального image
        proces_img = self.original_image.copy()

        # Применение цветов
        proces_img = self.apply_color_channels(proces_img)

        # Поворот
        proces_img = self.apply_rotation(proces_img)

        # Создаем QPixmap из обработанного изображения
        pixmap = QPixmap.fromImage(proces_img)

        # Прозрачность
        transparency = self.transparency_slider.value() / 100
        if transparency < 1:
            # Создаем временный QPixmap для применения прозрачности
            temp_pixmap = QPixmap(pixmap.size())
            temp_pixmap.fill(Qt.GlobalColor.transparent)

            # Используем QPainter для установки прозрачности
            painter = QPainter(temp_pixmap)
            painter.setOpacity(transparency)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()

            pixmap = temp_pixmap

        # Отображение результатов с масштабированием
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(),
                                                 Qt.AspectRatioMode.KeepAspectRatio,
                                                 Qt.TransformationMode.SmoothTransformation))

    def resizeEvent(self, event):
        """Обработчик изменения размера окна - перерисовываем изображение"""
        super().resizeEvent(event)
        self.apply_all_effects()

if __name__ == '__main__':
    # Создание и запуск приложения
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())