class SecuritySystem:
    def active(self):
        print("Система активирована")


    def not_activated(self):
        print("Система не активирована")


class VideoSurveillance:
    def enabled(self):
        print("Видеонаблюдение включено")


    def rotate_camera(self, degree):
        print(f"Камера повернута на {degree} градусов")


    def disabled(self):
        print("Видеонаблюдение отключено")


class AccessControl:
    def give_control(self):
        print("Контроль доступа включен")


    def set_access_level(self, level):
        print(f"Уровень доступа устанвлен: {level}")


    def not_control(self):
        print("Контроль доступа отключен")


class AlarmSystem:
    def alarm_on(self):
        print("Сигнализация включена")


    def trigger(self):
        print("ВНИМАНИЕ! СРАБОТАЛА СИГНАЛИЗАЦИЯ")


    def alarm_off(self):
        print("Сигнализация выключена")


# фАСАД
class SecuritySystemFacade:
    def __init__(self):
        self.security = SecuritySystem()
        self.video = VideoSurveillance()
        self.access = AccessControl()
        self.alarm = AlarmSystem()

     # Активировать систему
    def activate_security(self):
        print("--- Активация всех систем безопасности ---")
        self.security.active()  # Активировать охранную систему
        self.video.enabled()  # Начать запись видео
        self.video.rotate_camera(90)  # Повернуть камеры
        self.access.give_control()  # Контроль доступа отключен
        self.access.set_access_level("Максимальный")  # Установить уровень доступа
        self.alarm.alarm_on()  # Включить сигнализацию
        print("Система Безопасности активирована")


    # Выключить систему
    def deactivate_security(self):
        print("--- Деактивация всех систем безопасности ---")
        self.security.not_activated() # Отключить охранную систему
        self.video.disabled()   # Отключить видеонаблюдение
        self.access.not_control()   # Отключить контроль доступа
        self.access.set_access_level("Обычный") #Уровень доступа обычный
        self.alarm.alarm_off()  # Выключить сигнализацию
        print("Система Безопасности отключена")

    # Вклчение сигнализации
    def trigger_alarm(self):
        print("--- Активация тревоги ---")
        self.alarm.trigger()
        self.video.enabled()
        self.video.rotate_camera(180)
        print("Тревога Активирована")


def main():
    print("\033[1;32;40m Добро пожаловать в систему домашней безопасности!\n")

    # Создаем фасад системы безопасности
    home_security = SecuritySystemFacade()

    # Симулируем различные сценарии

    # Сценарий 1: Владелец уходит из дома и включает безопасность
    print("1. Владелец уходит из дома:")
    home_security.activate_security()

    # Сценарий 2: Попытка проникновения (срабатывает сигнализация)
    print("2. Обнаружена попытка проникновения:")
    home_security.trigger_alarm()

    # Сценарий 3: Владелец возвращается домой и отключает безопасность
    print("3. Владелец возвращается домой:")
    home_security.deactivate_security()

    # Сценарий 4: Владелец снова включает безопасность на ночь
    print("4. Владелец включает безопасность на ночь:")
    home_security.activate_security()

    # Сценарий 5: Утро - отключение безопасности
    print("5. Наступило утро:")
    home_security.deactivate_security()


if __name__ == "__main__":
    main()