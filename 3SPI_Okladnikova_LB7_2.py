class Cofee:

    def __init__(self):
        self.cost = 100
        self.description = "Кофе"

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description


# декоратор для добавления молока
class MilkDocorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 50

    def get_description(self):
        return self.coffee.get_description() + ", молоко"


# Декоратор для добавления сахара
class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 20

    def get_description(self):
        return self.coffee.get_description() + ", сахар"



# Декоратор для добавления сиропа
class SurupDecorator:
    def __init__(self, coffee, surop_type="кокосовый"):
        self.coffee = coffee
        self.surop_type = surop_type

    def get_cost(self):
        return self.coffee.get_cost() + 80

    def get_description(self):
        return self.coffee.get_description() + f", {self.surop_type} сироп"


# Демонстрация
def coffee_order_demo():
    print("--- Система онлайн заказа кофе ---\n")

    # Кофе без добавок
    print("--- Кофе без добавок ---")
    coffee = Cofee()
    print(f"Состав: {coffee.get_description()}")
    print(f"Стоимость: {coffee.get_cost()} руб.")
    print()



    # Кофе с молоком
    print("--- Кофе с молоком ---")
    coffee_with_milk = MilkDocorator(Cofee())
    print(f"Состав: {coffee_with_milk.get_description()}")
    print(f"Стоимость: {coffee_with_milk.get_cost()} руб.")
    print()

    # Кофе с молоком и сахаром
    print("--- Кофе с молоком и сахаром ---")
    coffee_with_sugar_milk = SugarDecorator(MilkDocorator(Cofee()))
    print(f"Состав: {coffee_with_sugar_milk.get_description()}")
    print(f"Стоимость: {coffee_with_sugar_milk.get_cost()} руб.")
    print()

    # Кофе с сиропом
    print("--- Кофе с сиропом ---")
    coffee_with_syrup = SurupDecorator(Cofee(), surop_type="кокосовый")
    print(f"Состав: {coffee_with_syrup.get_description()}")
    print(f"Стоимость: {coffee_with_syrup.get_cost()} руб.")
    print()


    # Кофе полным составом
    print("--- Кофе с молоком, сахаром и кокосовым сиропом ---")
    full_coffee = SurupDecorator(SugarDecorator(MilkDocorator(Cofee())), "кокосовый")
    print(f"Состав: {full_coffee.get_description()}")
    print(f"Стоимость: {full_coffee.get_cost()} руб.")
    print()


    # Разные комбинации
    print("---  Разные варианты заказов: ---")

    # Вариант 1: только сахар
    res1 = SugarDecorator(Cofee())
    print(f"Кофе с сахаром: {res1.get_description()} - {res1.get_cost()} руб.")

    # Вариант 2: молоко + сироп
    res2 = SurupDecorator(MilkDocorator(Cofee()), "кокосовый")
    print(f"Кофе с молоком и сиропом: {res2.get_description()} - {res2.get_cost()} рую.")

    # Вариант 3: Все добавки
    res3 = SurupDecorator(MilkDocorator(SugarDecorator(Cofee())), "карамельный")
    print(f"Кофе с молоком, сахаром и карамельным сиропом {res3.get_description()} - {res3.get_cost()} руб.")


if __name__ == "__main__":
    coffee_order_demo()

