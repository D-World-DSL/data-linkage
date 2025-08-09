from . import traffic_cctv
from . import sigungu

def ingest() -> dict:
    traffic_cctv.ingest()
    sigungu.ingest()

__all__ = ["ingest"]