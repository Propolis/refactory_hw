from fastapi import APIRouter, Response, status, Depends
from fastapi.responses import JSONResponse

from schemas import BaseUser, CreateUser
from services import UserService
from typing import List


router = APIRouter(prefix= "/users", tags=["Users"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_user(service: UserService = Depends()) -> JSONResponse:
    get_result = service.get_all_users()
    if not get_result:
        return JSONResponse({
            "status": "error",
            "message": "No users found"
        }, status.HTTP_404_NOT_FOUND)

    return get_result


@router.post("/", status_code=201)
def create_user(response: Response, user: CreateUser, service: UserService = Depends()):
    add_result = service.add_user(user)
    response.status_code = status.HTTP_201_CREATED
    return {"message": "User created", "user": add_result}
