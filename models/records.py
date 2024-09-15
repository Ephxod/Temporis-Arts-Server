from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from models.users import User
from models.musics import Music


class Record(SQLModel, table=True):
    record_id: int = Field(primary_key=True, index=True)
    user_id: str = Field(..., foreign_key="user.user_id")
    music_id: int = Field(..., foreign_key="music.music_id")
    difficulty: int = Field(..., index=True)
    high_score: int = Field(..., index=True)
    clear_status: bool = Field(default=False)
    full_combo_status: bool = Field(default=False)
    all_arts_status: bool = Field(default=False)
    score_updated_date: datetime = Field(index=True)

    user: "User" = Relationship()

    class Config:
        schema_extra = {
            "example": {
                "user_id": "1",
                "music_id": 0,
                "difficulty": 0,
                "high_score": 4567890,
                "clear_status": False,
                "full_combo_status": False,
                "all_arts_status": False
            }
        }

    def __repr__(self):
        return (f"<Record(record_id={self.record_id}, user_id={self.user_id}, music_id={self.music_id}, "
                f"difficulty={self.difficulty}, high_score={self.high_score}, "
                f"clear_status={self.clear_status}, full_combo_status={self.full_combo_status}, "
                f"all_arts_status={self.all_arts_status}, score_updated_date={self.score_updated_date})>")
