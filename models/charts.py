from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from models.musics import Music

class Chart(SQLModel, table=True):
    chart_id: int = Field(primary_key=True, index=True)
    music_id: int = Field(..., foreign_key="music.music_id")
    difficulty: int = Field(..., index=True)
    level: int = Field(..., index=True)


    class Config:
        schema_extra = {
            "example": {
                "music_id": 1,
                "difficulty": 0,
                "level": 8
            }
        }
        
    def __repr__(self):
        return f"<Chart(chart_id={self.chart_id}, music_id={self.music_id}, difficulty={self.difficulty}, level={self.level})>"
