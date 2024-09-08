from fastapi import APIRouter, Depends, Request, HTTPException, status
from database.connection import get_session
from models.records import Record
from models.responses.message import MessageResponse
from models.responses.datetime import DatetimeResponse
from datetime import datetime, timezone
from services.auths import get_current_user

record_router = APIRouter(
    tags=["Record"],
)


@record_router.post("", response_model= DatetimeResponse)
async def upsert_record(new_record: Record, session=Depends(get_session), current_user: dict = Depends(get_current_user)) -> dict:
    new_record.score_updated_date = datetime.now(timezone.utc)
    existing_record = session.get(Record, (new_record.user_id, new_record.music_id, new_record.difficulty))
    
    if existing_record:
        existing_record.high_score = new_record.high_score
        existing_record.score_updated_date = new_record.score_updated_date
        session.add(existing_record) 
    else:
        session.add(new_record)
    session.commit()
    session.refresh(new_record if existing_record is None else existing_record)  

    
    return DatetimeResponse(datetime = new_record.score_updated_date)

@record_router.patch("", response_model=MessageResponse)
async def update_record_status(new_record: Record, session=Depends(get_session), current_user: dict = Depends(get_current_user)) -> dict:
    existing_record = session.get(Record, (new_record.user_id, new_record.music_id, new_record.difficulty))

    if not existing_record:
        raise HTTPException(status_code=404, detail="Record not found")

    existing_record.clear_status = new_record.clear_status
    existing_record.full_combo_status = new_record.full_combo_status
    existing_record.all_arts_status = new_record.all_arts_status
    session.commit()
    session.refresh(existing_record) 

    return MessageResponse("Success")