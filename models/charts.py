from pydantic import BaseModel, Field
from musics import Music

class Chart(BaseModel):
    music_id: int = Field(..., description="Foreign key referencing Music model")
    difficulty: int
    level: int
    
    class Config:
        schema_extra = {
            "example": {
                "music_id": 1,
                "difficulty": 0,
                "level": 8
            }
        }