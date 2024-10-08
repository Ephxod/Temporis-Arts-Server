import pytest
from unittest.mock import patch, AsyncMock
import httpx
import base64
from sqlalchemy.orm import Session
from models.auths import Auth
from models.responses.auths import AuthResponse
from models.users import User

@pytest.mark.usefixtures("default_client")
async def test_auth(default_client: httpx.AsyncClient, db_session: Session) -> None:
    # 유저 삭제: 이전 테스트에서 남아있는 유저가 있을 수 있으므로 삭제
    db_session.query(User).filter_by(user_id="testid1").delete()
    db_session.commit()

    valid_ticket = str(base64.b64encode(b"test_ticket"), "utf-8")
    payload = {
        "user_id": "testid1",
        "user_ticket": valid_ticket,
        "name": "테스트 사용자"
    }

    mock_response = {
        "response": {
            "params": {
                "result": "OK"
            }
        }
    }

    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json = AsyncMock(return_value=mock_response)

        response = await default_client.post("/api/auth", json=payload)

        assert response.status_code == 200
        assert "token" in response.json()

        # 유저가 등록되었는지 확인
        user = db_session.query(User).filter_by(user_id="testid1").first()
        assert user is not None
        assert user.name == "테스트 사용자"  # 등록된 유저의 이름 확인