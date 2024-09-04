from pydantic import BaseModel, Field

class Auth(BaseModel):
    user_id: str = Field(...)
    user_ticket: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "sampleid123",
                "user_ticket": "sampleticket"
            }
        }