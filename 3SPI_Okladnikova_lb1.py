import json


class ConfigCache:
    # Ссылка на экземпляра
    _instance = None
    # словарь для хранения конфигурации
    _config = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_config()
        return cls._instance

    # Загрузка конфигурации и обработка ошибок
    def load_config(self, filename="config.json"):
        try:
            with open(filename, 'r') as file:
                self._config = json.load(file)
        except:
            self._config = {}
            print("Ошибка загрузки конфигурации")

    # Получаем значение по ключу
    def get(self, key):
        return self._config.get(key)

    # Устанавливаем значение
    def set(self, key, value):
        self._config[key] = value

    # Сохраняем данные
    def save(self, filename="config.json"):
        with open(filename, 'w') as file:
            json.dump(self._config, file, indent=4)


# Создаем экземпляр (автоматически загружает конфигурацию)
config = ConfigCache()

# Получаем значения
db_host = config.get("database_host")
print(f"Хост БД: {db_host}")

# Изменяем значение
config.set("database_host", "localhost1")

# Проверяем, что изменения видны везде
config2 = ConfigCache()
print(f"Из другого места: {config2.get('database_host')}")

# Сохраняем изменения
config.save()