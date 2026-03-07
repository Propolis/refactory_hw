from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    id: int
    name: str
    author: str
    description: str = Field(max_length=100)
    pages: int = None
    style: str = None
    isbn: str = None
    publisher: str = None


class UpdateBookSchema(BaseModel):
    id: int
    name: str
    author: str
    description: str = Field(max_length=100)
