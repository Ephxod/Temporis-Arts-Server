import pytest
import jwt
import httpx
from fastapi.testclient import TestClient
from models.charts import Chart
from models.musics import Music
from models.records import Record
from models.responses.charts import ChartsStatsResponse, RankingResponse
from sqlalchemy import text
from config import SECRET_KEY


@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_get_charts(default_client: httpx.AsyncClient, create_test_jwt_token: str) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}",
    }

    response = await default_client.get("/api/charts/stats", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  
    assert "data" in response.json()  
    data = response.json()["data"]
    assert len(data) > 0  
    assert data[0]["music_id"] == 0  
    assert data[0]["title"] == "samplemusic0"  
    assert data[0]["composer"] == "testcomposer" 


@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_get_ranking(default_client: httpx.AsyncClient, create_test_jwt_token: str) -> None:
    jwt_token = create_test_jwt_token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}",
    }

    music_id = 0
    difficulty = 0

    response = await default_client.get(
        f"/api/charts/ranking?music_id={music_id}&difficulty={difficulty}",
        headers=headers,
    )

    assert response.status_code == 200
    assert isinstance(response.json(), dict)  
    assert "data" in response.json()
    data = response.json()["data"]
    assert len(data) > 0  
    assert data[0]["user_id"] == "testid0"
    assert data[0]["name"] == "testname" 
    assert data[0]["high_score"] == 4567890  
