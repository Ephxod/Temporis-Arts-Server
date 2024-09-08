from pydantic import BaseModel, field_validator
from datetime import datetime

class DatetimeResponse(BaseModel):
    datetime: datetime  # datetime 필드를 정의

    @field_validator('datetime', mode='before')
    def format_datetime(cls, value):
        return value.strftime("%Y-%m-%d %H:%M:%S")  # 원하는 형식으로 변환
