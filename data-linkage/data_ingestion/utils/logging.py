import logging, sys

"""
모든 모듈에서 동일한 포맷/레벨로 로그를 남기도록 표준 로거 제공.
"""

def get_logger(name="ingestion"):
    logger = logging.getLogger(name)

    if not logger.handlers: # 중복 핸들러 방지
        # 핸들러 설정
        LOG_FORMAT = "%(asctime)s %(levelname)s [%(name)s] %(message)s"
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        # 로거 설정
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger