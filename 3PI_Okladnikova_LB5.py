from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class GasolineEngine(Engine):
    def start(self):
        print("Запуск бензинового двигателя: Ррррр-ррр-рр!")

    def stop(self):
        print("Остановка двигателя: Вжжжжж-жжж!")


class ElectricEngine(Engine):
    def start(self):
        print("Запуск электрического двигателя: Ррррр-ррр-рр!")

    def stop(self):
        print("Остановка электрического двигателя")


class HybridEngine(Engine):
    def start(self):
        print("Запуск гибридного двигателя: Тихий переход на электротягу!")

    def stop(self):
        print("Остановка гибридного двигателя: Полное отключение питания!")

class Vehicle(ABC):
    def __init__(self, engine:Engine):
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Машина начинает движение!")

        self.engine.start()
        print("Машина едет...")

class Bike(Vehicle):
    def drive(self):
        print("Велосипед начинает дижение:")
        self.engine.start()
        print("Велосипед едет...")
        self.engine.stop()

# Создаем различные двигатели
gasoline_engine = GasolineEngine()
electric_engine = ElectricEngine()
hybrid_engine = HybridEngine()

# Создаем автомобили с разными двигателями
gasoline_car = Car(gasoline_engine)
electric_car = Car(electric_engine)
hybrid_car = Car(hybrid_engine)

# Создаем велосипеды
electric_bike  = Bike(electric_engine)
hybrid_bike = Bike(hybrid_engine)


print("=== Демонстрация работы транспортных средств ===")
print("\n1. Автомобиль с бензиновым двигателем:")
gasoline_car.drive()

print("\n2. Автомобиль с электрическим двигателем:")
electric_car.drive()

print("\n3. Автомобиль с гибридным двигателем:")
hybrid_car.drive()

print("\n4. Электрический велосипед:")
electric_bike.drive()

print("\n1. Гибридный велосипед:")
hybrid_bike.drive()
