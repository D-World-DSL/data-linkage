from .api import fetching

TARGET_DATA = "LT_C_ADSIGG_INFO"

def ingest():
    data = fetching.fetch(TARGET_DATA)
    # 전처리 코드 들어갈 곳
    # 데이터베이스 업데이트 코드 들어갈 곳