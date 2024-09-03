from pydantic import BaseModel

class Music(BaseModel):
    music_id: int
    title: str
    composer: str
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Anecdote",
                "composer": "CUT-Turesse"
            }
        }