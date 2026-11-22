from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
NotFoundException,
ForbiddenException,
ConflictException
)

app = FastAPI()

@app.exception_handler(NotFoundException)
async def not_found_handler(
        request: Request,
        exc: NotFoundException
):
    return JSONResponse(status_code=404,content={'detail': exc.message})

@app.exception_handler(ForbiddenException)
async def forbidden_handler(
        request: Request,
        exc: ForbiddenException
):
    return JSONResponse(status_code=403, content={'detail': exc.message})

@app.exception_handler(ConflictException)
async def conflict_handler(
        request: Request,
        exc: ConflictException
):
    return JSONResponse(status_code=409, content={'detail': exc.message})

