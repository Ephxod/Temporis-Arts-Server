from pydantic import BaseModel, Field
from datetime import datetime
from users import User
from musics import Music
from charts import Chart

class Record(BaseModel):
    user_id: str = Field(..., description="Foreign key referencing User model")
    music_id: int = Field(..., description="Foreign key referencing Music model")
    difficulty: int = Field(..., description="Foreign key referencing Chart model")
    high_score: int
    clear_status: bool # 기본값 False
    full_combo_status: bool # 기본값 False
    all_arts_status: bool # 기본값 False
    score_updated_date: datetime
    
    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "music_id": 0,
                "difficulty": 0,
                "high_score": 4567890,
                "clear_status": False,
                "full_combo_status": False,
                "all_arts_status": False
            }
        }