from fastapi import Request
from fastapi.responses import JSONResponse

from .exceptions import BusinessException


async def business_exception_handler(
    request: Request,
    exc: BusinessException,
):

    return JSONResponse(
        status_code=400,
        content={
            "message": exc.message
        },
    )