from typing import List
from sqlmodel import SQLModel, Field, Relationship



class Music(SQLModel, table=True):
    music_id: int = Field(primary_key=True, index=True)  # auto_increment 지원
    title: str = Field(..., index=True)
    composer: str = Field(..., index=True)
    
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Anecdote",
                "composer": "CUT-Turesse"
            }
        }
    def __repr__(self):
        return f"<Music(music_id={self.music_id}, title={self.title}, composer={self.composer})>"