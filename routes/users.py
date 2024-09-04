from fastapi import APIRouter, Depends, Request, HTTPException, status
from database.connection import get_session
from models.users import User
from services.auths import get_current_user

user_router = APIRouter(
    tags=["User"],
)


@user_router.post("")
async def create_user(new_user: User, session=Depends(get_session), current_user: dict = Depends(get_current_user)) -> dict:
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    return {
        "message": "Success"
    }