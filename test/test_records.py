import pytest
import httpx
from models.users import User
from models.musics import Music
from models.charts import Chart
from sqlalchemy.orm import Session
from models.records import Record

@pytest.fixture
def sample_record() -> dict:
    return {
        "user_id": "testid0",
        "chart_id": "0_1",
        "judgement": 0,
    }

@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_create_record(default_client: httpx.AsyncClient, create_test_jwt_token: str, sample_record: dict,  db_session: Session) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }

    # 레코드 생성
    response = await default_client.post("/api/records", json=sample_record, headers=headers)
    assert response.status_code == 200
    assert response.json().get("msg") == "Success"

    # 동일한 레코드로 다시 요청
    response = await default_client.post("/api/records", json=sample_record, headers=headers)
    assert response.status_code == 200
    assert response.json().get("msg") == "Success"


    existing_record = db_session.query(Record).filter(
        Record.user_id == sample_record["user_id"],
        Record.chart_id == sample_record["chart_id"],
        Record.judgement == sample_record["judgement"]
    ).one() 
    assert existing_record.play_count == 2  

@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_update_record_status(default_client: httpx.AsyncClient, create_test_jwt_token: str, sample_record: dict) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }
    payload = {
        "user_id": "testid0",
        "chart_id": "0_0",
        "judgement": 0,
        "high_score": 1000000, \
        "clear_status": True, \
        "full_combo_status": False, \
        "all_arts_status":  False 
    }
    test_response = {
        "msg": "Success"
    }

    # 레코드 상태 업데이트 테스트
    response = await default_client.patch("/api/records", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response

@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_update_nonexistent_record(default_client: httpx.AsyncClient, create_test_jwt_token: str) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }
    payload = {
        "user_id": "testid1",
        "chart_id": "0_1",
        "judgement": 0,
        "high_score": 1000000, \
        "clear_status": True, \
        "full_combo_status": False, \
        "all_arts_status":  False 
    }
    response = await default_client.patch("/api/records", json=payload, headers=headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Record not found"