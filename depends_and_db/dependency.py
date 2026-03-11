from typing import Annotated

from fastapi import Depends

from schemas.dependency import PaginationParams, FilterParams

PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]
FilterParamsDep = Annotated[FilterParams, Depends(FilterParams)]