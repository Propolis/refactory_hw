from schemas import BookSchema, UpdateBookSchema

books = []

class BookService:
    def __init__(self):
        self.book_db = books

    def add_book(self, new_book: BookSchema) -> BookSchema:
        self.book_db.append(new_book)

        return new_book

    def get_book_by_id(self, id: int) -> BookSchema | None:
        for book in self.book_db:
            if book.id == id:
                return book

        return None

    def get_books(self, limit, offset) -> list[BookSchema] | None:
            return self.book_db[offset : offset + limit]

    def update_book(self, id: int, payload: UpdateBookSchema) -> BookSchema | None:
        for book in self.book_db:
            if book.id == id:
                for name, value in payload.model_dump().items():
                    setattr(book, name, value)

                return book

        return None

    def delete_book(self, id: int) -> bool:
        for book in self.book_db:
            if book.id == id:
                self.book_db.remove(book)
                return True

        return False
