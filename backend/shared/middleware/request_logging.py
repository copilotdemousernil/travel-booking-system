import time

from starlette.middleware.base import BaseHTTPMiddleware

from shared.logging.logger import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.time()

        response = await call_next(request)

        elapsed = time.time() - start

        logger.info(
            "%s %s %.3fs",
            request.method,
            request.url.path,
            elapsed,
        )

        return response