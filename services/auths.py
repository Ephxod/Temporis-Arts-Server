from fastapi import  HTTPException, status, Depends, Request
from config import SECRET_KEY 
import jwt


# JWT 검증 함수
def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

# JWT 인증 의존성 함수
async def get_current_user(authorization: str = Depends(lambda: Request.headers["Authorization"])):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authorization header missing or invalid",
        )
    
    token = authorization.split(" ")[1]
    payload = verify_jwt(token)
    return payload  # 사용자 정보를 반환할 수 있음