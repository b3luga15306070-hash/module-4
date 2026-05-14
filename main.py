def save_books(books):
    ...
  def add_book():
    books = load_books()

    author = input("Автор: ")
    title = input("Название: ")
    rating = int(input("Оценка: "))
    date = input("Дата: ")

    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    }

    books.append(book)

    save_books(books)

    print("Книга добавлена")
