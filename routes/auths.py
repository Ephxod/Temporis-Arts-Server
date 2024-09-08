from fastapi import APIRouter, HTTPException, status
from models.auths import Auth
from models.responses.auths import AuthResponse
from config import API_KEY, APP_ID, SECRET_KEY 
import datetime
from datetime import timezone
import httpx
import jwt
import base64


auth_router = APIRouter(
    tags=["Auth"],
)

@auth_router.post("", response_model=AuthResponse)
async def auth(data: Auth) -> dict:
    url = "https://api.steampowered.com/ISteamUserAuth/AuthenticateUserTicket/v1/"
    string_ticket = base64.b64decode(data.user_ticket).hex()
    params = {
        "key": API_KEY,
        "appid": APP_ID,  
        "ticket": string_ticket  
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="STEAM으로 인증 실패",
        )
    result = response.json()
    print("result from STEAM:", result) 
    
    
    # 스팀 API의 응답을 확인
    if result.get("response", {}).get("params", {}).get("result") != "OK":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ticket",
        )

        
    payload = {
        "sub": string_ticket,  # 사용자 식별 정보
        "exp": datetime.datetime.now(timezone.utc) + datetime.timedelta(hours=1)  # 만료 시간 설정
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return AuthResponse(token=token)