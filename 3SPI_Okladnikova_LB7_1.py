# Базовый класс для вывода текста
class TextPrinter:
    def __init__(self, text):
        self.text = text

    def print(self):
        return self.text


# Декоратор для преобразования в верхний регистр
class UpperCaseDecorator:
    def __init__(self, printer):
        self.printer = printer

    def print(self):
        return self.printer.print().upper()


# Декоратор для добавления рамки
class BorderDecorator:
    def __init__(self, printer):
        self.printer = printer

    def print(self):
        text = self.printer.print()
        lines = text.split('\n')
        max_length = max(len(line) for line in lines)

        result = ['+' + '-' * (max_length + 2) + '+']

        for line in lines:
            result.append('| ' + line.ljust(max_length) + ' |')

        result.append('+' + '-' * (max_length + 2) + '+')
        return '\n'.join(result)


# Декоратор для добавления восклицательных знаков
class ExclamationDecorator:
    def __init__(self, printer, count=1):
        self.printer = printer
        self.count = count

    def print(self):
        text = self.printer.print()
        return text + '!' * self.count


# Демонстрация работы декораторов
def demo():
    # Исходный текст
    original_text = "Hello World\nThis is a test"

    print("1. Оригинальный текст:")
    printer = TextPrinter(original_text)
    print(printer.print())
    print()

    print("2. Верхний регистр:")
    upper_printer = UpperCaseDecorator(printer)
    print(upper_printer.print())
    print()

    print("3. С рамкой:")
    border_printer = BorderDecorator(printer)
    print(border_printer.print())
    print()

    print("4. С восклицательными знаками:")
    exclamation_printer = ExclamationDecorator(printer, 3)
    print(exclamation_printer.print())
    print()

    print("5. Комбинация: верхний регистр + рамка:")
    combo1 = BorderDecorator(UpperCaseDecorator(printer))
    print(combo1.print())
    print()

    print("6. Комбинация: рамка + восклицательные знаки:")
    combo2 = ExclamationDecorator(BorderDecorator(printer), 2)
    print(combo2.print())
    print()

    print("7. Полная комбинация: верхний регистр + рамка + восклицательные знаки:")
    combo3 = ExclamationDecorator(BorderDecorator(UpperCaseDecorator(printer)), 4)
    print(combo3.print())


if __name__ == "__main__":
    demo()

