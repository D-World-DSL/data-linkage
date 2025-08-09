import os
import json
# import shapely
from dotenv import load_dotenv

from ....utils.logging import get_logger
from ...utils.session import create_session

load_dotenv()

API_KEY = os.getenv("VWORLD_API_KEY")
BASE_URL = r"https://api.vworld.kr/req/data?request=GetFeature"
COVER_KOREA = "BOX(124.5, 33.0, 131.9, 38.7)"

def fetch(target_data: str, geomFilter: str = COVER_KOREA) -> json:
    assert target_data, "target_data는 필수 인자입니다."
    
    logger = get_logger(__name__)
    params = {
        "key": API_KEY, 
        "data": target_data, 
        "geomFilter": geomFilter 
    }
    session = create_session()

    response = session.get(f"{BASE_URL}",params=params,timeout=(5, 15))
    response.raise_for_status() # 4xx/5xx면 예외 발생

    try: 
        data = response.json()
        logger.info(f"데이터 수집 완료: {data}")
    except json.JSONDecodeError as e:
        logger.error(f"JSON 파싱 실패: {e}")
        logger.error(f"응답 원문:\n{response.text}")
        raise
    return data