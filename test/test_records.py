import pytest
from fastapi.testclient import TestClient
import httpx
from models.users import User
from models.musics import Music
from models.charts import Chart

@pytest.fixture
def sample_record() -> dict:
    return {
        "user_id": "testid0",
        "music_id": 0,
        "difficulty": 1,
        "high_score": 4567890,
    }

@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_upsert_record(default_client: httpx.AsyncClient, create_test_jwt_token: str, sample_record: dict) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }

    # 레코드 생성
    response = await default_client.post("/api/records", json=sample_record, headers=headers)
    assert response.status_code == 200
    assert "datetime" in response.json()

    # 레코드 업데이트 테스트
    sample_record["high_score"] = 5000000 # 새로운 점수로 업데이트
    response = await default_client.post("/api/records", json=sample_record, headers=headers)
    assert response.status_code == 200
    assert "datetime" in response.json()

@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_update_record_status(default_client: httpx.AsyncClient, create_test_jwt_token: str, sample_record: dict) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }
    payload = {
        "user_id": "testid0",
        "music_id": 0,
        "difficulty": 0,
        "clear_status": True, \
        "full_combo_status": False, \
        "all_arts_status":  False 
    }
    test_response = {
        "msg": "Success"
    }

    # 레코드 생성
    response = await default_client.post("/api/records", json=sample_record, headers=headers)
    assert response.status_code == 200

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
        "music_id": 0,
        "difficulty": 0,
        "clear_status": True, \
        "full_combo_status": False, \
        "all_arts_status":  False 
    }
    response = await default_client.patch("/api/records", json=payload, headers=headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Record not found"