from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint
from models.musics import Music

class Chart(SQLModel, table=True):
    music_id: int = Field(..., foreign_key="music.music_id", primary_key=True)
    difficulty: int = Field(..., primary_key=True)
    level: int = Field(..., index=True)
    
    music: Music = Relationship(back_populates="charts")  # 관계 설정

    __table_args__ = (
        UniqueConstraint('music_id', 'difficulty', name='uq_music_difficulty'),  # 복합 고유 제약 조건
    )

    class Config:
        schema_extra = {
            "example": {
                "music_id": 1,
                "difficulty": 0,
                "level": 8
            }
        }
        
    def __repr__(self):
        return f"<Chart(music_id={self.music_id}, difficulty={self.difficulty}, level={self.level})>"
