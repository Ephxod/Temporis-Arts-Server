import pytest
import httpx

@pytest.mark.usefixtures("default_client", "create_test_jwt_token")
async def test_create_user(default_client: httpx.AsyncClient, create_test_jwt_token: str) -> None:
    jwt_token = create_test_jwt_token
    payload = {
        "user_id": "testid1",
        "name": "testname"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {jwt_token}"
    }
    test_response = {
        "msg": "Success"
    }
    response = await default_client.post("/api/users", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response
    



