def delete_book():
    books = load_books()

    title = input("Название книги: ")

    books = [
        book for book in books
        if book["title"].lower() != title.lower()
    ]

    save_books(books)

    print("Книга удалена")
