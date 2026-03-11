from fastapi import Depends

from schemas import BookSchema, UpdateBookSchema, CreateBookSchema
from repositories.books import BookRepository


class BookService:
    def __init__(self, repository: BookRepository = Depends()):
        self.repo = repository

    def add_book(self, new_book: CreateBookSchema):
        self.repo.create(new_book)

        return new_book

    def get_book_by_id(self, id: int):
        book_db = self.repo.get_by_id(id)

        return book_db

    def get_books(self, limit, offset) -> list[BookSchema] | None:
        return self.repo.get_all(limit, offset)

    def update_book(self, id: int, payload: UpdateBookSchema) -> BookSchema | None:
        return self.repo.update(id, payload)

    def delete_book(self, id: int) -> bool:
        return self.repo.delete(id)
