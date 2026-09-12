import logging
import sys

from app.core.config import settings

def setup_logging() -> None:
    logging.basicConfig(
        level="DEBUG",
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
