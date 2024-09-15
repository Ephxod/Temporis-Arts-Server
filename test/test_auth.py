import pytest
from unittest.mock import patch, AsyncMock
import httpx
import base64


@pytest.mark.usefixtures("default_client")
async def test_auth(default_client: httpx.AsyncClient) -> None:
    valid_ticket = str(base64.b64encode(b"test_ticket"), "utf-8")  
    payload = {
        "user_id": "testid1",
        "user_ticket": valid_ticket  
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
