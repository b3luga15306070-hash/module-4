def show_books():
    books = load_books()

    for book in books:
        print(
            f"{book['author']} - "
            f"{book['title']} - "
            f"{book['rating']}"
        )


def average_rating():
    books = load_books()

    if not books:
        print("Нет книг")
        return

    avg = sum(book["rating"] for book in books) / len(books)

    print("Средняя оценка:", round(avg, 2))
