import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def main():
    while True:
        print("\nТрекер книг")
        print("1. Добавить книгу")
        print("2. Показать книги")
        print("3. Средняя оценка")
        print("4. Удалить книгу")
        print("5. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_books()

        elif choice == "3":
            average_rating()

        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Выход")
            break

        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()
