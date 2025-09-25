from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, title, content):
        self.title = title
        self.content = content


    @abstractmethod
    def save(self):
        pass


    def file_information(self):
        print(f"Название документа: {self.title}")
        print(f"Содержимое документа: {self.content}")


class PDFDocument(Document):
    def save(self):
        print(f"Сохранение PDF документа: {self.title}.pdf")
        return f"{self.title}.pdf"


class WordDocument(Document):
    def save(self):
        print(f"Сохранение Word документа: {self.title}.docx")
        return f"{self.title}.docx"


class ExcelDocument(Document):
    def save(self):
        print(f"Сохранение Excel документа: {self.title}.xlsx")
        return f"{self.title}.xlsx"


# Фабричный метод
class DocumentFactory:
    @staticmethod
    def create_document(doc_type, title, content):
        if doc_type == "pdf":
            return PDFDocument(title, content)
        elif doc_type == "word":
            return WordDocument(title, content)
        elif doc_type == "excel":
            return ExcelDocument(title, content)
        else:
            raise ValueError(f"Неизвестный тип документа: {doc_type}")


# Пример
def main():
    print("--- Система генерации документов ---\n")

    # Создаем документы
    documents = [
        DocumentFactory.create_document("pdf", "Отчет за год", "Годовой финансовый отчет."),
        DocumentFactory.create_document("word", "Договор", "Условия сотрудничества."),
        DocumentFactory.create_document("excel", "Бюджет", "Таблица расходов и доходов")
    ]

    # Сохраняем все документы
    saved_files = []
    for doc in documents:
        doc.file_information()
        filename = doc.save()
        saved_files.append(filename)
        print()  # Пустая строка для разделения

    # Выводим список сохраненных файлов
    print("Созданные файлы:")
    for filename in saved_files:
        print(f"- {filename}")


if __name__ == "__main__":
    main()