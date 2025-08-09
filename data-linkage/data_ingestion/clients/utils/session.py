import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

"""재시도/백오프/타임아웃을 일괄 적용하기 위한 Session 생성"""
def create_session(retry_count:int = 5) -> requests.Session:
    session = requests.Session()                        # 세션 생성(연결 재사용)
    retry = Retry(                                # 재시도 규칙 정의
        total=retry_count,                                  # 최대 5회 재시도
        backoff_factor=0.5,                       # 0.5,1,2,4,… 초 백오프
        status_forcelist=[429,500,502,503,504],   # 재시도할 상태 코드
        allowed_methods=["GET"]
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))  # https에 어댑터 장착
    session.mount("http://", HTTPAdapter(max_retries=retry))   # http도 동일
    session.headers.update({"User-Agent": "DataLinkage/1.0"})  # UA 지정
    return session