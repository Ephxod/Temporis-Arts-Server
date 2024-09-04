from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from models.users import User
from models.musics import Music
from models.charts import Chart

class Record(SQLModel, table=True):
    user_id: str = Field(..., primary_key=True, foreign_key="user.user_id")
    music_id: int = Field(..., primary_key=True, foreign_key="music.music_id")
    difficulty: int = Field(..., primary_key=True, foreign_key="chart.difficulty")
    high_score: int = Field(..., index=True)
    clear_status: bool = Field(default=False)  # 기본값 False
    full_combo_status: bool = Field(default=False)  # 기본값 False
    all_arts_status: bool = Field(default=False)  # 기본값 False
    score_updated_date: datetime = Field(index=True)

    user: User = Relationship(back_populates="records")
    music: Music = Relationship(back_populates="records")
    chart: Chart = Relationship(back_populates="records")

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
        return (f"<Record(user_id={self.user_id}, music_id={self.music_id}, "
                f"difficulty={self.difficulty}, high_score={self.high_score}, "
                f"clear_status={self.clear_status}, full_combo_status={self.full_combo_status}, "
                f"all_arts_status={self.all_arts_status}, score_updated_date={self.score_updated_date})>")
