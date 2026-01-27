from src.config.logging import clear_context
from src.config.logging import get_logger
from src.config.logging import set_request_id
import uuid
from typing import Callable
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from fastapi import Request, Response


logger = get_logger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)


    async def dispatch(self,request:Request,call_next:Callable) -> Response:
        request_id = str(uuid.uuid4())
        set_request_id(request_id) 
        start_time = time.time()
        logger.info( "request_started", method=request.method, path=request.url.path, client_host=request.client.host if request.client else None)
        try:
            response = await call_next(request) # Process the Request
            duration = time.time() - start_time
            logger.info("request_completed", method=request.method, path=request.url.path, status_code=response.status_code, duration_seconds=round(duration, 4))
            response.headers["X-Request-ID"] = request_id
            return response
        except Exception as e:
            duration = time.time() - start_time
            logger.error("request_failed", method=request.method, path=request.url.path, duration_seconds=round(duration, 4), error=str(e), exc_info=True)
            raise
        finally:
            clear_context()