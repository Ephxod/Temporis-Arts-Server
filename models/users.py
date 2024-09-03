from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str
    
    class Config:
        schema_extra = {
            "example": {
                "user_id": "sampleid123",
                "name": "samplename"
            }
        }