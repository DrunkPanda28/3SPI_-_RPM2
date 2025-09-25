from abc import ABC, abstractmethod
import random

# Интерфейс стратегии конвертации валют
# Определяет общий метод convert, который должны реализовать все конкретные стратегии
class CurrencyConversionStrategy(ABC):
    @abstractmethod
    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        pass


# Конвертация по фикс курсу
# Использует заранее заданные курсы валют
class FixedRateConversion(CurrencyConversionStrategy):
    def __init__(self):
        # Словарь с фиксированными курсами валютных пар
        self.rates = {
            ('USD', 'EUR'): 0.85,  # 1 USD = 0.85 EUR
            ('EUR', 'USD'): 1.18,  # 1 EUR = 1.18 USD
        }

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        # Получаем курс для указанной валютной пары
        rate = self.rates.get((from_currency, to_currency))
        if rate is None:
            raise ValueError("Неподдерживаемая конвертация валют")
        # Выполняем конвертацию: умножаем сумму на курс
        return amount * rate


# Конвертация по рыночному курсу
# Имитирует изменчивость рыночных курсов с помощью случайных колебаний
class MarketRateConversion(CurrencyConversionStrategy):
    def __init__(self):
        # Базовые курсы, от которых будут рассчитываться рыночные колебания
        self.base_rates = {
            ('USD', 'EUR'): 0.85,
            ('EUR', 'USD'): 1.18,
        }

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        # Получаем базовый курс для валютной пары
        base_rate = self.base_rates.get((from_currency, to_currency))
        if base_rate is None:
            raise ValueError("Неподдерживаемая конвертация валют")
        # Добавляем случайное отклонение до ±2% для имитации рыночных колебаний
        fluctuation = random.uniform(0.98, 1.02)
        # Выполняем конвертацию с учетом рыночных колебаний
        return amount * base_rate * fluctuation


# Конвертация по курсу центрального банка
# Использует курсы, которые могут отличаться от рыночных
class CentralBankRateConversion(CurrencyConversionStrategy):
    def __init__(self):
        # Курсы валют, установленные центральным банком
        self.rates = {
            ('USD', 'EUR'): 0.86,  # Курс ЦБ может отличаться от рыночного
            ('EUR', 'USD'): 1.16,
        }

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        # Получаем курс ЦБ для указанной валютной пары
        rate = self.rates.get((from_currency, to_currency))
        if rate is None:
            raise ValueError("Неподдерживаемая конвертация валют")
        # Выполняем конвертацию по курсу ЦБ
        return amount * rate


# Класс контекста, который использует выбранную стратегию
# Позволяет динамически менять стратегию конвертации
class CurrencyConverterContext:
    def __init__(self, strategy: CurrencyConversionStrategy):
        # Инициализация с определенной стратегией
        self._strategy = strategy

    def set_strategy(self, strategy: CurrencyConversionStrategy):
        # Метод для изменения стратегии во время выполнения
        self._strategy = strategy

    def execute_conversion(self, amount: float, from_currency: str, to_currency: str) -> float:
        # Делегирование выполнения конвертации текущей стратегии
        return self._strategy.convert(amount, from_currency, to_currency)


# Основная функция для демонстрации работы системы
def main():
    # Создаем конвертер с начальной стратегией (фиксированный курс)
    converter = CurrencyConverterContext(FixedRateConversion())

    # Основной цик
    while True:
        print("\n1. Фиксированный курс")
        print("2. Рыночный курс")
        print("3. Курс ЦБ")
        print("4. Выход")

        # Получаем выбор пользователя
        choice = input("Выберите стратегию (1-4): ")

        # Выход
        if choice == '4':
            break

        # Словарь для сопоставления выбора с соответствующими стратегиями
        strategies = {
            '1': FixedRateConversion(),
            '2': MarketRateConversion(),
            '3': CentralBankRateConversion()
        }

        # Проверка корректности ввода
        if choice not in strategies:
            print("Неверный ввод!")
            continue

        # Устанавливаем выбранную стратегию
        converter.set_strategy(strategies[choice])

        try:
            # Получаем данные от пользователя
            amount = float(input("Сумма: "))
            from_curr = input("Из валюты (например USD): ").upper()
            to_curr = input("В валюту (например EUR): ").upper()

            # Выполняем конвертацию и выводим результат
            result = converter.execute_conversion(amount, from_curr, to_curr)
            print(f"Результат: {result:.2f} {to_curr}")

        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()