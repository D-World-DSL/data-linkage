from .api import fetching

TARGET_DATA = r"LT_P_UTISCCTV"

def ingest():
    data = fetching.fetch(TARGET_DATA)
    # 전처리 코드 들어갈 곳
    # 데이터베이스 업데이트 코드 들어갈 곳