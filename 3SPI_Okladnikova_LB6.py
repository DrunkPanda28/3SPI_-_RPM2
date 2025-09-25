class FibonacciIterator:
    def __init__(self, n):
        self.n = n  # количество чисел для генерации
        self.current = 0
        self.next = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        if self.count == 0:
            result = 0
        elif self.count == 1:
            result = 1
        else:
            result = self.current + self.next
            self.current = self.next
            self.next = result

        self.count += 1
        return result




# Реализация через генератор (yield)
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def demo_fibonacci():
    print("--- Числа Фибоначчи ---")
    print("\n1. Использование итератора (класс):")

    # Создаем итератор для 15 чисел
    fib_iter = FibonacciIterator(10)

    # Выводим числа
    for i, num in enumerate(fib_iter, 1):
        print(f"F({i - 1}) = {num}")

    print("\n2. Использование генератора (yield):")

    # Используем генератор для 15 чисел
    for i, num in enumerate(fibonacci_generator(10), 1):
        print(f"F({i - 1}) = {num}")

    print("\n3. Сравнение подходов:")

    # Создаем оба варианта
    iterator_nums = list(FibonacciIterator(10))
    generator_nums = list(fibonacci_generator(10))

    print(f"Итератор:  {iterator_nums}")
    print(f"Генератор: {generator_nums}")
    print(f"Результаты совпадают: {iterator_nums == generator_nums}")


if __name__ == "__main__":
    demo_fibonacci()