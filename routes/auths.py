from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from models.auths import Auth
from models.responses.auths import AuthResponse
from models.users import User
from config import API_KEY, APP_ID, SECRET_KEY 
import datetime
import jwt
import httpx
import base64
from database.connection import get_session

auth_router = APIRouter(
    tags=["Auth"],
)

@auth_router.post("", response_model=AuthResponse)
async def auth(data: Auth, session: Session = Depends(get_session)) -> AuthResponse:
    body = data.json()
    print("Received request:", body) 
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
    result = await response.json()

    print("result from STEAM:", result) 
    
    if result.get("response", {}).get("params", {}).get("result") != "OK":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ticket",
        )

    # 유저가 데이터베이스에 존재하는지 확인
    existing_user = session.query(User).filter(User.user_id == data.user_id).first()
    
    if not existing_user:
        # 유저 등록
        new_user = User(user_id=data.user_id, name=data.name)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    payload = {
        "sub": string_ticket,  # 사용자 식별 정보
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=6)  # 만료 시간 설정
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return AuthResponse(token=token)