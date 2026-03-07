from fastapi import APIRouter, Response, status, Depends, HTTPException
from fastapi.responses import JSONResponse

from schemas import BookSchema, UpdateBookSchema
from services import BookService
from typing import List


router = APIRouter(prefix= "/books", tags=["books"])


@router.post("/")
def add_book(
        payload: BookSchema,
        service: BookService = Depends()
) -> JSONResponse:
    add_result = service.add_book(payload)

    return JSONResponse({
        "message": "The book has been added",
        "book": add_result.model_dump()
    }, status_code=status.HTTP_201_CREATED)


@router.get("/{book_id}")
def get_book(
        book_id: int,
        service: BookService = Depends()
) -> JSONResponse:
    get_result = service.get_book_by_id(book_id)
    if get_result:
        return JSONResponse(get_result.model_dump(), status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@router.get("/")
def get_books_collection(
        limit: int = 5,
        offset: int = 0,
        service: BookService = Depends()
) -> list[BookSchema]:
    get_result = service.get_books(limit, offset)
    return get_result


@router.patch("/{book_id}")
def update_book(
        book_id: int,
        payload: UpdateBookSchema,
        service: BookService = Depends()
):
    update_result = service.update_book(book_id, payload)
    if update_result:
        return JSONResponse(update_result.model_dump(), status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@router.delete("/{book_id}")
def delete_book(
        book_id: int,
        service: BookService = Depends()
) -> JSONResponse:
    delete_result = service.delete_book(book_id)
    if delete_result:
        return JSONResponse({
            "status": "success"
        }, status.HTTP_200_OK)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
