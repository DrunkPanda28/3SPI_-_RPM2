from abc import ABC, abstractmethod
from typing import List


# Интерфейс подписчика
class Subscriber(ABC):
    @abstractmethod
    def update(self, currency: str, rate: float):
        pass


# Интерфейс издателя
class Publisher(ABC):
    @abstractmethod
    def attach(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


# Класс для хранения курсов валют и управления подписчиками
class CurrencyExchange(Publisher):
    def __init__(self):
        self._subscribers: List[Subscriber] = []
        self._rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.75,
            'JPY': 110.0
        }

    def attach(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            print(f"✅ {subscriber.name} подписался на обновления курсов")

    def detach(self, subscriber: Subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            print(f"❌ {subscriber.name} отписался от обновлений курсов")

    def notify(self):
        print(f"\n📢 Рассылка уведомлений для {len(self._subscribers)} подписчиков...")
        for subscriber in self._subscribers:
            subscriber.update(self._rates)

    def set_rate(self, currency: str, rate: float):
        old_rate = self._rates.get(currency)
        self._rates[currency] = rate

        print(f"\n💱 Изменение курса {currency}: {old_rate} → {rate}")
        self.notify()

    def get_rate(self, currency: str) -> float:
        return self._rates.get(currency, 0.0)

    def get_all_rates(self) -> dict:
        return self._rates.copy()


# Конкретные подписчики
class Bank(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, rates: dict):
        usd_rate = rates.get('USD', 0)
        eur_rate = rates.get('EUR', 0)
        print(f"🏦 Банк '{self.name}': Обновление курсов - USD: {usd_rate}, EUR: {eur_rate}")


class ExchangeOffice(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, rates: dict):
        buy_usd = rates.get('USD', 0) * 0.98  # Курс покупки
        sell_usd = rates.get('USD', 0) * 1.02  # Курс продажи
        print(f"💱 Обменник '{self.name}': Покупка USD: {buy_usd:.2f}, Продажа USD: {sell_usd:.2f}")


class Investor(Subscriber):
    def __init__(self, name: str):
        self.name = name
        self._portfolio = {'USD': 10000, 'EUR': 5000}

    def update(self, rates: dict):
        total_value = sum(amount * rates.get(currency, 0)
                          for currency, amount in self._portfolio.items())
        print(f"📊 Инвестор '{self.name}': Стоимость портфеля: ${total_value:.2f}")


# Дополнительный подписчик - Мобильное приложение
class MobileApp(Subscriber):
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.name = f"App_{user_name}"

    def update(self, rates: dict):
        print(f"📱 Пользователь '{self.user_name}': Получены новые курсы валют")
        for currency, rate in rates.items():
            print(f"   {currency}: {rate}")


# Демонстрация работы системы
def demo_currency_observer():
    print("=== Система отслеживания курсов валют ===\n")

    # Создаем издателя (биржу валют)
    exchange = CurrencyExchange()

    # Создаем подписчиков
    bank1 = Bank("Альфа-Банк")
    bank2 = Bank("Сбербанк")
    exchange_office = ExchangeOffice("Обменник 24/7")
    investor = Investor("Иван Петров")
    mobile_app = MobileApp("Анна Сидорова")

    # Подписываем всех на обновления
    subscribers = [bank1, bank2, exchange_office, investor, mobile_app]
    for sub in subscribers:
        exchange.attach(sub)

    print("\n" + "=" * 50)

    # Изменяем курсы валют (должны получить уведомления)
    exchange.set_rate('USD', 1.05)  # USD вырос
    print("\n" + "=" * 50)

    exchange.set_rate('EUR', 0.90)  # EUR вырос
    print("\n" + "=" * 50)

    exchange.set_rate('JPY', 115.0)  # JPY изменился
    print("\n" + "=" * 50)

    # Отписываем один банк
    exchange.detach(bank2)
    print("\n" + "=" * 50)

    # Еще одно изменение курса (банк2 не получит уведомление)
    exchange.set_rate('GBP', 0.80)
    print("\n" + "=" * 50)

    # Показываем текущие курсы
    print("📈 Текущие курсы валют:")
    for currency, rate in exchange.get_all_rates().items():
        print(f"   {currency}: {rate}")


# Расширенная демонстрация с разными сценариями
def extended_demo():
    print("\n\n=== Расширенная демонстрация ===")

    exchange = CurrencyExchange()

    # Создаем специализированных подписчиков
    crypto_exchange = ExchangeOffice("Крипто-Обменник")
    wealthy_investor = Investor("Олег Богатый")
    trader_app = MobileApp("Трейдер_Про")

    # Подписываем
    exchange.attach(crypto_exchange)
    exchange.attach(wealthy_investor)
    exchange.attach(trader_app)

    print("\nСимуляция валютных колебаний:")

    # Симуляция изменений курса
    changes = [
        ('USD', 1.10),
        ('EUR', 0.95),
        ('USD', 1.15),
        ('EUR', 0.85),
        ('JPY', 120.0)
    ]

    for currency, new_rate in changes:
        exchange.set_rate(currency, new_rate)
        print("---")


if __name__ == "__main__":
    demo_currency_observer()
    extended_demo()