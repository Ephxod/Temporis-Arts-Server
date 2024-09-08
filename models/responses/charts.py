from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime

class ChartResponse(BaseModel):
    difficulty: int
    level: int
    avg_score: float
    clear_rate: float
    full_combo_rate: float

class MusicResponse(BaseModel):
    music_id: int
    title: str
    composer: str
    charts: List[ChartResponse]

class ChartsStatsResponse(BaseModel):
    data: List[MusicResponse]
    
class UserHighScoreResponse(BaseModel):
    user_id: str
    name: str
    high_score: int
    score_updated_date: datetime
    
    @field_validator('score_updated_date', mode='before')
    def format_datetime(cls, value):
        return value.strftime("%Y-%m-%d %H:%M:%S")  # 원하는 형식으로 변환
    
class RankingResponse(BaseModel):
    data: List[UserHighScoreResponse]

    